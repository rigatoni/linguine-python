#!/usr/bin/env python
"""
Removes all nonessential punctuation from a text.
Returns the text as a single string separated by spaces.
"""
from nltk.tokenize import RegexpTokenizer
class remove_punct:
    def run(self, data):
        tokenizer = RegexpTokenizer(r'((?<=[^\w\s])\w(?=[^\w\s])|(\W))+', gaps=True)
        return " ".join(tokenizer.tokenize(data))

"""
Test code follows below: to be added to unit test suite.     

s = '''He said,"that's it." *u* Hello, World. O'Rourke is rockin'.'''
a = remove_punct()
print(a.run(s))
"""