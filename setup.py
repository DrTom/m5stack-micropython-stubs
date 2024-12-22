from setuptools import setup, find_packages
import os

setup(
    name='m5stack-micropython-stubs',
    version='0.1.15',
    packages=find_packages(include=[]),
    include_package_data=True,
    package_data={
        '': ['M5.pyi'],
    },
    data_files=[
        ('', ['M5.pyi']),
        ('unit', ['unit/pahub.pyi']),
    ],
    install_requires=[
        # List your package dependencies here
    ],
    extras_require={
        'dev': [
            'setuptools',
            'twine',
            'mypy',
        ],
    },
)
