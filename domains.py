from dataclasses import dataclass
from datetime import datetime


@dataclass
class Note:
    id: str
    content: str
    alias: str
    tags: []
    ts: datetime

    def __str__(self):
        n = self.content[:min(10, len(self.content))]
        if len(n) < len(self.content):
            n += '...'
        return f'Note(id: {self.id}, content:{n}, alias: {self.alias},tags: {self.tags}, ts:{self.ts})'
