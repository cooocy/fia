"""
This layer is responsible for handling the command line args and then calling the engine.
"""
import engine


def ls(args: dict):
    tag = args.get('tag')
    if tag is None or tag == '':
        tag = []
    marker = args.get('marker')
    if marker is None:
        marker = ''
    size = args.get('size')
    if size is None or size == '':
        size = 100
    notes = engine.ls(marker, size, tag)
    r = ''
    if args['verbose']:
        for note in notes:
            r += f'{note.id}    {note.alias}    {note.tags}    {note.ts}    {note.content_overview()}\n'
    else:
        for note in notes:
            r += f'{note.id}    {note.alias}    {note.content_overview()}\n'
    return r


def w(args: dict) -> str:
    note = engine.new_note(args['content'], args['alias'], args['tag'])
    return f'fia: Saved ok. id: {note.id}, alias: {note.alias}'


def rm(args: dict):
    id_or_alias = args['id_or_alias']
    engine.delete_by_id_or_alias(id_or_alias)
    return 'fia: Removed ok.'


def cat(args: dict) -> str:
    id_or_alias = args['id_or_alias']
    note = engine.find_by_id_or_alias(id_or_alias)
    if note:
        if args['verbose']:
            return note.__str__()
        else:
            return note.content
    else:
        return 'fia: Not found.'
