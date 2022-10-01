# 创建时间：2022/9/29 15:33
# 创建者：来自星星的奶
import pygame as pg


class Setting:
    def __init__(self):
        # 主屏幕
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_show_mode = pg.FULLSCREEN
        self.bg_color = (255, 255, 255)
        # 玩家类
        self.player_speed = 0.7
        self.player_image_filepath = 'images/cyr.png'
        self.player_image_size = (60, 80)
        self.player_blow_image_filepath = 'images/blowup.png'
        self.player_blow_image_size = (60, 60)
        # 鼠标指针类
        self.pointer_image_filepath = 'images/mouse.png'
        self.pointer_image_size = (60, 60)
        # 子弹类
        self.bullet_player_image_filepath = 'images/bullet.png'
        self.bullet_enemy_image_filepath = 'images/enemy_bullet.png'
        self.bullet_image_size = (30, 30)
        self.bullet_player_speed = 0.7
        self.bullet_enemy_speed = 0.4
        # 敌人类
        self.enemy_image_filepath = 'images/zdz.png'
        self.enemy_image_size = (60, 80)
        self.enemy_speed = 0.4
        self.enemy_fire_freq = 1000  # 越低频率越高
        self.enemy_create_freq = 1000