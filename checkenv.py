# Check that the packages are installed.
import os
from pkgutil import iter_modules

def check_import(packagename):
    if packagename in (name for _, name, _ in iter_modules()):
        print('{0} exists.'.format(packagename))
    else:
        print('Please install {0}.'.format(packagename))
        # print('Installing {0}...'.format(packagename))
        # os.system('conda install {0}'.format(p))

packages = ['networkx', 'numpy', 'matplotlib', 'circos', 'hiveplot', 'pandas']

for p in packages:
    check_import(p)
