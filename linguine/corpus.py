class Corpus:

    def __init__(self, id, title, contents, tags = []):
        self.id = id
        self.title = title
        self.contents = contents
        self.tags = tags

    def to_dict(self):
      return { 'title': self.title,  'tags': self.tags , 'contents': self.contents, 'id': self.id }
