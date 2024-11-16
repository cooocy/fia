from domains import Note


def save(note: Note):
    print(f'Saved successfully! note: {note}')


def delete(note: Note):
    print(f'Deleted successfully! note: {note}')


def find(id: int) -> Note:
    return None


def find_by_alias(alias: str) -> Note:
    return None
