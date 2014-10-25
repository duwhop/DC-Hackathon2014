import render
import webapp2

from resources import meal

# You probably want to put this template in a separate file,
# but this serves as an example for how you can use a template
# defined as a string rather than stored in another file.

TEMPLATE = '''<html>
<head>
  <title>Awesome People Meals</title>
</head>
<body>
  {% for meal in meals %}
  On {{meal.timestamp.strftime('%A, %B %d at %H:%M')}}, 
  {{meal.person}} ate {{meal.amount}} {{meal.food}} 
  <br />
  {% endfor %}
</body>
</html>
'''

class Handler(webapp2.RequestHandler):

  # Handles all HTTP GET requests to the '/meals' path
  def get(self):
    meals = None  # Define meal in function scope, but assign in if statements.
    person = self.request.get('name')
    if person:
      # Get meals for the person specified in the 'name' query parameter
      meals = meal.Meal.query(meal.Meal.person == person)
    else:
      # Get all of the meals
      meals = meal.Meal.query()
    # Remember, the results of the query is an iterable query object, so
    # you can treat it like a list in the template.
    template_values = {'meals': meals}      
    render.TextTemplateResponse(TEMPLATE, template_values, self.response)
