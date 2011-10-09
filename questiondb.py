# Model Defining Questions Database
import string
from google.appengine.ext import db
class question(db.Model):
	questionNumber = db.IntegerProperty(required=True)
	question = db.StringProperty(required=True, multiline=True)
	qimage = db.StringProperty(required=True)
	opt1 = db.StringProperty(required=True, multiline=True)
	opt2 = db.StringProperty(required=True, multiline=True)
	opt3 = db.StringProperty(required=True, multiline=True)
	opt4 = db.StringProperty(required=True, multiline=True)
	ans = db.StringProperty(required=True)
	
def getQuestion(num):
	query = question.all()
	result = query.fetch(45)
	for q in result:
		if q.questionNumber == string.atoi(num):
			return ("{"+
					"\"question\" : " + "\""+q.question.replace('\n','<br />')+"\""+","+
					"\"options\" : " + "["+
										"\""+q.opt1+"\""+","+
										"\""+q.opt2+"\""+","+
										"\""+q.opt3+"\""+","+
										"\""+q.opt4+"\""+
										"]"+
					"}")
