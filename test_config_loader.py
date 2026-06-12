import os
import unittest
from unittest.mock import patch

from config_loader import _expand_environment_variables


class ExpandEnvironmentVariablesTest(unittest.TestCase):
    def test_expands_environment_variables_in_nested_config(self):
        config = {
            'storage': {'path': '${MINE_TOOLS}/fia/storage/'},
            'tags': ['${TAG}', 1],
        }

        with patch.dict(
            os.environ,
            {'MINE_TOOLS': '/tmp/tools', 'TAG': 'notes'},
            clear=True,
        ):
            expanded = _expand_environment_variables(config)

        self.assertEqual(
            expanded,
            {
                'storage': {'path': '/tmp/tools/fia/storage/'},
                'tags': ['notes', 1],
            },
        )

    def test_uses_default_when_environment_variable_is_missing(self):
        with patch.dict(os.environ, {}, clear=True):
            expanded = _expand_environment_variables(
                '${MINE_TOOLS:/tmp/tools}/fia/storage/'
            )

        self.assertEqual(expanded, '/tmp/tools/fia/storage/')

    def test_supports_empty_default(self):
        with patch.dict(os.environ, {}, clear=True):
            expanded = _expand_environment_variables(
                '${MINE_TOOLS:}/fia/storage/'
            )

        self.assertEqual(expanded, '/fia/storage/')

    def test_raises_for_missing_required_environment_variable(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(
                ValueError,
                'Environment variable MINE_TOOLS is required',
            ):
                _expand_environment_variables('${MINE_TOOLS}/fia/storage/')


if __name__ == '__main__':
    unittest.main()
