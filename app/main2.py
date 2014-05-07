import os
import urllib
import urllib2
import logging
import json

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2
from datetime import date
import datetime

JINJA_ENVIRONMENT = jinja2.Environment( loader=jinja2.FileSystemLoader(os.path.dirname(__file__)), extensions=['jinja2.ext.autoescape'], autoescape=True)

class SchedulePage(webapp2.RequestHandler):
    def get(self):
        #pass
        logging.info('QQQ: main2')
        template_values={}
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        #template = JINJA_ENVIRONMENT.get_template('./index.html')
        #template = JINJA_ENVIRONMENT.get_template('templates/test.html')
        self.response.write(template.render(template_values))

application = webapp2.WSGIApplication([
    ('/', SchedulePage),
    ('/schedule', SchedulePage),
], debug=True)

