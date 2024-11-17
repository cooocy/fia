"""
This is the core layer, connect the upper-level interface and the lower-level repository.
"""
import repository
from datetime import datetime
from domains import Note


def new_note(content: str = '', alias: str = '', tags: list[str] = ()) -> Note:
    note = Note('-1', content, alias, tags, datetime.now())
    # The same alias will overwrite the original note.
    if len(note.alias) > 0:
        repository.delete_by_alias(note.alias)
    repository.save(note)
    return note


def delete_by_id_or_alias(id_or_alias: str):
    repository.delete_by_id_or_alias(id_or_alias)


def find_by_id_or_alias(id_or_alias: str) -> Note:
    return repository.find_by_id_or_alias(id_or_alias)


def ls(marker: str, size: int, tags: list[str]) -> list[Note]:
    return repository.ls(marker, size, tags)
