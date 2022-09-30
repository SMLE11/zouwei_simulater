# 创建时间：2022/9/29 20:41
# 创建者：来自星星的奶
import pygame.surface
from pygame.sprite import Sprite
import pygame as pg


class Bullet(Sprite):

    def __init__(self, game, move_to_pos):
        super().__init__()
        self.screen = game.screen
        self.setting = game.setting
        self.image = pg.transform.scale(pg.image.load(self.setting.bullet_image_filepath),
                                        self.setting.bullet_image_size)
        self.rect = self.image.get_rect()
        self.rect.center = game.player.rect.center
        self.move_to_pos = move_to_pos
        self.pos = pg.Vector2(float(self.rect.centerx), float(self.rect.centery))
        dist = self.move_to_pos - self.pos
        dist.normalize_ip()
        self.step = self.setting.bullet_speed * dist
        self.alive = True

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.pos += self.step
        self.rect.center = self.pos
        if self.rect.centerx < 0 or self.rect.centerx > self.setting.screen_width or self.rect.centery < 0 \
                or self.rect.centery > self.setting.screen_height:
            self.alive = False
