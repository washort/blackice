from django.conf import settings
from django.conf.urls import patterns, include, url as django_url
from django.utils.module_loading import import_by_path

from rest_framework.routers import SimpleRouter

from blackice.webapps.views import AppViewSet


def create_urls(datastore_loader):
    datastore = datastore_loader(settings)

    def url(pat, target, **kwargs):
        return django_url(pat, target, {'data': datastore}, **kwargs)

    apps = SimpleRouter()
    apps.register(r'app', AppViewSet, base_name='app')

    v1_urls = patterns(
        '',
        url(r'^apps/', include(apps.urls)),
    )
    v2_urls = patterns(
        '',
        ) + v1_urls

    return patterns(
        '',
        url('^api/', include(v1_urls, namespace='compat')),
        url(r'^api/v2/', include(v2_urls, namespace='api-v2')),
        url(r'^api/v1/', include(v1_urls))
    )

urlpatterns = create_urls(import_by_path(settings.DATASTORE))
