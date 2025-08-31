import pygame
from pygame.draw import circle, rect
from pygame.math import Vector2
from agent import Agent

#Setup
pygame.init()
window_width, window_height = 1280, 720
screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
running = True


#Shape setup
#Circle
circle_pos = Vector2(300, 200)
circle_vel = Vector2(4, 3)
circle_radius = 60
circle_color = (255, 0, 0)

#CirclePhys
circlephys_pos = pygame.math.Vector2(400, 300)
circlephys_vel = pygame.math.Vector2(0, 0)
circlephys_radius = 60
circlephys_color = (0, 255, 255)
circlephys_acc = 0.6 #Mouse Acceleration
circlephys_damp = 0.92 #Momentum

#Rectangle
rect_pos = Vector2(600, 400)
rect_vel = Vector2(-3, 4)
rect_size = (120, 80)
rect_color = (0, 255, 0)

#Triangle
triangle_pos = Vector2(900, 300)
triangle_vel = Vector2(3, -4)
triangle_size = 100
triangle_color = (0, 0, 255)

def draw_triangle(surface, pos, size, color):
    points = [
        (pos.x, pos.y - size/2),
        (pos.x - size/2, pos.y + size/2),
        (pos.x + size/2, pos.y + size/2)
    ]
    pygame.draw.polygon(surface, color, points)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            #Close on ESC
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()

    #Get mouse position
    mouse_pos = pygame.math.Vector2(pygame.mouse.get_pos())
    #circle Mouse Physics
    direction = mouse_pos - circlephys_pos
    circlephys_vel += direction * circlephys_acc * 0.01  #Accl towards mouse
    circlephys_vel *= circlephys_damp #Momentum Damping
    circlephys_pos += circlephys_vel #Update Position

    screen.fill("black")

    #Circle following Cursor
    circle(screen, circlephys_color, (int(circlephys_pos.x), int(circlephys_pos.y)), circlephys_radius)

    #Circle movement
    circle_pos += circle_vel
#Horizontal
    if circle_pos.x - circle_radius <= 0 or circle_pos.x + circle_radius >= window_width:
        circle_vel.x *= -1
        c = pygame.Color(0)  # create Color object
        c.hsva = (pygame.time.get_ticks() % 360, 100, 100, 100)
        circle_color = c

#Vertical
    if circle_pos.y - circle_radius <= 0 or circle_pos.y + circle_radius >= window_height:
        circle_vel.y *= -1
        c = pygame.Color(0)
        c.hsva = (pygame.time.get_ticks() % 360, 100, 100, 100)
        circle_color = c
    circle(screen, circle_color, (int(circle_pos.x), int(circle_pos.y)), circle_radius)

    #Rectangle
    rect_pos += rect_vel
    #Horizontal
    if rect_pos.x <= 0 or rect_pos.x + rect_size[0] >= window_width:
        rect_vel.x *= -1
    #Vertical
    if rect_pos.y <= 0 or rect_pos.y + rect_size[1] >= window_height:
        rect_vel.y *= -1
    rect_rect = pygame.Rect(rect_pos.x, rect_pos.y, rect_size[0], rect_size[1])
    rect(screen, rect_color, rect_rect)

    #Triangle movement
    triangle_pos += triangle_vel
    #Horizontal
    if triangle_pos.x - triangle_size/2 <= 0 or triangle_pos.x + triangle_size/2 >= window_width:
        triangle_vel.x *= -1
    #Vertical
    if triangle_pos.y - triangle_size/2 <= 0 or triangle_pos.y + triangle_size/2 >= window_height:
        triangle_vel.y *= -1
    draw_triangle(screen, triangle_pos, triangle_size, triangle_color)

    pygame.display.flip()
    clock.tick(60)