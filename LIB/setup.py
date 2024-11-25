#!/usr/bin/env python

#python3 -m pip install -e .

from setuptools import setup, find_packages

setup(
    name='sca',
    version='1.0',
    description="Screaming-channel attacks basic demo",
    long_description=open('README.md').read(),
    author="Jeremy GUILLAUME",
    author_email='jeremy.guillaume96@gmail.com',
    license='',
    url='',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'pyserial',
        'numpy==1.24',
        'matplotlib',
        'scipy',
        'pycrypto',
        'pycryptodome'
    ],
    python_requires='~=3.8',
)
