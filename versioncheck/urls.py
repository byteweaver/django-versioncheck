from django.conf.urls import url

from versioncheck.views import VersionView


urlpatterns = [
    url(r'^$', VersionView.as_view()),
]
