import pygame
import sys
import random
from game import Game

pygame.init()

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700
OFFSET = 50

FONT = pygame.font.Font('space-invaders/Font/monogram.ttf', 42)
game_over_text = FONT.render("GAME OVER", False, (243, 216, 63))

#*Screen
screen = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2*OFFSET))
pygame.display.set_caption('Space Invaders')

clock = pygame.time.Clock()

pygame.mixer.music.load('space-invaders/Sounds/music.ogg')
pygame.mixer.music.play(-1)

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, screen, OFFSET)

MYSTERYSHIP = pygame.USEREVENT
pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == MYSTERYSHIP:
            game.create_mystery_ship()
            pygame.time .set_timer(MYSTERYSHIP, random.randint(4000, 8000))      
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game.run:
                game.reset()

    
    #*Update Groups
    if game.run:
        game.spaceship_group.update()
        game.move_aliens()
        game.alien_shot()
        game.alien_lasers_group.update()
        game.mystery_ship_group.update()
        game.check_for_collisions()
            
    screen.fill((20, 20, 20))
    
    if not game.run:
        screen.blit(game_over_text, (600, 740))
    
    #*Draw Groups
    pygame.draw.rect(screen, (243, 216, 63), (10, 10, 780, 780), 2, 0, 60, 60, 60, 60)
    pygame.draw.line(screen, (243, 216, 63), (25, 730), (775, 730), 3)
    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.laser_group.draw(screen)
    for obstacle in game.obstacles:
        obstacle.blocks_group.draw(screen)
    game.aliens_group.draw(screen)
    game.alien_lasers_group.draw(screen)
    game.mystery_ship_group.draw(screen)
    game.show_scoreboard()
    game.show_lives()   
    
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
sys.exit()