import render
import webapp2

from resources import meal

class Handler(webapp2.RequestHandler):

  # Handles all HTTP GET requests sent to the '/' path.
  def get(self):
    names = ['Sabrina', 'Travis', 'Storm', 'Wolverine', 'Cyclops']
    template_values = {'names': names}
    render.TemplateResponse('home.html', template_values, self.response)

  # Handles all HTTP POST requests sent to the '/' path.
  def post(self):
    food = self.request.get('food')
    amount = self.request.get('amount')
    name = self.request.get('name')
    meal.Meal(person=name, food=food, amount=int(amount)).put()
    self.redirect('/meals?name={0}'.format(name))
