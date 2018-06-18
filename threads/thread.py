import _thread
import time
from thread_lock import thread_lock, target_fps


class Thread(object):

    def __init__(self, my_function, args, name='generic thread', delay=1 / target_fps, lock=thread_lock):
        self.args = args
        self.lock = lock
        self.name = name
        self.function = my_function
        self.delay = delay
        self.stop_ = False
        self.start()

    def run(self):
        while not self.stop_:
            self.lock.acquire()
            if self.args != ():
                self.function(self.args)
            else:
                self.function()
            self.lock.release()
            time.sleep(self.delay)
        else:
            pass
#            print('Finished:', self.name + '.')

    def start(self):
        _thread.start_new_thread(self.run, self.args)

    def stop(self):
        self.stop_ = True
