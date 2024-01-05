import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
PADDLE_SPEED = 10
BALL_RADIUS = 10
BALL_SPEED = 5
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
FPS = 60
BLOCK_WIDTH = 70
BLOCK_HEIGHT = 20
BLOCK_ROWS = 5
BLOCK_COLS = 10
BLOCK_PADDING = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")

paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - PADDLE_HEIGHT - 20, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed_x = 0
ball_speed_y = 0
ball_moving = False

block_width_total = BLOCK_COLS * BLOCK_WIDTH + (BLOCK_COLS - 1) * BLOCK_PADDING
block_start_x = (WIDTH - block_width_total) // 2

blocks = []
for row in range(BLOCK_ROWS):
    for col in range(BLOCK_COLS):
        block = pygame.Rect(
            block_start_x + col * (BLOCK_WIDTH + BLOCK_PADDING),
            row * (BLOCK_HEIGHT + BLOCK_PADDING) + 50,
            BLOCK_WIDTH,
            BLOCK_HEIGHT,
        )
        blocks.append(block)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT) and not ball_moving:
                ball_speed_x = BALL_SPEED
                ball_speed_y = BALL_SPEED
                ball_moving = True
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= PADDLE_SPEED
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.right += PADDLE_SPEED
        
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    if ball.left <=0 or ball.right >= WIDTH:
        ball_speed_x = -ball_speed_x
    if ball.top <= 0:
        ball_speed_y = -ball_speed_y
        
    if ball.colliderect(paddle) and ball_speed_y > 0:
        ball_speed_y = -ball_speed_y
        
    for block in blocks:
        if ball.colliderect(block):
            blocks.remove(block)
            ball_speed_y = -ball_speed_y
            
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.circle(screen, WHITE, ball.center, BALL_RADIUS)
    for block in blocks:
        pygame.draw.rect(screen, RED, block)
    
    if len(blocks) == 0:
        font = pygame.font.Font(None, 36)
        text = font.render("You Won!", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
        
    if ball.bottom >= HEIGHT:
        font = pygame.font.Font(None, 36)
        text = font.render("You Lost!", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
    
    pygame.display.flip()
    pygame.time.Clock().tick(FPS)
    
pygame.quit()
sys.exit()