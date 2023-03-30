#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-spreadsheets-anywhere",
    version="0.2.0",
    description="Singer.io tap for extracting spreadsheet data from cloud storage",
    author="Eric Simmerman",
    url="https://github.com/ets/tap-spreadsheets-anywhere",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_spreadsheets_anywhere"],
    install_requires=[
        "singer-python>=5.13.0",
        'smart_open>=6.3.0',
        'voluptuous>=0.13.1',
        'boto3>=1.26.102',
        'google-cloud-storage>=2.8.0',
        # 'protobuf>=4.22.1',
        'openpyxl>=3.1.2', # 3.2.0b1
        'xlrd3>=1.1.0',
        'paramiko>=3.1.0',
        'azure-storage-blob>=12.15.0' # 12.16.0b1
    ],
    entry_points="""
    [console_scripts]
    tap-spreadsheets-anywhere=tap_spreadsheets_anywhere:main
    """,
    packages=["tap_spreadsheets_anywhere"],
    include_package_data=True,
    tests_require=[
        'pytest'
    ]
)
