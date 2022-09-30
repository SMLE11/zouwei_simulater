# 创建时间：2022/9/29 15:33
# 创建者：来自星星的奶
import pygame as pg
class Setting:
    def __init__(self):
        #主屏幕
        self.screen_width=1200
        self.screen_height=800
        self.screen_show_mode=pg.FULLSCREEN
        self.bg_color=(255,255,255)
        #玩家类
        self.player_speed=1
        self.player_image_filepath='images/zdz.png'
        self.player_image_size=(60,80)
        #鼠标指针类
        self.pointer_image_filepath = 'images/mouse.png'
        self.pointer_image_size = (60, 60)
        #玩家子弹类
        self.bullet_image_filepath = 'images/bullet.png'
        self.bullet_image_size = (30, 30)
        self.bullet_speed = 1
