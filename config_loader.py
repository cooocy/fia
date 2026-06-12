import os
import re

import kits
import yaml


ENVIRONMENT_VARIABLE_PATTERN = re.compile(
    r'\$\{([A-Za-z_][A-Za-z0-9_]*)(?::([^}]*))?\}'
)


class Storage:
    def __init__(self, path: str):
        self.path = path


def _expand_environment_variables(value):
    if isinstance(value, dict):
        return {
            key: _expand_environment_variables(item)
            for key, item in value.items()
        }
    if isinstance(value, list):
        return [_expand_environment_variables(item) for item in value]
    if not isinstance(value, str):
        return value

    def replace(match):
        name, default = match.groups()
        if name in os.environ:
            return os.environ[name]
        if default is not None:
            return default
        raise ValueError(
            f'Environment variable {name} is required by config.yaml'
        )

    return ENVIRONMENT_VARIABLE_PATTERN.sub(replace, value)


def __load_config():
    with open(kits.current_path() + '/config.yaml') as f:
        return _expand_environment_variables(yaml.safe_load(f))


__configurations = __load_config()

storage__ = Storage(__configurations['storage']['path'])
