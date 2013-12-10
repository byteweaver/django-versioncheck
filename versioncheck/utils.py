import django
import re
from urllib import request
from distutils.version import LooseVersion


def get_available_versions():
    VERSION_REGEX = re.compile('^<a href=".*">Django-(.*)\.tar\.gz</a>')

    data = request.urlopen("https://pypi.python.org/packages/source/D/Django/").read()
    versions = []

    for line in data.splitlines():
        line = line.decode('utf-8')
        if VERSION_REGEX.match(line):
            version = LooseVersion(VERSION_REGEX.split(line)[1])
            versions.append(version)

    versions = sorted(versions, reverse=True)

    return versions


def get_lastest_version():
    return get_available_versions()[0]


def get_version():
    return django.get_version()
