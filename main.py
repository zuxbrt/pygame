#!/usr/bin/env python3

import math
import sys
import pygame


pygame.init()

size = width, height = 320, 240
speed = [0, 0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.dict['key'] == 119:  # w
                speed[1] = -3
            elif event.dict['key'] == 115:  # s
                speed[1] = 3
            elif event.dict['key'] == 97:  # a
                speed[0] = -3
            elif event.dict['key'] == 100:  # d
                speed[0] = 3
            print(event, flush=True)
        elif event.type == pygame.KEYUP:
            if event.dict['key'] in (119, 115):  # w s
                speed[1] = 0
            elif event.dict['key'] in (97, 100):  # a d
                speed[0] = 0
            print(event, flush=True)

    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = math.copysign(1, (-ballrect.left))
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = math.copysign(1, (-ballrect.top))

    ballrect = ballrect.move(speed)

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    clock.tick(120)
