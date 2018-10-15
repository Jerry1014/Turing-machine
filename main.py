# -*- coding:utf-8 -*-
import pygame
from settings import Settings
from surface import Current_state,Button,Readwrite_head
import events as e
from turing import Transition,Tape

def run():
    # 界面初始化
    pygame.init()
    my_settings = Settings()
    screen = pygame.display.set_mode((my_settings.screen_width,my_settings.screen_length))
    pygame.display.set_caption("图灵机")
    my_current_state = Current_state(my_settings, screen)
    my_button = Button(my_settings, screen, 'START')
    my_current_state = Current_state(my_settings, screen)
    my_readwrite_head = Readwrite_head(my_settings, screen)


    # 主循环
    while True:
        # 每一次载入图灵机前的初始化
        mouseup = [1]
        transitions = [] # 转换函数
        my_tape = [] # 纸带
        state_rec = {'ini_sta':0, 'fin_sta':[]} # 开始状态和结束状态集合
        state = {'state':0, 'location':1, 'result':0}# state 当前状态 location 当前读写头在纸带上的位置 result -1,0,1分别代表语句判断完毕\仍在判断,重新开始

        while True:
            if e.check_rule(transitions, state_rec) == 1:
                break;
        e.cheak_tape(my_settings, screen, my_tape)
        e.get_ready(my_settings, screen, state_rec, state, my_tape)
        while True:
            e.cheak_events(state, state_rec, screen, my_tape, transitions, my_button, my_settings, mouseup)
            if state['result'] == 0:
                e.update_screen(screen, my_settings, my_button, my_current_state, state, my_tape, my_readwrite_head, mouseup)
            elif state['result'] == 1:
                break

if __name__ == '__main__':
    run()