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


## Python version notice

The current version is developed to be used with Python 3 and only tested on this major version.


## Todo & Roadmap

It is just a protoype, most features are not ready yet.

* Email notifications if django is outdated
* View restricted to admins which shows django versions
