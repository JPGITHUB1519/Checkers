import pygame

class Partida() :

	def __init__(self) :

		pass

	def mover(self,squares, f_actual, c_actual, f_prox, c_prox, data_structure) :

		"""
		aux_piece = squares[f_actual][c_actual].piece
		squares[f_actual][c_actual].piece = squares[f_prox][c_prox].piece
		squares[f_prox][c_prox].piece = aux_piece
		"""

		squares[f_prox][c_prox].piece.image = squares[f_actual][c_actual].piece.image
		squares[f_actual][c_actual].piece.image = squares[f_actual][c_actual].piece.imagen_transparente
	
		squares[f_prox][c_prox].occupation = squares[f_actual][c_actual].occupation
		squares[f_actual][c_actual].occupation = 0

		squares[f_prox][c_prox].piece.piece_type = squares[f_actual][c_actual].piece.piece_type
		squares[f_actual][c_actual].piece.piece_type = 0

	def capture_piece(self,squares, f_actual, c_actual, f_prox, c_prox) :

		if squares[f_actual][c_actual].piece.piece_type == 1 :

			# capture left diagonal
			if c_actual - c_prox == 2 :

				squares[f_actual - 1][c_actual - 1].piece.image = squares[f_actual - 1][c_actual - 1].piece.imagen_transparente
				squares[f_actual - 1][c_actual - 1].occupation = 0
				squares[f_actual - 1][c_actual - 1].piece.piece_type = 0

			# capture right diagonal
			if c_actual - c_prox == - 2 :

				squares[f_actual - 1][c_actual + 1].piece.image = squares[c_actual - 1][c_actual + 1].piece.imagen_transparente
				squares[f_actual - 1][c_actual + 1].occupation = 0
				squares[f_actual - 1][c_actual + 1].piece.piece_type = 0

		if squares[f_actual][c_actual].piece.piece_type == 2 :

			# capture left diagonal
			if c_actual - c_prox == 2 :
				squares[f_actual + 1][c_actual - 1].piece.image = squares[f_actual + 1][c_actual - 1].piece.imagen_transparente
				squares[f_actual + 1][c_actual - 1].occupation = 0
				squares[f_actual + 1][c_actual - 1].piece.piece_type = 0

			# capture right diagonal
			if c_actual - c_prox == -2 :
				squares[f_actual + 1][c_actual + 1].piece.image = squares[f_actual + 1][c_actual + 1].piece.imagen_transparente
				squares[f_actual + 1][c_actual + 1].occupation = 0
				squares[f_actual + 1][c_actual + 1].piece.piece_type = 0

		squares[f_prox][c_prox].piece.image = squares[f_actual][c_actual].piece.image
		squares[f_actual][c_actual].piece.image = squares[f_actual][c_actual].piece.imagen_transparente
	
		squares[f_prox][c_prox].occupation = squares[f_actual][c_actual].occupation
		squares[f_actual][c_actual].occupation = 0

		squares[f_prox][c_prox].piece.piece_type = squares[f_actual][c_actual].piece.piece_type
		squares[f_actual][c_actual].piece.piece_type = 0

		# reset captured piece



	def check_movement(self,squares, f_actual, c_actual, f_prox, c_prox) :

		piece_actual = squares[f_actual][c_actual].piece
		piece_prox = squares[f_prox][c_prox].piece

		
		if self.check_ispiece(piece_actual) == False :
			return False

		if self.check_is_occupied(squares, f_prox, c_prox) == True :

			return False

		# check length of the move
		if self.check_piece_type(piece_actual) == 1 :
			
			if not(f_prox == f_actual - 1 and c_prox in self.check_diagonal(f_actual, c_actual)) :

				return False

		if self.check_piece_type(piece_actual) == 2 :

			if not(f_prox == f_actual + 1 and c_prox in self.check_diagonal(f_actual, c_actual)) :

				return False
	
		return True

	def check_diagonal(self,i,j) :

		if j == 0 :

			return [1]

		return [j - 1, j + 1]

	# to show the tipe of the piece
	def check_piece_type(self, piece) :

		return piece.piece_type

	# show if is a piece
	def check_ispiece(self, piece) :

		if self.check_piece_type(piece) == 1 or self.check_piece_type(piece) == 2 or self.check_piece_type(piece) == 11 or self.check_piece_type(piece) == 22 :
			
			return True

		else :

			return False

	def check_is_occupied(self,squares, f, c) :

		if squares[f][c].occupation == 1 or squares[f][c].occupation == 2 or squares[f][c].occupation == 11 or squares[f][c].occupation == 22 :

			return True

		return False

	# check if the player eats a piece
	def check_is_eaten(self,juego, f_prox, c_prox) :

		for list_comer in juego.pos_comer :

			if f_prox in list_comer and c_prox in list_comer :

				return True

		return False

	def check_can_eat(self, squares, f_actual, c_actual) :

		cond = False
		pos = []

		if squares[f_actual][c_actual].piece.piece_type == 1 :
			if c_actual != 0 :
				# si hay una pieza en la diagonal izquierda y esa pieza es del jugador 2

				if self.check_is_occupied(squares, f_actual -1, c_actual - 1) == True and squares[f_actual - 1][c_actual - 1].piece.piece_type == 2 :
					
					if self.check_is_occupied(squares, f_actual - 2, c_actual - 2) == False :
						
						cond = True
						pos.append([f_actual - 2, c_actual - 2])

			if c_actual != 7 and c_actual != 6 :
				# si hay una pieza en la diagonal derecha y esa pieza es del jugador 2
				
				if self.check_is_occupied(squares,f_actual - 1, c_actual + 1) == True and squares[f_actual - 1 ][c_actual + 1].piece.piece_type == 2 :

					if self.check_is_occupied(squares,f_actual - 2, c_actual + 2) == False :

						cond = True
						pos.append([f_actual - 2, c_actual + 2])

		if squares[f_actual][c_actual].piece.piece_type == 2 :

			if c_actual != 7 and c_actual != 6 and  f_actual != 6 :
				if self.check_is_occupied(squares, f_actual + 1, c_actual + 1) == True and squares[f_actual + 1][c_actual + 1].piece.piece_type == 1 :
				
					if self.check_is_occupied(squares, f_actual + 2, c_actual + 2) == False :

						cond = True
						pos.append([f_actual + 2, c_actual + 2])

			if c_actual != 0 and f_actual != 6 :
				if self.check_is_occupied(squares,f_actual + 1, c_actual - 1) == True and squares[f_actual + 1][c_actual - 1].piece.piece_type == 1 :

					if self.check_is_occupied(squares,f_actual + 2, c_actual - 2) == False :

						cond = True
						pos.append([f_actual + 2, c_actual - 2])



		return pos

	def check_all_pieces_movement(self, squares) :

		data_structure = {}
		element_name = ""
		aux_cant_eat = []

		for f in range(0,8) :
 
			for c in range(0,8) :

				aux_cant_eat = self.check_can_eat(squares, f, c)
				element_name = str(f) + str(c)
				data_structure[element_name] = []

				if len(aux_cant_eat) > 0 :

					data_structure[element_name].append(True)

					for i in aux_cant_eat :
						data_structure[element_name].append(i)
					continue
				if squares[f][c].piece.piece_type  == 1:

					# check right diagonal
					data_structure[element_name].append(False)
					if c != 7  :
						if self.check_movement(squares, f, c, f - 1, c + 1) == True :

							data_structure[element_name].append([f - 1, c + 1])
					
					if c != 0 :
						if self.check_movement(squares, f,c, f - 1, c - 1) == True :

							data_structure[element_name].append([f - 1, c - 1])

				if squares[f][c].piece.piece_type  == 2:

					data_structure[element_name].append(False)
					# check right diagonal
					if c != 7  :
						if self.check_movement(squares, f, c, f + 1, c + 1) == True :

							data_structure[element_name].append([f + 1, c + 1])
						
					if c != 0 :
						if self.check_movement(squares, f,c, f + 1, c - 1) == True :

							data_structure[element_name].append([f + 1, c - 1])
		return data_structure

	# check if any player has to capture and return a cond and the
	# pieces with their positions to capture

	def have_to_eat(self, data_structure, squares, player) :

		# positions = {"position" : [moves]... }
		positions = {}
		pos = []
		cond = False
		for f in range(0, 8) :

			for c in range(0,8) :

				# asking if the piece is the kind of the player
				if squares[f][c].piece.piece_type == player :

					element_name = str(f) + str(c)
					# asking if the piece has to eat
					if data_structure[element_name][0] == True :

						for i in range(1, len(data_structure[element_name])) :

							pos.append(data_structure[element_name][i])
						
						positions[element_name] = pos
						pos = []
						if cond == False :
							cond = True

		# [condition, dictionarie]
		return cond, positions

	# return the condition and the pos a piece have to eat
	def piece_have_to_eat(self,comer_data_structure,squares,i,j) :

		cond = False
		pos = []

		if comer_data_structure[str(i) + str(j)] > 0 :

			pos = comer_data_structure[str(i) + str(j)]
			cond = True

		return cond, pos




							












