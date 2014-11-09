#!/usr/bin/env python
"""
Given a set of texts, calculates the TF-IDF for each word-text pair in the set.
Returns: A list of dictionaries containing a term, a corpus id, the term's importance in that corpus.
Given: A list of corpuses
"""
import math, nltk, re, pprint
from linguine.transaction_exception import TransactionException
from nltk import word_tokenize

class Tfidf:
    def __init__(self):
        # a list of (words-freq) pairs for each document
        self.global_terms_in_doc = {}
        # list to hold occurrences of terms across documents
        self.global_term_freq = {}
        self.num_docs = 0
    def run(self, data):
        self.num_docs = len(data)
        try:
            results = []
            for corpus in data:
                terms_in_doc = {}
                tokens = word_tokenize(corpus.contents)
                for word in tokens:
                    if word in terms_in_doc:
                        terms_in_doc[word] += 1
                    else:
                        terms_in_doc[word] = 1
                for (word, freq) in terms_in_doc.items():
                    #If the word appears in a doc, increment the # of docs containing the word by 1
                    if word in self.global_term_freq:
                        self.global_term_freq[word] += 1
                    else:
                        self.global_term_freq[word] = 1
                self.global_terms_in_doc[corpus.id] = terms_in_doc
            for corpus in data:
                max_freq = 0
                for (term, freq) in self.global_terms_in_doc[corpus.id].items():
                    if freq > max_freq:
                        max_freq = freq
                for (term, freq) in self.global_terms_in_doc[corpus.id].items():
                    idf = math.log(float(1 + self.num_docs) / float(1 + self.global_term_freq[term]))
                    tfidf = float(freq) / float(max_freq) * float(idf)
                    results.append({ "term" : term, "importance" : tfidf, "corpus_id" : corpus.id })
            return results
        except LookupError:
            raise TransactionException('NLTK \'Punkt\' Model not installed.', 500)
        except TypeError:
            raise TransactionException('Corpus contents does not exist.')
