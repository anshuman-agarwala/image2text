import pygame
import pygame.freetype
import sys
import cv2
import numpy as np
from itertools import chain

def img2txt(img_src):
    width,height = 600,240
    asc = {9:' ', 8:'.', 7:':', 6:'-', 5:'=', 4:'+', 3:'*', 2:'#', 1:'%', 0:'@'}
    print(img_src.flatten()//26)
    asc_data = list(map(asc.get,map(int,[x // 26 for x in chain(*img_src)])))
    #img_src = img_src.flatten() //26
    #asc_data = list(map(asc.get,img_src))
    txt_img = [asc_data[i:i+width] for i in range(0,len(asc_data),width)]
    return txt_img

def cam_obj():
    cam = cv2.VideoCapture(0)
    def get_frame():
        _, frame = cam.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # print(frame.shape)
        frame = cv2.resize(frame, (600,240))
        return frame
    return get_frame

if __name__ == "__main__":
    camera = cam_obj()
    pygame.init()
    font = pygame.font.SysFont('Courier New',4)
    fontSize = font.get_height()
    size = screen_width, screen_height = 1920,1080
    screen = pygame.display.set_mode(size)
    screen.fill((255,255,255))

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        frame = camera()
        txt_img = img2txt(frame)
        screen.fill((255,255,255))
        for idx,line in enumerate(txt_img):
            currentTextline = font.render(''.join(line), False, (0, 0, 0))
            currentPostion = (0, idx * fontSize)
            screen.blit(currentTextline, currentPostion)
        pygame.display.flip()
        