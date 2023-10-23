import pygame
from settings import *

class Fish(pygame.sprite.Sprite):

    def __init__(self, x=200, y=200):

        self.right_image = pygame.image.load("assets/images/orange_fish.png").convert()
        self.right_image.set_colorkey((0, 0, 0))
        self.left_image = pygame.transform.flip(self.right_image, True, False)
        self.left_image.set_colorkey((0, 0, 0))
        self.image = self.right_image
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_left:
            self.rect.x -= 1
            self.image = self.left_image
        elif self.moving_right:
            self.rect.x += 1
            self.image = self.right_image
        elif self.moving_up:
            self.rect.y -= 1
        elif self.moving_down:
            self.rect.y += 1
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.bottom > SCREEN_HEIGHT - 2 * TILE_SIZE:
            self.rect.bottom = SCREEN_HEIGHT - 2 * TILE_SIZE