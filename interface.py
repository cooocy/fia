"""
This layer is responsible for handling the command line args and then calling the engine.
"""
import clipboard
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
    content = args['content']
    if content == '':
        content = str(clipboard.get().decode())
    if content == '':
        print('fia: Can not read from clipboard.')
        exit(1)
    note = engine.new_note(content, args['alias'], args['tag'])
    return f'fia: Saved ok. id: {note.id}, alias: {note.alias}'


def rm(args: dict):
    id_or_alias = args['id_or_alias']
    engine.delete_by_id_or_alias(id_or_alias)
    return 'fia: Removed ok.'


def cat(args: dict) -> str:
    id_or_alias = args['id_or_alias']
    note = engine.find_by_id_or_alias(id_or_alias)
    if not note:
        return 'fia: Not found.'

    if args['clipboard']:
        clipboard.set(note.content)
        return 'fia: Catted to clipboard.'
    else:
        if args['verbose']:
            return note.__str__()
        else:
            return note.content
