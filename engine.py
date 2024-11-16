import repository
from domains import Note


def new_note(note: Note) -> Note:
    # TODO set up id.
    note.id = 100
    # The same alias will overwrite the original note.
    if len(note.alias) > 0:
        note_with_save_alise = repository.find_by_alias(note.alias)
        if note_with_save_alise is not None:
            repository.delete(note_with_save_alise)
    repository.save(note)
    return note
