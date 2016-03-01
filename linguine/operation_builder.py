import sys
from linguine.transaction_exception import TransactionException
from linguine.ops.tfidf import Tfidf
from linguine.ops.no_op import NoOp
from linguine.ops.lemmatize import LemmatizerWordNet
from linguine.ops.pos_tag import PosTag
from linguine.ops.word_cloud_op import WordCloudOp
from linguine.ops.remove_caps import RemoveCapsGreedy
from linguine.ops.remove_caps import RemoveCapsPreserveNNP
from linguine.ops.remove_punct import RemovePunct
from linguine.ops.remove_stopwords import RemoveStopwords
from linguine.ops.sentence_tokenize import SentenceTokenize
from linguine.ops.stem import StemmerPorter
from linguine.ops.topic_model import TopicModel
from linguine.ops.word_tokenize import WordTokenizeTreebank, WordTokenizeWhitespacePunct, WordTokenizeStanford, WordTokenizeSpaces, WordTokenizeTabs
from linguine.ops.StanfordCoreNLP import StanfordCoreNLP

def get_operation_handler(operation):
    if operation == 'lemmatize_wordnet':
        return LemmatizerWordNet()
    elif operation == 'pos_tag':
        return PosTag()
    elif operation == 'removecapsgreedy':
        return RemoveCapsGreedy()
    elif operation == 'removecapsnnp':
        return RemoveCapsPreserveNNP()
    elif operation == 'removepunct':
        return RemovePunct()
    elif operation == 'remove_stopwords':
        return RemoveStopwords()
    elif operation == 'sentence_tokenize':
        return SentenceTokenize()
    elif operation == 'stem_porter':
        return StemmerPorter()
    elif operation == 'stem_lancaster':
        return StemmerLancaster()
    elif operation == 'stem_snowball':
        return StemmerSnowball()
    elif operation == 'tfidf':
        return Tfidf()
    elif operation == 'topic_model':
        return TopicModel()
    elif operation == 'wordcloudop':
        return WordCloudOp()
    elif operation == 'word_tokenize_treebank':
        return WordTokenizeTreebank()
    elif operation == 'word_tokenize_whitespace_punct':
        return WordTokenizeWhitespacePunct()
    elif operation == 'word_tokenize_stanford':
        return WordTokenizeStanford()
    elif operation == 'word_tokenize_spaces':
        return WordTokenizeSpaces()
    elif operation == 'word_tokenize_tabs':
        return WordTokenizeTabs()
    elif operation == 'nlp-pos':
        return StanfordCoreNLP(['pos'])
    elif operation == 'nlp-ner':
        return StanfordCoreNLP(['pos', 'ner'])
    elif operation == 'nlp-sentiment':
        return StanfordCoreNLP(['parse', 'sentiment'])
    elif operation == 'nlp-parse':
        return StanfordCoreNLP(['parse'])
    elif operation == 'noop':
        return NoOp()
    else:
        raise TransactionException("The requested operation does not exist.")
