

#lab2
import pygame
from pygame.draw import circle, line, rect
from pygame.math import Vector2
from ammo import Agent
import random
import math


window_width = 1280
window_height = 720

class App:
    def __init__(self):
        print("Application is created.")
        pygame.init()
        self.timer = 0
        self.screen = pygame.display.set_mode((window_width,window_height))
        self.clock = pygame.time.Clock()
        self.running = True
        
        #Tankpos
        self.tank_pos = Vector2(window_width/2, window_height - 50)


        self.min_angle = 45  
        self.max_angle = 135  

        #Target of missile
        self.target = []
        self.missiles = []
        self.missile_pool = []

        for _ in range(10):   # 10 ready missiles
            missile = Agent(Vector2(self.tank_pos), radius=10, color=(255,0,0))
            self.missile_pool.append(missile)


        self.target = Vector2(0, 0)
        self.angle_deg = random.uniform(self.min_angle, self.max_angle)
        self.angle_rad = math.radians(self.angle_deg)

        self.direction = Vector2(math.cos(self.angle_rad), -math.sin(self.angle_rad))



    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for missile in self.missile_pool:
                    if not missile.active:
                        barrel_length = 100
                        barrel_end = self.tank_pos + self.direction * barrel_length
                        missile.position = barrel_end.copy()
                        missile.vel = self.direction * 5
                        missile.active = True
                        break  # only launch 1 missile per click


    def update(self, delta_time_s):
        mouse_pos = Vector2(pygame.mouse.get_pos())

        for missile in self.missile_pool:
            if missile.active:
                missile.target = mouse_pos
                missile.home_to_target()
                missile.update(delta_time_s)
                if (missile.position - mouse_pos).length() < 10:  # 10 px threshold
                    missile.reset(Vector2(self.tank_pos))  # back to pool

        self.timer += delta_time_s
        if self.timer > 1:
            self.angle_deg = random.uniform(self.min_angle, self.max_angle)
            self.angle_rad = math.radians(self.angle_deg)
            self.direction = Vector2(math.cos(self.angle_rad), -math.sin(self.angle_rad))
            self.timer = 0

        

        
    def draw(self):
        self.screen.fill("gray")
        
        for missile in self.missile_pool:
            if missile.active:
                missile.draw(self.screen)

        barrel_length = 100
        barrel_end = self.tank_pos + self.direction * barrel_length

        # Convert to integers for Pygame drawing
        tank_pos_int = (int(self.tank_pos.x), int(self.tank_pos.y))
        barrel_end_int = (int(barrel_end.x), int(barrel_end.y))

                # Draw the barrel
        line(self.screen, (255,0,0), tank_pos_int, barrel_end_int, 10)
        circle(self.screen, (100,100,100), tank_pos_int, 40)  # smaller radius so barrel is visible


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
