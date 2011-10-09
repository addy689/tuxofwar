# Python Timer
# @author: Phil Tysoe
# https://github.com/igniteflow

import datetime

class Timer(object):
	"""A simple timer class"""
	
	def __init__(self):
		pass
	
	def start(self):
		"""Starts the timer"""
		self.start = datetime.datetime.now()
		return self.start
	
	def stop(self, message="Total: "):
		"""Stops the timer.  Returns the time elapsed"""
		self.stop = datetime.datetime.now()
		return self.stop - self.start
	
	def now(self, message="Now: "):
		"""Returns the current time with a message"""
		return datetime.datetime.now()
	
	def elapsed(self, message="Elapsed: "):
		"""Time elapsed since start was called"""
		return datetime.datetime.now() - self.start
	
	def split(self, message="Split started at: "):
		"""Start a split timer"""
		self.split_start = datetime.datetime.now()
		return self.split_start
	
	def unsplit(self, message="Unsplit: "):
		"""Stops a split. Returns the time elapsed since split was called"""
		return datetime.datetime.now() - self.split_start
