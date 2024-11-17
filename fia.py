#!/opt/homebrew/bin//python
import argparse

import interface

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Hi~ This is fia, your cli note assistant.')
    subparsers = parser.add_subparsers(dest='sub_cmd', help='you can ...')

    # fia ls [-h] [-k KEYWORD] [-a | -s SIZE]
    ls = subparsers.add_parser('ls', help='List your notes in fia.')
    ls.add_argument('-k', '--keyword', type=str, default='', required=False, help='filtered by KEYWORD contains')
    ls_g1 = ls.add_mutually_exclusive_group()
    ls_g1.add_argument('-a', '--all', action='store_true', required=False, help='list all')
    ls_g1.add_argument('-s', '--size', type=int, default=5, required=False, help='list by size')

    # fia w [-h] [NOTE] [-a <ALIAS>] [-k <KEYWORDS>]
    w = subparsers.add_parser('w', help='Write your note into fia.')
    w.add_argument('-c', '--content', type=str, default='', required=False,
                   help='the note content you want to write. if not specified, read from the clipboard')
    w.add_argument('-a', '--alias', type=str, default='', required=False, help='the alise of this note')
    w.add_argument('-k', '--keyword', type=str, default=[], required=False, nargs='+', help='the keywords of this note')

    args = parser.parse_args()
    ret = getattr(interface, args.sub_cmd)(vars(args))
    print(ret)
