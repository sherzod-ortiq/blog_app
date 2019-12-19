from .base import *

DATABASES = {

  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'blog_app_test',
    'USER': 'blog_app',
    'PASSWORD': 'password',
    'HOST': 'localhost',
    'PORT': '',
  }

}