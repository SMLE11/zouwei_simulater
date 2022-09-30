# 创建时间：2022/9/30 8:48
# 创建者：来自星星的奶
import pygame as pg


class Point:
    def __init__(self, game):
        self.screen = game.screen
        self.image = pg.transform.scale(pg.image.load(game.setting.pointer_image_filepath), game.setting.pointer_image_size)
        self.rect = self.image.get_rect()
        self.screen_rect = game.screen.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
