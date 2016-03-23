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
      team_db = model.Team.query(model.Team.team_identity==team_identity).fetch()[0]
      return helpers.make_response(team_db, model.Team.FIELDS)

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

@api_v1.resource('/teams/<team_identity>/recommend', endpoint='api.team.recommend')
class TeamRecommendationAPI(restful.Resource):
  """"""
  def post(self, team_identity):
    team_db = model.Team.query(model.Team.team_identity==team_identity).fetch()[0]
    #data = util.str_to_dict(util.param("data"))
    recommendations = [key.urlsafe() for key in team_db.recommendations]
    recommendations =  [ ndb.Key(urlsafe=key_url) for key_url in util.param("recommendations", list) if key_url not in recommendations]
    if not team_db:
      return helpers.make_not_found_exception('Team %s not found' % team_identity)
    team_db.recommendations += recommendations
    team_key = team_db.put()
    return flask.jsonify({
        'result': {'message': 'Team has been updated', 'key': team_key.urlsafe()},
        'status': 'success',
      })

@api_v1.resource('/teams/reload', endpoint='api.team.reload')
class TeamReloadAPI(restful.Resource):
  @auth.admin_required
  def post(self):
  	model.Team.repopulate_teams()
  	return "success"
