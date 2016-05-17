import pygame
import square
import piece

class Board() :

	def __init__ (self, color1, color2, x, y,width, height, pantalla) :

		self.color1 = color1
		self.color2 = color2
		self.squares = [[],[],[],[],[],[],[],[]]
		self.width = width
		self.height = height
		self.xpos = x
		self.ypos = y
		# initialize square

		for i in range(0,8) :

			for j in range(0,8) :

				self.squares[i].append(square.Square(self.xpos, self.ypos, width, height))
				self.xpos += 65
			self.xpos = x
			self.ypos += 65

		# assign pieces to squares
		for i in range(0,8) :

			for j in range(0,8) :

				# assign pieces to player 1

				if i in range(0,3) :

					if i % 2 == 0 :

						if j % 2 != 0 :

							self.assign_positions(i,j,pantalla,2)
						#to none	
						else :
							self.assign_positions(i,j,pantalla,0)

					else :

						if j % 2 == 0 :
							self.assign_positions(i,j,pantalla,2)
						else :
							self.assign_positions(i,j,pantalla,0)
				
				# player 2
				elif i in range(5,8) :

					if i % 2 == 0 :

						if j % 2 != 0 :
							self.assign_positions(i,j,pantalla,1)
						else :

							self.assign_positions(i,j,pantalla,0)

					else :

						if j % 2 == 0 :
							self.assign_positions(i,j,pantalla,1)

						else :

							self.assign_positions(i,j,pantalla,0)
				else :

					self.assign_positions(i,j,pantalla,0)

		self.board_string = self.get_string_data_structure()
		self.board_data_structure = self.get_list_data_structure()

		"""
		self.squares.append(pygame.Rect(x,y,width, height))
		self.squares.append(pygame.Rect(x + 65,y,width, height))
		self.squares.append(pygame.Rect(x,y + 65,width, height))
		"""
	def update(self, pantalla) :

		#pygame.draw.rect(pantalla,self.color1, self.squares[0])

		for i in range(0,8) :

			for j in range(0,8) :

				if i % 2 == 0 :

					if j % 2 == 0 :

						pygame.draw.rect(pantalla,self.color1, self.squares[i][j])

					else :

						pygame.draw.rect(pantalla, self.color2, self.squares[i][j])

				else :

					if j % 2 == 0 :

						pygame.draw.rect(pantalla, self.color2, self.squares[i][j])

					else :

						pygame.draw.rect(pantalla, self.color1, self.squares[i][j])

	def assign_positions(self,fila,columna,pantalla, occupation) :
		""" Asign The Piece and The ocupation to a Square"""
		self.squares[fila][columna].piece = piece.Piece(occupation, self.squares[fila][columna].left , self.squares[fila][columna].top )
		self.squares[fila][columna].occupation = occupation

	def draw_pieces(self,pantalla) :

		for fila in range(0,8) :

			for columna in range(0,8) :

				self.squares[fila][columna].draw_piece(pantalla,self.squares[fila][columna].piece)

	def get_string_data_structure(self) :

		string = ""

		for i in range(0,8) :

			for j in range(0,8) :

				string += " " + str(self.squares[i][j].piece.piece_type)

			string += "\n"

		return string

	def get_list_data_structure(self) :

		lista = []
		sub = []

		for i in range(0,8) :

			for j in range(0,8) :

				sub.append(self.squares[i][j].piece.piece_type)
			lista.append(sub)
			sub = []

		return lista







		

