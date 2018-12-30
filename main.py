import jinja2
import os
import webapp2

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)
# mainhandler is a type of RequestHandler
class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_template = jinja_env.get_template('main.html')
        html = main_template.render()
        self.response.write(html)

class PostCardHandler(webapp2.RequestHandler):
    def get(self):
        post_template = jinja_env.get_template('postcard/postcard.html')
        html = post_template.render()
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', MainHandler), # asking for slash, construct main handlers
    ('/postcard', PostCardHandler)
], debug = True)
