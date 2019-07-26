from google.appengine.ext import ndb

class Tree(ndb.Model):
    lat = ndb.FloatProperty(required=True)
    long = ndb.FloatProperty(required=True)
    number = ndb.FloatProperty(required=True)
    user_id = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
