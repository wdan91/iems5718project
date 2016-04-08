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
class DomInjection(webapp2.RequestHandler):
    def get(self):
        template_values = {
                'islesson': True,
                'content':'You want to get the free trial but you do not have redeem code.',
                'hint':'Your goal should be to try to get to enable the activate button.Check the source code and see what you can do.',
                'solution':'delete disable'}
        template = JINJA_ENVIRONMENT.get_template('dom_injection.html')
        self.response.write(template.render(template_values))
    def post(self):
        self.response.write("$('<p style=\'color:red\'>Congratulations!!!</p>').appendTo('#lessonContent'"); 
class DomInjectionCheck(webapp2.RequestHandler):
    def get(self):
        MYKEY = "AKDXMFAOW123KSDF"
        key = self.request.get("key")
        ajax = self.request.get("from")
        if ajax == "ajax" and key == MYKEY:
            self.response.write("$('#warning').hide();$('#SUBMIT').attr('disabled',false);")
        else:
            self.error(400)
            self.response.out.write("$('#warning').show();$('#SUBMIT').attr('disabled',true);")
            
