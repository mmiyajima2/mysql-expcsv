# -*- coding: utf-8 -*-
import os
from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as rme:
    README = rme.read()


setup(
        name="myexpcsv",
        version="0.1.0",
        license="MIT",
        packages=['myexpcsv'],
        include_package_data=False,
        description="CSV Export Utility for MySQL",
        long_description=README,
        author="MIYAJIMA, Masafumi",
        author_email="mmiyajima2@gmail.com",
        install_requires=[
            'click',
            'pymysql',
            ],
        entry_points={
            'console_scripts': ['myexpcsv=myexpcsv.commands:export'],
            },
        classifiers=[
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.6',
            ]
        )
