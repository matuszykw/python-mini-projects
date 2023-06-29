import math
import random
import time
import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
BG_COLOR = (20, 20, 20)
FPS = 60

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")


class Target():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 30
        
    def draw(self, win):
        pygame.draw.circle(win, (255, 0, 0), (self.x, self.y), self.size)
        pygame.draw.circle(win, (255, 255, 255), (self.x, self.y), self.size * 0.8)
        pygame.draw.circle(win, (255, 0, 0), (self.x, self.y), self.size * 0.6)
        pygame.draw.circle(win, (255, 255, 255), (self.x, self.y), self.size * 0.4)    

    def collide(self, x, y):
        distance = math.sqrt((self.x - x)**2 + (self.y - y)**2)
        return distance <= self.size

def draw_window(targets):
    win.fill(BG_COLOR)
    for target in targets:
        target.draw(win)
    pygame.display.update()
    

def create_targets(targets, targets_remaining):
    if len(targets) == 0:
        if targets_remaining == 30:
            x = 385
            y = 285
        else:
            x = random.randint(30, 770)
            y = random.randint(30, 570)
        new_target = Target(x, y)
        targets.append(new_target)
    return targets


def end_screen(win, time):
    win.fill(BG_COLOR)
    font = pygame.font.SysFont('Arial', 30)
    time_label = font.render(
        f"Average time per target {int(time/30)}ms", 1, 'white')
    win.blit(time_label, (200, 280))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                quit()

    
def main():
    running = True
    clock = pygame.time.Clock()
    click = False
    targets_remaining = 30
    targets = []
    
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                click = True
            
        targets = create_targets(targets, targets_remaining)
        
        for target in targets:
            if click and target.collide(*pos):
                click = False
                targets.remove(target)
                targets_remaining -= 1
        
        if targets_remaining == 30:
            start_time = pygame.time.get_ticks()
        elif targets_remaining == 0:
            end_time = pygame.time.get_ticks()
            time = end_time - start_time
            end_screen(win, time)
            
        
        draw_window(targets)
                
    pygame.quit()
                
if __name__ == '__main__':
    main()
                