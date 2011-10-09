import os
import time
import string
import questiondb
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
		#user = users.get_current_user()
		#if user:
			self.response.headers['Content-Type'] = 'plain/text'
			r = questiondb.getQuestion(var)
			self.response.out.write(r)
		#else:
			#self.redirect(users.create_login_url(self.request.uri))

class adminQuestionsAdd(webapp.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		path = os.path.join(os.path.dirname(__file__), 'templates/question.html')
		self.response.out.write(template.render(path,""))

class adminQuestionsSubmit(webapp.RequestHandler):
	def post(self):
		q = questiondb.question(questionNumber=string.atoi(self.request.get('qno')),
								question=self.request.get('ques'),
								qimage=self.request.get('qimg'),
								opt1=self.request.get('opt1'),
								opt2=self.request.get('opt2'),
								opt3=self.request.get('opt3'),
								opt4=self.request.get('opt4'),
								ans=self.request.get('ans'))
		q.put()

class adminQuestionsList(webapp.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		query = questiondb.question.all()
		result = query.fetch(5)
		template_values = { 'questions' : result }
		path = os.path.join(os.path.dirname(__file__), 'templates/questionlist.html')
		self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication(
									[('/', index),
									('/contest/start(|/)',contestStart),
									('/contest/question/(\d)/', contestQuestion),
									('/admin/questions/add/', adminQuestionsAdd),
									('/admin/questions/submit/', adminQuestionsSubmit),
									('/admin/questions/list/',adminQuestionsList)],
									debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()
