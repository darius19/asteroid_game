import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255),
                           self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)
        new_radius_for_smaller_asteroids = self.radius - ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(
            self.position.x, self.position.y, new_radius_for_smaller_asteroids)
        first_asteroid.velocity = vector1 * 1.2
        second_asteroid = Asteroid(
            self.position.x, self.position.y, new_radius_for_smaller_asteroids)
        second_asteroid.velocity = vector1 * 1.2
