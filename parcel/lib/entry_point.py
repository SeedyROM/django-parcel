import time
import atexit
from threading import Thread


watching = True

def watch():
    global watching
    while watching:
        time.sleep(0.5)

watch_thread = Thread(target=watch)


def stop():
    global watching
    global watch_thread

    print('Parcel is shutting down...')
    watching = False
    watch_thread.join()


def start_parcel():
    atexit.register(stop)
    print('Parcel is waiting...')
    watch_thread.start()