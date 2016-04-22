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
	"corpora_ids": ["12345"], //Collection of corpora to pipe into analysis
	"cleanup": ['stopwords'], //Cleanup steps to add
	"operation": "nlp-relation", //Type of analysis to be preformed
	"tokenizer": "", //Tokenizer used (if required)
	"library": "", //Library associated w/ analysis (if required)
	"transaction_id": "", (Field to be populated by linguine-python)
	"analysis_name": "Relation Extraction (Stanford CoreNLP)", //Name to display in text fields
	"time_created": 1461342250445, //Used to calculate ETA of analyses
	"user_id": "12345" //Unique identifier of user who created analysis
}
```
## Currently implemented operations:

* Term Frequency
* Part of Speech Tagging
* Sentiment
* Named Entity Recognition
* Relation Extraction
* Coreference Resolution

## Dependencies

* Python 3.4 or newer (Requires implementation of Future object)
* MongoDB
* [NLTK Punkt model](http://stackoverflow.com/questions/4867197/failed-loading-english-pickle-with-nltk-data-load)
* Stanford Corenlp Pywrapper (Installation instructions can be found [here.](https://github.com/Pastafarians/linguine/wiki/Stanford-CoreNLP-Installation) 

## Development

1. install stanford CoreNLP module following docs [here.](https://github.com/Pastafarians/linguine/wiki/Stanford-CoreNLP-Installation) 
2. `sudo pip install -r requirements.txt`
3. `python -m textblob.download_corpora`
4. `python -m linguine.webserver`

To run tests:

1. `sudo pip install -r requirements.txt`
2. `nosetests` #Requires 'nose' to work properly. Check out https://nose.readthedocs.org/en/latest/ if it's not working for you

Note: running the program from a directory other than the linguine-python root directory will cause directory linking errors.
