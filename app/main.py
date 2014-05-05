
import os
import urllib
import urllib2
import logging
import json

from google.appengine.api import users
from google.appengine.ext import ndb

#import jinja2
import webapp2
from datetime import date
import datetime


# JINJA_ENVIRONMENT = jinja2.Environment( loader=jinja2.FileSystemLoader(os.path.dirname(__file__)), extensions=['jinja2.ext.autoescape'], autoescape=True)



class X311Page(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = "application/json"

        #data={'test':'test1'}
        today=date.today()
        beyondtoday=(date.today()+datetime.timedelta(days=8))
        begindate = today.strftime('%m%d%Y')
        enddate=(beyondtoday).strftime('%m%d%Y')
        url='https://api.cityofnewyork.us/311/v1/municipalservices?app_id=ead6efd5&app_key=ed81466916ab613fb8e632405d196a64&startDate=%s&endDate=%s' % (begindate,enddate)
        logging.info('QQQ url: %s' % url)
        data=urllib2.urlopen(url).read()
        object=json.loads(data)


        logging.info('QQQ: object: %s' % object)
        logging.info('QQQ: object["items"]: %s' % object['items'])
        logging.info('QQQ: data: %s' % data)

        data3 = {\
        "data": {\
        "start-date": today.isoformat(),\
        "end-date": beyondtoday.isoformat(),\
        "timezone": "US/New_York",\
        "timezone-offset": "-05:00",\
        "tracks": []
##         [\
##         {\
##         "id": "246810121",\
##         "title": "Room 1",\
##         "class": "room-1",\
##         "sessions": [\
##         {\
##         "id": "session01",\
##         "start-date": "2013-05-15T09:00:00",\
##         "end-date": "2013-05-15T10:00:00",\
##         "title": "A More Awesome Web: Features You've Always Wanted"\
##         }\
##         ]\
##         }\
##         ]\
        }\
        }

        for level1 in object["items"]:
            #logging.info('QQQ: level1: %s' % level1)
            logging.info('QQQ: level1: %s' % level1['date'])
            for level2 in level1["items"]:
                #logging.info('>>> QQQ: level2: %s' % level2)
                logging.info('>>> QQQ: level2: %s' % level2['icon'])
                logging.info('>>> QQQ: level2: %s' % level2['status'])
                logging.info('>>> QQQ: level2: %s' % level2['details'])
                data3['data']['tracks'].append({"title": level1['date'], "sessions": [{"title": '%s %s' % (level2['status'],level2['details'])}]})


        self.response.out.write(json.dumps(data3))

        #self.error(403)

## //ead6efd5
## //ed81466916ab613fb8e632405d196a64
## 
## var begindate = new Date()
## var enddate = new Date()
## enddate.setDate(enddate.getDate() + 8)
## var parmenddate= pad(enddate.getMonth(),2) + pad(enddate.getDate(),2)+enddate.getFullYear()
## var parmbegindate= pad(begindate.getMonth(),2) + pad(begindate.getDate(),2)+begindate.getFullYear()
## var link =  'https://api.cityofnewyork.us/311/v1/municipalservices?app_id=ead6efd5&app_key=ed81466916ab613fb8e632405d196a64&startDate='+parmbegindate+'&endDate=' + parmenddate
## 
## var feed=UrlFetchApp.fetch(link).getContentText()
## 
## var datafrom311 = JSON.parse(feed)
## return ContentService.createTextOutput(e.parameter.callback + '(' + JSON.stringify(datafrom311) + ')').setMimeType(ContentService.MimeType.JAVASCRIPT)
     



application = webapp2.WSGIApplication([
    #('/', MainPage),
    ('/api/311.json', X311Page),
], debug=True)

