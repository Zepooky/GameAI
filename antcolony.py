
#lab2
import pygame
from pygame.draw import circle, line, rect
from pygame.math import Vector2

from ants import Ant

window_width = 1280
window_height = 720

class App:
    def __init__(self):
        print("Application is created.")
        pygame.init()
        self.screen = pygame.display.set_mode((window_width, window_height))
        self.clock = pygame.time.Clock()
        self.CHANGE_DIR = pygame.USEREVENT +1
        pygame.time.set_timer(self.CHANGE_DIR, 2000)
        self.running = True
        self.burger_img = pygame.image.load("images/food.png")
        self.home_img = pygame.image.load("images/home.png")
        self.home = Vector2(100, 500)   
        self.food = Vector2(1000, 200)             

        self.ants = [
            Ant(position=self.home, radius=30, color=(200,0,0), home=self.home, food=self.food, delay=0),
            Ant(position=self.home, radius=20, color=(0,200,0), home=self.home, food=self.food, delay=1000),  
            Ant(position=self.home, radius=10, color=(0,0,200), home=self.home, food=self.food, delay=2000),  
]


        
        self.target = Vector2(0, 0)
        self.waypoints = [Vector2(100, 100),Vector2(400, 100),Vector2(400, 400),Vector2(100, 400)]  
        self.current_waypoint = 0
        self.waypoint_radius = 10  

        
        for ant in self.ants:
            ant.set_waypoints(self.waypoints)
        



    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False



    def update(self, delta_time_ms):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        predator = Vector2(mouse_x, mouse_y)

        for ant in self.ants:
            ant.flee_from(predator)
            ant.forage(delta_time_ms) 
            ant.update(delta_time_ms)

    def draw(self):
        self.screen.fill("gray")

        home_img = pygame.transform.scale(self.home_img, (80, 80))
        self.screen.blit(home_img, (self.home.x - 15, self.home.y - 15))

        
        burger_img = pygame.transform.scale(self.burger_img, (80, 80))
        self.screen.blit(burger_img, (self.food.x - 15, self.food.y - 15))

        for ant in self.ants:
            ant.draw(self.screen)  

        pygame.display.flip()


    

    def run(self):
        while self.running:
            dt = self.clock.tick(60)
            self.handle_input()
            self.update(dt)
            self.draw()
            

        pygame.quit()


def main():
    app = App()
    app.run()

if __name__ == "__main__":
    main()
