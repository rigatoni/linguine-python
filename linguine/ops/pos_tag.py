#!/usr/bin/env python
"""
Returns: A list of tuples pairing tokens, in order, to their POS tag
Given: A string containing a bunch of text.
Uses the Penn Treebank corpus to tag words (reasonably accurate, not the best)
Uses TextBlob's tagger implementation because NLTK is stupid and released a
broken tagger trainer for their 3.0 release.
"""
from textblob import TextBlob
class PosTag:
    def __init__(self):
        pass
    def run(self, data):
        results = []
        for corpus in data:
            blob = TextBlob(corpus.contents)
            results.append({'corpus_id': corpus.id, 'tags': blob.tags })
        return results