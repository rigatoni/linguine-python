linguine-python
===============
## Overview
linguine-python is a Python web server for use in the Linguine natural language processing workbench. The server accepts requests in a JSON format, and performs text analysis operations as they are implemented in Python. 
The implemented operations can be found in /linguine/ops.

## Operation template

```python
#A sample operation
#Useful for unit testing or acting as a placeholder
#Data will be passed to the op in a form that suits the operation,
#either a text or a collection of text. The op transforms the text and returns an output.
class FooOp:
	def run(self, data):
		return Bar(data)
```
## API

- `HTTP POST '/':` It expects a JSON payload in the provided format.
```javascript
{
  "transaction_id": "transactionId", // An ID associated with the current request.
  "operation": "tfidf", // The analytic operation to be performed.
  "library": "nltk", // The library to use when executing the analysis.
  "corpora_ids": ["id1", "id2", "etc"] // The corpora ID's to run the analysis on.
}
```

## Dependencies

* Python 3
* MongoDB
* [NLTK Punkt model](http://stackoverflow.com/questions/4867197/failed-loading-english-pickle-with-nltk-data-load)

## Development

1. `pip install -r requirements.txt`
2. `python -m linguine.webserver`

To run tests:

1. `pip install -r requirements.txt`
2. `nosetests`
