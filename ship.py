# 创建时间：2022/9/29 15:38
# 创建者：来自星星的奶
from math import sqrt

import pygame as pg
from pygame import freetype


class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pg.transform.scale(pg.image.load('images/ship.JPG'), (20, 20))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.speed = ai_game.setting.ship_speed
        self.move_to_pos = pg.Vector2(1070,780)
        self.now_pos = pg.Vector2(self.rect.x, self.rect.y)
        self.setting = ai_game.setting

    def blitme(self):
        self.screen.blit(self.image, self.now_pos)

    def update(self):
        self.move()

    def move(self):
        dist = self.move_to_pos - self.now_pos
        dist_len = dist.length()
        if dist_len>self.setting.ship_speed:
            dist.normalize_ip()
            step = self.setting.ship_speed * dist
            self.now_pos+=step
        else:
            self.now_pos=self.move_to_pos


