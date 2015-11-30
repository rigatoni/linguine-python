#!/usr/bin/env python
import os

"""
Performs some core NLP operations as a proof of concept for the library.
"""

from stanford_corenlp_pywrapper import CoreNLP

class StanfordCoreNLP:

    proc = None
    
    """
    When the JSON segments return from the CoreNLP library, they
    separate the data acquired from each word into their own element.

    For readability's sake, it would be nice to pair all of the information
    for a given word with that word, making a list of words with their 
    part of speech tags
    """
    def jsonCleanup(self, data):
      for corpus in data:
          res = StanfordCoreNLP.proc.parse_doc(corpus.contents)
          for sentence in res["sentences"]:
            words = [] 
            for index, token in enumerate(sentence["tokens"]):
              word = {}

              word["token"] = sentence["tokens"][index]
              word["lemma"] = sentence["lemmas"][index]
              word["part-of-speech"] = sentence["pos"][index]

              words.append(word)

      return words


    def __init__(self):
        coreNLPPath = os.path.join(os.path.dirname(__file__), '../../lib/stanfordCoreNLP.jar')
        coreNLPModelsPath = os.path.join(os.path.dirname(__file__), '../../lib/stanfordCoreNLPModels.jar')
        if StanfordCoreNLP.proc == None:
            StanfordCoreNLP.proc = CoreNLP(configdict={'annotators':'tokenize, ssplit, pos, lemma, ner, parse, dcoref'}, corenlp_jars=[coreNLPPath, coreNLPModelsPath])

    def run(self, data):
        return self.jsonCleanup(data) 

