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
    def jsonCleanup(self, data, analysisTypes):
      for corpus in data:
          res = StanfordCoreNLP.proc.parse_doc(corpus.contents)
          words = [] 
          for sentence in res["sentences"]:
            for index, token in enumerate(sentence["tokens"]):
              word = {}
              
              word["token"] = sentence["tokens"][index]
              for atype in analysisTypes:
                word[atype] = sentence[atype][index]

              words.append(word)

      return words

    def __init__(self, analysisType):
        self.analysisType = analysisType

        if StanfordCoreNLP.proc == None:
            StanfordCoreNLP.proc = CoreNLP(configdict={'annotators':'tokenize, ssplit, pos, lemma, ner'}, 
            corenlp_jars=[os.path.join(os.path.dirname(__file__), '../../lib/*')])

    def run(self, data):
        return self.jsonCleanup(data, self.analysisType) 

