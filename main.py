#main.py
import webapp2
import jinja2
import json
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
        if my_user == None:
            self.redirect('/login')
        else:
            logout_url = users.create_logout_url('/')
            trees = Tree.query().filter(Tree.user_id == my_user.user_id()).fetch()
            dict_for_template = {
                'email': my_user.nickname(),
                'trees': trees,
                'logouturl': logout_url
                }
            self.response.write(map_template.render(dict_for_template))

    def post(self):
        map_template = JINJA_ENVIRONMENT.get_template('templates/map.html')
        my_user = users.get_current_user()
        logout_url = users.create_logout_url('/')
        self.response.write( logout_template.render( {'logouturl': logout_url} )  )

class LoginPage(webapp2.RequestHandler):
    def get(self):
        login_template = JINJA_ENVIRONMENT.get_template('templates/welcome.html')
        my_user = users.get_current_user()
        login_url = users.create_login_url('/')
        self.response.write( login_template.render( {'loginurl': login_url} )  )

class TreeHandler(webapp2.RequestHandler):
    def post(self):
        data = json.loads(self.request.body)
        m_lat = data["lat"]
        m_lng = data["lng"]
        my_user = users.get_current_user()
        my_userid = my_user.user_id()
        m_email = my_user.email()
        tree = Tree(lat=m_lat, long=m_lng, user_id=my_userid, email=m_email)
        tree.put()
# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/login', LoginPage),
    ('/tree', TreeHandler)
], debug=True)
