#!/usr/bin/env python
"""
Returns: A list of words that have been stemmed using the chosen method
Given: A list of strings representing a tokenized collection of words.
There are three stemming algorithms available: The Porter stemmer,
the Lancaster stemmer, and the Snowball stemmer.
"""
from nltk.stem.snowball import EnglishStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.porter import PorterStemmer
class StemmerSnowball:
    def __init__(self):
        pass
    def run(self, data):
    	english = EnglishStemmer()
    	results = []
        for corpus in data:
	        corpus.tokenized_contents = [english.stem(word) for word in corpus.tokenized_contents]
            corpus.contents = ''.join(corpus.tokenized_contents)
	        results.append(corpus)
	    return results
class StemmerLancaster:
    def __init__(self):
        pass
    def run(self, data):
    	lancaster = LancasterStemmer()
    	results = []
        for corpus in data:
        	corpus.tokenized_contents = [lancaster.stem(word) for word in corpus.tokenized_contents]
            corpus.contents = ''.join(corpus.tokenized_contents)
        	results.append(corpus)
        return results
class StemmerPorter:
    def __init__(self):
        pass
    def run(self, data):
    	porter = PorterStemmer()
    	results = []
        for corpus in data:
        	corpus.tokenized_contents = [porter.stem(word) for word in corpus.tokenized_contents]
            corpus.contents = ''.join(corpus.tokenized_contents)
        	results.append(corpus)
        return results