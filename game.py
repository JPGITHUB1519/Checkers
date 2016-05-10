import pygame
import board
import cursor
import partida

class Game() :

	def __init__(self) :

		self.pantalla = pygame.display.set_mode([700,700])
		self.salir = False
		self.seleccionado = False
		self.factual = 0
		self.cactual = 0
		self.clock = pygame.time.Clock()
		self.color_negro = (0,0,0)
		self.color_rojo = (255,0,0)
		self.color_blanco = (255,255,255)
		self.color_fondo = (250,128,114)
		self.tablero = board.Board(self.color_blanco, self.color_negro,100,100,65,65, self.pantalla)
		self.pos_comer = []
		self.dic_elemento = ""
		self.cond_comer = False
		self.cursor1 = cursor.Cursor()
		self.partida = partida.Partida()
		self.game_data_structure = [[0,2,0,2,0,2,0,2],
									[2,0,2,0,2,0,2,0],
									[0,2,0,2,0,2,0,2],
									[0,0,0,0,0,0,0,0],
									[0,0,0,0,0,0,0,0],
									[1,0,1,0,1,0,1,0],
									[0,1,0,1,0,1,0,1],
									[1,0,1,0,1,0,1,0]],
		#conds
		self.cond_main_game = True

	def main_game(self) :

		self.pantalla.fill(self.color_fondo)

		self.tablero.update(self.pantalla)

		self.cursor1.update(self.pantalla)

		self.tablero.draw_pieces(self.pantalla)



