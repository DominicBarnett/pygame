from game import GameObject
from random import randint, choice

lanes = [93, 218, 343]
class Bomb(GameObject):
    def __init__(self):
        super(Bomb, self).__init__(0, 0, 'bomb.png')
        # self.dx = (randint(0, 200) / 100) + 1
        # self.dy = 0
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
        self.speed = (randint(0,200) / 100) + 1
        if choice_direction == "down":
            self.angle = 0
            self.x = choice(lanes)
            self.y = -64
        elif choice_direction == "left":
            self.angle = 3.14 / 2
            self.x = -0
            self.y = choice(lanes)
            

        
