#!/usr/bin/env python
"""
Removes all nonessential punctuation from a text.
Returns the text as a single string separated by spaces.
"""
from nltk.tokenize import RegexpTokenizer
class RemovePunct:
    def run(self, data):
        tokenizer = RegexpTokenizer(r'((?<=[^\w\s])\w(?=[^\w\s])|(\W))+', gaps=True)
        return " ".join(tokenizer.tokenize(data))
