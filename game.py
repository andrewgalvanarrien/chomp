import pygame
import time
import sys

print(f" the quit event is type {pygame.QUIT}")
pygame.init()


screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Chomp!")
screen.fill((114,159,255))
pygame.draw.rect(screen, (100,25,0), (0, 380, 400, 400))
pygame.draw.rect(screen, (0,255,0), (200,200, 50,50))
pygame.display.flip()

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("Thanks for playing")
            pygame.quit()
            sys.exit()
