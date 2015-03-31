#!/usr/bin/env python
"""
Returns: A list of topics, where each topic lists pairs of words-probabilities
that fit the topic
Given: A list of strings, where each string is an entire document to be examined
Uses the Gensim Topic Modeling library to find the most relevant topics

TODO: define JSON format such that user can define num_topics, passes
"""
from gensim.corpora import Dictionary
from gensim.models import LdaModel
class TopicModel:
    def __init__(self):
        pass
    def run(self, data):
        dictionary = Dictionary(data)
        dictionary.filter_extremes(no_above=0.5)
        bags_of_words = [ dictionary.doc2bow(t) for t in data]
        #This can take a while to run:
        lda = LdaModel(bags_of_words, id2word = dictionary, num_topics=30, passes=10)
        return self.assemble_topics(lda)
    #Because LdaModelling is resource intensive, this test case is used for Nosetests.
    #It's identical to run, except that the passes attribute is a smaller number for shorter
    #runtime.
    def test_run(self, data):
        dictionary = Dictionary(data)
        dictionary.filter_extremes(no_above=0.5)
        bags_of_words = [ dictionary.doc2bow(t) for t in data]
        #This can take a while to run:
        lda = LdaModel(bags_of_words, id2word = dictionary, num_topics=30, passes=2)
        return self.assemble_topics(lda)
    """Print LDA model topics into a human-interpretable data structure

    Example:
    [
        #Topic 1:
        [
            (prob1, word1)
            (prob2, word2)
            ...
        ]
        #Topic 2:
        [
            (prob1, word1)
            ...
        ]
        ...
    ]
    Args:
        lda_model: gensim LDA model
    Returns:
        A list of topics, with each topic listing the word-prob pairs
    """
    def assemble_topics(self, lda_model):
        topics = list()
        for n,topic in enumerate(lda_model.show_topics(formatted=False)):
            topics.append(list())
            topics[n] = list()
            for prob, word in topic:
                topics[n].append((prob, word))
        return topics