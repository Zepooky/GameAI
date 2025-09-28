
#lab2
import pygame
from pygame.draw import circle, line, rect
from pygame.math import Vector2
import pygame_gui
from agent import Agent
import random
import math

window_width = 1280
window_height = 720

class App:
    def __init__(self):
        print("Application is created.")
        pygame.init()
        
        self.timer = 0
        self.screen = pygame.display.set_mode((window_width, window_height))
        self.manager = pygame_gui.UIManager((window_width,window_height))
        self.hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350,275),(100,50)),
                                                    text='Say Hello',
                                                    manager=self.manager)
        self.clock = pygame.time.Clock()
        self.CHANGE_DIR = pygame.USEREVENT +1
        pygame.time.set_timer(self.CHANGE_DIR, 2000)
        self.running = True

        #self.ball = Agent(position = Vector2(window_width/2, window_height/2), 
         #                 radius = 30,  
          #                color = (100,0,0))
        
        self.agents = []

        #self.agents[0].set_gravity(Vector2(0,1))
        #self.agents[1].set_gravity(Vector2(0,1))
        #self.agents[2].set_gravity(Vector2(0,1))
        for i in range(50):
            agent = Agent(position = Vector2(random.randint(0,window_width), random.randint(0,window_height)), 
                          radius = 10, 
                          color = (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            agent.mass = 10
            self.agents.append(agent)

        self.target = Vector2(0, 0)
        self.current_waypoint = 0
        

        



    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if hasattr(event, 'ui_element'):
                    #if event.ui_element == self.hello_button:
                if self.hello_button.rect.collidepoint(event.pos):
                    print("Button pressed!")
            elif event.type == pygame.QUIT:
                self.running = False

           # elif event.type == pygame_gui.UI_BUTTON_PRESSED:
            #    if event.ui_element == self.hello_button:
             #       print("Hello World")
                    
            self.manager.process_events(event)

        #mouse_x, mouse_y = pygame.mouse.get_pos()
        #self.target = Vector2(mouse_x, mouse_y)

    def bound_check(self,agent):
        if agent.position.x < -10:
            agent.position.x = window_width + 30
        elif agent.position.x > window_width + 34:
            agent.position.x = -5 
        if agent.position.y < -10:
            agent.position.y = window_height + 30
        elif agent.position.y > window_height + 34:
            agent.position.y = -5 


    def update(self, delta_time_s):
        self.manager.update(delta_time_s)
        for i,agent in enumerate(self.agents):
            cohesion_f = agent.get_cohesion_force(self.agents)
            agent.apply_force(cohesion_f)
            separation_f = agent.get_separation_force(self.agents)
            agent.apply_force(separation_f)
            align_f = agent.get_align_force(self.agents)
            agent.apply_force(align_f)

            self.bound_check(agent)
            agent.update(delta_time_s)
            
            

        
    def draw(self):
        self.screen.fill("gray")
        for agent in self.agents:
            agent.draw(self.screen)

        self.manager.draw_ui(self.screen)
        pygame.display.flip()

    

    def run(self):
        while self.running:
            dt = self.clock.tick(60) /1000.0
            self.handle_input()
            self.update(dt)
            self.draw()


        pygame.quit()


def main():
    app = App()
    app.run()

if __name__ == "__main__":
    main()
