from datetime import datetime


class Note:
    def __init__(self, content: str, alias: str = '', tags: list[str] = ()):
        self.id = '-1'
        self.content = content
        self.alias = alias
        self.tags = tags
        self.ts = datetime.now()

    @staticmethod
    def new(id: str, content: str, alias: str, tags: list[str], ts: str):
        note = Note('')
        note.id = id
        note.content = content
        note.alias = alias
        note.tags = tags
        note.ts = ts
        return note

    def __str__(self):
        n = self.content[:min(10, len(self.content))]
        if len(n) < len(self.content):
            n += '...'
        return f'Note(id: {self.id}, content:{n}, alias: {self.alias},tags: {self.tags}, ts:{self.ts})'
