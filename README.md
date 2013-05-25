# django-versioncheck

Prototyping a small django app which tries to be annoying if your django version is outdated.

## Installation

If you want to install the latest stable release from PyPi:

    $ pip install django-versioncheck

If you want to install the latest development version from GitHub:

    $ pip install -e git://github.com/noxan/django-versioncheck#egg=django-versioncheck

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
