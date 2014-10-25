from google.appengine.ext import ndb


class Meal(ndb.Model):
  person = ndb.StringProperty(required=True)
  food = ndb.StringProperty(required=True)
  amount = ndb.IntegerProperty(required=True)
  timestamp = ndb.DateTimeProperty(auto_now_add=True)
