linguine-python
===============
## Overview
linguine-python is a Python web server for use in the Linguine natural language processing workbench. The server accepts requests in a JSON format, and performs text analysis operations as they are implemented in Python. 
The implemented operations can be found in /linguine/ops.

## Adding an operation

To add a new analysis or cleanup operation to this project:

1. Create a new Python file in /linguine/ops.
2. Fill the operation in using the template below.
3. Import the op in /linguine/operation_builder.py and add the operation to the get_operation_handler function body.
4. Any unit tests should go in /test.

## Operation template

```python
#A sample cleanup operation
#Used to modify the existing text in a corpus set for easier analysis.
#Data will be passed to the op in the form of a collection of corpora.
#The op transforms the contents of each corpus and returns the results.
class FooOp:
	def run(self, data):
		for corpus in data:
			corpus.contents = Bar(corpus.contents)
		return data
```

```python
#A sample analysis operation
#Used to generate meaningful data from a corpus set.
#Data will be passed to the op in the form of a collection of corpora.
#The op runs analysis on each corpus (or the set as a whole).
#It builds a set of results which are then returned in place of corpora.
class FooOp:
	def run(self, data):
		results = []
		for corpus in data:
			results.append({ 'corpus_id' : corpus.id, 'bar': Bar(corpus.contents) })
		return results
```

## API

- `HTTP POST '/':` It expects a JSON payload in the provided format.
```javascript
{
  "transaction_id": "transactionId", // An ID associated with the current request.
  "operation": "tfidf", // The analytic operation to be performed.
  "library": "nltk", // The library to use when executing the analysis.
  "corpora_ids": ["id1", "id2", "etc"] // The corpora ID's to run the analysis on.
  "user_id": "user1", // The user who requested the analysis.
  "cleanup": ["removeCapsGreedy","removePunct", "etc"] // The cleanup operations to perform on the text.
  "tokenizer": "whitespaceTokenizer" // The tokenizer to use to break text into word tokens if needed.
}
```
## Currently implemented operations:

* Remove capitalization
* Remove punctuation
* Stem words
* TF-IDF
* Word Cloud
* Part of Speech tagging
* Topic Modeling

## Dependencies

* Python 3.3 or newer
* MongoDB
* [NLTK Punkt model](http://stackoverflow.com/questions/4867197/failed-loading-english-pickle-with-nltk-data-load)

## Development

1. `sudo pip install -r requirements.txt`
2. `python -m textblob.download_corpora`
3. `python -m linguine.webserver`

To run tests:

1. `sudo pip install -r requirements.txt`
2. `nosetests` #Requires 'nose' to work properly. Check out https://nose.readthedocs.org/en/latest/ if it's not working for you

Note: running the program from a directory other than the linguine-python root directory will cause directory linking errors.
