import pygame

class Piece(pygame.sprite.Sprite) :

	def __init__(self, piece_type, x, y) :

		imagen_pieza_negra = pygame.image.load("images/black_piece.png")
		imagen_pieza_roja = pygame.image.load("images/red_piece.png")
		imagen_transparente = pygame.image.load("images/fondo_transparente.png")
		self.piece_type = piece_type

		if self.piece_type == 0 :
			self.player1 = True
			self.player2 = False
			self.image = imagen_transparente

		if self.piece_type == 1 :
			self.player1 = True
			self.player2 = False
			self.image = imagen_pieza_roja

		if self.piece_type == 2 : 

			self.player2 = True
			self.player1 = False
			self.image = imagen_pieza_negra

		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = x, y

		self.isking = False


