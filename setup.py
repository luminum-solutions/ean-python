# -*- coding: utf-8 -*-
from setuptools import setup
import sys
from docs.conf import CURRENT_VERSION, REQUIRES

PY_VERSION = sys.version_info[0], sys.version_info[1]

if PY_VERSION < (3, 0):
    long_description = open('README.md').read()
else:
    long_description = open('README.md', encoding='utf-8').read()


setup(
    name='ean-api',
    version=CURRENT_VERSION,
    author=u'Zowie Langdon',
    author_email='zowie@akoten.com',
    url='https://github.com/Akoten/ean-api',
    license='None yet',
    description='A Python client for the EAN API.',
    long_description=long_description,
    zip_safe=False,
    install_requires=REQUIRES,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
