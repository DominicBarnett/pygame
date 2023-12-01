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
   self.x = choice(lanes)
   self.y = -64
