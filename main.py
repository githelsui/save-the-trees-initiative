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
            othertrees = Tree.query().filter(Tree.user_id != my_user.user_id()).fetch()
            dict_for_template = {
                'email': my_user.nickname(),
                'trees': trees,
                'containertype': "tree-container",
                'headermessage': "Trees you've saved: ",
                'loadmytrees': "true",
                'othertrees':othertrees,
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
        latlng = data["coordinates"]
        m_lat = latlng["lat"]
        m_lng = latlng["lng"]
        number = data["number"]
        date = data['date']
        my_user = users.get_current_user()
        my_userid = my_user.user_id()
        m_email = my_user.nickname()
        # current_user = Planter.query().filter(Planter.user_id == my_userid).fetch()[0]
        # current_user.numberOfTrees = numberOfTrees
        # current_user.put()
        tree = Tree(lat=m_lat, long=m_lng, number=number, user_id=my_userid, email=m_email, date=date)
        tree.put()

class CommunityHandler(webapp2.RequestHandler):
    def get(self):
        map_template = JINJA_ENVIRONMENT.get_template('templates/map.html')
        my_user = users.get_current_user()
        if my_user == None:
            self.redirect('/login')
        else:
            logout_url = users.create_logout_url('/')
            alltrees = Tree.query().fetch()

            trees_per_user = {}
            # {'gith': 8,
            # 'gith': 9,
            # 'sam': 10}
            for tree in alltrees:
                if tree.email not in trees_per_user:
                    trees_per_user[tree.email] = tree.number #adds email key only once
                elif tree.number > trees_per_user[tree.email]: #swaps key's value if greater than
                    trees_per_user[tree.email] = tree.number


            # for key, value in trees_per_user.iteritems():
            #     if key


            trees = Tree.query().filter(Tree.user_id == my_user.user_id()).fetch()
            othertrees = Tree.query().filter(Tree.user_id != my_user.user_id()).fetch()
            dict_for_template = {
                'email': my_user.nickname(),
                'trees': trees,
                'othertrees':othertrees,
                'loadmytrees': "false",
                'containertype': "leaderboard-container",
                'headermessage': "Community Leaderboard",
                'logouturl': logout_url,
                'planters': trees_per_user
                }
            self.response.write(map_template.render(dict_for_template))

# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/login', LoginPage),
    ('/tree', TreeHandler),
    ('/community', CommunityHandler),
], debug=True)
