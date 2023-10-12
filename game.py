import pygame
import time

print(f" the quit event is type {pygame.QUIT}")
pygame.init()


screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Chomp!")
screen.fill((0,0,255))
pygame.draw.rect(screen, (100,25,0), (0, 380, 400, 400))
pygame.draw
pygame.display.flip()

while True:
    for event in pygame.event.get():
        print(event.type)
        if event.type == pygame.QUIT:
            print("Not today! You will play forever!!!")
