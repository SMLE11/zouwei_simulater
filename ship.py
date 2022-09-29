# 创建时间：2022/9/29 15:38
# 创建者：来自星星的奶
from math import sqrt

import pygame as pg


class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pg.transform.scale(pg.image.load('images/ship.JPG'), (20, 20))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.move_right = False
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.speed = ai_game.setting.ship_speed
        self.move_to_pos = pg.Vector2(self.rect.x, self.rect.y)
        self.now_pos = self.move_to_pos
        self.setting = ai_game.setting

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.move()

    def move(self):
        dist = self.move_to_pos-self.now_pos
        dist_len=dist.length()
        if dist_len:
            dist.normalize_ip()
            step = self.setting.ship_speed*dist
            v_x = abs(step.x)
            v_y = abs(step.y)
        else:
            v_x=0
            v_y=0
        if self.rect.x > self.move_to_pos.x:
            self.rect.x -= v_x
            if self.rect.x < self.move_to_pos.x:
                self.rect.x = self.move_to_pos.x  # 修正位置
        else:
            self.rect.x += v_x
            if self.rect.x > self.move_to_pos.x:
                self.rect.x = self.move_to_pos.x  # 修正位置

        if self.rect.y > self.move_to_pos.y:
            self.rect.y -= v_y
            if self.rect.y < self.move_to_pos.y:
                self.rect.y = self.move_to_pos.y  # 修正位置
        else:
            self.rect.y += v_y
            if self.rect.y > self.move_to_pos.y:
                self.rect.y = self.move_to_pos.y  # 修正位置


