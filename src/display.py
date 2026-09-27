from mazegenerator import MazeGenerator
import pygame
from os.path import join
from models import Player, PacGum, Direction
from os import system


def test():
    system("clear")
    pygame.init()
    WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 700
    screen = pygame.display.set_mode((WINDOW_WIDTH,
                                      WINDOW_HEIGHT),
                                     pygame.RESIZABLE)
    running = True

    all_sprites = pygame.sprite.Group()
    pacgum_sprites = pygame.sprite.Group()
    paku = Player(all_sprites, WINDOW_WIDTH, WINDOW_HEIGHT)
    gum = pygame.Surface((5, 5))
    gum.fill("yellow")
    for _ in range(20):
        PacGum((all_sprites, pacgum_sprites), gum)

    num_pacgums = 20

    clock = pygame.time.Clock()
    # Main Loop
    while running:
        dt = clock.tick() / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        all_sprites.update(dt)
        if pygame.sprite.spritecollide(paku, pacgum_sprites, True):
            num_pacgums -= 1
        if num_pacgums == 0:
            paku.state = "ded"
            paku.direction = Direction.NONE

        screen.fill("navyblue")
        all_sprites.draw(screen)

        pygame.display.set_caption("paku paku")
        pygame.display.update()

    pygame.quit()
