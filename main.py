import sys
import pygame as pg
from setting import Setting

class AlienInvasion:

    def __init__(self):
        pg.init()
        self.setting = Setting()
        self.screen = pg.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        pg.display.set_caption('Alien Invasion')

    def run_game(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            pg.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
