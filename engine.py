"""
This is the core layer, connect the upper-level interface and the lower-level repository.
"""
import clipboard
import repository
from domains import Note


def new_note_from_clipboard(alias: str = '', keywords: list[str] = ()) -> Note:
    note = Note(str(clipboard.get().decode()), alias, keywords)
    # TODO set up id.
    note.id = 100
    # The same alias will overwrite the original note.
    if len(note.alias) > 0:
        note_with_save_alise = repository.find_by_alias(note.alias)
        if note_with_save_alise is not None:
            repository.delete(note_with_save_alise)
    repository.save(note)
    return note
