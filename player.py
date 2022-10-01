# 创建时间：2022/9/29 15:38
# 创建者：来自星星的奶
from math import sqrt

import pygame as pg


class Player:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.setting = game.setting
        self.image = pg.transform.scale(pg.image.load(self.setting.player_image_filepath),
                                        self.setting.player_image_size)
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.pos = pg.Vector2(float(self.rect.centerx), float(self.rect.centery))
        self.move_right = False
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.speed = game.setting.player_speed
        self.move_to_pos = pg.Vector2(self.rect.x, self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.move()

    def move(self):
        dist = self.move_to_pos - self.pos
        dist_len = dist.length()
        if dist_len > self.speed:
            dist.normalize_ip()
            step = self.setting.player_speed * dist
            self.pos += step
        else:
            self.pos = self.move_to_pos

        self.rect.center = self.pos

    def blow_up(self):
        self.image = pg.transform.scale(pg.image.load(self.setting.player_blow_image_filepath),
                                        self.setting.player_blow_image_size)
