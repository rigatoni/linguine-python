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
        return [english.stem(word) for word in data]
class StemmerLancaster:
    def __init__(self):
        pass
    def run(self, data):
    	lancaster = LancasterStemmer()
        return [lancaster.stem(word) for word in data]
class StemmerPorter:
    def __init__(self):
        pass
    def run(self, data):
    	porter = PorterStemmer()
        return [porter.stem(word) for word in data]