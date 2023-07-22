import argparse
import json
import os.path

import pyautogui as gui

from heroes import Tinker


class StartUpMacro:

    _ALLOWED_HEROES = {
        'tinker': Tinker
    }

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-hero', help='Select hero name', nargs=1, required=True, dest='NAME')
        self.hero, *_ = parser.parse_args().NAME

    def run(self):
        self.__open()
        hero = self._ALLOWED_HEROES.get(self.hero.lower())
        if hero:
            hero(*self._read_settings()).run_macro()
        else:
            raise SystemExit('Unknown hero')

    def _read_settings(self):
        with open(f'{os.path.dirname(__file__)}/settings.json', 'r') as f:
            settings = json.load(f)
            return settings.get(self.hero.title()), settings.get('Hotkey')

    @staticmethod
    def __open():
        windows = gui.getAllWindows()
        for w in windows:
            if 'Dota 2' in w.title: return w.activate()
        else:
            raise SystemExit("Dota 2 has not opened yet")


if __name__ == '__main__':
    StartUpMacro().run()
