from mazegenerator import MazeGenerator
import pygame
from os.path import join
from random import randint

def test():
    pygame.init()
    WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 700
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
    running = True

    # plain surface
    block = pygame.Surface((200, 200))
    block.fill("yellow")
    
    # importes
    paku = pygame.image.load(join("assets", "2d-paku.png")).convert_alpha()
    paku_rect = paku.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
    paku_direction = pygame.Vector2(1, 1)
    movement_speed = 500

    heart = pygame.image.load(join("assets", "hardcoreheart.png")).convert_alpha()
    heart_rect = heart.get_frect(bottomright = (WINDOW_WIDTH - 20, WINDOW_HEIGHT/2))

    stars = pygame.image.load(join('assets', 'stars.png')).convert_alpha()
    star_pos = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]
    
    clock = pygame.time.Clock()

    while running:
        dt = clock.tick() / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        screen.fill("darkgray")
        for pos in star_pos:
            screen.blit(stars, pos)

        paku_rect.center += paku_direction * movement_speed * dt

        if paku_rect.top < -0 or paku_rect.bottom > WINDOW_HEIGHT:
            paku_direction.y *= -1

        if paku_rect.left < -0 or paku_rect.right > WINDOW_WIDTH:
            paku_direction.x *= -1

        screen.blit(paku, paku_rect)
        screen.blit(heart, heart_rect)

        pygame.display.set_caption("paku paku")    
        pygame.display.update()
            
    pygame.quit()