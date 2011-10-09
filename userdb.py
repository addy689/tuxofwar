#User operations and database

import random
import string
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
	endTime = db.IntegerProperty

def userPlayStart(tid,stime):
	u = userPlay(user = users.get_current_user(),
				questionSet = generateSet(),
				tathvaID = tid,
				startTime = stime)
	u.put()
	return u.user.nickname() + u.tathvaID

def userPlayStop(etime):
	query = userPlay.all()
	u = query.filter('user = ', users.get_current_user()).get()
	u.endTime = etime
	u.put()
	return u.user.nickname() + u.tathvaID + str(u.endTime)

class userAnswers(db.Model):
	user = user = db.UserProperty(required=True)
	question = db.IntegerProperty(required=True)
	answer = db.StringProperty(required=True)
	elapsedTime = db.IntegerProperty(required=True)

