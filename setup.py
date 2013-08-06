from distutils.core import setup
from os import popen

setup(
	name="rdb2csv",
	version="0.0.1",
	url='https://github.com/meou/rdb2csv',
	author="Shang-Chieh Wu",
	author_email="pypi@meou.org",
	packages=["rdb2csv"],
	license="MIT",
	long_description=open('README.md').read(),
)
