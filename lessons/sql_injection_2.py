from google.appengine.ext import ndb    
import itertools
import json
import webapp2

# import users api
from google.appengine.api import users
import os
import MySQLdb

# import module for templates
import jinja2
# for logging message to server log
import logging

JINJA_ENVIRONMENT = jinja2.Environment(
    #loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    loader=jinja2.FileSystemLoader('templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
def dictfetchall(cursor):
    desc = cursor.description
    return [dict(itertools.izip([col[0] for col in desc], row))
                                 for row in cursor.fetchall()]
class SqlInjection2Check(webapp2.RequestHandler):
    def post(self):
        name = self.request.get("result")
        if name == "tiffany fletcher":
            succeed = "$(\"<p style=\'color:red\'>Congratulations!!!</p>\").appendTo('#lessonContent')" 
            self.response.write(succeed)
        else:
            self.error(400);

class SqlInjection2(webapp2.RequestHandler):
    def get(self):
        db = MySQLdb.connect(host='104.197.210.151', port=3306, user='root', passwd='Hv3F4qSX', db='sqlinjection')
        cursor = db.cursor()
        print os.path.dirname(__file__)
        for line in open(os.path.dirname(__file__)+'/sql/sql_injection_2.sql'):
            try:
                cursor.execute(line)
                db.commit()
            except:
                db.rollback()
        #query.replace('%20',' ')
        sql = 'select * from reviews'
            
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        numresults = int(cursor.rowcount)
        data = dictfetchall(cursor)
        cursor.close()
        db.close()

        for review in data:
            if review["is_anonymous"] == 1:
                review["name"]="anonymous"
        template_values = {
                'islesson': True,
                'content':'You want to get a sony camera at a very low price, say, 0.01 dollar.',
                'hint':'Try SQL injection',
                'solution':'\'; select name as review_title, name, content, is_anonymous from reviews; #',
                'reviews':data
        }
        template = JINJA_ENVIRONMENT.get_template('sql_injection_2.html')
        self.response.write(template.render(template_values))

    def post(self):
        db = MySQLdb.connect(host='104.197.210.151', port=3306, user='root', passwd='Hv3F4qSX', db='sqlinjection')
        cursor = db.cursor()
        query = self.request.get("query")
        querynew = query.split(';')
        print querynew[0]
        cursor.execute(querynew[0])
        db.commit()
        data = dictfetchall(cursor)

        for review in data:
            if review["is_anonymous"] == 1:
                review["name"]="anonymous"
                
        if querynew[1]!="":
            print querynew[1]
            cursor.execute(querynew[1])
            db.commit()
            data = dictfetchall(cursor)
        print data
        for review in data:
            if review["is_anonymous"] == 1:
                review["name"]="anonymous"
        success = ""
        datas = {
                'data': data,
                'succeed': success
                }
        jsonstring = json.dumps(datas)
        self.response.write(jsonstring)

        cursor.close()
        db.close()
