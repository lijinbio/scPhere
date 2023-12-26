#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='scPhere',
    description="Deep generative model embedding single-cell RNA-Seq profiles on hyperspheres or hyperbolic spaces",
    version='0.1.0',
    author='Jiarui Ding and Aviv Regev',
    author_email='jding@broadinstitue.org',
    keywords="scPhere",
    license='BSD 3-clause',
    url="https://github.com/klarman-cell-observatory/scPhere",
    install_requires=['numpy',
                      'tensorflow',
                      'scipy',
                      'pandas',
                      'matplotlib',
                      'tensorflow-probability',
                      ],
    packages=find_packages(),
    python_requires='>=3.7',
)
