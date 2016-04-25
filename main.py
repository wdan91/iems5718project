from google.appengine.ext import ndb    
from lessons.dom_injection import DomInjection, DomInjectionCheck
from lessons.sql_injection_1 import *
from lessons.sql_injection_2 import * 
from lessons.concurrency import *
from lessons.insecure_client_storage import *
from lessons.insecure_communication import *
from lessons.cookie_change import *
from lessons.hidden_section import *
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
    ('/sql_injection_knowledge',SqlInjectionKnowledge),
    ('/sql_injection_2',SqlInjection2),
    ('/sql_injection_2/check',SqlInjection2Check),
    ('/insecure_client_storage',InsecureClientStorage),
    ('/insecure_communication',InsecureCommunication),
    ('/insecure_communication_knowledge',InsecureCommunicationKnowledge),
    ('/insecure_communication/check',InsecureCommunicationCheck),
    ('/dom_injection/check',DomInjectionCheck),
    ('/concurrency',Concurrency),
    ('/concurrency/check',ConcurrencyCheck),
    ('/concurrency/lock',ConcurrencyLock),
    ('/concurrency/buy',ConcurrencyBuy),
    ('/hidden_section',HiddenSection),
    ('/hidden_section/login',HiddenSectionLogin),
    ('/cookie_change',CookieChange),
    ('/cookie_change/login',CookieChangeLogin),
    ('*.', MainHandler)
    ], debug=True)













