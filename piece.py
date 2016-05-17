import pygame

class Piece(pygame.sprite.Sprite) :

	def __init__(self, piece_type, x, y) :

		self.imagen_pieza_negra = pygame.image.load("images/black_piece.png")
		self.imagen_pieza_roja = pygame.image.load("images/red_piece.png")
		self.imagen_pieza_king1 = pygame.image.load("images/king_red_piece.png")
		self.imagen_pieza_king2 = pygame.image.load("images/king_black_piece.png")
		self.imagen_transparente = pygame.image.load("images/fondo_transparente.png")
		self.imagen_highlight_none = pygame.image.load("images/azul_blanco.png")
		self.imagen_highlight_red = pygame.image.load("images/azul_blanco_red.png")
		self.imagen_highlight_black = pygame.image.load("images/azul_blanco_black.png")
		self.imagen_highlight_red_king = pygame.image.load("images/azul_blanco_red_king.png")
		self.imagen_highlight_black_king = pygame.image.load("images/azul_blanco_black_king.png")

		self.piece_type = piece_type


		if self.piece_type == 0 :
			self.image =  self.imagen_transparente

		if self.piece_type == 1 :

			self.image = self.imagen_pieza_roja

		if self.piece_type == 2 : 

			self.image = self.imagen_pieza_negra

		if self.piece_type == 11 : 

			self.image = self.imagen_pieza_king1

		if self.piece_type == 22 :

			self.image = self.imagen_pieza_king2


		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = x, y

		self.isking = False












