# coding: utf-8

from __future__ import absolute_import

import hashlib

from google.appengine.ext import ndb

from api import fields
import model
import util
import config


class Vote(model.Base):
  downvote = ndb.IntegerProperty(default=0)
  upvote = ndb.IntegerProperty(default=0)
  total = ndb.ComputedProperty(lambda self: (self.upvote - self.downvote))
  item = ndb.KeyProperty() #to recognize owner Entity
  voters = ndb.KeyProperty(kind='User', repeated=True)
  vote_items = ndb.KeyProperty(kind='VoteItem', repeated=True)

  def vote(self, voter, upvote=0, downvote=0):
  	voter = ndb.Key(urlsafe=voter)
  	if voter in self.voters:
  		vote_item_db = VoteItem.query(VoteItem.voter == voter,VoteItem.vote == self.key).fetch()[0]
  		if vote_item_db.upvote and downvote and (vote_item_db.downvote == 0):
  			vote_item_db.upvote -= 1
  			vote_item_db.downvote += 1
  			self.upvote -= 1
  			self.downvote += 1
  		elif vote_item_db.downvote and upvote and (vote_item_db.upvote == 0):
  			vote_item_db.upvote += 1
  			vote_item_db.downvote -= 1
  			self.upvote += 1
  			self.downvote -= 1
  		vote_item_db.put()
  	elif voter and (upvote or downvote):
  		vote_item = VoteItem(voter=voter, vote= self.key, upvote=upvote, downvote = downvote).put()
  		self.voters += [voter]
  		self.vote_items += [vote_item]
  		self.upvote += upvote
  		self.downvote += downvote
  	self.put()

class VoteItem(model.Base):
  voter = ndb.KeyProperty(kind='User')
  vote = ndb.KeyProperty(kind='Vote')
  downvote = ndb.IntegerProperty(default=0)
  upvote = ndb.IntegerProperty(default=0)
