from threading import Thread
from typing import Callable
import time


class appThread(Thread):
    def __init__(self, thread: Callable) -> None:
        Thread.__init__(self)
        self.thread = thread

    def run(self) -> None:
        self.thread()


def app() -> None:
    while True:
        time.sleep(1)
        print("Thread loop")


if __name__ == "__main__":
    t = appThread(thread=app)
    t.start()
    while True:
        time.sleep(2)
        print("Main loop")
