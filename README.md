# Fia: Your CLI Note Assistant

[English](README.md) | [中文](README.zh.md)

Fia is a simple and efficient command-line note-taking assistant designed to help you manage your notes with ease.

It allows you to create, read, update, and delete notes directly from your terminal.

What is even more amazing is that she can directly operate your system clipboard.

## Features

- **Create Note**: Quickly jot down thoughts and save them.
- **Read Notes**: Retrieve notes by ID or alias, or display all notes with filtering options.
- **Delete Notes**: Remove specific notes or clean up all notes at once.
- **Clipboard Integration**: Automatically read from and write to the system clipboard for convenience.

## Installation and Configurations

To install Fia, simply clone the repository and run the setup script:

```shell
git clone --depth=1 git@github.com:cooocy/fia.git
cd fia & pip3 install -r requirements
# Add alias in your shell. like this
alias fia="python $HOME/fia/fia.py"
```

And then Modify the value in the configuration file `.config.yaml`.

## Run

Execute `fia --help` in the command line and then refer to the document.

```shell
fia --help

usage: fia.py [-h] {ls,w,cat,rm,clean} ...

Hi~ This is fia, your cli note assistant.

positional arguments:
  {ls,w,cat,rm,clean}  you can ...
    ls                 List your notes.
    w                  Write your note into fia.
    cat                Cat your note.
    rm                 Remove your note.
    clean              Clean all your notes.

options:
  -h, --help           show this help message and exit
```