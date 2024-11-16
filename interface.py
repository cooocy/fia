"""
This layer is responsible for handling the requests from command line, and then calling the system clipboard.
"""
import clipboard
import engine
from domains import Note


def new_note_from_clipboard(alias: str = '', keywords: list[str] = ()) -> Note:
    note = Note(str(clipboard.get().decode()), alias, keywords)
    note = engine.new_note(note)
    return note
