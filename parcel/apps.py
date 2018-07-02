from django.apps import AppConfig

from parcel.lib.entry_point import start_parcel


class ParcelConfig(AppConfig):
    name = 'parcel'

    def ready(self):
        start_parcel()