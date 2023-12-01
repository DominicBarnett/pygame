from game import GameObject
from random import randint, choice

lanes = [93, 218, 343]
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
   choice_direction = choice(["down", "left"])
   self.speed = (randint(0,200) / 100) + 1
   if choice_direction == "down":
      self.angle = 0
      self.x = choice(lanes)
      self.y = -64
   elif choice_direction == "left":
      self.angle = 3.14 / 2
      self.x = -0
      self.y = choice(lanes)
