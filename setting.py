# 创建时间：2022/9/29 15:33
# 创建者：来自星星的奶
import pygame as pg
class Setting:
    def __init__(self):
        self.screen_width=1200
        self.screen_height=800
        self.screen_show_mode=pg.FULLSCREEN
        self.bg_color=(255,255,255)
        self.ship_speed=1