import sys
from linguine.transaction_exception import TransactionException
from linguine.ops.tfidf import Tfidf
from linguine.ops.no_op import NoOp
from linguine.ops.word_cloud_op import WordCloudOp
from linguine.ops.remove_caps import RemoveCapsGreedy
from linguine.ops.remove_caps import RemoveCapsPreserveNNP
from linguine.ops.remove_punct import RemovePunct

def get_operation_handler(operation):
    if operation == 'tfidf':
        return Tfidf()
    elif operation == 'wordcloudop':
    	return WordCloudOp()
    elif operation == 'noop':
    	return NoOp()
    elif operation == 'removecapsgreedy':
    	return RemoveCapsGreedy()
    elif operation == 'removecapsnnp':
    	return RemoveCapsPreserveNNP()
    elif operation == 'removepunct':
        return RemovePunct()
    else:
        raise TransactionException("The requested operation does not exist.")
