import webapp2
from google.appengine.ext.webapp import template


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(template.render('index.html', {}))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
