# coding: utf-8

from __future__ import absolute_import

import hashlib

from google.appengine.ext import ndb

from api import fields
import model
import util
import config
import constants as ct

class Vote(model.Base):
  total = ndb.IntegerProperty(default=0)
  item = ndb.KeyProperty() #to recognize owner Entity e.i: Lesson, Course
  voters = ndb.KeyProperty(kind='User', repeated=True)
  vote_items = ndb.KeyProperty(kind='VoteItem', repeated=True)

  def vote(self, voter, vote=0):
    voter = ndb.Key(urlsafe=voter)
    if voter in self.voters:
      vote_item_db = VoteItem.query(VoteItem.voter == voter, VoteItem.vote_key == self.key).fetch()[0]
      self.setVote(vote_item_db, vote)
      self.put()
    elif voter:
      vote_item = VoteItem(voter=voter, vote_key= self.key).put()
      self.setVote(vote_item.get(), vote)
      self.voters += [voter]
      self.vote_items += [vote_item]
      self.put()

  def setVote(self, vote_item, vote):
    if vote == vote_item.voted:
      pass
    else:
      vote_diff = 0
      if vote == ct.UP_VOTE:#making a upvote
        vote_diff = 1
        if vote_item.voted == ct.NEUTRAL_VOTE:
          vote_item.voted = ct.UP_VOTE
        elif vote_item.voted == ct.DOWN_VOTE:
          vote_item.voted = ct.NEUTRAL_VOTE
      elif vote == ct.DOWN_VOTE:#making a downvote
        vote_diff = -1
        if vote_item.voted == ct.UP_VOTE:
          vote_item.voted = ct.NEUTRAL_VOTE
        elif vote_item.voted == ct.NEUTRAL_VOTE:
          vote_item.voted = ct.DOWN_VOTE
      vote_item.put()
      self.total += vote_diff

class VoteItem(model.Base):
  voter = ndb.KeyProperty(kind='User')
  vote_key = ndb.KeyProperty(kind='Vote')
  voted = ndb.IntegerProperty(default=ct.NEUTRAL_VOTE)