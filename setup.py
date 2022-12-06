#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import re
from setuptools import setup

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

with io.open('pyzentao/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \"(.*?)\"', f.read()).group(1)

setup(
    name='pyzentao',
    version=version,
    url='https://github.com/philip1134/pyzentao',
    license='MIT',
    author='Philip CHAN',
    author_email='philip1134@imior.com',
    description='Python SDK for Zentao.',
    long_description=readme,
    packages=['pyzentao'],
    package_data={
        '': ['*.md', '*.rst'],
    },
    platforms='any',
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "requests",
        "PyYAML",
    ],
    extras_require={
        'dev': [
            'tox',
            'check-manifest',
            'flake8'
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    keywords='Python SDK',
)
