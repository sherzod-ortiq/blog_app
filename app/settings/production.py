from .base import *

DEBUG = False

DATABASES = {

  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'blog_app_development',
    'USER': 'blog_app',
    'PASSWORD': 'password',
    'HOST': 'localhost',
    'PORT': '',
  }

}
