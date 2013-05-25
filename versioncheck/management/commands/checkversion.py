from django.core.management.base import BaseCommand

from versioncheck.utils import get_version, get_lastest_version


class Command(BaseCommand):
    def handle(self, *args, **options):
        print "Current version: %s" % (get_version())
        print "Latest version: %s" % (get_lastest_version())
