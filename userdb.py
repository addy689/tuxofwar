#User operations and database

import random
import string
import datetime
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.api import users

def generateSet():
	a = []
	for i in range(45):
		a.append(i+1)
	random.shuffle(a)
	return a

class userPlay(db.Model):
	user = db.UserProperty(required=True)
	questionSet = db.ListProperty(int)
	tathvaID = db.StringProperty(required=True)
	startTime = db.DateTimeProperty(required=True)
	endTime = db.DateTimeProperty

def userPlayExist():
	query = userPlay.all()
	u = query.filter('user = ', users.get_current_user()).get()
	if not u:
		return False
	else:
		return True

def userPlayStart(tid):
	if not userPlayExist():
		u = userPlay(user = users.get_current_user(),
					questionSet = generateSet(),
					tathvaID = tid,
					startTime = datetime.datetime.now())
		u.put()
		return u.user.nickname() + u.tathvaID
	else:
		print "Error. Contest already started."

def userPlayStop():
	query = userPlay.all()
	u = query.filter('user = ', users.get_current_user()).get()
	if not u.endTime:
		u.endTime = datetime.datetime.now()
		u.put()
	return u.user.nickname() + u.tathvaID + str(u.endTime)

def userElapsedTime():
	query = userPlay.all()
	u = query.filter('user = ', users.get_current_user()).get()
	return ((datetime.datetime.now() - u.startTime).microseconds/1000)

def userSetQuestion(num):
	query = userPlay.all()
	u = query.filter('user = ', users.get_current_user()).get()
	return u.questionSet[num-1]

class userAnswer(db.Model):
	user = user = db.UserProperty(required=True)
	question = db.IntegerProperty(required=True)
	answer = db.StringProperty(required=True)
	elapsedTime = db.IntegerProperty(required=True)

def userAnswerSubmit(ques,ans):
	a = userAnswer(user = users.get_current_user(),
					question = ques,
					answer = ans,
					elapsedTime = userElapsedTime())
	a.put()
	return str(ques) + ans + str(userElapsedTime())



