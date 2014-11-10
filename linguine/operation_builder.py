import sys
from linguine.transaction_exception import TransactionException
from linguine.ops.tfidf import Tfidf
from linguine.ops.no_op import NoOp

def get_operation_handler(operation):
    if operation == 'tfidf':
        return Tfidf()
    else:
        raise TransactionException("The requested operation does not exist.")
