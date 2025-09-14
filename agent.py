
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
        self.EYE_SIGHT = 100
        self.STOP_DIST = 5
        self.waypoints = [Vector2(100, 100),Vector2(400, 100),Vector2(400, 400),Vector2(100, 400)]
        self.current_waypoint = 0     # Start index for waypoint tracking
        self.waypoint_radius = 10
    
    def set_waypoints(self, waypoint_list):
        self.waypoints = waypoint_list
        self.current_waypoint = 0
    
    def follow_waypoints(self):
        if not self.waypoints:
            return
        target = self.waypoints[self.current_waypoint]
        dist = (target - self.position).length()

        if dist < self.waypoint_radius:
        # Move to the next waypoint
            self.current_waypoint += 1
            if self.current_waypoint >= len(self.waypoints):
                self.current_waypoint = 0  # Loop back to start (optional)
        self.arrive_to(target)

        
    def seek_to(self, target_pos):
        MAX_FORCE = 5
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

    def flee_from(self, target_pos):
        MAX_FORCE = 5
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
        circle(screen, "Yellow", self.position, self.EYE_SIGHT, width = 1)
        circle(screen, self.circle_color, self.position, self.radius)
        circle(screen, "Green", self.position, self.STOP_DIST, width = 1)
