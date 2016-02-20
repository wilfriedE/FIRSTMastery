# coding: utf-8
import logging
from flask.ext import wtf
import flask
import wtforms

from google.appengine.ext import ndb

import auth
import config
import model
import util
import task
import json

from main import app


###############################################################################
# Team List
###############################################################################
"""
@app.route('/team/list')
def team_list():
  team_dbs = model.Team.query().fetch()
  return flask.render_template(
      'course/course_list.html',
      html_class='course-list',
      title='Course List',
      team_dbs=team_dbs,
      api_url=flask.url_for('api.course.list'),
    )
"""

###############################################################################
# Team View
###############################################################################
@app.route('/team/<team_identity>')
def team(team_identity):
  team_db = model.Team.query(model.Team.team_identity==team_identity).fetch()[0]   
  return flask.render_template(
      'team/team.html',
      team_db = team_db,
      title= 'Team Page',
      html_class='team-view',
    )

@app.route('/card/tm/<team_identity>')
def team_card(team_identity):
  team_db = model.Team.query(model.Team.team_identity==team_identity).fetch()[0]
  return flask.render_template(
      'team/team_card.html',
      title='Team card',
      team_db=team_db,
      html_class='team-card',
    )


###############################################################################
# Team Form - Team is only editable by team admins or moderators
#only certain fields are made editable for teams.
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
###############################################################################

class TeamForm(wtf.Form):
  email = wtforms.StringField('Email')
  website = wtforms.StringField('Website')
  recommendations = wtforms.StringField('Recommendations')
  admins = wtforms.StringField('Recommendations')

@app.route('/team/<team_identity>/update')
def team_update(team_identity):
  user_db = auth.current_user_db()
  team = model.Team.query(model.Team.team_identity==team_identity).fetch()[0]
  form =  TeamForm(email = team.email, website = team.website,
   recommendations = ','.join([ key.urlsafe() for key in team.recommendations]),
   admins = ','.join([ key.urlsafe() for key in team.admins]))

  return flask.render_template(
      'team/team_update.html',
      title='Team Update - (Team Admin Only)',
      post_path=flask.url_for('api.team',team_key=team.key.urlsafe()),
      form=form,
      team_db=team,
      html_class='team-update',
    )