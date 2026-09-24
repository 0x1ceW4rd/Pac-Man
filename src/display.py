from mazegenerator import MazeGenerator
import pygame
from os.path import join
from random import randint

def test():
    pygame.init()
    WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 700
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    running = True

    # plain surface
    block = pygame.Surface((200, 200))
    block.fill("yellow")
    
    # importes
    paku = pygame.image.load(join("assets", "2d-paku.png")).convert_alpha()
    paku_rect = paku.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
    paku_direction = 1

    heart = pygame.image.load(join("assets", "hardcoreheart.png")).convert_alpha()
    heart_rect = heart.get_frect(bottomright = (WINDOW_WIDTH - 20, WINDOW_HEIGHT - 20))

    stars = pygame.image.load(join('assets', 'stars.png')).convert_alpha()
    star_pos = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]
    

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        screen.fill("darkgray")
        for pos in star_pos:
            screen.blit(stars, pos)

        paku_rect.left += paku_direction * 0.4
        if paku_rect.right > WINDOW_WIDTH or paku_rect.left < 0:
            paku_direction *= -1

        print(paku_rect.left)
        screen.blit(paku, paku_rect)
        screen.blit(heart, heart_rect)

        pygame.display.set_caption("paku paku")    
        pygame.display.update()
            
    pygame.quit()