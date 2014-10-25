import os

import jinja2

################################ IGNORE: START ################################
# This statement will cause jinja to look for templates in the 'templates' 
# directory.
jinja = jinja2.Environment(
    loader=jinja2.FileSystemLoader(
        os.path.join(os.path.dirname(__file__), 'templates')))


# Helper function; you probably don't want to use this directly.
def TemplateString(template_name, template_values):
  t = jinja.get_template(template_name)
  return t.render(template_values)


# Helper function; you probably don't want to use this directly.
def Template(template_name, template_values, output_stream):
  output_stream.write(TemplateString(template_name, template_values))

################################# IGNORE: END #################################

# Writes the given text to the response. Use to display simple text 
# on the page.
#
# Example:
#   render.Text('Hello, world!!', self.response)
def TextResponse(text, response):
  response.out.write(text)


# Executes the provided template text and writes the resulting string to the
# provided output stream. In this function, the template text is a string
# rather than reading it from a file.
#
# Example:
#    template = 'Hello, {{name}}'
#    template_values = {'name': 'Sabrina'}
#    render.TemplateText(template, template_values, self.response)
def TextTemplateResponse(template_string, template_values, response):
  t = jinja.from_string(template_string)
  response.out.write(t.render(template_values))

# Looks in the templates folder for a file with the name provided in template_name.
# The template gets executed with the given template_values and writes the resulting
# string out to the given response object.
# 
# Example:
#    template_values = {
#        'key1': 'value1',
#        'key2': 'value2'
#    }
#    render.TemplateResponse('home.html', template_values, self.response)  
def TemplateResponse(template_name, template_values, response):
  Template(template_name, template_values, response.out)
