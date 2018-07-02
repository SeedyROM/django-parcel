import atexit
import sys
import time
from threading import Thread


watching = True

def build():
    pass

def watch():
    global watching

    if 'test' in sys.argv:
        build()
        return

    while watching or not TESTING:
        build()
        time.sleep(0.5)


watch_thread = Thread(target=watch)
watch_thread.setDaemon(True)

def stop():
    global watching
    global watch_thread

    print('Parcel is shutting down...')
    watching = False
    watch_thread.join()


def start_parcel():
    global watch_thread

    atexit.register(stop)
    print('Parcel is waiting...')
    watch_thread.start()
