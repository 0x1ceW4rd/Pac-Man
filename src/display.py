from mazegenerator import MazeGenerator
import pygame, sys
from mlx import Mlx
import mlx
from os.path import join
from models import Player, PacGum, Direction
from os import system
import os


class Display:
    def __init__(self):
        pass


    def handle_keypress(self, keycode, param):
        # ESC key code (Linux/Mac)
        if keycode in (53, 65307):
            print("Exiting application...")
            os._exit(0)  # Use os._exit to bypass the ctypes callback exception
        return 0


    def new_test(self):
        # 1. Initialize MLX connection directly from the module namespace
        mlx_ptr = Mlx().mlx_init()
        if not mlx_ptr:
            print("Failed to initialize MLX display backend.")
            return

        # 2. Create the window (Passing mlx_ptr as the first argument)
        win_ptr = Mlx().mlx_new_window(mlx_ptr, 800, 600, "42 Python Window")
        if not win_ptr:
            print("Failed to create MLX window.")
            return

        # 3. Setup window event hooks using the module functions
        Mlx().mlx_key_hook(win_ptr, self.handle_keypress, None)
        image = Mlx().mlx_png_file_to_image(
            mlx_ptr, "/home/aezzirar/Documents/Pac-Man/assets/paku-paku-states/right/1.png"
        )
        img_ptr = Mlx().mlx_new_image(mlx_ptr, 100, 100)
        Mlx().mlx_put_image_to_window(mlx_ptr, win_ptr, img_ptr, 100, 100)

        # 4. Start the graphic execution loop
        Mlx().mlx_loop(mlx_ptr)

    def start(self):
        system("clear")
        pygame.init()
        WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
        screen = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE
        )
        running = True

        all_sprites = pygame.sprite.Group()
        pacgum_sprites = pygame.sprite.Group()
        paku = Player(all_sprites, WINDOW_WIDTH, WINDOW_HEIGHT)
        gum = pygame.Surface((5, 5))
        gum.fill("yellow")
        for _ in range(10):
            PacGum((all_sprites, pacgum_sprites), gum)

        num_pacgums = 10
        is_ded = False
        clock = pygame.time.Clock()

        def collisions(num_pacgums):
            is_ded = False
            if pygame.sprite.spritecollide(paku, pacgum_sprites, True):
                num_pacgums -= 1
            if num_pacgums <= 0:
                is_ded = True
                paku.state = "ded"
                paku.direction = Direction.NONE
            return is_ded, num_pacgums

        # Main Loop
        while running:
            dt = clock.tick() / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

            screen.fill("navyblue")
            all_sprites.update(dt, is_ded, screen.get_width(), screen.get_height())
            is_ded, num_pacgums = collisions(num_pacgums)
            all_sprites.draw(screen)

            pygame.display.set_caption("Paku-Paku Man")
            pygame.display.update()

        pygame.quit()
