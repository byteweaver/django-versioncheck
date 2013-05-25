import django
import re
import urllib


def get_available_versions():
    VERSION_REGEX = re.compile('^<a href=".*">Django-(.*)\.tar\.gz</a>')

    data = urllib.urlopen("https://pypi.python.org/packages/source/D/Django/").read()
    versions = []

    for line in data.splitlines():
        if VERSION_REGEX.match(line):
            versions.append(VERSION_REGEX.split(line)[1])

    versions = sorted(versions, key=lambda version: -int(version.replace('.', '')))

    return versions


def get_lastest_version():
    return get_available_versions()[0]


def get_version():
    return django.get_version()
