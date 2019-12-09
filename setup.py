#!/usr/bin/env python
"""
Installation script:

To release a new version to PyPi:
- Ensure the version is correctly set in oscar.__init__.py
- Run: make release
"""
import os
import sys

from setuptools import find_packages, setup

PROJECT_DIR = os.path.dirname(__file__)

sys.path.append(os.path.join(PROJECT_DIR, 'src'))
from src.sample import get_version

install_requires = [
    'django',
    # PIL is required for image fields, Pillow is the "friendly" PIL fork
    'djangorestframework',
]

setup(
    name='sample',
    version=get_version(),
    url='https://github.com/django-oscar/django-oscar',
    author="Sandesh Rana (Vimm)",
    author_email="vimmrana0@gmail.com",
    description="Example project",
    # long_description=long_description,
    keywords="Accounting application, Django, domain-driven",
    license='BSD',
    platforms=['linux'],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Application Frameworks']
)
