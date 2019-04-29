#!/usr/bin/python3

import pygame
import time

pygame.init()
def main():

    screen = pygame.display.set_mode((480,852), 0, 32)
    background = pygame.image.load("/home/he/Pictures/wangzai.jpg")
    while True:
        screen.blit(background, (0,0))
        pygame.display.update()

 if __name__ == '__main__':
    main()
