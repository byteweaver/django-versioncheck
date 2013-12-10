import os
from setuptools import setup, find_packages

import versioncheck


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-versioncheck',
    version=versioncheck.__version__,
    description='A small django app which tries to be annoying if your django version is outdated.',
    long_description=read('README.md'),
    license='BSD',
    author='Richard Stromer',
    author_email='noxan@byteweaver.org',
    url='https://github.com/noxan/django-versioncheck',
    packages=find_packages(),
    install_requires=[
        'django',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)
