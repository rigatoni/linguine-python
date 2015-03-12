import sys
from linguine.transaction_exception import TransactionException
from linguine.ops.tfidf import Tfidf
from linguine.ops.no_op import NoOp
from linguine.ops.pos_tag import PosTag
from linguine.ops.word_cloud_op import WordCloudOp
from linguine.ops.remove_caps import RemoveCapsGreedy
from linguine.ops.remove_caps import RemoveCapsPreserveNNP
from linguine.ops.remove_punct import RemovePunct
from linguine.ops.stem import StemmerLancaster, StemmerPorter, StemmerSnowball
from linguine.ops.topic_model import TopicModel

def get_operation_handler(operation):
    if operation == 'tfidf':
        return Tfidf()
    elif operation == 'wordcloudop':
    	return WordCloudOp()
    elif operation == 'pos_tag':
        return PosTag()
    elif operation == 'stem_porter':
        return StemmerPorter()
    elif operation == 'stem_lancaster':
        return StemmerLancaster()
    elif operation == 'stem_snowball':
        return StemmerSnowball()
    elif operation == 'topic_model':
        return TopicModel()
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
