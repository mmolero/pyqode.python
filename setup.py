#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This setup script packages pyqode.python
"""
from setuptools import setup, find_packages


def read_version():
    with open("pyqode/python/__init__.py") as f:
        lines = f.read().splitlines()
        for l in lines:
            if "__version__" in l:
                return l.split("=")[1].strip().replace('"', '')


def readme():
    return str(open('README.rst').read())


# get requirements
requirements = ['pyqode.core>=2.0.0-alpha1', 'jedi>=0.7',
                'pep8', 'frosted', 'docutils']


setup(
    name='pyqode.python',
    namespace_packages=['pyqode'],
    version=read_version(),
    packages=find_packages(),
    keywords=["CodeEdit PySide PyQt code editor widget python"],
    package_dir={'pyqode': 'pyqode'},
    url='https://github.com/pyQode/pyqode.python',
    license='MIT',
    author='Colin Duquesnoy',
    author_email='colin.duquesnoy@gmail.com',
    description='Add python support to pyqode',
    long_description=readme(),
    install_requires=requirements,
    entry_points={'pyqode_plugins':
                  ['pyqode_python = '
                   'pyqode.python.designer_plugin']},
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: X11 Applications :: Qt',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Widget Sets',
        'Topic :: Text Editors :: Integrated Development Environments (IDE)'
    ]
)
