# coding: utf-8

from __future__ import absolute_import

import hashlib

from google.appengine.ext import ndb

from api import fields
import model
import util
import config
import urllib2
import json

class Team(model.Base):
	program = ndb.StringProperty(required=True)
	name = ndb.StringProperty(default='')
	number = ndb.IntegerProperty(required=True)
	email = ndb.StringProperty(default='')
	website = ndb.StringProperty(default='')
	team_identity = ndb.StringProperty()
	recommendations = ndb.KeyProperty(repeated=True)
	admins = ndb.KeyProperty(repeated=True)
	activities = ndb.KeyProperty(repeated=True, kind='Message')

	def _pre_put_hook(self):
		self.team_identity = self.program.lower() + "-" + str(self.number)

	def get_members(self):
		return model.User.query(model.User.teams.IN([self.key]))

	@classmethod
	def bulk_delete_teams(cls):
		team_keys = cls.query().fetch(keys_only=True)
		ndb.delete_multi(team_keys)

	@classmethod
	def repopulate_teams(cls):
	  """
	    program = ndb.KeyProperty(required=True)
	    name = ndb.StringProperty(default='')
	    number = ndb.IntegerProperty(required=True)
	    email = ndb.StringProperty(default='')
	    website = ndb.StringProperty(default='')
	    team_identity = ndb.StringProperty()
	    recommendations = ndb.KeyProperty(repeated=True)
	    admins = ndb.KeyProperty(repeated=True)
	    activities = ndb.KeyProperty(repeated=True, kind='Message')
	  """
	  frc_teams = "https://raw.githubusercontent.com/wilfriedE/FIRST-TeamsDataset/master/frc_teams.json"
	  #ftc_teams = "https://raw.githubusercontent.com/wilfriedE/FIRST-TeamsDataset/master/ftc_teams.json"
	  #fll_teams = "https://raw.githubusercontent.com/wilfriedE/FIRST-TeamsDataset/master/fll_teams.json"
	  response = urllib2.urlopen(frc_teams)
	  data = json.load(response)
	  #delete all teams before repopulating.
	  cls.bulk_delete_teams()
	  for team in data["teams"]:
	    """
	     team e.i {u'website': u'http://www.team3044.com', u'city': u'Ballston Spa',
	     u'name': u'Team 0xBE4', u'rookieyear': 2009, u'country': u'USA', u'number': 3044,
	     u'program': u'FRC',
	     u'state_or_providence': u'NY',
	     u'motto':
	     u'The Ox is in The House!'}
	    """
	    cls(program=team["program"],
	      name=team["name"],
	      number=team["number"],
	      email="",
	      website=team["website"]).put()
	  return True

	FIELDS = {
    'program': fields.String,
    'name': fields.String,
    'website': fields.String,
    'number': fields.Integer
	}

	FIELDS.update(model.Base.FIELDS)
