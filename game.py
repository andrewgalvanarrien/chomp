import pygame
import sys
import fish
import random
from minnow import Minnow, minnows
from settings import *

pygame.init()

# score =
game_font = pygame.font.Font("assets/fonts/Black_Crayon.ttf", 128)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chomp!")
screen.fill(WATER_COLOR)
sand = pygame.image.load("assets/images/sand.png").convert()
sand_top = pygame.image.load("assets/images/sand_top.png").convert()
seagrass = pygame.image.load("assets/images/seagrass.png").convert()
star = pygame.image.load("assets/images/star.png").convert()
rock = pygame.image.load("assets/images/rock.png").convert()
sand_top.set_colorkey((0,0,0))
seagrass.set_colorkey((0,0,0))
star.set_colorkey((0,0,0))
rock.set_colorkey((0,0,0))

clock = pygame.time.Clock()

background = screen.copy()
my_fish = fish.Fish()  # create a new fish
for _ in range(NUM_MINNOWS):
    minnows.add(Minnow(random.randint(0, SCREEN_WIDTH- TILE_SIZE),
                          random.randint(0, WATER_BOTTOM-2*TILE_SIZE)))


def draw_background():

    background.fill(WATER_COLOR)
    # Blit sand tiles across the bottom of the screen
    for i in range(SCREEN_WIDTH // TILE_SIZE):
        background.blit(sand, (i * TILE_SIZE, SCREEN_HEIGHT-TILE_SIZE, TILE_SIZE, TILE_SIZE))
        background.blit(sand_top, (i * TILE_SIZE, SCREEN_HEIGHT - (2 * TILE_SIZE), TILE_SIZE, TILE_SIZE))

    for i in range(4):
        x = random.randint(0, SCREEN_WIDTH-TILE_SIZE)
        y = random.randint(SCREEN_HEIGHT - (2 * TILE_SIZE), SCREEN_HEIGHT) - (0.5 * TILE_SIZE)
        background.blit(seagrass, (x, y, TILE_SIZE, TILE_SIZE))

    text = game_font.render("Chomp!", True, (255, 69, 0))
    # background.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2,SCREEN_HEIGHT//2 - text.get_height()//2))


draw_background()

while len(minnows) > 0:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("Thanks for playing")
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                my_fish.moving_left = True
            if event.key == pygame.K_RIGHT:
                my_fish.moving_right = True
            if event.key == pygame.K_UP:
                my_fish.moving_up = True
            if event.key == pygame.K_DOWN:
                my_fish.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                my_fish.moving_left = False
            if event.key == pygame.K_RIGHT:
                my_fish.moving_right = False
            if event.key == pygame.K_UP:
                my_fish.moving_up = False
            if event.key == pygame.K_DOWN:
                my_fish.moving_down = False

    # update game objects
    my_fish.update()
    minnows.update()

    # check for collisions
    chomped_minnows = pygame.sprite.spritecollide(my_fish, minnows, False)
    # if len(chomped_minnows) > 0:
        # print(f"Chomped a minnow, your score is {score}!")

    # update screen
    screen.blit(background, (0,0))
    my_fish.draw(screen)
    minnows.draw(screen)
    pygame.display.flip()
    clock.tick(60)
