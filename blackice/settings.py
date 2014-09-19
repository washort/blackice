import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'blackice.webapps',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'blackice.urls'
WSGI_APPLICATION = 'blackice.wsgi.application'

SECRET_KEY = 'please change this'

DATASTORE = 'blackice.fake_data.create'
