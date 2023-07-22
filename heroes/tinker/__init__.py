import pyautogui as gui
import keyboard as kb
import mouse


class Tinker:
    def __init__(self, keys, hotkey):
        self.keys = keys
        self.hotkey = hotkey

    def run_macro(self):
        while True:
            mouse.on_middle_click(self.__cast)
            if not kb.wait("Esc"):
                mouse.unhook_all()

    def __cast(self):
        for key in self.keys.values():
            kb.send(key.lower())
            gui.sleep(.1)
        gui.sleep(1.2)
