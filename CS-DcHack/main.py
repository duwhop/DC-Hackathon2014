import httplib2
import logging
import os
import cgi
import pickle
import urllib2
import httplib
import json
import datetime
import mimetypes

#from apiclient.discovery import build
#from oauth2client.appengine import oauth2decorator_from_clientsecrets
#from oauth2client.client import AccessTokenRefreshError
#from oauth2client.client import Credentials
from apiclient.http import MediaFileUpload
from google.appengine.api import memcache
from google.appengine.api import users
from google.appengine.api import images
from google.appengine.ext import ndb
import webapp2
import jinja2
import oauth2client.appengine
import oauth2client.client


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    autoescape=True,
    extensions=['jinja2.ext.autoescape'])

class User(ndb.Model):
    username = ndb.UserProperty()
    top = ndb.JsonProperty(required=True)
    bottom = ndb.JsonProperty(required=True)
    shoes = ndb.JsonProperty(required=True)

    
class QueryTest(webapp2.RequestHandler):
    def get(self):
        #query = db.Query(User)
        requestQuery = User.query(User.username == users.get_current_user())
        response = requestQuery.get()
        self.response.out.write(dir(response))
        self.response.out.write(json.dumps(response.top))
    
class MainPage(webapp2.RequestHandler):
    def get(self):
        currentUser = users.get_current_user()
        if currentUser:
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                          (currentUser.nickname(), users.create_logout_url('/')))
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                        users.create_login_url('/'))
                        
        template = JINJA_ENVIRONMENT.get_template('home.html')
        self.response.write(template.render({'greeting': greeting}))
        
class FormHandler(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        template = JINJA_ENVIRONMENT.get_template('choose-outfit.html')
        self.response.write(template.render({'user': user}))
    
class ImagesHandler(webapp2.RequestHandler):

    def post(self):
        day = cgi.escape(self.request.get('day_of_week'))
        top_category = cgi.escape(self.request.get('top_category'))
        top_presence = cgi.escape(self.request.get('top_presence'))
        top_color_presence = cgi.escape(self.request.get('top_color_presence'))
        top_clothing_color = cgi.escape(self.request.get('top_clothing_color'))
        #top_img = cgi.escape(self.request.get('top_img'))
        bot_category = cgi.escape(self.request.get('bot_category'))
        bot_presence = cgi.escape(self.request.get('bot_presence'))
        bot_color_presence = cgi.escape(self.request.get('bot_color_presence'))
        bot_clothing_color = cgi.escape(self.request.get('bot_clothing_color'))
        #bot_img = cgi.escape(self.request.get('bot_img'))
        shoe_type = cgi.escape(self.request.get('shoe_type'))
        shoe_color = cgi.escape(self.request.get('shoe_color'))
        #shoe_img = cgi.escape(self.request.get('shoe_img'))
        query = User.query(User.username == users.get_current_user())
        response = query.get()
        if not response:
            newUser = User()
            newUser.top = {}
            newUser.bottom = {}
            newUser.shoes = {}
        else:
            newUser = User()
        newUser.username = users.get_current_user()
        date = datetime.datetime.now().strftime("%m%d%y")
        if not newUser.top:
            newUser.top = {}
        if date not in newUser.top:
            newUser.top[date] = []
        newUser.top[date].append({"day": day,
                        "top_category": top_category,
                        "top_presence": top_presence,
                        "top_color_presence": top_color_presence,
                        "top_clothing_color": top_clothing_color,
                        "top_img": "",                        
                      })
        if not newUser.bottom:
            newUser.bottom = {}
        if date not in newUser.bottom:
            newUser.bottom[date] = []
        newUser.bottom[date].append({"day": day,
                        "bot_category": bot_category,
                        "bot_presence": bot_presence,
                        "bot_color_presence": bot_color_presence,
                        "bot_clothing_color": bot_clothing_color,
                        "bot_img": "",
                        })
        if not newUser.shoes:
            newUser.shoes = {}
        if date not in newUser.shoes:
            newUser.shoes[date] = []
        newUser.shoes[date].append({"day": day,
                        "shoe_type": shoe_type,
                        "shoe_color": shoe_color,
                        })
        newUser.put()
        #html = '<html><body><h1>Thank you for Submitting</h1></body></html>' 
        #self.response.out.write(html)
        template = JINJA_ENVIRONMENT.get_template('images.html')
        self.response.write(template.render())
             

class AboutHandler(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('about.html')
        self.response.write(template.render())

class homeHandler(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('home.html')
        self.response.write(template.render())
    

class contactHandler(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('contact.html')
        self.response.write(template.render())

class chooseOutfitHandler(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('choose-outfit.html')
        self.response.write(template.render())

class rateOutfitHandler(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('outfit-feedback.html')
        self.response.write(template.render())

"""class imagesHandler(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('images.html')
        self.response.write(template.render())
"""         
 
class ThanksHandler(webapp2.RequestHandler):

    def post(self):
        user = users.get_current_user()
        template = JINJA_ENVIRONMENT.get_template('thank_you.html')
        self.response.write(template.render({'user': user}))
        
application = webapp2.WSGIApplication(
    [
        ('/', MainPage),
        ('/outfitform', FormHandler),
        ('/query_test', QueryTest),
        ('/about', AboutHandler),
        ('/home', homeHandler),
        ('/contact', contactHandler),
        ('/choose-outfit', chooseOutfitHandler),
        ('/rateOutfit', rateOutfitHandler),
        ('/images', ImagesHandler),
        ('/thank_you', ThanksHandler)
    ],
                              debug=True)
