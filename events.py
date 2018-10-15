# -*- coding:utf-8 -*-
import tkinter
from tkinter.filedialog import askopenfilename
import pygame
from turing import Transition,Tape
import sys
from time import sleep

def check_rule(transitions, state_rec):
    """响应载入规则按钮"""
    try:
        while True:
            # 窗口初始化
            root = tkinter.Tk()
            root.geometry('500x300+500+200')
            root.title('载入规则')
            lb = tkinter.Label(root,text = '')
            lb.pack()

            # 读取文件
            filename = askopenfilename()
            if filename:
                sign = read_rule(filename, transitions, state_rec)
                if sign == -2:
                    root.destroy()
                    return 1
                elif sign == -1:
                    lb.config(text="变换规则有错")
                elif sign == 0:
                    lb.config(text="没有找到文件或读取文件失败")
                else: lb.config(text="文件错误，在第"+str(sign)+"行")
    except:
        root.destroy()
        sys.exit()

def read_rule(filename, transitions, state_rec):
    """从文件中读取规则"""
    line_sign = 0
    try:
        file = open(filename,"r")
    except IOError:
        return 0

    while True:
        line = file.readline()

        # 文件至少有三行
        if not line:
            if line_sign >= 3:
                line_sign = -2
            else: line_sign = -1
            break

        line_sign += 1
        line.split()
        try:
            # 第一行为开始状态，第二行为结束状态集合
            if line_sign == 1:
                state_rec['ini_sta'] = line[0]
            elif line_sign == 2:
                for i in range(0,len(line),2):
                    state_rec['fin_sta'].append(line[i])
            else:
                transition = line[0]
                sym = line[2]
                transition2 = line[4]
                sym2 = line[6]
                if line[8] == 'L':
                    dir = -1
                elif line[8] == 'S':
                    dir = 0
                else: dir = 1

                new_transition = Transition(transition, sym, transition2, sym2, dir)
                transitions.append(new_transition)
        except:
            return line_sign
    return line_sign

def cheak_tape(my_settings, screen, my_tape):
    """响应载入纸带按钮"""
    try:
        # 窗口初始化
        root = tkinter.Tk()
        root.geometry('500x200+500+200')
        root.title('载入纸带')
        e = tkinter.Entry(root,)
        e.pack(pady = 30)

        def input_string():
            if e.get():
                input_strings = list(e.get())
                for s in input_strings:
                    new_str = Tape(my_settings, screen, s)
                    my_tape.append(new_str)
                root.quit()

        b = tkinter.Button(root,text='确认',command=input_string)
        b.pack()
        root.mainloop()
        if len(my_tape) > 0:
            root.destroy()
            return 1
    except:
        sys.exit()

def get_ready(my_settings, screen, state_rec, state, my_tape):
    """程序开始时的准备工作"""
    state['state'] = state_rec['ini_sta']
    state['direction'] = 1
    # 在纸带前后加入空白B
    new_block_str = Tape(my_settings, screen, 'B')
    new_block_str2 = Tape(my_settings, screen, 'B')
    my_tape.insert(0,new_block_str)
    my_tape.insert(len(my_tape),new_block_str2)

    arrange_tape_location(state, screen, my_settings, my_tape)

def cheak_events(state, state_rec, screen, my_tape, transitions, my_button, my_settings, mouseup):
    """响应”START“按钮"""
    button_clicked = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseup[0] = 0
            button_clicked = my_button.rect.collidepoint(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONUP:
            mouseup[0] = 1

    # 按下“START”或者“START AGAIN”
    if button_clicked or mouseup[0] == 0:
        # 判断当前为“START”还是“START AGAIN”
        if state['result'] != -1:
            # 当鼠标一直为按下时，缓慢进行变换
            if mouseup[0] == 0:
                sleep(0.2)
            # 将在进行缓慢移动的纸带马上安排到正确位置上
            for i in my_tape:
                i.arrange_location_imi()

            state['result'] = -1
            for t in transitions:
                # 寻找对应的转移函数
                res = t.cheak(state['state'], my_tape[state['location']].str)
                if res:
                    state['state'] = res[0]

                    # 当修改的为纸带前后的B，且是更改为其他的字符时
                    if my_tape[state['location']].str == 'B' and res[1] != 'B':
                        if state['location'] == 0:
                            new_block_str = Tape(my_settings, screen, 'B')
                            my_tape.insert(0,new_block_str)
                        elif state['location'] == len(my_tape) - 1:
                            new_block_str = Tape(my_settings, screen, 'B')
                            my_tape.insert(len(my_tape),new_block_str)

                    my_tape[state['location']].str = res[1]
                    state['location'] += res[2]
                    state['result'] = 0
                    break

            # 无符合的状态转移函数
            if state['result'] == -1:
                if state['state'] in state_rec['fin_sta']:
                    game_over(my_button, screen, my_settings, 'Received')
                else: game_over(my_button, screen, my_settings, 'Not Received')
        else: 
        # 按下“START AGAIN”且不是一直按住”START“时，重新初始化按钮
            for event2 in pygame.event.get():
                if event2.type == pygame.MOUSEBUTTONUP:
                    state['result'] = 1
                    my_button.str = 'Start'
                    my_button.y = my_settings.button_location_y
                    my_button.draw_button()


def arrange_tape_location(state, screen, my_settings, my_tape):
    """安排纸带中每个字符一个合适的位置"""
    centerx = screen.get_rect().centerx
    my_tape[state['location']].the_next_x = centerx
    for i in range(state['location'] - 1, -1, -1):
        my_tape[i].the_next_x = centerx - (state['location'] - i) * my_settings.tape_width
    for j in range(state['location'] + 1, len(my_tape), 1):
        my_tape[j].the_next_x = centerx + (j - state['location']) * my_settings.tape_width

def update_screen(screen, my_settings, my_button, my_current_state, state, my_tape, my_readwrite_head, mouseup):
    # 重新绘制屏幕
    screen.fill(my_settings.bg_color)

    my_current_state.show(str(state['state']))
    arrange_tape_location(state, screen, my_settings, my_tape)
    for i in my_tape:
        i.arrange_location()
        #i.draw_str()
    my_button.draw_button()
    my_readwrite_head.draw_rt_head()

    pygame.display.flip()

def game_over(my_button, screen, my_settings, str):
    """覆盖原来的屏幕，绘制“START AGAIN"""
    screen.fill(my_settings.bg_color)
    my_button.str = 'Start again'
    my_button.y = my_settings.button_location_end_y
    my_button.draw_button()

    text_color = my_settings.start_again_textcolor
    font = pygame.font.SysFont(None,48)
    image = font.render(str,True,text_color)
    rect = image.get_rect()
    rect.centerx = screen.get_rect().centerx
    rect.y = my_settings.start_again_location_y
    screen.blit(image,rect)

    pygame.display.flip()
