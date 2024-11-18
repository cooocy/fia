from dataclasses import dataclass
from datetime import datetime


@dataclass
class Note:
    id: str
    content: str
    alias: str
    tags: list[str]
    ts: datetime

    def __str__(self):
        return f'Note(id: {self.id}, content:{self.content_overview()}, alias: {self.alias},tags: {self.tags_overview()}, ts:{self.ts})'

    def content_overview(self) -> str:
        overview = self.content[:min(30, len(self.content))]
        if len(overview) < len(self.content):
            overview += ' ... '
        return overview.replace('\n', '↲')

    def tags_overview(self) -> str:
        return ','.join(self.tags)
