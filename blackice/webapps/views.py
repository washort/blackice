from rest_framework import response
from rest_framework import viewsets

from blackice.regions_constants import REGION_LOOKUP, RESTOFWORLD
from blackice.exceptions import HttpLegallyUnavailable
from blackice.webapps.serializers import AppSerializer


def region_from_request(request):
    # XXX look up GeoIP
    url_region = request.REQUEST.get('region')
    return REGION_LOOKUP.get(url_region, RESTOFWORLD)


class AppViewSet(viewsets.ViewSet):
    cors_allowed_methods = ('get', 'put', 'post', 'delete')
    authentication_classes = []

    def slug_or_id(self):
        pk = self.kwargs.get('pk')
        if pk and not pk.isdigit():
            # If the `pk` contains anything other than a digit, it's a `slug`.
            return {"pk": None, "slug": self.kwargs['pk']}
        return self.kwargs

    def retrieve(self, request, data, **kwargs):
        region = region_from_request(request)
        # user = user_from_request(request)
        app = data.fetch_visible_webapp(
            region=region,
            user=None,
            **self.slug_or_id())
        if not app.available_in_region(region):
            raise HttpLegallyUnavailable({
                'name': app.name,
                'support_email': app.support_email,
                'support_url': app.support_url,
                'reason': 'Not available in your region.'})
        return response.Response(
            AppSerializer(app, context={'lang': region.default_language}).data)
