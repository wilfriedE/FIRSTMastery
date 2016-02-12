# coding: utf-8

from __future__ import absolute_import

import hashlib

from google.appengine.ext import ndb

from api import fields
import model
import util
import config


class Message(model.Base):
  name = ndb.StringProperty(required=True)
  description = ndb.TextProperty(required=True)

  def html_description():
    pass