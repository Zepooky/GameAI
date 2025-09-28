
from pygame.math import Vector2
from pygame.draw import circle, line, rect

class Agent:
    def __init__(self, position, radius, color):
        self.circle_color = color
        self.radius = radius
        self.position = position
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)
        self.mass = 1.0
        self.EYE_SIGHT = 300
        self.STOP_DIST = 5
        self.target = Vector2(0,0)
        self.active = False

    def reset(self, position):
        self.position = position
        self.vel = Vector2(0,0)
        self.acc = Vector2(0,0)
        self.active = False

        
    def seek_to(self, target_pos):
        self.target = target_pos

        MAX_FORCE = 2
        d = target_pos - self.position
        if d.length_squared() == 0:
            return
        
        desired = d.normalize() * MAX_FORCE
        steering = desired - self.vel
        
        if steering.length() > MAX_FORCE:
            steering.scale_to_length(MAX_FORCE)

        self.apply_force(steering)

    def arrive_to(self, target_pos):
        MAX_FORCE = 5
        d = target_pos - self.position
        if d.length_squared() == 0:
            return
        
        desired = d.normalize() * MAX_FORCE
        steering = desired - self.vel
        
        if steering.length() > MAX_FORCE:
            steering.scale_to_length(MAX_FORCE)
 
        self.apply_force(steering)
    
    def home_to_target(self):
        MAX_FORCE = 1.0
        to_target = self.target - self.position
        distance = to_target.length()

        if distance == 0:
            return


        desired_direction = to_target.normalize()

        MAX_SPEED = 5
        self.vel = self.vel.normalize() * MAX_SPEED if self.vel.length() > 0 else desired_direction * MAX_SPEED

        turn_strength = 0.15  
        self.vel = self.vel.lerp(desired_direction * MAX_SPEED, turn_strength)

    def flee_from(self, target_pos):
        MAX_FORCE = 7
        d = (target_pos - self.position)
        if d.length_squared() == 0:
            return
        
        dist = d.length()
        if dist > self.EYE_SIGHT:
            desired = Vector2(0, 0)
        else:
            desired = (-d).normalize() * (MAX_FORCE * ((self.EYE_SIGHT - dist)/self.EYE_SIGHT))
        
        steering = desired - self.vel
         
        if steering.length() > MAX_FORCE:
            steering.scale_to_length(MAX_FORCE)
        self.apply_force(steering)     

    def apply_force(self, force):
        self.acc += force / self.mass

    def update(self, delta_time_ms):
        self.vel = self.vel + self.acc
        self.position = self.position + self.vel
        self.acc = Vector2(0,0)

    def draw(self, screen):

        circle(screen, self.circle_color, self.position, self.radius)
        line(screen, (100,100,100),self.position,self.target,1)