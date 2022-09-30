import sys

import pygame
import pygame as pg

from setting import Setting
from player import Player
from pointer import Point
from bullet import Bullet
from enemy import Enemy


class Game:

    def __init__(self):
        pg.init()
        self.setting = Setting()
        self.screen = pg.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        self.screen.fill(self.setting.bg_color)
        pg.mouse.set_visible(False)
        pg.display.set_caption('走位模拟器')
        self.player = Player(self)
        self.ptr = Point(self)
        self.bullets = pg.sprite.Group()
        self.enemies = pg.sprite.Group()

    def _check_events(self):
        for event in pg.event.get():
            if event.type == pygame.MOUSEMOTION:
                self.ptr.rect.x = event.pos[0]
                self.ptr.rect.y = event.pos[1]
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    sys.exit()
                elif event.key == pg.K_q:
                    self.fire(pg.Vector2(self.ptr.rect.x, self.ptr.rect.y))
                elif event.key == pg.K_0:
                    self.create_enemy()
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.player.move_to_pos = pg.Vector2(event.pos)

    def create_enemy(self):
        enemy = Enemy(self)
        self.enemies.add(enemy)

    def fire(self, move_to_pos):
        bullet = Bullet(self, move_to_pos)
        self.bullets.add(bullet)

    def _check_collide_bullet_enemy(self):
        pg.sprite.groupcollide(self.bullets,self.enemies,True,True)

    def _update(self):
        self.player.update()
        self.bullets.update()
        self.enemies.update()

    def _draw(self):
        self.screen.fill(self.setting.bg_color)
        self.player.blitme()
        self.ptr.blitme()

        for bullet in self.bullets.sprites():
            if bullet.alive:
                bullet.blitme()
            else:
                self.bullets.remove(bullet)
        for enemy in self.enemies.sprites():
            enemy.blitme()

        pg.display.flip()
        self._check_collide_bullet_enemy()

    def run_game(self):

        while True:
            self._check_events()
            self._update()
            self._draw()


if __name__ == '__main__':
    ai = Game()
    ai.run_game()
