"""
This layer is responsible for handling the command line args and then calling the engine.
Additionally, assemble the result to stdout.
"""
import clipboard
import colorama
import engine

from colorama import Fore, Style
from prettytable import PrettyTable

colorama.init()


def ls(args: dict) -> str:
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
    if len(notes) == 0:
        return 'fia: Sorry, you has no data.'

    tbl = PrettyTable()
    if args['verbose']:
        tbl.field_names = [Fore.CYAN + 'id' + Style.RESET_ALL, Fore.CYAN + 'alias' + Style.RESET_ALL,
                           Fore.CYAN + 'tag' + Style.RESET_ALL, Fore.CYAN + 'ts' + Style.RESET_ALL,
                           Fore.CYAN + 'content' + Style.RESET_ALL]
        for note in notes:
            tbl.add_row([note.id, note.alias, note.tags_overview(), note.ts, note.content_overview()])

    else:
        tbl.field_names = [Fore.CYAN + 'id' + Style.RESET_ALL, Fore.CYAN + 'alias' + Style.RESET_ALL,
                           Fore.CYAN + 'content' + Style.RESET_ALL]
        for note in notes:
            tbl.add_row([note.id, note.alias, note.content_overview()])
    return tbl.__str__()


def w(args: dict) -> str:
    content = args['content']
    if content == '':
        content = str(clipboard.get().decode())
    if content == '':
        print(f'{Fore.RED}fia: Can not read from clipboard.{Style.RESET_ALL}')
        exit(1)
    note = engine.new_note(content, args['alias'], args['tag'])
    return f'{Fore.GREEN}fia: Saved ok. id: {note.id}, alias: {note.alias}{Style.RESET_ALL}'


def rm(args: dict) -> str:
    id_or_alias = args['id_or_alias']
    engine.delete_by_id_or_alias(id_or_alias)
    return f'{Fore.GREEN}fia: Removed ok.{Style.RESET_ALL}'


def clean(args: dict) -> str:
    user_input = input(f'{Fore.RED}fia: Do you want to continue? (yes/no): {Style.RESET_ALL}').strip().lower()
    if user_input == 'yes':
        cnt = engine.clean()
        return f'{Fore.GREEN}fia: Removed {cnt} notes.{Style.RESET_ALL}'
    else:
        return f'{Fore.GREEN}fia: Canceled.{Style.RESET_ALL}'


def cat(args: dict) -> str:
    id_or_alias = args['id_or_alias']
    note = engine.find_by_id_or_alias(id_or_alias)
    if not note:
        return f'{Fore.RED}fia: Not found.{Style.RESET_ALL}'

    if args['clipboard']:
        clipboard.set(note.content)
        return f'{Fore.GREEN}fia: Catted to clipboard.{Style.RESET_ALL}'
    else:
        if args['verbose']:
            return f'{Fore.GREEN}note{Style.RESET_ALL}'
        else:
            return note.content
