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

class HiddenSection(webapp2.RequestHandler):
    def get(self):
        finished = False;
        template_values = {
                'finished' : finished,
                }
        template = JINJA_ENVIRONMENT.get_template('hidden_section.html')
        self.response.write(template.render(template_values))
    def post(self):
        finished = True;
        template_values = {
                'finished' : finished,
                }
        template = JINJA_ENVIRONMENT.get_template('hidden_section.html')
        self.response.write(template.render(template_values))

class HiddenSectionLogin(webapp2.RequestHandler):
    def post(self):
        username = self.request.POST.get("username")
        password = self.request.POST.get("password")
        ajax = self.request.POST.get("from")
        writeword = '$("#glassDiv").css("display", "block");'
        # writewordtt = 'document.cookie="name=ewd";'
        writewordt = '$("#glassDiv0").css("display", "block");'
        if ajax == "ajax":
            if username=="admin" and password=="keyofgod":
                self.response.write(writeword)
                # self.response.write(writewordtt)
            else:
                self.response.write(writewordt)
                # self.response.write(writewordtt)
        else: 
            return

