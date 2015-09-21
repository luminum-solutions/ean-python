# -*- coding: utf-8 -*-
from distutils.core import setup
import sys

PY_VERSION = sys.version_info[0], sys.version_info[1]

if PY_VERSION < (3, 0):
    long_description = open('README.md').read()
else:
    long_description = open('README.md', encoding='utf-8').read()

setup(
    name='ean-api',
    version='0.1',
    author=u'Zowie Langdon',
    author_email='zowie@akoten.com',
    packages=['ean-api'],
    url='https://github.com/Akoten/ean-api',
    license='None yet',
    description='A Python client for the EAN API.',
    long_description=long_description,
    zip_safe=False,
    install_requires=['nose', 'mock', 'sphinx', 'urllib3', 'django>=1.7'],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
    ],
)
