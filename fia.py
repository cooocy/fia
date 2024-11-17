#!/opt/homebrew/bin//python
import argparse
import interface

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Hi~ This is fia, your cli note assistant.')
    subparsers = parser.add_subparsers(dest='sub_cmd', help='you can ...')

    # fia ls [-h] [-t TAG] [-m MARKER] [-s SIZE]
    ls = subparsers.add_parser('ls', help='List your notes in fia.')
    ls.add_argument('-t', '--tag', type=str, default=[], required=False, nargs='+', help='filtered by TAG contains')
    ls.add_argument('-m', '--marker', type=str, required=False, help='list by id ge this marker')
    ls.add_argument('-s', '--size', type=int, default=100, required=False, help='list by size, default 100')
    ls.add_argument('-v', '--verbose', action='store_true', required=False, help='be a little more verbose')

    # fia w [-h] [-c CONTENT] [-a <ALIAS>] [-t <TAG>]
    w = subparsers.add_parser('w', help='Write your note into fia.')
    w.add_argument('-c', '--content', type=str, default='', required=False,
                   help='the note content you want to write. if not specified, read from the clipboard')
    w.add_argument('-a', '--alias', type=str, default='', required=False,
                   help='the alise of this note, global unique, override when duplicate')
    w.add_argument('-t', '--tag', type=str, default=[], required=False, nargs='+', help='the tags of this note')

    # fia rm [-h] id_or_alias
    rm = subparsers.add_parser('rm', help='Remove your note in fia.')
    rm.add_argument('id_or_alias', type=str, help='the note id or alise')

    # fia cat [-h] [-v | -b] id_or_alias
    cat = subparsers.add_parser('cat', help='Cat your note in fia.')
    cat.add_argument('id_or_alias', type=str, help='the note id or alise')
    cat_g1 = cat.add_mutually_exclusive_group(required=False)
    cat_g1.add_argument('-v', '--verbose', action='store_true', required=False, help='be a little more verbose')
    cat_g1.add_argument('-b', '--clipboard', action='store_true', required=False,
                        help='if specified, cat to sys clipboard instead of stdout')

    args = parser.parse_args()
    ret = getattr(interface, args.sub_cmd)(vars(args))
    print(ret)
