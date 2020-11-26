#!/usr/bin/env python3
import pygame
# from pygame.locals import *
from glib import character
pygame.init()

angel_left = [pygame.image.load('data/angel/angel_L1.png'), pygame.image.load('data/angel/angel_L2.png'),
              pygame.image.load('data/angel/angel_L3.png'), pygame.image.load('data/angel/angel_L4.png'),
              pygame.image.load('data/angel/angel_L5.png'), pygame.image.load('data/angel/angel_L6.png'),
              pygame.image.load('data/angel/angel_L7.png'), pygame.image.load('data/angel/angel_L8.png'),
              pygame.image.load('data/angel/angel_L9.png')]
angel_right = [pygame.image.load('data/angel/angel_R1.png'), pygame.image.load('data/angel/angel_R2.png'),
               pygame.image.load('data/angel/angel_R3.png'), pygame.image.load('data/angel/angel_R4.png'),
               pygame.image.load('data/angel/angel_R5.png'), pygame.image.load('data/angel/angel_R6.png'),
               pygame.image.load('data/angel/angel_R7.png'), pygame.image.load('data/angel/angel_R8.png'),
               pygame.image.load('data/angel/angel_R9.png')]
walk_count = 0
direct = "left"

win = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
pygame.display.set_caption("Wiggle Brawl")

p = character.Character(100, 100, 5, 54, 78)


def refresh_screen():
    global walk_count
    if walk_count >= 24:
        walk_count = 0

    if not p.grav == 0:
        walk_count = 0

    if direct == "left":
        win.blit(angel_left[walk_count//3], (p.x, p.y))
        walk_count += 1
    elif direct == "right":
        win.blit(angel_right[walk_count//3], (p.x, p.y))
        walk_count += 1
    pygame.display.update()


run = True
while run:
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        direct = "left"
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        direct = "right"

    win.fill((100, 100, 100))
    p.move(keys)
    refresh_screen()
