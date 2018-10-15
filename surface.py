# -*- coding:utf-8 -*-
import pygame


class Current_state:
    """显示当前状态框的类"""
    def __init__(self, my_settings, screen):
        self.screen = screen

        # 初始化
        self.x = my_settings.current_state_location_x
        self.y = my_settings.current_state_location_y
        self.text_color = my_settings.current_state_textcolor
        self.font = pygame.font.SysFont(None,48)
        self.str = "State: q"


    def show(self, state_string):
        """显示当前状态框"""
        all_str = self.str + state_string
        self.image = self.font.render(all_str,True,self.text_color)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.screen.blit(self.image,self.rect)

class Button:
    def __init__(self, my_settings, screen, str):
        self.screen = screen
        self.width = my_settings.button_width
        self.height = my_settings.button_length
        self.button_color = my_settings.button_color
        self.text_color = my_settings.button_textcolor
        self.font = pygame.font.SysFont(None,48)
        self.str = str
        self.y = my_settings.button_location_y


    def pre_button(self):
        # 创建按钮的rect对象，并使其居中
        #self.rect = pygame.Rect(self.screen.get_rect().centerx,self.y,self.width,self.height)

        self.msg_image = self.font.render(self.str,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.centerx = self.screen.get_rect().centerx
        self.msg_image_rect.y = self.y
        self.rect = self.msg_image_rect

    def draw_button(self):
        # 绘制一个用颜色填充的按钮，再绘制文本
        self.pre_button()
        #self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class Readwrite_head:
    def __init__(self, my_settings, screen):
        self.screen = screen
        self.color = my_settings.readwrite_head_color
        self.rect = pygame.Rect(screen.get_rect().centerx - 0.5*my_settings.readwrite_head_width, my_settings.readwrite_head_location_y, my_settings.readwrite_head_width, my_settings.readwrite_head_length)

    def draw_rt_head(self):
        self.screen.fill(self.color, self.rect)