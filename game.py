# Example 2

# Import and initialize pygame
import pygame
import math
from random import randint,choice

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
   
   
class GameObject(pygame.sprite.Sprite):
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    self.surf = pygame.image.load(image)
    self.x = x
    self.y = y
    self.angle = 0 # angle in radians
    self.speed = randint(2,10) # speed in pixels

  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))

  def move(self):
    self.x += math.sin(self.angle) * self.speed # calculate dx from angle and speed
    self.y += math.cos(self.angle) * self.speed # calculate dy from angle and speed

class Apple(GameObject):
 def __init__(self):
   super(Apple, self).__init__(0, 0, 'apple.png')
   self.dx = 0
   self.dy = (randint(0, 200) / 100) + 1
   self.reset() # call reset here! 
   self.rect = self.surf.get_rect()
   self.rect.topleft = (self.x, self.y)

 def move(self):
    super().move()
   # Check the y position of the apple
    if self.y > 500: 
       self.reset()
    self.rect.topleft = (self.x, self.y)

 # add a new method
 def reset(self):
   self.x = choice(lanes)
   self.y = -64

class Strawberry(GameObject):
  def __init__(self):
    super(Strawberry, self).__init__(0, 0, 'strawberry.png')
    self.dx = (randint(0,200) / 100) + 1
    self.dy = 0
    self.reset()
    self.rect = self.surf.get_rect()
    self.rect.topleft = (self.x, self.y)

  def move(self):
    super().move()
    if self.x > 500 or self.y > 500:
      self.reset()
    self.rect.topleft = (self.x, self.y)
  
  def reset(self):
    self.y = -64
    self.x = choice(lanes)

class Bomb(GameObject):
    def __init__(self):
        super(Bomb, self).__init__(0, 0, 'bomb.png')
        self.dx = (randint(0, 200) / 100) + 1
        self.dy = 0
        self.reset()
        # Add the following lines to create a rect attribute
        self.rect = self.surf.get_rect()
        self.rect.topleft = (self.x, self.y)

    def move(self):
        super().move()
        if self.x > 500 or self.x < -64 or self.y > 500 or self.y < -64:
            self.reset()
        # Update the rect attribute
        self.rect.topleft = (self.x, self.y)

    def reset(self):
        # Randomly choose whether the bomb comes down or scrolls from the left
        choice_direction = choice(["down", "left"])
        if choice_direction == "down":
            self.dx = 0
            self.dy = (randint(0, 200) / 100) + 1
            self.x = choice(lanes)
            self.y = -64
        elif choice_direction == "left":
            self.dx = (randint(0, 200) / 100) + 1
            self.dy = 0
            self.x = -64
            self.y = choice(lanes)

class Player(GameObject):
  def __init__(self):
    super(Player, self).__init__(0, 0, 'player.png')
    self.dx = 0
    self.dy = 0
    self.pos_x = 1
    self.pos_y = 1
    self.reset()
    self.rect = self.surf.get_rect()
    self.rect.topleft = (self.x, self.y)

  def left(self):
    if self.pos_x > 0:
        self.pos_x -= 1
        self.update_dx_dy()

  def right(self):
    if self.pos_x < len(lanes) - 1:
        self.pos_x += 1
        self.update_dx_dy()

  def up(self):
    if self.pos_y > 0:
        self.pos_y -= 1
        self.update_dx_dy()

  def down(self):
    if self.pos_y < len(lanes) - 1:
        self.pos_y += 1
        self.update_dx_dy()

  def move(self):
    self.x -= (self.x - self.dx) * 0.25
    self.y -= (self.y - self.dy) * 0.25
    self.rect.topleft = (self.x, self.y)

  def update_dx_dy(self):
    self.dx = lanes[self.pos_x]
    self.dy = lanes[self.pos_y]

  def reset(self):
    self.x = lanes[self.pos_x]
    self.y = lanes[self.pos_y]
    self.dx = self.x
    self.dy = self.y
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
