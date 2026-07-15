import io
import unittest
from datetime import datetime
from unittest.mock import Mock, patch

import interface
from domains import Note


class WriteInterfaceTest(unittest.TestCase):
    def _args(self, content=None):
        return {
            'content': content,
            'alias': 'example',
            'tag': ['pipe'],
        }

    @patch('interface.engine.new_note')
    @patch('interface.clipboard.get')
    def test_explicit_content_takes_precedence_over_stdin(
        self,
        clipboard_get,
        new_note,
    ):
        new_note.return_value = Note(
            '1', 'explicit', 'example', ['pipe'], datetime.now()
        )
        stdin = Mock()
        stdin.isatty.return_value = False

        with patch('interface.sys.stdin', stdin):
            interface.w(self._args('explicit'))

        new_note.assert_called_once_with('explicit', 'example', ['pipe'])
        stdin.read.assert_not_called()
        clipboard_get.assert_not_called()

    @patch('interface.engine.new_note')
    def test_reads_piped_stdin_without_changing_content(self, new_note):
        content = 'first line\n  second line\n'
        new_note.return_value = Note(
            '1', content, 'example', ['pipe'], datetime.now()
        )

        with patch('interface.sys.stdin', io.StringIO(content)):
            interface.w(self._args())

        new_note.assert_called_once_with(content, 'example', ['pipe'])

    @patch('interface.engine.new_note')
    @patch('interface.clipboard.get', return_value=b'clipboard content')
    def test_reads_clipboard_when_stdin_is_a_tty(self, clipboard_get, new_note):
        new_note.return_value = Note(
            '1', 'clipboard content', 'example', ['pipe'], datetime.now()
        )
        stdin = Mock()
        stdin.isatty.return_value = True

        with patch('interface.sys.stdin', stdin):
            interface.w(self._args())

        clipboard_get.assert_called_once_with()
        new_note.assert_called_once_with(
            'clipboard content', 'example', ['pipe']
        )

    @patch('interface.engine.new_note')
    @patch('interface.clipboard.get')
    def test_rejects_empty_piped_stdin(self, clipboard_get, new_note):
        stderr = io.StringIO()

        with patch('interface.sys.stdin', io.StringIO('')):
            with patch('interface.sys.stderr', stderr):
                with self.assertRaisesRegex(SystemExit, '1'):
                    interface.w(self._args())

        self.assertIn('Note content can not be empty.', stderr.getvalue())
        clipboard_get.assert_not_called()
        new_note.assert_not_called()


class CatInterfaceTest(unittest.TestCase):
    @patch('interface.engine.find_by_id_or_alias')
    def test_writes_note_content_exactly_to_stdout(self, find_note):
        for content in ('without newline', 'with newline\n'):
            with self.subTest(content=content):
                find_note.return_value = Note(
                    '1', content, 'example', [], datetime.now()
                )
                stdout = io.StringIO()

                with patch('interface.sys.stdout', stdout):
                    result = interface.cat({
                        'id_or_alias': 'example',
                        'clipboard': False,
                        'verbose': False,
                    })

                self.assertIsNone(result)
                self.assertEqual(stdout.getvalue(), content)

    @patch('interface.engine.find_by_id_or_alias', return_value=None)
    def test_missing_note_writes_only_to_stderr_and_exits_nonzero(
        self,
        find_note,
    ):
        stdout = io.StringIO()
        stderr = io.StringIO()

        with patch('interface.sys.stdout', stdout):
            with patch('interface.sys.stderr', stderr):
                with self.assertRaisesRegex(SystemExit, '1'):
                    interface.cat({
                        'id_or_alias': 'missing',
                        'clipboard': False,
                        'verbose': False,
                    })

        self.assertEqual(stdout.getvalue(), '')
        self.assertIn('fia: Not found.', stderr.getvalue())


if __name__ == '__main__':
    unittest.main()
