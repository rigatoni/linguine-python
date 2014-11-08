import sys

from linguine.ops.no_op import no_op
from linguine.ops.tfidf import tfidf
from linguine.transaction_exception import TransactionException

def get_operation_handler(operation):
    if operation in globals():
        constructor = globals()[operation]
        return constructor()
    else:
        raise TransactionException("The requested operation does not exist.")
