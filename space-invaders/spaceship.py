import pygame
from laser import Laser

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, position, offset):
        super().__init__()
        self.position = position
        self.offset = offset
        self.image = pygame.image.load('space-invaders/Graphics/spaceship.png')
        self.rect = self.image.get_rect(midbottom = self.position)
        self.speed = 5
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = 500
        self.laser_group = pygame.sprite.Group()
        self.laser_sound = pygame.mixer.Sound('space-invaders/Sounds/laser.ogg')
        
    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and self.rect.x > self.offset:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < 750 - self.rect.width:
            self.rect.x += self.speed
        if keys[pygame.K_SPACE] and self.laser_ready():
            laser = Laser((self.rect.centerx, self.rect.centery), 6)
            self.laser_group.add(laser)
            self.laser_sound.play()

    def update(self):
        self.get_input()
        self.laser_group.update()
    
    def laser_ready(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot > self.shoot_delay:
            self.last_shot = current_time
            return True
        return False
    
    def reset(self):
        self.rect = self.image.get_rect(midbottom = self.position)
        self.laser_group.empty()