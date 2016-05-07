import pygame

class Square(pygame.Rect) :

	def __init__(self, x, y, width, height) :

		pygame.Rect.__init__(self,x,y,width, height)
		self.piece = None


	def draw_piece(self, pantalla, piece) :

		if self.piece != None :

			pantalla.blit(piece, self.width/6, self.height/6)

