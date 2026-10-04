import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self,screen,LINE_WIDTH):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self,dt):
        self.position += self.velocity*dt

    def split(self)
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS
            return
        else:
            log_event("asteroid_split)
            angle = random.uniform(20,50)
            velocity1 = self.velocity.rotate(angle)
            velocity2 = self.velocity.rotate(-angle)
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            new1 = Asteroid(self.position[0],self.position[1],new_rad)
            new2 = Asteroid(self.position[0],self.position[1],new_rad)
            new1.velocity = velocity1 * 1.2
            new2.velocity = velocity2 * 1.2

