# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

import polls


setup(
    name='coplan_polls',
    version=polls.__version__,
    description='',
    author='Oerd Cukalla',
    author_email='oerdcukalla@gmail.com',
    include_package_data=True,
    url='https://github.com/co-plan/coplan-polls/tree/v%s' % polls.__version__,
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)

# Usage of setup.py:
# $> python setup.py register             # registering package on PYPI
# $> python setup.py build sdist upload   # build, make source dist and upload to PYPI
