"""
This is the core layer, connect the upper-level interface and the lower-level repository.
"""
import clipboard
import repository
from domains import Note


def new_note(content: str = '', alias: str = '', tags: list[str] = ()) -> Note:
    if content == '':
        content = str(clipboard.get().decode())
    if content == '':
        print('fia: can not read from clipboard.')
        exit(1)
    note = Note(content, alias, tags)
    # The same alias will overwrite the original note.
    if len(note.alias) > 0:
        note_with_same_alise = repository.find_by_alias(note.alias)
        if note_with_same_alise is not None:
            repository.delete(note_with_same_alise)
    repository.save(note)
    return note
