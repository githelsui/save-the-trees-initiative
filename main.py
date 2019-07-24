#main.py
import webapp2
import jinja2
import os
from google.appengine.ext import ndb
from google.appengine.api import users

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# the handler section
class MainPage(webapp2.RequestHandler):
    def get(self):
        map_template = JINJA_ENVIRONMENT.get_template('templates/map.html')
        self.response.write(map_template.render())

        my_user = users.get_current_user()
        # user = users.get_current_user()
        # if user:
        #     nickname = user.nickname()
        #     logout_url = users.create_logout_url('/')
        #     greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
        #         nickname, logout_url)
        # else:
        #     login_url = users.create_login_url('/')
        #     greeting = '<a href="{}">Sign in</a>'.format(login_url)
        # self.response.write(
        #     '<html><body>{}</body></html>'.format(greeting))

# class EditInfo(webapp2.RequestHandler):
#     def get(self):
#         key_string = self.request.get('key')
#
# class ShowMemeHandler(webapp2.RequestHandler):
#     def get(self):
        # results_template = JINJA_ENVIRONMENT.get_template('templates/results.html')
        # meme_key = ndb.Key(urlsafe=self.request.get("key"))
        #
        # meme = meme_key.get()
        #
        #
        # the_variable_dict = {
        #     "title_color": "red",
        #     "line1": meme.top_text,
        #     "line2": meme.middle_text,
        #     "line3": meme.bottom_text,
        #     "img_url": meme.image_url,
        # }
        # self.response.write(results_template.render(the_variable_dict))

        #def post(self):
        # Access the user data via the form's input elements' names.
        # meme_first_line = self.request.get('user-first-ln')
        # meme_second_line = self.request.get('user-second-ln')
        # meme_third_line = self.request.get('user-third-ln')
        # meme_img_choice = self.request.get('meme-type')
        # pic_url = get_meme_url(meme_img_choice)
        #
        # new_meme = Meme(image_url=pic_url,
        #                 top_text=meme_first_line,
        #                 middle_text=meme_second_line,
        #                 bottom_text=meme_third_line)
        # meme_key = new_meme.put()
        # permalink_url = "/memeresult?key=%s" % (meme_key.urlsafe())
        # results_template = JINJA_ENVIRONMENT.get_template('templates/results.html')
        #
        # # Organize that user data into a dictionary.
        # the_variable_dict = {
        #     "line1": meme_first_line,
        #     "line2": meme_second_line,
        #     "line3": meme_third_line,
        #     "img_url": pic_url,
        #     "permalink_url": permalink_url,
        # }
        # self.response.write(results_template.render(the_variable_dict))

# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage),
    # ('/memeresult', ShowMemeHandler)
], debug=True)
