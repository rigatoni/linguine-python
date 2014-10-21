#!/usr/bin/env python
"""
The Tornado server used to receive operation requests and deliver results to the user.
"""

from sys import stderr
from transaction import Transaction

"""
Check to ensure Tornado is installed
"""
try:
	import tornado.ioloop
	import tornado.web
except ImportError:
	sys.stderr.write("Tornado not found.")


class MainHandler(tornado.web.RequestHandler):
	def get(self):
		transaction = Transaction()
		if transaction.parse_json(self.request.body):
			self.write("useful output")
		else:
			self.write("Not a JSON file")

	
if __name__ == "__main__":
	application = tornado.web.Application([ 
		(r"/", MainHandler),
		])
	application.listen(5555)
	tornado.ioloop.IOLoop.instance().start()