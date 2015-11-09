# Check that the packages are installed.
import os
from pkgutil import iter_modules

def check_import(packagename):
    if packagename in (name for _, name, _ in iter_modules()):
        return True
    else:
        return False

packages = ['networkx', 'numpy', 'matplotlib', 'circos', 'hiveplot', 'pandas']

for p in packages:
    try:
        assert check_import(p)
        print('{0} present, great!'.format(p))
    except AssertionError:
        print('{0} not present. Please install via pip or conda.'.format(p)
