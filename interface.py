"""
This layer is responsible for handling the command line args and then calling the engine.
"""
import engine


def ls(args: dict):
    return 'This is ls.'


def w(args: dict) -> str:
    note = engine.new_note(args['content'], args['alias'], args['keyword'])
    return f'fia: Saved successfully. id: {note.id}'
