import pygame

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