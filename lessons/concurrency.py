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

class Concurrency(webapp2.RequestHandler):
    def get(self):
        finished = False;
        template_values = {
                'islesson': True,
                'finished' : finished,
                'price1' : 3998,
                'price2' : 3998,
                'price3' : 2688,
                'price4' : 8888
                }
        template = JINJA_ENVIRONMENT.get_template('concurrency.html')
        self.response.write(template.render(template_values))

    # def post(self):
    #     finished = True;
    #     template_values = {
    #             'finished' : finished,
    #             'price1' : 3998,
    #             'price2' : 3998,
    #             'price3' : 2688,
    #             'price4' : 8888
    #             }
    #     template = JINJA_ENVIRONMENT.get_template('concurrency.html')
    #     self.response.write(template.render(template_values))


class ConcurrencyCheck(webapp2.RequestHandler):
    def get(self):
        price1 = 3998
        price2 = 3998
        price3 = 2688
        price4 = 8888
        qty1 = int(self.request.get("qty1"))
        qty2 = int(self.request.get("qty2"))
        qty3 = int(self.request.get("qty3"))
        qty4 = int(self.request.get("qty4"))
        totalprice = qty1*price1+qty2*price2+qty3*price3+qty4*price4
        ajax = self.request.get("from")
        writeword1 = "document.getElementById('subt1').innerHTML = '$ " + str(qty1*price1) + ".00';"
        writeword2 = "document.getElementById('subt2').innerHTML = '$ " + str(qty2*price2) + ".00';"
        writeword3 = "document.getElementById('subt3').innerHTML = '$ " + str(qty3*price3) + ".00';"
        writeword4 = "document.getElementById('subt4').innerHTML = '$ " + str(qty4*price4) + ".00';"
        if ajax == "ajax":
            self.response.write(writeword1)
            self.response.write(writeword2)
            self.response.write(writeword3)
            self.response.write(writeword4)
        else: 
            return

class ConcurrencyLock(webapp2.RequestHandler):
    def get(self):
        price1 = 3998
        price2 = 3998
        price3 = 2688
        price4 = 8888
        qty1 = int(self.request.get("qty1"))
        qty2 = int(self.request.get("qty2"))
        qty3 = int(self.request.get("qty3"))
        qty4 = int(self.request.get("qty4"))
        totalprice = qty1*price1+qty2*price2+qty3*price3+qty4*price4
        ajax = self.request.get("from")
        writeword = "document.getElementById('buysec').innerHTML = \"<th align='left' width='40%'></th><th width='30%'></th><th align='right' width='30%'><input id='buy' value='Buy!!!!!' type='button' onclick='buyit();' >\";"
        writewordt = "document.getElementById('total').innerHTML = 'Total: $ " + str(totalprice) + ".00';"
        writewordt2 = "document.getElementById('total').value =" + str(totalprice) + ";"
        if ajax == "ajax":
            self.response.write(writeword)
            self.response.write(writewordt)
            self.response.write(writewordt2)
        else: 
            return

class ConcurrencyBuy(webapp2.RequestHandler):
    def post(self):
        price1 = 3998
        price2 = 3998
        price3 = 2688
        price4 = 8888
        qty1 = int(self.request.POST.get("qty1"))
        qty2 = int(self.request.POST.get("qty2"))
        qty3 = int(self.request.POST.get("qty3"))
        qty4 = int(self.request.POST.get("qty4"))
        totalprice = qty1*price1+qty2*price2+qty3*price3+qty4*price4
        paytotal = int(self.request.POST.get("total"))
        ajax = self.request.POST.get("from")
        writewordsucc = "document.getElementById('information').innerHTML = 'You are so smart!! Congratulations!!!';"
        writewordeq = "document.getElementById('information').innerHTML = 'You are an upright man!! Thank you!!';"
        writewordover = "document.getElementById('information').innerHTML = 'You must be a rich man!! Money means nothing to you!!!';"
        ale = "alert('"+str(paytotal)+"?"+str(totalprice)+"');"
        if ajax == "ajax":
            if  paytotal < totalprice:
                self.response.write(writewordsucc)
            elif paytotal == totalprice:
                self.response.write(writewordeq)
            else:
                self.response.write(writewordover)
        else: 
            return