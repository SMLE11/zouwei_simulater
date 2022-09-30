import sys

import pygame
import pygame as pg

import player
from setting import Setting
from player import Player
from pointer import Point


class Game:

    def __init__(self):
        pg.init()
        self.setting = Setting()
        self.screen = pg.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        self.screen.fill(self.setting.bg_color)
        pg.mouse.set_visible(False)
        pg.display.set_caption('走位模拟器')
        self.ship = Player(self)
        self.ptr = Point(self)

    def _check_events(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:

                if event.key == pg.K_ESCAPE:
                    sys.exit()

            elif event.type == pg.MOUSEBUTTONDOWN:
                self.ship.move_to_pos = pg.Vector2(event.pos)
            if event.type == pygame.MOUSEMOTION:
                self.ptr.rect = event.pos

    def _update_screem(self):
        self.screen.fill(self.setting.bg_color)
        self.ship.blitme()
        self.ptr.blitme()
        pg.display.flip()

    def run_game(self):

        while True:
            self._check_events()
            self.ship.update()
            self._update_screem()


if __name__ == '__main__':
    ai = Game()
    ai.run_game()
