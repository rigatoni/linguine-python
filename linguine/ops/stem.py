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
class StemmerPorter:
    def __init__(self):
        pass
    def run(self, data):
        porter = PorterStemmer()
        for corpus in data:
            corpusString = ""
            corpus.tokenized_contents = [porter.stem(word) for word in corpus.tokenized_contents]
            for index, word in enumerate(corpus.tokenized_contents):
                corpusString += corpus.tokenized_contents[index] + " "
            
            print(corpusString)
            corpus.contents = corpusString

        return data
