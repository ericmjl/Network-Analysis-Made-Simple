# Check that the packages are installed.
import sys
from pkgutil import iter_modules
import subprocess


def check_import(packagename):
    if packagename in (name for _, name, _ in iter_modules()):
        return True
    else:
        return False


# If there are new packages that you can import, add them to the list.
package_names = [
    "networkx",
    "numpy",
    "matplotlib",
    "hiveplot",
    "pandas",
    "jupyter",
    "nxviz",
    "tqdm",
]
packages = {n: n for n in package_names}
# Only add the packages whose import names are different from the
# package name (what we `pip install` or `conda install`).
packages["community"] = "python-louvain"


assert (
    sys.version_info.major >= 3 and sys.version_info.minor >= 6
), "Please install Python >=3.6!"


def print_error(p, i):
    """
    Returns the error message for package installation issues.

    :param str p: The name of the package to install.
    :param str i: The name of the package when imported.
    """
    error_message = f"""
    {i} not present. Please do the installation using either:

    - pip install {p}
    - conda install -c conda-forge {p}
    """
    return error_message


for p, i in packages.items():
    assert check_import(p), print_error(i, p)


# Credit: @bill-tucker-zywave for suggesting this fix.
# https://github.com/ericmjl/Network-Analysis-Made-Simple/issues/286#issuecomment-1108793656
result = subprocess.run("ffmpeg -version", shell=True)
assert (
    result.returncode == 0
), "please install ffmpeg and ensure that it is on your PATH."

# Credit: @zmilicc for requesting this.
print("All checks passed. Your environment is good to go!")
