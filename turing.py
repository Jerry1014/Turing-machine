# -*- coding:utf-8 -*-
import pygame

class Transition():
    """规则变换集合"""
    def __init__(self, transition, sym, transition2, sym2, dir):# 状态前，读取符号，状态后，更改符号，读写头移动方向
        super(Transition,self).__init__()
        self.transition = transition
        self.sym = sym
        self.transition2 = transition2
        self.sym2 = sym2
        self.dir = dir

    def cheak(self, state, str):
        if self.transition == state:
            if self.sym == str:
                return (self.transition2, self.sym2, self.dir)

class Tape():
    """纸带字符集合"""
    def __init__(self, my_settings, screen, str):
        super(Tape,self).__init__()
        # 设置大小和字符
        self.str = str
        self.screen = screen
        self.width = my_settings.tape_width
        self.length = my_settings.tape_length
        self.bg_color = my_settings.tape_bg_color
        self.text_color = my_settings.tape_text_color
        self.font = pygame.font.SysFont(None,48)

        self.rect = pygame.Rect(0,0,self.width,self.length)
        self.rect.y = my_settings.tape_location_y
        self.prep_str()
        self.the_next_x = 0
        self.speed = my_settings.tape_speed

    def prep_str(self):
        """将str渲染为图像"""
        self.str_image = self.font.render(self.str,True,self.text_color,self.bg_color)
        self.str_image_rect = self.str_image.get_rect()
        self.str_image_rect.center = self.rect.center

    def draw_str(self):
        """绘制一个用颜色填充的方块，再绘制文本"""
        self.prep_str()
        self.screen.fill(self.bg_color,self.rect)
        self.screen.blit(self.str_image,self.str_image_rect)

    def arrange_location(self):
        """缓慢更新字符在屏幕上的位置"""
        #if (self.the_next_x - self.rect.centerx) < 5 or (self.the_next_x - self.rect.centerx) > -5:
        #    self.rect.centerx = self.the_next_x
        if self.the_next_x > self.rect.centerx:
            self.rect.centerx += self.speed
        elif self.the_next_x < self.rect.centerx:
            self.rect.centerx -= self.speed

        self.str_image_rect.centerx = self.rect.centerx
        self.draw_str()

    def arrange_location_imi(self):
        """马上更新字符在屏幕上的位置"""
        self.rect.centerx = self.the_next_x
        self.str_image_rect.centerx = self.rect.centerx
        self.draw_str()
