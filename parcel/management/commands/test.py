import atexit
import signal
import sys

from django.core.management.commands.test import Command as TestCommand

class Command(TestCommand):
    def handle(self, *args, **kwargs):
        super(Command, self).handle(*args, **kwargs)

