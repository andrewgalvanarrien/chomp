import pygame
import time
import sys

# Dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SAND_HEIGHT = 20
TILE_SIZE = 64  #   tiles are squares

# Colors
WATER_COLOR = (114,159,255)
SAND_COLOR = (100,25,0)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chomp!")
screen.fill(WATER_COLOR)
pygame.draw.rect(screen, SAND_COLOR, (0, SCREEN_HEIGHT-SAND_HEIGHT, SCREEN_WIDTH, SAND_HEIGHT))
sand = pygame.image.load("assets/images/sand.png").convert()
screen.blit(sand, (SCREEN_WIDTH/2 - TILE_SIZE/2, SCREEN_HEIGHT/2 - TILE_SIZE/2, TILE_SIZE, TILE_SIZE))


while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("Thanks for playing")
            pygame.quit()
            sys.exit()

        pygame.display.flip()
