from tower import ugettext as _, ugettext_lazy as _lazy

# ADDON_WEBAPP Types
ADDON_WEBAPP_HOSTED = 1
ADDON_WEBAPP_PACKAGED = 2
ADDON_WEBAPP_PRIVILEGED = 3

ADDON_WEBAPP_TYPES = {
    ADDON_WEBAPP_HOSTED: 'hosted',
    ADDON_WEBAPP_PACKAGED: 'packaged',
    ADDON_WEBAPP_PRIVILEGED: 'privileged',
}
ADDON_WEBAPP_TYPES_LOOKUP = dict((v, k) for k, v in ADDON_WEBAPP_TYPES.items())


ADDON_FREE = 0
ADDON_PREMIUM = 1
ADDON_PREMIUM_INAPP = 2
ADDON_FREE_INAPP = 3
# The addon will have payments, but they aren't using our payment system.
ADDON_OTHER_INAPP = 4

ADDON_PREMIUM_TYPES = {
    ADDON_FREE: _('Free'),
    ADDON_PREMIUM: _('Premium'),
    ADDON_PREMIUM_INAPP: _('Premium with in-app payments'),
    ADDON_FREE_INAPP: _('Free with in-app payments'),
    ADDON_OTHER_INAPP: _("I'll use my own system for in-app payments")
}

# Non-locale versions for the API.
ADDON_PREMIUM_API = {
    ADDON_FREE: 'free',
    ADDON_PREMIUM: 'premium',
    ADDON_PREMIUM_INAPP: 'premium-inapp',
    ADDON_FREE_INAPP: 'free-inapp',
    ADDON_OTHER_INAPP: 'other',
}

CATEGORY_CHOICES = (
    ('books', _lazy(u'Books')),
    ('business', _lazy(u'Business')),
    ('education', _lazy(u'Education')),
    ('entertainment', _lazy(u'Entertainment')),
    ('games', _lazy(u'Games')),
    ('health-fitness', _lazy(u'Health & Fitness')),
    ('lifestyle', _lazy(u'Lifestyle')),
    ('maps-navigation', _lazy(u'Maps & Navigation')),
    ('music', _lazy(u'Music')),
    ('news-weather', _lazy(u'News & Weather')),
    ('photo-video', _lazy(u'Photo & Video')),
    ('productivity', _lazy(u'Productivity')),
    ('reference', _lazy(u'Reference')),
    ('shopping', _lazy(u'Shopping')),
    ('social', _lazy(u'Social')),
    ('sports', _lazy(u'Sports')),
    ('travel', _lazy(u'Travel')),
    ('utilities', _lazy(u'Utilities'))
)

CATEGORY_CHOICES_DICT = dict(CATEGORY_CHOICES)

TARAKO_CATEGORIES_MAPPING = {
    'tarako-tools': ['business', 'education', 'productivity',
                     'reference', 'utilities'],
    'tarako-games': ['games'],
    'tarako-lifestyle': ['books', 'entertainment', 'health-fitness',
                         'lifestyle', 'maps-navigation', 'music',
                         'news-weather', 'photo-video', 'shopping',
                         'social', 'sports', 'travel'],
}

TARAKO_CATEGORY_CHOICES = (
    ('tarako-tools', _lazy(u'Tools')),
    ('tarako-games', _lazy(u'Games')),
    ('tarako-lifestyle', _lazy(u'Lifestyle')),
)
