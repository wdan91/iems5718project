from google.appengine.ext import ndb    
from lessons.dom_injection import DomInjection, DomInjectionCheck
from lessons.sql_injection_1 import SqlInjection1
from lessons.concurrency import *
import json
import webapp2

# import users api
import os
import jinja2

# for logging message to server log
import logging
JINJA_ENVIRONMENT = jinja2.Environment(
    #loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    loader=jinja2.FileSystemLoader('templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


        
class MainHandler(webapp2.RequestHandler):
    def get(self):
        
        template_values = {
        }
        template = JINJA_ENVIRONMENT.get_template('welcome.html')
        self.response.write(template.render(template_values))
        
app = webapp2.WSGIApplication([    
    ('/', MainHandler),  
    ('/dom_injection',DomInjection),
    ('/sql_injection_1',SqlInjection1),
    ('/dom_injection/check',DomInjectionCheck),
    ('/concurrency',Concurrency),
    ('/concurrency/check',ConcurrencyCheck),
    ('/concurrency/lock',ConcurrencyLock),
    ('/concurrency/buy',ConcurrencyBuy),
    ('*.', MainHandler)
    ], debug=True)













