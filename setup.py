#!/usr/bin/env python3

from setuptools import setup

setup(
    name='bartbot',
    version='2',
    url='https://github.com/bthate/bartbot',
    author='Bart Thate',
    author_email='bthate@dds.nl',
    description="my bot.",
    long_description="BARTBOT contains no copyright or LICENSE",
    license='Public Domain',
    zip_safe=True,
    install_requires=["obot"],
    scripts=["bin/bb"],
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: Public Domain',
                 'Operating System :: Unix',
                 'Programming Language :: Python',
                 'Topic :: Utilities'
                ]
)
