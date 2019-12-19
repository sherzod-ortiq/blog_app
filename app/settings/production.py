import django_heroku
from .base import *

DEBUG = False

DATABASES = {

  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'blog_app_production',
    'USER': 'blog_app',
    'PASSWORD': 'password',
    'HOST': '',
    'PORT': '',
  }

}

django_heroku.settings(locals())
