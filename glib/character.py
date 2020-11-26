#!/usr/bin/env python3
import pygame
# from pygame.locals import *
pygame.init()


class Character:
    def __init__(self, x, y, vel, wid, hei):
        self.x = x
        self.y = y
        self.vel = vel
        self.grav = 0
        self.count = 5
        self.running = False
        self.jumping = False
        self.wid = wid
        self.hei = hei
        self.jump_power = 10

    def move(self, way):
        if way[pygame.K_LEFT] or way[pygame.K_a] and self.x > 0:
            self.x -= self.vel
            self.running = True
        if way[pygame.K_RIGHT] or way[pygame.K_d] and self.x < pygame.display.Info().current_w - self.wid:
            self.x += self.vel
            self.running = True
        if self.x < 0:
            self.x = 0
        if self.x > pygame.display.Info().current_w - self.wid:
            self.x = pygame.display.Info().current_w - self.wid
        if self.y < pygame.display.Info().current_h - self.hei:
            self.y += self.grav
            if self.grav < 10:
                self.grav += 1
        elif way[pygame.K_UP] or way[pygame.K_SPACE] or way[pygame.K_w]:
            self.grav = -1 * self.jump_power
            self.y += self.grav
        else:
            self.grav = 0
            self.y = pygame.display.Info().current_h - self.hei

        if not self.grav == 0:
            self.jumping = True
