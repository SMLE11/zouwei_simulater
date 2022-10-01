# 创建时间：2022/9/29 15:33
# 创建者：来自星星的奶
import pygame as pg


class Setting:
    def __init__(self, game):
        # 游戏难度系数
        self.scale = 0
        self.scale_limit = 25
        # 主屏幕
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_show_mode = pg.FULLSCREEN
        self.bg_color = (255, 255, 255)
        # 玩家类
        self.player_speed = 0.9
        self.player_image_filepath = 'images/cyr.png'
        self.player_image_size = (60, 100)
        self.player_blow_image_filepath = 'images/blowup.png'
        self.player_blow_image_size = (60, 60)
        # 鼠标指针类
        self.pointer_image_filepath = 'images/mouse.png'
        self.pointer_image_size = (60, 60)
        # 子弹类
        self.bullet_player_image_filepath = 'images/bullet.png'
        self.bullet_enemy_image_filepath = 'images/enemy_bullet.png'
        self.bullet_image_size = (30, 30)
        self.bullet_player_speed = 1
        self.bullet_enemy_speed = 0.4
        # 敌人类
        self.enemy_image_filepath = 'images/zdz.png'
        self.enemy_image_size = (60, 80)
        self.enemy_speed = 0.4
        self.enemy_fire_freq = 2500
        self.enemy_create_freq = 2500

    def update_scale(self):
        self.bullet_enemy_speed = 0.4 + 0.05 * self.scale
        self.enemy_create_freq = 2500 - 100 * self.scale
        self.enemy_fire_freq = 2500 - 100 * self.scale  # 越低频率越高
        self.enemy_speed = 0.4 + 0.05 * self.scale

    def show_score(self, game):
        self.font = pg.font.SysFont(None, 48)
        self.scoreboard_image = self.font.render("score:" + str(self.scale), True, (0, 0, 0,), (255, 255, 255))
        self.scoreboard_image_rect = self.scoreboard_image.get_rect()
        self.scoreboard_image_rect.center = (60, 40)
        game.screen.blit(self.scoreboard_image, self.scoreboard_image_rect)
