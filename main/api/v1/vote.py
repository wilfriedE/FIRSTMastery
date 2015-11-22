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

#Vote api endpoint does not need to be created. Creation should occur on other element creations.
@api_v1.resource('/vote/<vote_key>', endpoint='api.vote')
class VoteAPI(restful.Resource):
  """ Handles updating votes."""
  @auth.login_required
  def post(self, vote_key):
    """Update a specific vote"""
    vote_db = ndb.Key(urlsafe=vote_key).get()
    upvote = 0
    downvote = 0
    if util.param('data', str) == 'upvote':
      upvote = 1
    elif util.param('data', str) == 'downvote':
      downvote = 1
    else:
      flask.abort(505)
    if auth.current_user_key() and (upvote or downvote):
      vote_db.vote(auth.current_user_key().urlsafe(), upvote, downvote)
    return "Success"

  @auth.admin_required
  def delete(self, vote_key):
    """Delete a specific vote."""
    vote_db = ndb.Key(urlsafe=vote_key)
    if vote_db and (vote_db.kind() == 'Vote'):
      vote_db.delete()
    flask.abort(505)