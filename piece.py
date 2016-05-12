import pygame

class Piece(pygame.sprite.Sprite) :

	def __init__(self, piece_type, x, y) :

		self.imagen_pieza_negra = pygame.image.load("images/black_piece.png")
		self.imagen_pieza_roja = pygame.image.load("images/red_piece.png")
		self.imagen_pieza_king1 = pygame.image.load("images/green_piece.png")
		self.imagen_pieza_king2 = pygame.image.load("images/blue_piece.png")
		self.imagen_transparente = pygame.image.load("images/fondo_transparente.png")
		self.imagen_highlight = pygame.image.load("images/azul_blanco.png")
		self.piece_type = piece_type


		if self.piece_type == 0 :
			self.image =  self.imagen_transparente

		if self.piece_type == 1 :

			self.image = self.imagen_pieza_roja

		if self.piece_type == 2 : 

			self.image = self.imagen_pieza_negra

		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = x, y

		self.isking = False












