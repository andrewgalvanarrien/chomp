import pygame
class Minnow:
    def __init__(self, x, y):
        self.right_image = pygame.image.load("assets/images/minnow.png").convert()
        self.right_image.set_colorkey((0, 0, 0))
        self.left_image = pygame.transform.flip(self.right_image, True, False)
        self.left_image.set_colorkey((0, 0, 0))
        self.image = self.right_image
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def draw(self,screen):
        screen.blit(self.image, self.rect)
