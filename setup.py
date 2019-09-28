import setuptools
from setuptools import find_packages
from distutils.core import setup

setup(
        name="calculator",
        version="0.1",
        packages=find_packages(),
        license="MIT",
        long_description=open("README.md").read()
)
