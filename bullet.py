# 创建时间：2022/9/29 20:41
# 创建者：来自星星的奶
import pygame.surface
from pygame.sprite import Sprite
import pygame as pg


class Bullet(Sprite):

    def __init__(self, game, pos, move_to_pos, flag):
        super().__init__()
        self.screen = game.screen
        self.setting = game.setting
        if flag:
            self.image = pg.transform.scale(pg.image.load(self.setting.bullet_player_image_filepath),
                                            self.setting.bullet_image_size)
            self.speed = self.setting.bullet_player_speed
        else:
            self.image = pg.transform.scale(pg.image.load(self.setting.bullet_enemy_image_filepath),
                                            self.setting.bullet_image_size)
            self.speed = self.setting.bullet_enemy_speed

        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.move_to_pos = pg.Vector2(move_to_pos)
        self.pos = pg.Vector2(pos)
        dist = self.move_to_pos - self.pos
        if dist:
            dist.normalize_ip()
            self.alive = True
        else:
            self.alive = False
        self.step = self.speed * dist

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.pos += self.step
        self.rect.center = self.pos
        if self.rect.centerx < 0 or self.rect.centerx > self.setting.screen_width or self.rect.centery < 0 \
                or self.rect.centery > self.setting.screen_height:
            self.alive = False
