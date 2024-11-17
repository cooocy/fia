"""
This layer is responsible for handling the command line args and then calling the engine.
"""
import engine
from domains import Note


def new_note_from_clipboard(alias: str = '', keywords: list[str] = ()) -> Note:
    note = engine.new_note_from_clipboard(alias, keywords)
    return note


def ls(args: dict):
    return 'This is ls.'


def w(args: dict):
    return 'This is w.'
