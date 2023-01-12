#! /usr/bin/env python3

from setuptools import setup, find_packages, Command

from distutils.command.build_py import build_py

setup(
    name             = 'pyPBS_EL',
    version          = '1.0.4',
    description      = 'Package for distribution',
    author           = 'msjeon27',
    author_email     = 'msjeon27@cau.ac.kr',
    url              = '',
    download_url     = '',
    install_requires = ['argparse'],
	include_package_data=True,
	packages=find_packages(),
    keywords         = ['PYPBSEL', 'pypbsel'],
    cmdclass         = {'build_py': build_py},
	scripts          = ['scripts/pyPBS_EL'],
    python_requires  = '>=3.6',
    zip_safe=False,
    classifiers      = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
) 
