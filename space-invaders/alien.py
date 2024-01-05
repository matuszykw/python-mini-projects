import pygame
import random

class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        super().__init__()
        self.type = type
        self.image = pygame.image.load(f"space-invaders/Graphics/alien_{type}.png")
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 1

    def update(self, speed):
        self.rect.x += speed


class MysteryShip(pygame.sprite.Sprite):
    def __init__(self, screen_width):
        super().__init__()
        self.screen_width = screen_width
        self.image = pygame.image.load("space-invaders/Graphics/mystery.png")
        x=random.choice([0, self.screen_width - self.image.get_width()])
        self.rect = self.image.get_rect(topleft=(x, 90))
        if x == 0:
            self.speed = 3
        else:
            self.speed = -3
        
    def update(self):
        self.rect.x += self.speed
        if self.rect.right > self.screen_width:
            self.kill()
        elif self.rect.left < 0:
            self.kill()