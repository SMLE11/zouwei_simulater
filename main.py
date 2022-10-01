import random
import sys
from time import sleep

import pygame
import pygame as pg

from setting import Setting
from player import Player
from pointer import Point
from bullet import Bullet
from enemy import Enemy
from button import Button


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
        self.enemies_bullets = pg.sprite.Group()
        self.status = False
        self.button = Button(self, 'Play')
        self.mouse_down_pos = (0, 0)

    def _check_events_wtih_input(self):
        for event in pg.event.get():
            if event.type == pygame.MOUSEMOTION:
                self.ptr.rect.x = event.pos[0]
                self.ptr.rect.y = event.pos[1]
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_down_pos = pg.mouse.get_pos()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    sys.exit()
                elif event.key == pg.K_q:
                    self.fire((self.ptr.rect.x, self.ptr.rect.y))
                elif event.key == pg.K_0:
                    self.create_enemy()
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.player.move_to_pos = pg.Vector2(event.pos)

    def _check_events_wtihout_input(self):
        self._check_collide_bullet_enemy()
        self._check_collide_player()

    def create_enemy(self):
        enemy = Enemy(self)
        self.enemies.add(enemy)

    def auto_create_enemy(self):
        num = random.randint(0, self.setting.enemy_create_freq)
        if num == 0:
            self.create_enemy()

    def fire(self, move_to_pos):
        bullet = Bullet(self, self.player.rect.center, move_to_pos, True)
        self.bullets.add(bullet)

    def auto_fire(self, pos):
        num = random.randint(0, self.setting.enemy_fire_freq)
        if num == 0:
            bullet = Bullet(self, pos, self.player.rect.center, False)
            self.enemies_bullets.add(bullet)

    def _check_collide_bullet_enemy(self):
        pg.sprite.groupcollide(self.bullets, self.enemies, True, True)

    def _check_collide_player(self):
        item1 = pg.sprite.spritecollideany(self.player, self.enemies_bullets)
        item2 = pg.sprite.spritecollideany(self.player, self.enemies)
        if item1 or item2:
            self.enemies_bullets.remove(item1)
            self.enemies.remove(item2)
            self.player.blow_up()
            self.status = 0

    def ready_to_play(self):
        if self.button.rect.collidepoint(self.mouse_down_pos[0], self.mouse_down_pos[1]):
            self.status = True
            self.reset()

    def _update(self):

        self.player.update()
        self.bullets.update()
        self.enemies_bullets.update()
        self.enemies.update()
        self.auto_create_enemy()

    def reset(self):
        self.enemies.empty()
        self.bullets.empty()
        self.enemies_bullets.empty()
        self.player.__init__(self)

    def _draw(self):
        self.screen.fill(self.setting.bg_color)
        self.player.blitme()
        if not self.status:
            self.button.blitme()
        for bullet in self.bullets.sprites():
            if bullet.alive:
                bullet.blitme()
            else:
                self.bullets.remove(bullet)

        for bullet in self.enemies_bullets.sprites():
            if bullet.alive:
                bullet.blitme()
            else:
                self.enemies_bullets.remove(bullet)

        for enemy in self.enemies.sprites():
            enemy.blitme()
        self.ptr.blitme()

    def run_game(self):

        while True:

            self._check_events_wtih_input()
            self._check_events_wtihout_input()
            self._draw()
            if self.status:
                self._update()
            else:
                self.ready_to_play()
            pg.display.flip()


if __name__ == '__main__':
    ai = Game()
    ai.run_game()
