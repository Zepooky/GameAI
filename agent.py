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

        self.circlephys_pos = pygame.math.Vector2(400, 300)
        self.circlephys_vel = pygame.math.Vector2(0, 0)
        self.circlephys_radius = 60
        self.circlephys_color = (0, 255, 255)
        self.circlephys_acc = 0.01 #Mouse Acceleration
        self.circlephys_damp = 0.92 #Momentum
        self.EYESIGHT = 100
        self.DIST = 5
        
    def seek_to(self, target_pos):
        d = target_pos - self.circle_pos
        if d.length() != 0:
            d = d.normalize()
            self.apply_force(d)
    
    def apply_force(self, force):
        self.circle_acc += force / self.mass

    def update(self, dt):
        self.circle_pos += self.circle_vel

        if self.circle_pos.x - self.circle_radius <= 0 or self.circle_pos.x + self.circle_radius >= window_width:
            self.circle_vel.x *= -1
            c = pygame.Color(0)
            c.hsva = (pygame.time.get_ticks() % 360, 100, 100, 100)
            self.circle_color = c

        if self.circle_pos.y - self.circle_radius <= 0 or self.circle_pos.y + self.circle_radius >= window_height:
            self.circle_vel.y *= -1
            c = pygame.Color(0)
            c.hsva = (pygame.time.get_ticks() % 360, 100, 100, 100)
            self.circle_color = c

        mouse_vec = Vector2(pygame.mouse.get_pos())  #Current mouse position
        direction = mouse_vec - self.circlephys_pos

        #Apply acceleration toward the mouse
        direction *= self.circlephys_acc

        #Update velocity and apply damping
        self.circlephys_vel += direction
        self.circlephys_vel *= self.circlephys_damp

        #Update position
        self.circlephys_pos += self.circlephys_vel



    def draw(self, screen):
        #Draw bouncing circle
        circle(screen, self.circle_color, (int(self.circle_pos.x), int(self.circle_pos.y)), self.circle_radius)

        #Draw physics-following circle
        circle(screen, (100,100,0), (int(self.circlephys_pos.x), int(self.circlephys_pos.y)), self.EYESIGHT,width=1)
        circle(screen, self.circlephys_color, (int(self.circlephys_pos.x), int(self.circlephys_pos.y)), self.circlephys_radius)


