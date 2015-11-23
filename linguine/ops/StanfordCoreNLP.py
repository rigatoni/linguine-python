#!/usr/bin/env python
"""
Performs some core NLP operations as a proof of concept for the library.
"""

from stanford_corenlp_pywrapper import CoreNLP

class StanfordCoreNLP:
    def __init__(self):
        # I don't see anywhere to put properties like this path...
        # For now it's hardcoded and would need to be changed when deployed...
        self.proc = CoreNLP('pos', corenlp_jars=['/home/keegan/Programs/stanford-corenlp-full-2015-04-20/*'])

    def run(self, data):
        results = []
        for corpus in data:
            results.append(self.proc.parse_doc(corpus.contents))
        return results
