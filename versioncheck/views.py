from django.http import JsonResponse
from django.views.generic import View

from versioncheck import utils


class VersionView(View):
    def get(self, request):
        return JsonResponse({
            'current': utils.get_version(),
            'latest': utils.get_latest_version(),
        })
