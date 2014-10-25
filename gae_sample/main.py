"""Contains the main WSGI application for the application site."""
import logging

from handlers import home
from handlers import meals

import webapp2

app = webapp2.WSGIApplication(
    [
        ('/', home.Handler),
        ('/meals', meals.Handler)
    ]
)
