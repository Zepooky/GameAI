import pygame
from pygame.math import Vector2
from pygame.draw import circle, line, rect
from agent import Agent

class Ant(Agent):
    def __init__(self, position, radius, color, home, food, delay=0):
        super().__init__(position, radius, color)
        self.ant = pygame.image.load("images/ant.png")
        self.home = home
        self.food = food
        self.state = "waiting"  # start in waiting state
        self.delay = delay      # delay in milliseconds
        self.elapsed = 0        # counter for how long ant has been waiting


    def forage(self, dt):
        # If waiting, count elapsed time
        if self.state == "waiting":
            self.elapsed += dt
            if self.elapsed >= self.delay:
                self.state = "to_food"
            else:
                return  # still waiting, don't move

        # Normal foraging behavior
        if self.state == "to_food":
            self.arrive_to(self.food)
            if (self.food - self.position).length() < self.waypoint_radius:
                self.state = "to_home"

        elif self.state == "to_home":
            self.arrive_to(self.home)
            if (self.home - self.position).length() < self.waypoint_radius:
                self.state = "to_food"


    def draw(self, screen):
        ant_img = pygame.transform.scale(self.ant, (50, 50))
        rect = ant_img.get_rect(center=(self.position.x, self.position.y))
        screen.blit(ant_img, rect)

        
        
    