
from google.appengine.ext import ndb    
import json
import webapp2

# import users api
from google.appengine.api import users
import os

# import module for templates
import jinja2
# for logging message to server log
import logging

JINJA_ENVIRONMENT = jinja2.Environment(
    #loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    loader=jinja2.FileSystemLoader('templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
class InsecureClientStorage(webapp2.RequestHandler):
    def get(self):
        template_values = {
                'islesson': True,
                'content':'You want to get the free trial but you do not have redeem code.',
                'hint':'Your goal should be to try to get to enable the activate button.Check the source code and see what you can do.',
                'solution':'delete disable'}
        template = JINJA_ENVIRONMENT.get_template('insecure_client_storage.html')
        self.response.write(template.render(template_values))
    def post(self):
        subTotal = self.request.get("subtot")
        grandTotal = self.request.get("grandtot")
        print subTotal
        print grandTotal
        if subTotal!=grandTotal:
            self.response.write("$('<p style=\'color:red\'>Congratulations!!!</p>').appendTo('#lessonContent'"); 
        else:
            self.error(400)

            

