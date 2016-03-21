# coding: utf-8
from __future__ import absolute_import

from google.appengine.ext import ndb
from flask.ext import restful

import flask
from api import helpers
import auth
import model
import util
from main import api_v1

@api_v1.resource('/teams/', endpoint='api.team.list')
class TeamListAPI(restful.Resource):
  """Returns all available teams"""
  def get(self):
    return helpers.make_response(model.Team.query().fetch(), model.Team.FIELDS)

@api_v1.resource('/teams/<team_identity>', endpoint='api.team')
class TeamAPI(restful.Resource):
  """Returns a specific team data"""
  def get(self, team_identity):
      team = model.Team.query(model.Team.team_identity==team_identity).fetch()
      return helpers.make_response(team, model.Team.FIELDS)

  def post(arg):
	"""
	#updating team recommendations
	recommendations = ["ahRkZXZ-ZGV2LWZpcnN0bWFzdGVyeXITCxIGTGVzc29uGICAgICAgIAJDA",
	"ahRkZXZ-ZGV2LWZpcnN0bWFzdGVyeXITCxIGTGVzc29uGICAgICAwK8KDA",
        "ahRkZXZ-ZGV2LWZpcnN0bWFzdGVyeXITCxIGQ291cnNlGICAgICA0LsKDA",
        "ahRkZXZ-ZGV2LWZpcnN0bWFzdGVyeXISCxIFVHJhY2sYgICAgIDQ-wgM"]
        team_db = ndb.Key(urlsafe="ahRkZXZ-ZGV2LWZpcnN0bWFzdGVyeXIRCxIEVGVhbRiAgICAgOSACAw").get()
        team_db.recommendations  = [ndb.Key(urlsafe=url_key) for url_key in recommendations]
        team_db.put()
	"""
	pass

@api_v1.resource('/teams/reload', endpoint='api.team.reload')
class TeamReloadAPI(restful.Resource):
  @auth.admin_required
  def post(self):
  	model.Team.repopulate_teams()
  	return "success"
