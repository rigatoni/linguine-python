class Corpus:

    def __init__(self, id, title, contents, tags = [],tokenized_contents = None):
        self.id = id
        self.title = title
        self.contents = contents
        self.tags = tags
        self.tokenized_contents = tokenized_contents

    def to_dict(self):
      return { 'title': self.title,  'tags': self.tags , 'contents': self.contents, 'tokenized_contents': self.tokenized_contents, 'id': self.id }
