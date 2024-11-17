"""
This layer is responsible for handling the command line args and then calling the engine.
"""
import engine


def ls(args: dict):
    return 'This is ls.'


def w(args: dict) -> str:
    note = engine.new_note(args['content'], args['alias'], args['tag'])
    return f'fia: Saved successfully. id: {note.id}'


def cat(args: dict) -> str:
    id_or_alias = args['id_or_alias']
    note = engine.find_by_id_or_alias(id_or_alias)
    if note:
        return note.__str__()
    else:
        return 'fia: Not Found.'
