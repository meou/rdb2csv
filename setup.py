from distutils.core import setup
from os import popen

setup(
	name="rdb2csv",
	version="0.0.1",
	package=["rdb2csv",],
	license="MIT",
	long_description=open('README.md').read(),
)
