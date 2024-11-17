import kits
import yaml


class Storage:
    def __init__(self, path: str):
        self.path = path


def __load_config():
    with  open(kits.current_path() + '/config.yaml') as f:
        y = yaml.safe_load(f)
        f.close()
        return y


__configurations = __load_config()

storage__ = Storage(__configurations['storage']['path'])
