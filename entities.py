#!/usr/bin/env python2.5
#
#  entities.py
#  Run Plus Plus
#  Datastore entity definitions
#
#  Created by Jordan Bouvier on 6/9/08.
#  Copyright (c) 2008 Jordan Bouvier. All rights reserved.
#

from google.appengine.ext import db

class UserPrefs(db.Model):
  user = db.UserProperty()
  metric = db.BooleanProperty()

class EmpedIDs(db.Model):
  emped = db.StringProperty()
  user = db.ReferenceProperty(UserPrefs)
    
class RunData(db.Model):
  workout_name = db.StringProperty()
  time = db.DateTimeProperty()
  duration = db.IntegerProperty()
  duration_string = db.StringProperty()
  distance = db.FloatProperty()
  distance_string = db.StringProperty()
  pace = db.StringProperty()
  calories = db.IntegerProperty()
    
class ExtendedData(db.Model):
  intervals = db.TextProperty()
  run = db.ReferenceProperty(RunData)