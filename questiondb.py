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
	q = query.filter('questionNumber =',num).get()
	if q:
		return ("{"+
				"\"question\" : "+"\""+q.question.replace('\n','<br />')+"\""+","+
				"\"image\" : "+"\""+q.qimage+"\""+","+ 
				"\"options\" : " + "["+
									"\""+q.opt1.replace('\n','<br />')+"\""+","+
									"\""+q.opt2.replace('\n','<br />')+"\""+","+
									"\""+q.opt3.replace('\n','<br />')+"\""+","+
									"\""+q.opt4.replace('\n','<br />')+"\""+
									"]"+
				"}")
