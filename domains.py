from datetime import datetime


class Note:
    def __init__(self, note: str, alias: str = '', keywords: list[str] = ()):
        self.id = -1
        self.note = note
        self.alias = alias
        self.keywords = keywords
        self.ts = datetime.now()

    def __str__(self):
        n = self.note[:min(10, len(self.note))]
        if len(n) < len(self.note):
            n += '...'
        return f'Note(id: {self.id}, note:{n}, alias: {self.alias},keywords: {self.keywords}, ts:{self.ts})'
