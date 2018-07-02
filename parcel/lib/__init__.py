import atexit
import sys
import time
from threading import Thread

import chalk

from parcel.lib.singleton import Singleton


@Singleton
class __Parcel:
    watching = True

    def __init__(self):
        self.watch_thread = Thread(target=self.watch)
        self.watch_thread.setDaemon(True)

    def build(self):
        pass

    def watch(self):
        if 'test' in sys.argv:
            self.build()
            return

        while self.watching or not TESTING:
            self.build()
            time.sleep(0.5)

    def stop(self):
        print(chalk.yellow('Parcel is shutting down...'))
        self.watching = False
        self.watch_thread.join()


    def start(self):
        atexit.register(self.stop)
        print(chalk.green('Parcel is waiting...'))
        self.watch_thread.start()
