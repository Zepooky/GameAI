import pygame
from pygame.draw import circle, rect
from pygame.math import Vector2
from agent import Agent

window_width, window_height = 1280, 720

class App:
    def __init__(self):
        print("Application is created")
        pygame.init()
        self.screen = pygame.display.set_mode((window_width, window_height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.ball = Agent(Vector2(window_width/2, window_height/2),radius=80,color=(255, 0, 0))
        #Pending ph




    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self,dt):
        mouse_pos = Vector2(pygame.mouse.get_pos())
        self.ball.seek_to(mouse_pos)
        self.ball.update(dt)

        


    def draw(self):
        pygame.display.flip()
        self.screen.fill("black")
        self.ball.draw(self.screen)
        

    def run(self):
        while self.running:
            events = pygame.event.get()  # Get events ONCE per frame

            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False

            dt = self.clock.tick(60)
            self.update(dt)
            self.draw()


        pygame.quit()

def main():
    app = App()
    app.run()

if __name__ == "__main__":
    main()
    