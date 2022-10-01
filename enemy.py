# 创建时间：2022/9/30 19:45
# 创建者：来自星星的奶
import pygame as pg
import random
from pygame.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.image = pg.transform.scale(pg.image.load(game.setting.enemy_image_filepath),
                                        game.setting.enemy_image_size)
        self.setting = game.setting
        self.speed = self.setting.enemy_speed
        self.rect = self.image.get_rect()
        self.game=game
        num_start_pos = random.randint(1, 4)
        if num_start_pos == 1:
            self.rect.centerx = random.randint(0, self.setting.screen_width)
            self.rect.centery = -40
        elif num_start_pos == 2:
            self.rect.centerx = random.randint(0, self.setting.screen_width)
            self.rect.centery = self.setting.screen_height + 40
        elif num_start_pos == 3:
            self.rect.centerx = -40
            self.rect.centery = random.randint(0, self.setting.screen_height)
        else:
            self.rect.centerx = self.setting.screen_width + 40
            self.rect.centery = random.randint(0, self.setting.screen_height)
        self.pos = pg.Vector2(float(self.rect.centerx), float(self.rect.centery))
        self.move_to_pos = pg.Vector2(random.randint(0, self.setting.screen_width),
                                      random.randint(0, self.setting.screen_width))

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.game.auto_fire(self.rect.center)
        dist = self.move_to_pos - self.pos
        dist_len = dist.length()
        if dist_len > self.speed:
            dist.normalize_ip()
            step = self.setting.player_speed * dist
            self.pos += step
        else:
            self.pos = self.move_to_pos
            self.move_to_pos = pg.Vector2(random.randint(0, self.setting.screen_width),
                                          random.randint(0, self.setting.screen_width))
        self.rect.center = self.pos

