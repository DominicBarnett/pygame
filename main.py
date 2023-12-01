# Example 2

# Import and initialize pygame
import pygame
from random import randint, choice
from apple import Apple
from strawberry import Strawberry
from bomb import Bomb
from player import Player
from scoreboard import ScoreBoard


# from pygame.sprite import _Group
pygame.init()
pygame.font.init()
# Configure the screen
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()
lanes = [93, 218, 343]

apple = Apple()
apple2 = Apple() 
apple3 = Apple()
strawberry = Strawberry()
strawberry2 = Strawberry()
strawberry3 = Strawberry()
player = Player()
bomb = Bomb()
bomb2 = Bomb()
bomb3 = Bomb()
score = ScoreBoard(30, 30, 0)
# Make a group
all_sprites = pygame.sprite.Group()
bombs = pygame.sprite.Group()
# make a fruits Group
fruit_sprites = pygame.sprite.Group()
# Add sprites to group
all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(apple2)
all_sprites.add(apple3)
all_sprites.add(strawberry)
all_sprites.add(strawberry2)
all_sprites.add(strawberry3)
all_sprites.add(bomb)
all_sprites.add(bomb2)
all_sprites.add(bomb3)
bombs.add(bomb)
bombs.add(bomb2)
bombs.add(bomb3)
all_sprites.add(score)
fruit_sprites.add(apple)
fruit_sprites.add(apple2)
fruit_sprites.add(apple3)
fruit_sprites.add(strawberry)
fruit_sprites.add(strawberry2)
fruit_sprites.add(strawberry3)

running = True
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      elif event.key == pygame.K_LEFT:
        player.left()
      elif event.key == pygame.K_RIGHT:
        player.right()
      elif event.key == pygame.K_UP:
        player.up()
      elif event.key == pygame.K_DOWN:
        player.down()

  # Clear screen
  screen.fill((255, 255, 255))
  # Move and render Sprites
  for entity in all_sprites:
    entity.move()
    entity.render(screen)
# Check Colisions
  fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
  if fruit:
    score.update(100)
    fruit.reset()
# Check collision player and bomb
  explode = pygame.sprite.spritecollideany(player, bombs)
  if explode:
    running = False
  # Update the window
  pygame.display.flip()
  # Update the window

  # Tick the clock
  clock.tick(60)
