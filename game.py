import pygame
from random import randint
import math

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
