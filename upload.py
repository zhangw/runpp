#!/usr/bin/env python2.5
#
#  upload.py
#  Run Plus Plus
#  Facilitates uploading of a Nike + XML file and saves it to the database.
#
#  Created by Jordan Bouvier on 6/9/08.
#  Copyright (c) 2008 Jordan Bouvier. All rights reserved.
#

import os
import cgi
import datetime
import iso8601
import wsgiref.handlers
import gnosis.xml.objectify


from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template


from entities import *


class Upload(webapp.RequestHandler):

  def get(self):
    path = os.path.join(os.path.dirname(__file__), 'upload.html')
    self.response.out.write(template.render(path, {}))
    
  def post(self):
    form_data = cgi.FieldStorage()
    file_data = form_data['myfile'].value
    xml_obj = gnosis.xml.objectify.XML_Objectify(file_data)
    py_obj = xml_obj.make_instance() 
    
    #self.response.out.write(iso8601.parse_date(str(py_obj.runSummary.time.PCDATA)))

    run = RunData()
    run.workout_name = py_obj.runSummary.workoutName.PCDATA
    run.time = iso8601.parse_date(str(py_obj.runSummary.time.PCDATA))
    run.duration = int(py_obj.runSummary.duration.PCDATA)
    run.duration_string = py_obj.runSummary.durationString.PCDATA
    run.distance = float(py_obj.runSummary.distance.PCDATA)
    run.distance_string = py_obj.runSummary.distanceString.PCDATA
    run.pace = py_obj.runSummary.pace.PCDATA
    run.calories = int(py_obj.runSummary.calories.PCDATA)
    run_key = run.put()
    
    extended = ExtendedData()
    extended.intervals = py_obj.extendedDataList.extendedData.PCDATA
    extended.run = run_key
    extended.put()
    
    self.redirect('/upload')

def main():
  application = webapp.WSGIApplication([('/upload', Upload)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
