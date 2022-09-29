import sys

import pygame
import pygame as pg

import ship
from setting import Setting
from ship import Ship


class AlienInvasion:

    def __init__(self):
        pg.init()
        self.setting = Setting()
        self.screen = pg.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        self.screen.fill(self.setting.bg_color)
        pg.display.set_caption('Alien Invasion')
        self.ship = Ship(self)

    def _check_events(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:

                if event.key == pg.K_ESCAPE:
                    sys.exit()

            elif event.type == pg.MOUSEBUTTONDOWN:
                self.ship.move_to_pos= pg.Vector2(event.pos)
                self.ship.now_pos= pg.Vector2(self.ship.rect.x, self.ship.rect.y)

    def _update_screem(self):
        self.screen.fill(self.setting.bg_color)
        self.ship.blitme()
        pg.display.flip()

    def run_game(self):

        while True:
            self._check_events()
            self.ship.update()
            self._update_screem()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
