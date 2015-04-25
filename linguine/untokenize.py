import string
def untokenize(tokens):
    #Joins all tokens in the list into a single string.
    #If a token doesn't start with an apostrophe and isn't a punctuation mark, add a space in front of it before joining.
    #Then strip the total string so that leading spaces and trailing spaces are removed.
    return "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in tokens]).strip()
