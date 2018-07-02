import time
import atexit
from threading import Thread


watching = True

def watch():
    global watching
    while watching:
        time.sleep(0.5)

watch_thread = Thread(target=watch)

@atexit.register
def stop():
    print('Parcel is shutting down...')
    global watching
    watching = False
    watch_thread.join()


def start_parcel():
    print('Parcel is waiting...')
    watch_thread.start()