"""
This file is responsible for operating the system clipboard.
"""
import subprocess

from colorama import Fore, Style


def get():
    """
    Get clipboard content.
    Only support string text.
    :return: bytes of clipboard content.
    """

    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    return_code = p.wait()
    b = p.stdout.read()
    if return_code != 0:
        print(f'{Fore.RED}fia: Read from system clipboard error. code: {return_code}{Style.RESET_ALL}')
        exit(1)
    return b


def set(data: str):
    """
    Set data to clipboard.
    :param data: data to set
    """

    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.stdin.write(data.encode())
    p.stdin.close()
    return_code = p.wait()
    if return_code != 0:
        print(f'{Fore.RED}fia: Set to system clipboard error. code: {return_code}{Style.RESET_ALL}')
        exit(1)
