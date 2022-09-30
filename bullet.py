# 创建时间：2022/9/29 20:41
# 创建者：来自星星的奶
from pygame.sprite import Sprite
import pygame as pg


class Bullet(Sprite):

    def __init__(self, game):
        super().__init__()
        self.setting = game.setting
        self.image = pg.transform.scale(pg.image.load(self.setting.bullet_image_filepath),
                                        self.setting.bullet_image_size)
        self.rect = self.image.get_rect()
