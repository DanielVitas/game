import _thread
import time
from thread_lock import thread_lock


class AnimationThread(object):

    def __init__(self, generator, args, delay=[1/3], name='animation thread', lock=thread_lock):
        self.args = args
        self.lock = lock
        self.name = name
        self.generator = generator
        self.delay = delay
        self.stop_ = False
        self.start()

    def run(self, *args):
        i = 0
        if args != ():
            gen = self.generator(args)
        else:
            gen = self.generator()
        while not self.stop_:
            if self.delay[i] < 0:
                self.stop()
            else:
                self.lock.acquire()
                next(gen)
                self.lock.release()
                time.sleep(self.delay[i])
                i += 1
                i %= len(self.delay)

    def start(self):
        _thread.start_new_thread(self.run, self.args)

    def stop(self):
        self.stop_ = True
