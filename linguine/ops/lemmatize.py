#!/usr/bin/env python
"""
Returns: A list of lemmas generated from the given corpora
Given: Tokenized contents of corpora
Uses the NLTK POS Tagger (Penn Treebank) to look up parts of speech,
and the WordNet Lemmatizer to get the lemma for each word.
"""
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag

class LemmatizerWordNet:
    def __init__(self):
        pass
    def run(self, data):
        for corpus in data:
            tags = pos_tag(corpus.tokenized_contents)
            lemmatizer = WordNetLemmatizer()
            corpus.tokenized_contents = [lemmatizer.lemmatize(word, self.getWordNetPartOfSpeech(tag)) 
                    if not self.getWordNetPartOfSpeech(tag) == None 
                    else word 
                    for (word,tag) in tags]

            corpusString = ""
            for index, word in enumerate(corpus.tokenized_contents):
                corpusString += corpus.tokenized_contents[index] + " "

            corpus.contents = corpusString

        return data
    def getWordNetPartOfSpeech(self,treebank_tag):
        #So the WordNetLemmatizer in NLTK expects POS tags in a different format than NLTK itself writes them. 
        #So this function does the conversion to make them compatible.
        if treebank_tag.startswith('J'):
            return 'a'
        elif treebank_tag.startswith('V'):
            return 'v'
        elif treebank_tag.startswith('N'):
            return 'n'
        elif treebank_tag.startswith('R'):
            return 'r'
