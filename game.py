import pygame
import board

class Game() :

	def __init__(self) :

		self.pantalla = pygame.display.set_mode([700,600])
		self.salir = False
		self.clock = pygame.time.Clock()
		self.color_negro = (0,0,0)
		self.color_rojo = (255,0,0)
		self.color_blanco = (255,255,255)
		self.color_fondo = (250,128,114)
		self.tablero = board.Board(self.color_blanco, self.color_negro,0,0,65,65)

