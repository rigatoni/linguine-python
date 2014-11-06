#!/usr/bin/env python
"""
Given a set of texts, calculates the TF-IDF for each word-text pair in the set.
Returns: A list of tuples pairing corpus name to TFIDF list - each TFIDF list is
a sorted list of tuples mapping TFIDF value to a string token.
Given: Data containing a list of tuples, tuple element one being the corpus name/ID,
element two being a list of all tokens in the corpus, i.e.
[ ('1',['hello', 'world']), ('2',['how', 'now', 'brown', 'cow']), ('3',['and', 'how']) ]
"""
import math, nltk, re, pprint
from nltk import word_tokenize

class tfidf:
    def __init__(self):
        # a list of (words-freq) pairs for each document
        self.global_terms_in_doc = {}
        # list to hold occurrences of terms across documents
        self.global_term_freq = {}
        self.num_docs = 0
    def run(self, data):
        self.num_docs = len(data.data_ids)
        result = []
        for index, doc in enumerate(data.data):
            terms_in_doc = {}
            tokens = word_tokenize(doc)
            for word in tokens:
                if word in terms_in_doc:
                    terms_in_doc[word] += 1
                else:
                    terms_in_doc[word] = 1
            for (word,freq) in terms_in_doc.items():
                #If the word appears in a doc, increment the # of docs containing the word by 1
                if word in self.global_term_freq:
                    self.global_term_freq[word] += 1
                else:
                    self.global_term_freq[word] = 1
            self.global_terms_in_doc[data.data_ids[index]] = terms_in_doc
        for index, doc in enumerate(data.data):
            max_freq = 0
            doc_result = []
            for (term, freq) in self.global_terms_in_doc[data.data_ids[index]].items():
                if freq > max_freq:
                    max_freq = freq
            for (term, freq) in self.global_terms_in_doc[data.data_ids[index]].items():
                idf = math.log(float(1 + self.num_docs) / float(1 + self.global_term_freq[term]))
                tfidf = float(freq) / float(max_freq) * float(idf)
                doc_result.append((tfidf, term))
            result.append((data.data_ids[index],sorted(doc_result, reverse=True)))
        return result
