# Model Defining Questions Database
from google.appengine.ext import db
class question(db.Model):
	questionNumber = db.IntegerProperty(required=True)
	question = db.StringProperty(required=True)
	qimage = db.StringProperty(required=True)
	opt1 = db.StringProperty(required=True)
	opt2 = db.StringProperty(required=True)
	opt3 = db.StringProperty(required=True)
	opt4 = db.StringProperty(required=True)
	ans = db.StringProperty(required=True)
	
