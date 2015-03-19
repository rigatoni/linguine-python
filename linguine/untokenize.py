import string
def untokenize(tokens):
	return "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in tokens]).strip()
