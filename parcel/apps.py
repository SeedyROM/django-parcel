from django.apps import AppConfig
from parcel import Parcel


class ParcelConfig(AppConfig):
    name = 'parcel'

    def ready(self):
        Parcel.start()