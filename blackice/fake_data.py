from datetime import date
from random import randrange

from blackice.constants import ADDON_FREE, ADDON_WEBAPP_HOSTED
from blackice.devicetype_constants import DEVICE_DESKTOP, DEVICE_GAIA


class FakeWebapp(object):
    def __init__(self, slug, pk):
        self.categories = ['books', 'games', 'reference']

        self.device_types = [DEVICE_DESKTOP, DEVICE_GAIA]
        self.description = {'en': u'The fake app you love',
                            'es': u'(espa\xf1ol) The fake app you love'}
        self.id = 4731
        self.homepage = {'en': 'http://marketplace.mozilla.org/'}
        self.name = {'en': u'Fake App',
                     'es': u'(espa\xf1ol) Fake App'}
        self.premium_type = ADDON_FREE
        self.price = None
        self.slug = slug
        self.support_email = {'en': 'dev-marketplace@mozilla.com'}
        self.support_url = {'en': 'http://zombo.com/'}

        self.app_type = ADDON_WEBAPP_HOSTED
        self.author = 'ashort@mozilla.com'
        self.banner_message = {'en': 'Your ad here'}
        self.created = date(2014, 9, 1)
        self.current_version = '1.0'
        self.default_locale = 'en'
        self.is_offline = True
        self.is_packaged = False
        self.manifest_url = 'http://zombo.com/'
        self.modified = date.today()
        self.pk = pk
        self.package_path = ''
        self.public_stats = False
        self.ratings = 3
        self.status = 4

    def available_in_region(self, region):
        return True


class FakeDatastore(object):
    def fetch_visible_webapp(self, region, user, slug=None, pk=None):
        if pk is None:
            pk = randrange(0, 10000)
        if slug is None:
            slug = "app-%s" % (pk,)
        return FakeWebapp(slug, pk)


def create(settings):
    return FakeDatastore()
