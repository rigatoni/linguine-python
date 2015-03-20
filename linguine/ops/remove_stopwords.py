#!/usr/bin/env python
"""
Returns: The corpus list, with tokenized contents generated
Given: Data containing a list of corpora to tokenize
Uses the Penn Treebank corpus for the WordTokenizeTreebank tokenization.
Uses the Stanford Tokenizer for WordTokenizeStanford.
WordTokenizeWhitespacePunct splits the text on whitespace and punctuation marks.
WordTokenizeSpaces splits the text using the space character as a delimiter.
WordTokenizeTabs splits the text using the tab character as a delimiter.
"""
from nltk.corpus import stopwords
from linguine.untokenize import untokenize
class RemoveStopwords:
    def __init__(self):
        pass
    def run(self, data):
        stopset = set(stopwords.words('english'))
    	for corpus in data:
	        corpus.tokenized_contents = [w for w in corpus.tokenized_contents if not w in stopset]
            corpus.contents = untokenize(corpus.tokenized_contents)
	    return data