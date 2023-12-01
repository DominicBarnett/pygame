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

fruits_list = [Apple(), Apple(), Apple(), Strawberry(), Strawberry(), Strawberry()]
bomb_list = [Bomb(), Bomb(), Bomb()]
player = Player()
score = ScoreBoard(30, 30, 0)

all_sprites = pygame.sprite.Group()
bombs = pygame.sprite.Group()
fruit_sprites = pygame.sprite.Group()


all_sprites.add(player)
all_sprites.add(fruits_list)
all_sprites.add(bomb_list)
bombs.add(bomb_list)
all_sprites.add(score)
fruit_sprites.add(fruits_list)

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
