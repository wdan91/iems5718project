from google.appengine.ext import ndb    
from lessons.dom_injection import DomInjection, DomInjectionCheck
from lessons.sql_injection_1 import SqlInjection1
import json
import webapp2

# import users api
import os

# for logging message to server log
import logging


        
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello!<br>')
        self.response.write('Start your <a href="/edit/form">form</a>')        
        
app = webapp2.WSGIApplication([    
    ('/', MainHandler),  
    ('/dom_injection',DomInjection),
    ('/sql_injection_1',SqlInjection1),
    ('/dom_injection/check',DomInjectionCheck),
    ('*.', MainHandler)
    ], debug=True)
