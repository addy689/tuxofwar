import os
import time
import simplejson as json
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class index(webapp.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		path = os.path.join(os.path.dirname(__file__), 'templates/index.html')
		self.response.out.write(template.render(path,""))

class contestStart(webapp.RequestHandler):
	def get(self):
		self.response.out.write(time.time())
		self.response.out.write("<br />")
		self.response.out.write(time.time()-1317815757.3)
	
class contestQuestion(webapp.RequestHandler):
	def get(self,var):
		user = users.get_current_user()
		if user:
			self.response.headers['Content-Type'] = 'text/plain'
			#self.response.out.write('Hello, ' + user.nickname())
			self.response.out.write(json.dumps({"question": var, "opt1": "man", "opt2": "cat", "opt3": "touch", "opt4": "does"}))
			#self.response.out.write(json.dumps(m))
		else:
			self.redirect(users.create_login_url(self.request.uri))

class admin(webapp.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		path = os.path.join(os.path.dirname(__file__), 'templates/question.html')
		self.response.out.write(template.render(path,""))

class adminSubmitQuestions(webapp.RequestHandler):
	def post(self):
		self.response.out.write(self.request.get('ques'))

application = webapp.WSGIApplication(
									[('/', index),
									('/contest/start(|/)',contestStart),
									('/contest/question/(\d)/', contestQuestion),
									('/admin/', admin),
									('/admin/submit/questions/', adminSubmitQuestions)],
									debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()
