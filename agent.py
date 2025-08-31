import pygame
from pygame.draw import circle, rect
from pygame.math import Vector2

window_width = 1280
window_height = 720

class Agent:
    def __init__(self, position, radius, color):
        self.circle_pos = position
        self.circle_vel = Vector2(4, 3)
        self.circle_radius = radius
        self.circle_color = color
        #Pending physics
        self.circle_acc = Vector2(0,0)
        self.mass = 1.0

    def seek_to(self, target_pos):
        d = target_pos - self.circle_pos
        d.normalize()
        self.apply_force(d)

    def apply_force(self, force):
        self.circle_acc += force / self.mass

    def update(self, dt):

        self.circle_pos += self.circle_vel
        #Horizontal
        if self.circle_pos.x - self.circle_radius <= 0 or self.circle_pos.x + self.circle_radius >= window_width:
            self.circle_vel.x *= -1
            c = pygame.Color(0)  # create Color object
            c.hsva = (pygame.time.get_ticks() % 360, 100, 100, 100)
            self.circle_color = c

        #Vertical
        if self.circle_pos.y - self.circle_radius <= 0 or self.circle_pos.y + self.circle_radius >= window_height:
            self.circle_vel.y *= -1
            c = pygame.Color(0)
            c.hsva = (pygame.time.get_ticks() % 360, 100, 100, 100)
            self.circle_color = c
        #Pending physics
        self.circle_acc = Vector2(0,0)

    def draw(self, screen):
        circle(screen, self.circle_color, (int(self.circle_pos.x), int(self.circle_pos.y)), self.circle_radius)
