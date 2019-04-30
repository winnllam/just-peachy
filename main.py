import jinja2
import os
import webapp2

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)
# mainhandler is a type of RequestHandler
class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_template = jinja_env.get_template('templates/main.html')
        html = main_template.render()
        self.response.write(html)

class PCHandler(webapp2.RequestHandler):
    def get(self):
        post_template = jinja_env.get_template('templates/postcard.html')
        html = post_template.render()
        self.response.write(html)

class SNHandler(webapp2.RequestHandler):
    def get(self):
        night_template = jinja_env.get_template('templates/starrynight.html')
        html = night_template.render()
        self.response.write(html)

class MinHandler(webapp2.RequestHandler):
    def get(self):
        min_template = jinja_env.get_template('templates/minimalist.html')
        html = min_template.render()
        self.response.write(html)

class SSHandler(webapp2.RequestHandler):
    def get(self):
        ss_template = jinja_env.get_template('templates/sunset.html')
        html = ss_template.render()
        self.response.write(html)

class OcHandler(webapp2.RequestHandler):
    def get(self):
        oc_template = jinja_env.get_template('templates/oceans.html')
        html = oc_template.render()
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', MainHandler), # asking for slash, construct main handlers
    ('/postcard', PCHandler),
    ('/starrynight', SNHandler),
    ('/minimalist', MinHandler),
    ('/sunset', SSHandler),
    ('/oceans', OcHandler)
], debug = True)
