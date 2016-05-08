# Check that the packages are installed.
from pkgutil import iter_modules
import sys


def check_import(packagename):
    if packagename in (name for _, name, _ in iter_modules()):
        return True
    else:
        return False

packages = ['networkx', 'numpy', 'matplotlib', 'circos', 'hiveplot', 'pandas',
            'jupyter']

for p in packages:
    assert check_import(p), '{0} not present. Please install via pip or conda.'.format(p)

assert sys.version_info.major >= 3, 'Please install Python 3!'
