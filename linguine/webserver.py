#!/usr/bin/env python
"""
The Tornado server used to receive operation requests and deliver results to the user.
"""
import json

from sys import stderr
from linguine.transaction import Transaction
from linguine.transaction_exception import TransactionException
from tornado import gen

"""
Check to ensure Tornado is installed
"""
try:
    import tornado.ioloop
    import tornado.web
except ImportError:
    sys.stderr.write("Tornado not found.")

class MainHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def post(self):
        self.set_header('Content-Type', 'application/json')
        try:
            transaction = Transaction()
            requestObj = transaction.parse_json(self.request.body)
            transaction.read_corpora(transaction.corpora_ids)
            analysis_id = transaction.create_analysis_record()

            #Generate response to server before kicking off analysis
            self.write(json.JSONEncoder().encode({'analysis_id': str(analysis_id)}))
            self.finish()

            #Encapsulate running of analysis in a future
            result = yield transaction.run()

            transaction.write_result(result, analysis_id)
            

        except TransactionException as err:
            self.set_status(err.code)
            self.write(json.JSONEncoder().encode({'error': err.error}))

if __name__ == "__main__":
    try:
        application = tornado.web.Application([(r"/", MainHandler)])
        application.listen(5555)
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        pass
