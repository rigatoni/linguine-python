#!/usr/bin/env python
import os
import json

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
          sentences = []
          for sentence_res in res["sentences"]:
            words = []
            for index, token in enumerate(sentence_res["tokens"]):
              word = {}
              word["token"] = sentence_res["tokens"][index]
              for atype in analysisTypes:
                if atype is "sentiment":
                    word[atype] = sentence_res[atype]
                    word["sentimentValue"] = sentence_res["sentimentValue"]
                elif atype is not "parse":
                    word[atype] = sentence_res[atype][index]

              words.append(word)
            sentence = {}
            sentence['tokens'] = words
            if "sentiment" in analysisTypes:
              sentence['sentiment'] = sentence_res['sentiment']
              sentence['sentimentValue'] = sentence_res['sentimentValue']
              sentence['sentiment_json'] = json.loads(sentence_res['sentiment_json'])

            if "parse" in analysisTypes:
                sentence["parse"] = sentence_res["parse"]

            sentence['deps_json'] = json.loads(sentence_res['deps_json'])
            sentences.append(sentence)

      return sentences

    def __init__(self, analysisType):
        self.analysisType = analysisType

        if StanfordCoreNLP.proc == None:
            StanfordCoreNLP.proc = CoreNLP(configdict={'annotators':'tokenize, ssplit, pos, lemma, ner, parse, sentiment'},
            corenlp_jars=[os.path.join(os.path.dirname(__file__), '../../lib/*')])

    def run(self, data):
        return self.jsonCleanup(data, self.analysisType)

