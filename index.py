import os
import datetime
import string
import userdb
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
	def get(self,var):
		user = users.get_current_user()
		if not user:
			self.redirect(users.create_login_url(self.request.uri))
		else:
			print userdb.userPlayStart(var)


class contestStop(webapp.RequestHandler):
	def get(self):
		self.response.out.write(userdb.userPlayStop())
		

class contestQuestion(webapp.RequestHandler):
	def get(self,var):
		user = users.get_current_user()
		if user:
			r = questiondb.getQuestion(var)
			self.response.out.write(r)

class contestAnswer(webapp.RequestHandler):
	def get(self):
		self.response.out.write(userdb.userAnswerSubmit(int(self.request.get('question')),
								self.request.get('answer')))

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

class adminQuestionsAnswered(webapp.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		query = userdb.userAnswer.all().order('elapsedTime')
		result = query.fetch(100)
		for ans in result:
			self.response.out.write(ans.user.nickname()+str(ans.question)+
									ans.answer+str(ans.elapsedTime)+"<br />")

class adminContestUsers(webapp.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		query = userdb.userPlay.all().order('startTime')
		result = query.fetch(100)
		for ans in result:
			self.response.out.write(ans.user.nickname()+ans.tathvaID+"<br />")
			self.response.out.write(ans.questionSet)
			self.response.out.write("<br />")

application = webapp.WSGIApplication(
									[('/', index),
									('/contest/start/(.*)|/',contestStart),
									('/contest/stop/',contestStop),
									('/contest/question/(\d)|/', contestQuestion),
									('/contest/answer/', contestAnswer),
									('/admin/questions/add/', adminQuestionsAdd),
									('/admin/questions/submit/', adminQuestionsSubmit),
									('/admin/questions/list/',adminQuestionsList),
									('/admin/questions/answered/',adminQuestionsAnswered),
									('/admin/contest/users/',adminContestUsers)],
									debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()
