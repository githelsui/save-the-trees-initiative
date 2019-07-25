#main.py
import webapp2
import jinja2
import os
from google.appengine.ext import ndb
from models import Tree
from google.appengine.api import users

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# the handler section
class MainPage(webapp2.RequestHandler):
    def get(self):
        map_template = JINJA_ENVIRONMENT.get_template('templates/map.html')
        my_user = users.get_current_user()
        #map_url = users.create_map_url('/')
        #self.response.write(map_template.render({'mapurl': map_url}))
        if my_user:
            logout_url = users.create_logout_url('/')
            self.response.write(map_template.render())
        else:
            self.redirect('/login')

    def post(self):
        map_template = JINJA_ENVIRONMENT.get_template('templates/map.html')
        my_user = users.get_current_user()
        #map_url = users.create_map_url('/')
        #self.response.write(map_template.render({'mapurl': map_url}))
        if my_user:
            logout_url = users.create_logout_url('/')
            self.response.write(map_template.render())
        else:
            self.redirect('/login')



class LoginPage(webapp2.RequestHandler):
    def get(self):
        login_template = JINJA_ENVIRONMENT.get_template('templates/welcome.html')
        my_user = users.get_current_user()
        login_url = users.create_login_url('/')
        self.response.write( login_template.render( {'loginurl': login_url} )  )

    def post(self):
        login_template = JINJA_ENVIRONMENT.get_template('templates/welcome.html')
        my_user = users.get_current_user()
        login_url = users.create_login_url('/')
        self.response.write( login_template.render( {'loginurl': login_url} )  )

# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/login', LoginPage)
], debug=True)
