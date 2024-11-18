"""
This layer interacts with the disk, used for storing and retrieving notes.
"""
import base64
import config_loader
import kits
import os.path
from colorama import Fore, Style
from datetime import datetime
from domains import Note

INDEX_SEPARATOR = '%'
storage = config_loader.storage__
if not os.path.exists(storage.path):
    os.makedirs(storage.path)
index_path = os.path.join(kits.current_path(), storage.path, 'index')


def __get_content_path(__id: str):
    return os.path.join(storage.path, __id)


def __deserialize_from_index(line: str) -> Note:
    blobs = line.split(INDEX_SEPARATOR)
    ts = datetime.strptime(blobs[3], '%Y-%m-%d %H:%M:%S.%f')
    return Note(blobs[0], base64.b64decode(blobs[4].encode()).decode(), blobs[1], blobs[2].split(','), ts)


def __serialize_to_index(note: Note) -> str:
    encoded_content = base64.b64encode(note.content_overview().encode()).decode()
    return f'{note.id}{INDEX_SEPARATOR}{note.alias}{INDEX_SEPARATOR}{note.tags_overview()}{INDEX_SEPARATOR}{note.ts}{INDEX_SEPARATOR}{encoded_content}'


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


def delete_all() -> int:
    if not os.path.exists(index_path):
        return 0
    ids = []
    with open(index_path, 'r') as index_f:
        for line in index_f.readlines():
            blobs = line.split(INDEX_SEPARATOR)
            ids.append(blobs[0])
    os.remove(index_path)
    for id in ids:
        if os.path.exists(__get_content_path(id)):
            os.remove(__get_content_path(id))
    return len(ids)


def delete(note: Note):
    print(f'Deleted successfully! note: {note}')


def delete_by_alias(alias: str):
    if not os.path.exists(index_path):
        return
    # First read all lines and then write back line by line, compare the alias, if equals, ignore.
    with open(index_path, 'r') as index_f:
        lines = index_f.readlines()
    id_to_delete = '-1'
    with open(index_path, 'w') as index_f:
        for line in lines:
            blobs = line.split(INDEX_SEPARATOR)
            if blobs[1] == alias:
                # This one will be deleted, record its id.
                id_to_delete = blobs[0]
            else:
                index_f.write(line)
    if id_to_delete != '-1':
        path_to_delete = __get_content_path(id_to_delete)
        if os.path.exists(path_to_delete):
            os.remove(path_to_delete)


def delete_by_id_or_alias(id_or_alias: str):
    # First read all lines and then write back line by line, compare the alias, if equals, ignore.
    if os.path.exists(index_path):
        with open(index_path, 'r') as index_f:
            lines = index_f.readlines()
        id_to_delete = '-1'
        with open(index_path, 'w') as index_f:
            for line in lines:
                blobs = line.split(INDEX_SEPARATOR)
                if blobs[0] == id_or_alias or blobs[1] == id_or_alias:
                    # This one will be deleted, record its id.
                    id_to_delete = blobs[0]
                else:
                    index_f.write(line)
        if id_to_delete != '-1':
            path_to_delete = __get_content_path(id_to_delete)
            if os.path.exists(path_to_delete):
                os.remove(path_to_delete)


def find_by_id_or_alias(id_or_alias: str):
    if not os.path.exists(index_path):
        return None
    note = None
    with open(index_path, 'r') as index_f:
        for line in index_f:
            blobs = line.split(INDEX_SEPARATOR)
            if blobs[0] == id_or_alias or blobs[1] == id_or_alias:
                note = __deserialize_from_index(line)
                break
    if note is not None:
        if os.path.exists(__get_content_path(note.id)):
            with open(__get_content_path(note.id), 'r') as content_f:
                note.content = content_f.read()
        else:
            print(f'{Fore.RED}fia: The index not match the content, please rm the note(id: {note.id}){Style.RESET_ALL}')
    return note


def ls(marker: str, size: int, tags: list[str]):
    if not os.path.exists(index_path):
        return []
    with open(index_path, 'r') as index_f:
        picked = []
        for line in index_f:
            blobs = line.split(INDEX_SEPARATOR)
            if blobs[0] < marker:
                continue
            note = __deserialize_from_index(line)
            if len(tags) == 0 or set(note.tags).intersection(set(tags)):
                picked.append(note)
            if len(picked) >= size:
                break
        return picked
