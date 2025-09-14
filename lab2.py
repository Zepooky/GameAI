
#lab2
import pygame
from pygame.draw import circle, line, rect
from pygame.math import Vector2

from agent import Agent

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

        self.ball = Agent(position = Vector2(window_width/2, window_height/2), 
                          radius = 30,  
                          color = (100,0,0))
        
        self.agents = [
            Agent(position = Vector2(window_width/2, window_height/2), 
                          radius = 30, 
                          color = (200,0,0)),
            Agent(position = Vector2(window_width/2, window_height/2), 
                          radius = 20, 
                          color = (0,20,0)),
            Agent(position = Vector2(window_width/2, window_height/2), 
                          radius = 10, 
                          color = (100,0,0))
        ]
        
        self.target = Vector2(0, 0)
        self.waypoints = [Vector2(100, 100),Vector2(400, 100),Vector2(400, 400),Vector2(100, 400)]  # list of Vector2
        self.current_waypoint = 0
        self.waypoint_radius = 10  # how close to get before switching
        self.ball.set_waypoints(self.waypoints)
        
        for agent in self.agents:
            agent.set_waypoints(self.waypoints)
        



    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        #mouse_x, mouse_y = pygame.mouse.get_pos()
        #self.target = Vector2(mouse_x, mouse_y)


    def update(self, delta_time_ms):
        #self.ball.flee_from(self.target)   # Apply a fleeing force based on mouse position
        #self.ball.seek_to(self.target)
        
        for agent in self.agents:
            agent.follow_waypoints()
            agent.update(delta_time_ms)

        
    def draw(self):
        self.screen.fill("gray")
        for agent in self.agents:
            agent.draw(self.screen)
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
