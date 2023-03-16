from threading import Thread
from typing import Callable
import time

"""
App thread
"""

class appThread(Thread):
    def __init__(self, thread: Callable) -> None:
        Thread.__init__(self)
        self.thread = thread

    def run(self) -> None:
        while True:
            self.thread()

def app() -> None:
    time.sleep(1)
    print("Thread")


"""
Pausable app thread
"""

class pausableAppThread(Thread):
    def __init__(self, thread: Callable) -> None:
        Thread.__init__(self)
        self.thread = thread
        self.condition = True
        self.stop = False

    def pause(self) -> None:
        self.condition = False

    def resume(self) -> None:
        self.condition = True

    def toggle(self) -> None:
        self.condition = not self.condition

    def kill(self) -> None:
        self.stop = True
        self.condition = False

    def run(self) -> None:
        while True:
            while self.condition:
                self.thread()
            if self.stop:
                return
            time.sleep(0.1)

def pausableApp() -> None:
    time.sleep(1)
    print("Pausable")


if __name__ == "__main__":
    t = appThread(thread=app)
    t.start()

    pt = pausableAppThread(thread=pausableApp)
    pt.start()

    k = 0
    while True:
        k += 1
        time.sleep(2)
        print("Main")
        if k % 10 == 0:
            print("kill")
            pt.kill()
