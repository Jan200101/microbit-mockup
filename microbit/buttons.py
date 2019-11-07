from .__init__ import A_KEY, B_KEY

import os

try:
    if os.name == "posix" and os.getuid() != 0:
        raise ImportError("User is not root")
        
    import keyboard
except ImportError:
    keyboard = None

class Button:

    def __init__(self, kbdkey = None):
        self.__kbdkey__ = kbdkey

    def is_pressed(self):
        if keyboard and self.__kbdkey__:
            return keyboard.is_pressed(self.__kbdkey__)
        return False


button_a = Button(A_KEY)
button_b = Button(B_KEY)