import json
import time
import linguine.operation_builder
from multiprocessing import Pool
from linguine.corpus import Corpus
from tornado import gen
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.errors import InvalidId
from linguine.database_adapter import DatabaseAdapter
from linguine.transaction_exception import TransactionException

class Transaction:
    def __init__(self, env=None):
        self.transaction_id = -1
        self.eta = None
        self.library = None
        self.operation = None
        self.user_id = None
        self.corpora_ids = []
        self.time_created = None
        self.corpora = []
        self.analysis_pool = Pool(processes=5)
        self.analysis_name = ""
        self.cleanups = []
        self.current_result = None
        self.tokenizer = None
        self.token_based_operations = ['tfidf','word_cloud_op',
                'stem_porter','stem_lancaster',
                'stem_snowball','lemmatize_wordnet']
    #Read in all corpora that are specified for a given transaction
    def read_corpora(self, corpora_ids):
        try:
            #load corpora from database
            corpora = DatabaseAdapter.getDB().corpus
            for id in self.corpora_ids:
                corpus = corpora.find_one({"_id" : ObjectId(id)})
                self.corpora.append(Corpus(id, corpus["title"],
                    corpus["contents"], corpus["tags"]))
        except (TypeError, InvalidId):
            raise TransactionException('Could not find corpus.')
    #Insert an analysis record into the database,
    # acknowledging that an analysis is to be processed.
    def create_analysis_record(self):
        analysis = {'user_id':ObjectId(self.user_id),
                    'analysis_name': self.analysis_name,
                    'corpora_ids':self.corpora_ids,
                    'cleanup_ids':self.cleanups,
                    'result': "",
                    'tokenizer': self.tokenizer,
                    'eta': self.eta,
                    'complete': False,
                    'time_created': self.time_created,
                    'analysis':self.operation}
        return DatabaseAdapter.getDB().analyses.insert(analysis)

    #Write result object to DB
    def write_result(self, result, analysis_id):
        analysis  = DatabaseAdapter.getDB().analyses.\
                find_one({"_id" : ObjectId(analysis_id)})

        analysis['complete'] = True
        analysis['result'] = result

        print("Analysis " + str(analysis_id) + " complete. submitting record to DB")

        DatabaseAdapter.getDB().analyses.update({'_id': ObjectId(analysis_id)} ,
                analysis);
    #Parse a JSON request from the linguine-node webserver,
    #Requesting that an analysis should be preformed
    def parse_json(self, json_data):
        try:
            input_data = json.loads(json_data.decode())

            self.transaction_id = input_data['transaction_id']
            self.operation = input_data['operation']
            self.library = input_data['library']
            self.analysis_name = input_data['analysis_name']
            self.time_created = input_data['time_created']

            if 'user_id' in input_data.keys():
                self.user_id = input_data['user_id']
            if 'cleanup' in input_data.keys():
                self.cleanups = input_data['cleanup']
            self.corpora_ids = input_data['corpora_ids']
            if 'tokenizer' in input_data.keys():
                self.tokenizer = input_data['tokenizer']

        except KeyError:
            raise TransactionException('Missing property transaction_id, \
                    operation, library, tokenizer or corpora_ids.')
        except ValueError:
            raise TransactionException('Could not parse JSON.')
    """
    Calculate the estimated time that a transaction will require to complete.
    this will be stored in the database record to display on the client
    """
    def calcETA(self, numTransactions):
      time = 0
      #For now, assume the transaction queue adds 30secs per transaction
      time += numTransactions * 30
      #Check which type of transaction is being preformed
      if "nlp" in self.operation:
          #A raw guess that a CoreNLP analysis will take 1 second per
          #10 words processed. 
          time += (len(self.corpora[0].contents.split(" ")) / 10)

      self.eta = time

    """
    Execute the given analysis that has been fetched from the thread pool
    @args: MainHandler - Instance of parent class that keeps track of
    num of Transactions
           analysis_id - unique identifier of this Transaction
    """
    def run(self, analysis_id, MainHandler):
        try:
            start = time.clock()
            corpora = self.corpora
            tokenized_corpora = []
            analysis = {}
            if not self.tokenizer == None and not self.tokenizer == '':
                op_handler = linguine.operation_builder \
                .get_operation_handler(self.tokenizer)
                tokenized_corpora = op_handler.run(corpora)
            for cleanup in self.cleanups:

                op_handler = linguine.operation_builder.\
                get_operation_handler(cleanup)
                corpora = op_handler.run(corpora)
                #Corpora must be re tokenized after each cleanup
                if not self.tokenizer == None and not self.tokenizer == '':
                  op_handler = linguine.operation_builder \
                  .get_operation_handler(self.tokenizer)
                  tokenized_corpora = op_handler.run(corpora)

            op_handler = linguine.operation_builder.\
                    get_operation_handler(self.operation)

            print("Preforming core operation for analysis " + str(analysis_id) + " with op " +str(op_handler))
            self.write_result(op_handler.run(corpora), str(analysis_id))

            #write transaction time to console 
            print(self.analysis_name,',', (time.clock() - start) * 1000)
            #Subtract one from analysis running count now that we're complete
            MainHandler.numTransactionsRunning -= 1

        except Exception as e:
            print("===========error==================")
            print(json.JSONEncoder().encode({'error': err.error}))
            print("===========end_error==================")

