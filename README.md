# django-versioncheck

Prototyping a small django app which tries to be annoying if your django version is outdated.

## Installation

If you want to install the latest stable release from PyPi:

    $ pip install django-versioncheck

If you want to install the latest development version from GitHub:

    $ pip install -e git://github.com/byteweaver/django-versioncheck#egg=django-versioncheck

Add `versioncheck` to your `INSTALLED_APPS`:

    INSTALLED_APPS = (
        ...
        'versioncheck',
        ...
    )

## How to use

At the momement django-versioncheck does just provide a simple management command to display the installed django
version and the latest upstream version on PYPI.

    $ python manage.py checkversion

### Web view usage

Hook this app into your urls.py:

    urlpatterns = patterns('',
        ...
        url(r'^versioncheck/', include('versioncheck.urls', namespace='versioncheck')),
        ...
    )

WARNING: This view is not secured and exposes your current Django version, use with caution!

## Python version notice

The current version is developed to be used with Python 3 and only tested on this major version.


## Changelog

See `Changelog.md` file.

## Todo & Roadmap

It is just a protoype, most features are not ready yet.

https://github.com/byteweaver/django-versioncheck/issues
