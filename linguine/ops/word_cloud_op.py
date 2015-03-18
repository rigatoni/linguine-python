class WordCloudOp:

    def run(self, data):
        terms = { }
        results = [ ]
        try:
            for corpus in data:
                tokens = corpus.tokenized_contents
                for token in tokens:
                    if token in terms:
                        terms[token]+=1
                    else:
                        terms[token]=1
            for term in terms:
                results.append({ "term" : term, "frequency" : terms[term]})
            return results
        except LookupError:
            raise TransactionException('NLTK \'Punkt\' Model not installed.', 500)
        except TypeError:
            raise TransactionException('Corpus contents does not exist.')

