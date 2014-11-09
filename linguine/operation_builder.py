import sys
from linguine.transaction_exception import TransactionException
from linguine.ops.no_op import NoOp

def get_operation_handler(operation):
    if operation in globals():
        constructor = globals()[operation]
        return constructor()
    else:
        raise TransactionException("The requested operation does not exist.")
