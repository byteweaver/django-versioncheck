import django

try:
    import xmlrpclib
except ImportError:
    import xmlrpc.client as xmlrpclib


def get_available_versions():
    client = xmlrpclib.ServerProxy('https://pypi.python.org/pypi')
    return client.package_releases('Django')


def get_latest_version():
    return get_available_versions()[0]


def get_version():
    return django.get_version()
