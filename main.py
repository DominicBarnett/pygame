# Example 2

# Import and initialize pygame
import pygame
from random import randint, choice
from apple import Apple
from strawberry import Strawberry
from bomb import Bomb
from player import Player


# from pygame.sprite import _Group
pygame.init()
pygame.font.init()
# Configure the screen
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()
lanes = [93, 218, 343]
# Create the game loop
# Game Object
class ScoreBoard(pygame.sprite.Sprite):
    def __init__(self, x, y, score):
       super(ScoreBoard, self).__init__()
       self.score = score
       self.font = pygame.font.SysFont('Comic Sans MS', 30)
       self.surf = self.font.render(f"{self.score}", False, (0, 0, 0))
       self.dx = 0
       self.dy = 0
       self.x = x
       self.y = y
	
    def update(self, points):
        self.score += points

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def render(self, screen):
        self.surf = self.font.render(f"{self.score}", False, (0, 0, 0))
        screen.blit(self.surf, (self.x, self.y))

    def reset(self):
	    self.score = 0
   
   
# class GameObject(pygame.sprite.Sprite):
#   def __init__(self, x, y, image):
#     super(GameObject, self).__init__()
#     self.surf = pygame.image.load(image)
#     self.x = x
#     self.y = y
#     self.angle = 0 # angle in radians
#     self.speed = randint(2,10) # speed in pixels

#   def render(self, screen):
#     screen.blit(self.surf, (self.x, self.y))

#   def move(self):
#     self.x += math.sin(self.angle) * self.speed # calculate dx from angle and speed
#     self.y += math.cos(self.angle) * self.speed # calculate dy from angle and speed


# Make instances of GameObject and Apple
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
  if pygame.sprite.collide_rect(player, bomb):
    running = False
  # Update the window
  pygame.display.flip()
  # Update the window

  # Tick the clock
  clock.tick(60)
