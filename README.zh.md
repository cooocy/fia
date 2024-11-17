# Fia：您的命令行笔记助手

[English](README.md) | [中文](README.zh.md)

Fia 是一个简单高效的命令行笔记助手，旨在帮助你轻松管理笔记。

她允许你直接从终端创建、阅读、更新和删除笔记。

更棒的是，她可以直接操作你的系统剪贴板。

## 功能

- 创建笔记：快速记录想法并保存它们。
- 阅读笔记：通过 ID 或别名检索笔记，或使用过滤选项显示所有笔记。
- 删除笔记：移除特定笔记或一次性清除所有笔记。
- 剪贴板集成：自动从系统剪贴板读取和写入，方便操作。

## 安装和配置

要安装 Fia，只需克隆仓库并运行安装脚本：

```shell
git clone --depth=1 git@github.com:cooocy/fia.git
cd fia & pip3 install -r requirements
# 在你的 shell 中添加别名，如下所示
alias fia="python $HOME/fia/fia.py"
```

然后修改配置文件 .config.yaml 中的值。

## 运行

在命令行执行 `fia --help`，参考帮助文档即可。

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