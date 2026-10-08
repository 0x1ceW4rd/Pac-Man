from enum import Enum
from os.path import join
from os import walk
import pygame
from random import randint


class CellType(Enum):
    WALL = "wall"
    PACGUM = "pacgum"
    SUPER_PACGUM = "super_pacgum"
    EMPTY = "empty"


class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    NONE = (0, 0)


class Player(pygame.sprite.Sprite):
    def __init__(
        self,
        groups: pygame.sprite.Group,
        window_width: int,
        window_height: int,
    ) -> None:
        super().__init__(groups)
        self.load_frames()
        image_path: str = join("assets", "paku-paku-states", "right", "1.png")
        self.state, self.frame_index = "right", 0
        self.image: pygame.Surface = pygame.image.load(image_path).convert_alpha()
        self.rect: pygame.FRect = self.image.get_frect(
            center=(window_width / 2, window_height / 2)
        )
        self.direction: Direction = Direction.NONE
        self.speed: float = 150.0

    def load_frames(self):
        self.frames = {"ded": [], "down": [], "left": [], "right": [], "up": []}
        for state in self.frames.keys():
            for folder_path, sub_folders, file_names in walk(
                join("assets", "paku-paku-states", state)
            ):
                if file_names:
                    for file_name in sorted(
                        file_names, key=lambda name: int(name.split(".")[0])
                    ):
                        full_path = join(folder_path, file_name)
                        surf = pygame.image.load(full_path).convert_alpha()
                        self.frames[state].append(surf)

    def animate(self, dt):
        dx, dy = self.direction.value
        if dx != 0:
            self.state = "right" if dx > 0 else "left"
        if dy != 0:
            self.state = "down" if dy > 0 else "up"

        self.frame_index = (
            self.frame_index + 10 * dt if self.direction != Direction.NONE else 1
        )
        self.image = self.frames[self.state][
            int(self.frame_index) % len(self.frames[self.state])
        ]

    def ded_animate(self, dt):
        if self.state == "ded":
            self.frame_index = self.frame_index + 5 * dt
            self.image = self.frames[self.state][
                int(self.frame_index) % len(self.frames[self.state])
            ]

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction = Direction.RIGHT
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction = Direction.LEFT
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction = Direction.UP
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction = Direction.DOWN

    def mouvement(self, dt, window_width: int, window_height: int):

        dx, dy = self.direction.value
        self.rect.centerx += dx * self.speed * dt
        self.rect.centery += dy * self.speed * dt

        if self.rect.right >= window_width:
            self.rect.right = window_width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom >= window_height:
            self.rect.bottom = window_height
        if self.rect.top < 0:
            self.rect.top = 0

    def update(
        self, dt: float, ded: bool, window_width: int, window_height: int
    ) -> None:
        self.input()
        if not ded:
            self.mouvement(dt, window_width, window_height)
            self.animate(dt)
        else:
            self.ded_animate(dt)


class PacGum(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)

        self.image = surf
        self.rect = self.image.get_frect(center=(randint(80, 1200), randint(20, 700)))


class Ghost(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
