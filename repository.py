"""
This layer interacts with the disk, used for storing and retrieving notes.
"""
import base64
import os.path

import config_loader
from domains import Note

INDEX_SEPARATOR = '%'

storage = config_loader.storage__
if not os.path.exists(storage.path):
    os.makedirs(storage.path)
index_path = os.path.join(storage.path, 'index')


def __get_content_path(__id: str):
    return os.path.join(storage.path, __id)


def __deserialize_from_index(line: str) -> Note:
    blobs = line.split(INDEX_SEPARATOR)
    tags_str = blobs[2].replace(' ', '').replace("'", "").replace('[', '').replace(']', '')
    return Note.new(blobs[0], base64.b64decode(blobs[4].encode()).decode(), blobs[1], tags_str.split(','), blobs[3])


def __serialize_to_index(note: Note) -> str:
    # Truncate the first 25 chars for encoding.
    encoded_content = base64.b64encode(note.content[:min(25, len(note.content))].encode()).decode()
    return f'{note.id}{INDEX_SEPARATOR}{note.alias}{INDEX_SEPARATOR}{note.tags}{INDEX_SEPARATOR}{note.ts}{INDEX_SEPARATOR}{encoded_content}'


def save(note: Note):
    """
    Save the note, the note.id will be set to the next id auto.
    :param note: the note to save
    :return: saved note
    """

    # To set the id.
    if os.path.exists(index_path):
        with open(index_path, 'r') as index_f:
            # Find top id.
            lines = index_f.readlines()
            last_line = lines[-1] if lines else ''
            if last_line == '':
                note.id = '1'
            else:
                top = __deserialize_from_index(last_line)
                note.id = str(int(top.id) + 1)
    else:
        note.id = '1'

    # Save index and content.
    with open(index_path, 'a') as index_f:
        index_f.write(__serialize_to_index(note))
        index_f.write('\n')
    with open(__get_content_path(note.id), 'w') as content_f:
        content_f.write(note.content)
    print(f'Saved successfully! note: {note}')


def delete(note: Note):
    print(f'Deleted successfully! note: {note}')


def find(id: str) -> Note:
    with open(index_path, 'r') as index_f:
        for line in index_f:
            blobs = line.split(INDEX_SEPARATOR)
            if blobs[0] == id:
                note = __deserialize_from_index(line)
                break
    with open(__get_content_path(id), 'r') as content_f:
        note.content = content_f.read()
    return note


def find_by_id_or_alias(id_or_alias: str) -> Note:
    note = None
    with open(index_path, 'r') as index_f:
        for line in index_f:
            blobs = line.split(INDEX_SEPARATOR)
            if blobs[0] == id_or_alias or blobs[1] == id_or_alias:
                note = __deserialize_from_index(line)
                break
    if note is not None:
        with open(__get_content_path(note.id), 'r') as content_f:
            note.content = content_f.read()
    return note


def find_by_alias(alias: str) -> Note:
    return None
