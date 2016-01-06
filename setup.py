#-*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open

with open("README.rst", 'r') as f:
    desc = f.read()

setup(
        name='spread-confiture',
        version="0.17.1rc2",
        description="A checker for required fields in yaml files",
        long_description=desc,
        url="https://github.com/Frky/confiture",
        author="_Frky",
        author_email="francky.dg@gmail.com",
        license="MIT",
        classifiers=[
                        "Development Status :: 4 - Beta",
                        "Intended Audience :: Developers", 
                        "Topic :: Software Development :: Testing",
                        "License :: OSI Approved :: MIT License",
                ],
        keywords="yaml configuration config required fields template",
        packages=find_packages(),
        install_requires=['pyyaml'],
    )
