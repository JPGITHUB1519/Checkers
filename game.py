import pygame
import board
import cursor
import partida
import boton
import sys

class Game() :

	def __init__(self) :

		self.pantalla = pygame.display.set_mode([700,700])
		pygame.display.set_caption("CHECKERS GAME")
		self.icon = pygame.image.load("images/icon_checkers.png")
		pygame.display.set_icon(self.icon)
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
		self.dic_elemento = ""
		# to know if we have to capture
		self.cond_comer = False
		#to save the turn of the player
		self.turno = 1
		# to save the pieces that has to eat
		self.comer_data_structure = {} 
		self.comer_data_structure_element = ""
		# to know if the player ate
		self.comio = False
		self.cursor1 = cursor.Cursor()
		self.partida = partida.Partida()
		# to know if the player playerd a valid play
		self.cond_play_well = False

		# comer multiple
		self.comer_multiple_cond = False
		self.aux_comer_data_structure = {}
		self.aux_game_data_structure = {}
		self.f_comer_multiple = 0
		self.cond_comer_multiple = False

		self.game_data_structure = {}

		# squares to selected 
		self.square_selected = pygame.Rect(0,0,50,50)

		# f , c, cantidad
		self.comidas = [None,None,0]


		"""
		self.game_data_structure = [[0,2,0,2,0,2,0,2],
									[2,0,2,0,2,0,2,0],
									[0,2,0,2,0,2,0,2],
									[0,0,0,0,0,0,0,0],
									[0,0,0,0,0,0,0,0],
									[1,0,1,0,1,0,1,0],
									[0,1,0,1,0,1,0,1],
									[1,0,1,0,1,0,1,0]],
		"""
		#conds
		self.cond_main_game = False
		self.cond_menu = True

		# imagenes
		self.fondo_menu = pygame.image.load("images/fondo_menu.png")
		self.fondo_title = pygame.image.load("images/title.png")

		self.imagen_boton_jugar = pygame.image.load("images/jugar.png")
		self.imagen_boton_jugar_hover = pygame.image.load("images/jugar_hover.png")

		self.imagen_boton_salir = pygame.image.load("images/salir.png")
		self.imagen_boton_salir_hover = pygame.image.load("images/salir_hover.png")
		
		# botones
		self.boton_jugar = boton.Boton(self.imagen_boton_jugar, self.imagen_boton_jugar_hover, 200,500)
		self.boton_salir = boton.Boton(self.imagen_boton_salir, self.imagen_boton_salir_hover, 400,500)

		# fonts

		self.font_orena = pygame.font.Font("fonts/Orena.ttf",30)
		self.text_credits = self.font_orena.render("Game Created By Jean Urenia", 0, (255,69,0))

		# sounds and sounds_conds

		self.cond_music_title = False
		self.cond_music_background = False

	def main_game(self) :

		self.pantalla.fill(self.color_fondo)

		self.tablero.update(self.pantalla)

		self.cursor1.update(self.pantalla)

		self.tablero.draw_pieces(self.pantalla)

		if self.cond_music_background == False :
			pygame.mixer.music.stop()
			pygame.mixer.music.load("music/background.mp3")
			pygame.mixer.music.play(-1)
			self.cond_music_background = True 


	def menu(self) :

		self.cursor1.update(self.pantalla)
		self.pantalla.blit(self.fondo_menu, (0,0))
		self.pantalla.blit(self.fondo_title, (100,150))
		self.boton_jugar.update(self.pantalla, self.cursor1)
		self.boton_salir.update(self.pantalla, self.cursor1)
		self.pantalla.blit(self.text_credits, (75,650))

		if self.cond_music_title == False :
			pygame.mixer.music.load("music/sountrack_title.mp3")
			pygame.mixer.music.play(-1)
			self.cond_music_title = True 




		#pygame.draw.rect(self.pantalla,(0,0,0),self.square_selected)

	

