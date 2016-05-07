import pygame

class Piece(pygame.sprite.Sprite) :

	def __init__(self, piece_type, x, y) :

		imagen_pieza_negra = pygame.image.load("black_piece.png")
		imagen_pieza_roja = pygame.image.load("red_piece")

		if piece_type == "player1" :
			self.player1 = True
			self.player2 = False
			self.image = imagen_pieza_roja

		if piece_type == "player2" : 

			self.player2 = True
			self.player1 = False
			self.image = imagen_pieza_negra

		self.rect = image.get_rect()
		self.rect.left, self.rect.top = x, y

		self.isking = False


