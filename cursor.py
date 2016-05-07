import pygame

class Cursor(pygame.Rect) :

	def __init__(self) :

		pygame.Rect.__init__(self,0,0,0,1)

	def update(self, pantalla) :

		self.left, self.top = pygame.mouse.get_pos()
