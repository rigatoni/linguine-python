#!/usr/bin/env python
"""
Returns: A list of strings produced by tokenizing the given data
Given: A string containing a bunch of text.
Uses the Penn Treebank corpus for the WordTokenizeTreebank tokenization.
Uses the Stanford Tokenizer for WordTokenizeStanford.
WordTokenizeWhitespacePunct splits the text on whitespace and punctuation marks.
WordTokenizeSpaces splits the text using the space character as a delimiter.
WordTokenizeTabs splits the text using the tab character as a delimiter.
"""
from nltk.tokenize import sent_tokenize
class SentenceTokenize:
    def __init__(self):
        pass
    def run(self, data):
        results = []
        for corpus in data:
            results.append({'corpus_id':corpus.id, 'sentences': sent_tokenize(corpus.contents) }) 
        return results