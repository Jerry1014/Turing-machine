# -*- coding:utf-8 -*-
class Settings:
    def __init__(self):
        # 屏幕设置
        self.screen_width = 1200
        self.screen_length = 600
        self.bg_color = (255,255,255)

        # 显示“请在此输入纸带”设置
        self.input_tape_location_x = 112
        self.input_tape_location_y = 90
        self.input_tape_textcolor = (30,30,30)

        # 当前状态显示框设置
        self.current_state_location_x = 26
        self.current_state_location_y = 33
        self.current_state_textcolor = (30,30,30)

        # 按建设置
        self.button_width = 91
        self.button_length = 39
        self.button_color = (160,160,160)
        self.button_textcolor = (30,30,30)
        self.button_location_centerx = 600
        self.button_location_y = 150
        self.button_location_end_y = 50

        # 纸带设置
        self.tape_width = 50
        self.tape_length = 100
        self.tape_bg_color = (160,160,160)
        self.tape_text_color = (255,255,255)
        self.tape_location_y = 290
        self.tape_speed = 1 # 每次移动的像素，越大越快

        # 读写头设置
        self.readwrite_head_width = 20
        self.readwrite_head_length = 40
        self.readwrite_head_color = (255,0,0)
        self.readwrite_head_location_y = 250

        # 判断结束显示设置
        self.start_again_location_y = 250
        self.start_again_textcolor = (30,30,30)



