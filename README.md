linguine-python
===============

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
4. `python -m linguine.webserver`

To run tests:

1. `pip install -r requirements.txt`
2. `nosetests`
