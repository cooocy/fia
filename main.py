import argparse
import interface

if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='这是一个示例程序。')
    # parser.add_argument('echo', help='echo command argument')
    # parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    # args = parser.parse_args()
    # print(args.echo)
    # interface.new_note_from_clipboard('x1')
    interface.new_note_from_clipboard('m1', ['x', 'y', 'z'])
