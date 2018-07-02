import atexit
import sys
import time
import os 
from threading import Thread

import chalk

from django.conf import settings

from parcel.lib.singleton import Singleton
from parcel.lib import node


@Singleton
class __Parcel:
    watching = True
    node_version = None

    def __init__(self):
        self.watch_thread = Thread(target=self.watch)
        self.watch_thread.setDaemon(True)
        
        if hasattr(settings, 'PARCEL_CLIENT_PATH'):
            self.client_path = os.path.join(settings.BASE_DIR, settings.PARCEL_CLIENT_PATH)
        else:
            self.client_path = os.path.join(settings.BASE_DIR, 'client')

    def build(self):
        print(self.client_path)
        node.test_npm()

    def watch(self):  
        node.check_node_installed()    
        print(chalk.green(f'Parcel started... (Node v{self.node_version})'))        

        if 'test' in sys.argv:
            self.build()
            return

        print(chalk.yellow('Parcel is waiting...'))
        while self.watching and not TESTING:
            self.build()
            time.sleep(0.5)

    def start(self):
        self.watch_thread.start()
        atexit.register(self.stop)

    def stop(self):
        self.watching = False
        self.watch_thread.join()
        print(chalk.yellow('Parcel is shutting down...'))
        print(chalk.green('Parcel finished'))
