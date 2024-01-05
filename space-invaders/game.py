import pygame
from spaceship import Spaceship
from alien import Alien, MysteryShip
from obstacle import Obstacle, grid
from laser import Laser
import random, sys

class Game:
    def __init__(self, width, height, screen, offset):
        self.screen_width = width
        self.screen_height = height
        self.screen = screen
        self.offset = offset
        self.spaceship_group = pygame.sprite.GroupSingle()
        self.spaceship_group.add(Spaceship((self.screen_width/2, self.screen_height), self.offset))
        self.aliens_group = pygame.sprite.Group()
        self.alien_lasers_group = pygame.sprite.Group()
        self.mystery_ship_group = pygame.sprite.GroupSingle()
        self.alien_speed = 1
        self.obstacles = self.create_obstacles()
        self.create_aliens()
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = random.randint(1000, 4000)
        self.lives = 3
        self.run = True
        self.score = 0
        self.load_highscore()
        self.explosion_sound = pygame.mixer.Sound('space-invaders/Sounds/explosion.ogg')


    def create_obstacles(self):
        obstacle_width = len(grid[0]) * 3
        gap = (self.screen_width + self.offset - (4 * obstacle_width)) / 5
        obstacles = []
        for i in range(4):
            offset_x = (i + 1) * gap + i * obstacle_width
            obstacle = Obstacle(offset_x, self.screen_height - 100)
            obstacles.append(obstacle)
        return obstacles
    
    def create_aliens(self):
        for row in range(5):
            for col in range(11):
                x = 75 + col * 55
                y = 130 + row * 55
                if row == 0:
                    alien_type = 3
                elif row in (1, 2):
                    alien_type = 2
                else:
                    alien_type = 1
                alien = Alien(x, y, alien_type)
                self.aliens_group.add(alien)
                
    def move_aliens(self):
        self.aliens_group.update(self.alien_speed)
        aliens_sprites = self.aliens_group.sprites()
        for alien in aliens_sprites:
            if alien.rect.right == self.screen_width or alien.rect.left == self.offset:
                self.alien_speed *= -1
                for alien in aliens_sprites:
                    alien.rect.y += 0.5
                break
    
    def alien_shot(self):
        if self.alien_laser_ready():
            random_alien = random.choice(self.aliens_group.sprites())
            laser_sprite = Laser((random_alien.rect.centerx, random_alien.rect.centery), -6)
            self.alien_lasers_group.add(laser_sprite)
        
    def alien_laser_ready(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot > self.shoot_delay:
            self.last_shot = current_time
            return True
        return False
    
    def create_mystery_ship(self):
        if self.run:
            self.mystery_ship_group.add(MysteryShip(self.screen_width))
        
    def check_for_collisions(self):
        if self.spaceship_group.sprite.laser_group:
            for laser in self.spaceship_group.sprite.laser_group:
                aliens_hit = pygame.sprite.spritecollide(laser, self.aliens_group, True)
                if aliens_hit:
                    for alien in aliens_hit:
                        self.score += alien.type * 100
                        laser.kill()
                        self.explosion_sound.play()
                            
                if pygame.sprite.spritecollide(laser, self.mystery_ship_group, True):
                    laser.kill()
                    self.score += 500
                    self.explosion_sound.play()
                    
                for obstacle in self.obstacles:
                    if pygame.sprite.spritecollide(laser, obstacle.blocks_group, True):
                        laser.kill()
                        
                if pygame.sprite.spritecollide(laser, self.alien_lasers_group, True):
                    laser.kill()
        
        if self.alien_lasers_group:
            for laser in self.alien_lasers_group:
                if pygame.sprite.spritecollide(laser, self.spaceship_group, False):
                    laser.kill()
                    self.lives -= 1
                    if self.lives == 0:
                        self.game_over()
                
                for obstacle in self.obstacles:
                    if pygame.sprite.spritecollide(laser, obstacle.blocks_group, True):
                        laser.kill()
                        
        if self.aliens_group:
            for alien in self.aliens_group:
                for obstacle in self.obstacles:
                    pygame.sprite.spritecollide(alien, obstacle.blocks_group, True)
                if pygame.sprite.spritecollide(alien, self.spaceship_group, False):
                    self.game_over()
        
        if not self.aliens_group:
            self.game_over()
                
    def game_over(self):
        self.run = False
        self.save_highscore()
        
    def show_scoreboard(self):
        font = pygame.font.Font("space-invaders/Font/monogram.ttf", 42)
        score_text = font.render("SCORE", False, (243, 216, 63))
        formatted_score = str(self.score).zfill(5)
        score = font.render(formatted_score, False, (243, 216, 63))
        h_score_text = font.render("HIGH-SCORE", False, (243, 216, 63))
        formatted_h_score = str(self.highscore).zfill(5)
        h_score = font.render(formatted_h_score, False, (243, 216, 63))
        self.screen.blit(score_text, (self.offset, 20))
        self.screen.blit(score, (self.offset, 50))
        self.screen.blit(h_score_text, (self.screen_width-h_score_text.get_width(), 20))
        self.screen.blit(h_score, (self.screen_width-h_score.get_width(), 50))

    def show_lives(self):
        for life in range(self.lives):
            self.screen.blit(self.spaceship_group.sprite.image, (self.offset+(self.offset*life), self.screen_height + self.offset))

    def reset(self):
        self.run = True
        self.lives = 3
        self.score = 0
        self.spaceship_group.sprite.reset()
        self.aliens_group.empty()
        self.alien_lasers_group.empty()
        self.mystery_ship_group.empty()
        self.obstacles = []
        self.obstacles = self.create_obstacles()
        self.create_aliens()
        
    def save_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('space-invaders/highscore.txt', 'w') as f:
                f.write(str(self.highscore))
                
    def load_highscore(self):
        try:
            with open('space-invaders/highscore.txt', 'r') as f:
                self.highscore = int(f.read())
        except FileNotFoundError:
            self.highscore = 0