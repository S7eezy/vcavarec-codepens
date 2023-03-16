import keyboard
from pynput.mouse import Listener, Controller, Button
import vgamepad as vg
import time
import math
from typing import List


"""
Mouse virtualization
"""

mouseHandler = Controller()

def on_click(x, y, button, pressed):
    if pressed:
        print(f"{button} pressed, mouse position ({x}, {y})")
    if not pressed:
        print(f"{button} released, mouse position ({x}, {y})")

MouseListener = Listener(on_click=on_click)
MouseListener.start()

"""
Keyboard virtualization
"""

def keyboard_listener():
    while True:
        if keyboard.is_pressed("h"):
            keyboard.write("ello world")
            while keyboard.is_pressed("h"):
                pass

def keyboard_examples():
    keyboard.press("shift")
    time.sleep(0.1)
    keyboard.release("shift")

    keyboard.press("alt")
    keyboard.press("tab")
    time.sleep(0.1)
    keyboard.release("alt")
    keyboard.release("tab")

    keyboard.press_and_release("escape")

"""
Gamepad virtualization
"""

class Gamepad:
    def __init__(self):
        # Init gamepad
        self.vx = vg.VX360Gamepad()
        self.circle = self.buildCircle()

    def reset(self) -> None:
        self.vx.reset()
        self.vx.update()

    def left_stick(self, x) -> None:
        self.vx.left_joystick_float(math.cos(x), math.sin(x))
        time.sleep(0.02)
        self.vx.update()

    @staticmethod
    def buildCircle(start: int = 0, end: int = 360, step: int = 360/20) -> List[float]:
        """
        Creates a list of points in radians
        """
        pts = []
        for angle in range(start, end, step):
            pts.append(math.radians(angle))
        pts.append(pts[0])
        return pts

    def infinite_circle(self) -> None:
        while True:
            for pt in self.circle:
                self.left_stick(x=pt)


if __name__ == "__main__":
    keyboard_examples()
    keyboard_listener()

    gamepad = Gamepad()
    gamepad.infinite_circle()