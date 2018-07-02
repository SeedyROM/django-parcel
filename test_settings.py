import os

BASE_DIR = os.path.join(os.path.dirname(__file__), 'test')

SECRET_KEY = "EE26B0DD4AF7E749AA1A8EE3C10AE9923F618980772E473F8819A5D4940E0DB27AC185F8A0E1D5F84F88BC887FD67B143732C304CC5FA9AD8E6F57F50028A8FF"

INSTALLED_APPS = (
    'parcel',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}


# Custom settings
PARCEL_CLIENT_PATH = 'client'