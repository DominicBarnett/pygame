from game import GameObject
from random import randint, choice

lanes = [93, 218, 343]
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
