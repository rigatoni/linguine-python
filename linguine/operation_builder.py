import sys
from linguine.transaction_exception import TransactionException
from linguine.ops.tfidf import Tfidf
from linguine.ops.no_op import NoOp
from linguine.ops.word_cloud_op import WordCloudOp
def get_operation_handler(operation):
    if operation == 'tfidf':
        return Tfidf()
    elif operation == 'wordcloudop':
    	return WordCloudOp()
    elif operation == 'noop':
    	return NoOp()
    else:
        raise TransactionException("The requested operation does not exist.")
