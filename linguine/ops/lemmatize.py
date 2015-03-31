#!/usr/bin/env python
"""
Returns: A list of lemmas generated from the given corpora
Given: Tokenized contents of corpora
Uses the NLTK POS Tagger (Penn Treebank) to look up parts of speech,
and the WordNet Lemmatizer to get the lemma for each word.
"""
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag
class LemmatizerWordNet:
    def __init__(self):
        pass
    def run(self, data):
        for corpus in data:
            tags = nltk.pos_tag(corpus.tokenized_contents)
            lemmatizer = WordNetLemmatizer()
	        corpus.tokenized_contents = [lemmatizer.lemmatize(word,getWordNetPartOfSpeech(tag)) for (word,tag) in tags]
            corpus.contents = ''.join(corpus.tokenized_contents)
	    return data
    def getWordNetPartOfSpeech(self,treebank_tag):
        #So the WordNetLemmatizer in NLTK expects POS tags in a different format than NLTK itself writes them. 
        #So this function does the conversion to make them compatible.
        if treebank_tag.startswith('J'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
