#!/usr/bin/env python
import os

"""
Performs some core NLP operations as a proof of concept for the library.
"""

from stanford_corenlp_pywrapper import CoreNLP

class StanfordCoreNLP:
    def __init__(self):
        # I don't see anywhere to put properties like this path...
        # For now it's hardcoded and would need to be changed when deployed...
        
        coreNLPPath = os.path.join(os.path.dirname(__file__), '../../lib/stanfordCoreNLP.jar')
        coreNLPModelsPath = os.path.join(os.path.dirname(__file__), '../../lib/stanfordCoreNLPModels.jar')
        self.proc = CoreNLP('pos', corenlp_jars=[coreNLPPath, coreNLPModelsPath])

    def run(self, data):
        results = []
        for corpus in data:
            results.append(self.proc.parse_doc(corpus.contents))
        return results
