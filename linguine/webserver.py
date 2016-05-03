#!/usr/bin/env python
"""
The Tornado server used to receive operation requests and deliver results to the user.
"""
import json
import os

from sys import stderr
from linguine.transaction import Transaction
from concurrent.futures import ThreadPoolExecutor
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
    numTransactionsRunning = 0
    try:
        maxThreadPoolWorkers = int(os.environ['LINGUINE_THREADS'])
    except KeyError as err:
        maxThreadPoolWorkers = 2
    print("starting thread pool with " + str(maxThreadPoolWorkers) + " threads.")
    analysis_executor = ThreadPoolExecutor(max_workers=maxThreadPoolWorkers)

    def post(self):
        self.set_header('Content-Type', 'application/json')
        try:
            self.numTransactionsRunning+=1
            transaction = Transaction()
            requestObj = transaction.parse_json(self.request.body)
            transaction.read_corpora(transaction.corpora_ids)
            transaction.calcETA(self.numTransactionsRunning)
            analysis_id = transaction.create_analysis_record()

            #Generate response to server before kicking off analysis
            self.write(json.JSONEncoder().encode({'analysis_id': str(analysis_id)}))
            self.finish()

            #Encapsulate running of analysis in a future
            print("Submitting analysis " + str(analysis_id) + " to analysis queue")
            self.analysis_executor.submit(transaction.run, analysis_id, self)

        #Keep this error instance as a catch-all for all web requests
        except Exception as err:

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
