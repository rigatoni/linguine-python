#!/usr/bin/env python
"""
The Tornado server used to receive operation requests and deliver results to the user.
"""
import json

from sys import stderr
from linguine.transaction import Transaction
from linguine.transaction_exception import TransactionException

"""
Check to ensure Tornado is installed
"""
try:
    import tornado.ioloop
    import tornado.web
except ImportError:
    sys.stderr.write("Tornado not found.")

class MainHandler(tornado.web.RequestHandler):

    def post(self):
        self.set_header('Content-Type', 'application/json')
        try:
            print(self.request.body)
            transaction = Transaction()
            transaction.parse_json(self.request.body)
            self.write(transaction.run())
        except TransactionException as err:

            print("===========error==================")
            print(json.JSONEncoder().encode({'error': err.error})) 
            print("===========end_error==================")
            self.set_status(err.code)
            self.write(json.JSONEncoder().encode({'error': err.error}))

if __name__ == "__main__":

    try:
        application = tornado.web.Application([(r"/", MainHandler)])
        application.listen(5555)
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        pass
