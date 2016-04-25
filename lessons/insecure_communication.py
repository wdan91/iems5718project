
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
class InsecureCommunicationKnowledge(webapp2.RequestHandler):
    def get(self):
        template_values = {
                'islesson': False,
        }
        template = JINJA_ENVIRONMENT.get_template('insecure_communication_knowledge.html')
        self.response.write(template.render(template_values))

class InsecureCommunication(webapp2.RequestHandler):
    def get(self):
        template_values = {
                'logged': False,
                'islesson': True,
                'content':'You want to get the free trial but you do not have redeem code.',
                'hint':'Your goal should be to try to get to enable the activate button.Check the source code and see what you can do.',
                'solution':'delete disable'}
        template = JINJA_ENVIRONMENT.get_template('insecure_communication.html')
        self.response.write(template.render(template_values))
    def post(self):
        userName = self.request.POST.get("username")
        password = self.request.POST.get("password")
        print userName 
        print password 
        if password == "iems5718" and userName=="admin":
            self.response.write("document.getElementById('logincontainer').innerHTML = \"<p>You are logged in as admin</p><p>&nbsp</p><div class='input-group'><input id='result' type='text' class='form-control' placeholder='What is the password?'><span class='input-group-btn'><button id='submit_result' class='btn btn-default' type='button'>Submit</button></span></div>\"");
        else:   
            self.error(400)

            

class InsecureCommunicationCheck(webapp2.RequestHandler):
    def post(self):
        password = self.request.POST.get("password")
        if password == "iems5718":
            self.response.write("$('<p style=\'color:red\'>Congratulations!!!</p>').appendTo('#lessonContent'"); 
        else:
            self.error(400)
        
