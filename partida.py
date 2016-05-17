import pygame

class Partida() :

	def __init__(self) :

		pass

	def mover(self,squares, f_actual, c_actual, f_prox, c_prox, data_structure) :

		""" Move a piece in the Board to a specified position"""

		squares[f_prox][c_prox].piece.image = squares[f_actual][c_actual].piece.image
		squares[f_actual][c_actual].piece.image = squares[f_actual][c_actual].piece.imagen_transparente
	
		squares[f_prox][c_prox].occupation = squares[f_actual][c_actual].occupation
		squares[f_actual][c_actual].occupation = 0

		squares[f_prox][c_prox].piece.piece_type = squares[f_actual][c_actual].piece.piece_type
		squares[f_actual][c_actual].piece.piece_type = 0

	def capture_piece(self,squares, f_actual, c_actual, f_prox, c_prox, eat_multiple = False) :

		""" To Capture a Specified Piece """

		
		if eat_multiple == False :
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

		# kings capturing 
		if squares[f_actual][c_actual].piece.piece_type == 11 or squares[f_actual][c_actual].piece.piece_type == 22 or (squares[f_actual][c_actual].piece.piece_type == 1 and eat_multiple == True) or(squares[f_actual][c_actual].piece.piece_type == 2 and eat_multiple == True) :
			# capture left diagonal UP
			if c_actual - c_prox == 2 and f_actual - f_prox == 2 :

				squares[f_actual - 1][c_actual - 1].piece.image = squares[f_actual - 1][c_actual - 1].piece.imagen_transparente
				squares[f_actual - 1][c_actual - 1].occupation = 0
				squares[f_actual - 1][c_actual - 1].piece.piece_type = 0

			# capture right diagonal UP
			if c_actual - c_prox == - 2 and f_actual - f_prox == 2 :

				squares[f_actual - 1][c_actual + 1].piece.image = squares[c_actual - 1][c_actual + 1].piece.imagen_transparente
				squares[f_actual - 1][c_actual + 1].occupation = 0
				squares[f_actual - 1][c_actual + 1].piece.piece_type = 0

			# capture left diagonal Down
			if c_actual - c_prox == 2 and f_actual - f_prox ==  - 2 :
				squares[f_actual + 1][c_actual - 1].piece.image = squares[f_actual + 1][c_actual - 1].piece.imagen_transparente
				squares[f_actual + 1][c_actual - 1].occupation = 0
				squares[f_actual + 1][c_actual - 1].piece.piece_type = 0

			# capture right diagonal Down
			if c_actual - c_prox == -2 and f_actual - f_prox ==  - 2 :
				squares[f_actual + 1][c_actual + 1].piece.image = squares[f_actual + 1][c_actual + 1].piece.imagen_transparente
				squares[f_actual + 1][c_actual + 1].occupation = 0
				squares[f_actual + 1][c_actual + 1].piece.piece_type = 0
		
		# reset captured piece	
		squares[f_prox][c_prox].piece.image = squares[f_actual][c_actual].piece.image
		squares[f_actual][c_actual].piece.image = squares[f_actual][c_actual].piece.imagen_transparente
	
		squares[f_prox][c_prox].occupation = squares[f_actual][c_actual].occupation
		squares[f_actual][c_actual].occupation = 0

		squares[f_prox][c_prox].piece.piece_type = squares[f_actual][c_actual].piece.piece_type
		squares[f_actual][c_actual].piece.piece_type = 0

		

	def check_movement(self,squares, f_actual, c_actual, f_prox, c_prox) :

		""" Checks if a move is a valid Move"""

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

		# check king piece movement

		if not((f_prox == f_actual - 1 or f_prox == f_actual + 1) and (c_prox == c_actual - 1 or c_prox ==  c_actual + 1)) :

			return False
	
		return True

	def check_diagonal(self,i,j) :

		if j == 0 :

			return [1]

		return [j - 1, j + 1]

	# to show the tipe of the piece
	def check_piece_type(self, piece) :

		""" Returns The piece type of a piece """

		return piece.piece_type

	# show if is a piece
	def check_ispiece(self, piece) :

		""" Check if a Square have a valid piece """

		if self.check_piece_type(piece) == 1 or self.check_piece_type(piece) == 2 or self.check_piece_type(piece) == 11 or self.check_piece_type(piece) == 22 :
			
			return True

		else :

			return False

	def check_is_occupied(self,squares, f, c) :

		""" Check if a square is occuppied"""

		if squares[f][c].occupation == 1 or squares[f][c].occupation == 2 or squares[f][c].occupation == 11 or squares[f][c].occupation == 22 :

			return True

		return False

	# check if the player eats a piece
	def check_is_eaten(self,juego, f_prox, c_prox) :

		""" Check if the player eaten a piece """

		for list_comer in juego.pos_comer :

			if f_prox in list_comer and c_prox in list_comer :

				return True

		return False

	def check_can_eat(self, squares, f_actual, c_actual, eat_multiple = False) :

		""" Returns the position where a piece have to eat 
			Eat Multiple is a flag when it is True Normal Pieces can eat like a king
			when it is false normal pieces eat normal
		"""

		cond = False
		pos = []

		
		# player 1

		if eat_multiple == False :
			if squares[f_actual][c_actual].piece.piece_type == 1 :

				if c_actual != 0 and c_actual != 1 and f_actual != 0 and f_actual != 1 :
					# si hay una pieza en la diagonal izquierda y esa pieza es del jugador 2

					if self.check_is_occupied(squares, f_actual -1, c_actual - 1) == True and (squares[f_actual - 1][c_actual - 1].piece.piece_type == 2 or squares[f_actual - 1][c_actual - 1].piece.piece_type == 22) :
						
						if self.check_is_occupied(squares, f_actual - 2, c_actual - 2) == False :
							
							cond = True
							pos.append([f_actual - 2, c_actual - 2])

				if c_actual != 7 and c_actual != 6 and f_actual != 0 and f_actual != 1 :
					# si hay una pieza en la diagonal derecha y esa pieza es del jugador 2
					
					if self.check_is_occupied(squares,f_actual - 1, c_actual + 1) == True and (squares[f_actual - 1 ][c_actual + 1].piece.piece_type == 2 or squares[f_actual - 1 ][c_actual + 1].piece.piece_type == 22) :

						if self.check_is_occupied(squares,f_actual - 2, c_actual + 2) == False :

							cond = True
							pos.append([f_actual - 2, c_actual + 2])

			# player 2
			if squares[f_actual][c_actual].piece.piece_type == 2 :

				# si hay una pieza en la diagonal Izquierda y esa pieza es del jugador 1
				if c_actual != 0 and c_actual != 1 and f_actual != 6 and f_actual != 7:

					if self.check_is_occupied(squares,f_actual + 1, c_actual - 1) == True and (squares[f_actual + 1][c_actual - 1].piece.piece_type == 1 or squares[f_actual + 1][c_actual - 1].piece.piece_type == 11) :

						if self.check_is_occupied(squares,f_actual + 2, c_actual - 2) == False :

							cond = True
							pos.append([f_actual + 2, c_actual - 2])

				# si hay una pieza en la diagonal Derecha y esa pieza es del jugador 1
				if c_actual != 6 and c_actual != 7 and  f_actual != 6  and f_actual != 7:
					if self.check_is_occupied(squares, f_actual + 1, c_actual + 1) == True and (squares[f_actual + 1][c_actual + 1].piece.piece_type == 1 or squares[f_actual + 1][c_actual + 1].piece.piece_type == 11):
					
						if self.check_is_occupied(squares, f_actual + 2, c_actual + 2) == False :

							cond = True
							pos.append([f_actual + 2, c_actual + 2])

		# kings player 1

		if squares[f_actual][c_actual].piece.piece_type == 11 or (squares[f_actual][c_actual].piece.piece_type == 1 and eat_multiple == True)  :

			# si hay una pieza en la diagonal izquierda arriba y esa pieza es del jugador 2
			if c_actual != 0 and c_actual != 1 and f_actual != 0 and f_actual != 1 :

				if self.check_is_occupied(squares, f_actual -1, c_actual - 1) == True and (squares[f_actual - 1][c_actual - 1].piece.piece_type == 2 or squares[f_actual - 1][c_actual - 1].piece.piece_type == 22) :
					
					if self.check_is_occupied(squares, f_actual - 2, c_actual - 2) == False :
						
						cond = True
						pos.append([f_actual - 2, c_actual - 2])

			# si hay una pieza en la diagonal derecha arriba y esa pieza es del jugador 2
			if c_actual != 6 and c_actual != 7 and f_actual != 0 and f_actual != 1 :
				
				if self.check_is_occupied(squares,f_actual - 1, c_actual + 1) == True and (squares[f_actual - 1 ][c_actual + 1].piece.piece_type == 2 or squares[f_actual - 1 ][c_actual + 1].piece.piece_type == 22) :

					if self.check_is_occupied(squares,f_actual - 2, c_actual + 2) == False :

						cond = True
						pos.append([f_actual - 2, c_actual + 2])

			# si hay una pieza en la diagonal izquierda abajo y esa pieza es del jugador 2
			if c_actual != 0 and c_actual != 1 and f_actual != 7 and f_actual != 6 :

				if self.check_is_occupied(squares, f_actual + 1, c_actual - 1) == True and (squares[f_actual + 1][c_actual - 1].piece.piece_type == 2 or squares[f_actual + 1][c_actual - 1].piece.piece_type == 22) :
					
					if self.check_is_occupied(squares, f_actual + 2, c_actual - 2) == False :
						
						cond = True
						pos.append([f_actual + 2, c_actual - 2])

			# si hay una pieza en la diagonal Derecha abajo y esa pieza es del jugador 2
			if c_actual != 6 and c_actual != 7 and  f_actual != 6  and f_actual != 7:

				if self.check_is_occupied(squares, f_actual + 1, c_actual + 1) == True and (squares[f_actual + 1][c_actual + 1].piece.piece_type == 2 or squares[f_actual + 1][c_actual + 1].piece.piece_type == 22):
				
					if self.check_is_occupied(squares, f_actual + 2, c_actual + 2) == False :

						cond = True
						pos.append([f_actual + 2, c_actual + 2])
		# kings player 2
		if squares[f_actual][c_actual].piece.piece_type == 22 or (squares[f_actual][c_actual].piece.piece_type == 2 and eat_multiple == True):

			# si hay una pieza en la diagonal izquierda arriba y esa pieza es del jugador 1
			if c_actual != 0 and c_actual != 1 and f_actual != 0 and f_actual != 1 :

				if self.check_is_occupied(squares, f_actual -1, c_actual - 1) == True and (squares[f_actual - 1][c_actual - 1].piece.piece_type == 1 or squares[f_actual - 1][c_actual - 1].piece.piece_type == 11) :
					
					if self.check_is_occupied(squares, f_actual - 2, c_actual - 2) == False :
						
						cond = True
						pos.append([f_actual - 2, c_actual - 2])

			# si hay una pieza en la diagonal derecha arriba y esa pieza es del jugador 1
			if c_actual != 6 and c_actual != 7 and f_actual != 0 and f_actual != 1 :
				
				if self.check_is_occupied(squares,f_actual - 1, c_actual + 1) == True and (squares[f_actual - 1 ][c_actual + 1].piece.piece_type == 1 or squares[f_actual - 1 ][c_actual + 1].piece.piece_type == 11) :

					if self.check_is_occupied(squares,f_actual - 2, c_actual + 2) == False :

						cond = True
						pos.append([f_actual - 2, c_actual + 2])

			# si hay una pieza en la diagonal izquierda abajo y esa pieza es del jugador 1
			if c_actual != 0 and c_actual != 1 and f_actual != 7 and f_actual != 6 :

				if self.check_is_occupied(squares, f_actual + 1, c_actual - 1) == True and (squares[f_actual + 1][c_actual - 1].piece.piece_type == 1 or squares[f_actual + 1][c_actual - 1].piece.piece_type == 11) :
					
					if self.check_is_occupied(squares, f_actual + 2, c_actual - 2) == False :
						
						cond = True
						pos.append([f_actual + 2, c_actual - 2])

			# si hay una pieza en la diagonal Derecha abajo y esa pieza es del jugador 1
			if c_actual != 6 and c_actual != 7 and  f_actual != 6  and f_actual != 7:

				if self.check_is_occupied(squares, f_actual + 1, c_actual + 1) == True and (squares[f_actual + 1][c_actual + 1].piece.piece_type == 1 or squares[f_actual + 1][c_actual + 1].piece.piece_type == 11):
				
					if self.check_is_occupied(squares, f_actual + 2, c_actual + 2) == False :

						cond = True
						pos.append([f_actual + 2, c_actual + 2])

		return pos

	def check_all_pieces_movement(self, squares, eat_multiple = False) :

		""" Returns a dictionary with all pieces with their respective
		Movement. dict key = piece, dic value = position to capture

		"""
		data_structure = {}
		element_name = ""
		aux_cant_eat = []

		for f in range(0,8) :
 
			for c in range(0,8) :

				if eat_multiple == False :

					aux_cant_eat = self.check_can_eat(squares, f, c)

				else :

					aux_cant_eat = self.check_can_eat(squares, f, c, True)

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
					if c != 7 and f != 0 :
						if self.check_movement(squares, f, c, f - 1, c + 1) == True :

							data_structure[element_name].append([f - 1, c + 1])
					
					if c != 0  and f != 0:
						if self.check_movement(squares, f,c, f - 1, c - 1) == True :

							data_structure[element_name].append([f - 1, c - 1])

				if squares[f][c].piece.piece_type  == 2:

					data_structure[element_name].append(False)
					# check right diagonal
					if c != 7 and f != 7 :
						if self.check_movement(squares, f, c, f + 1, c + 1) == True :

							data_structure[element_name].append([f + 1, c + 1])
						
					if c != 0 and f!= 7 :
						if self.check_movement(squares, f,c, f + 1, c - 1) == True :

							data_structure[element_name].append([f + 1, c - 1])
				
				# check kings movement
				if squares[f][c].piece.piece_type  == 11 or squares[f][c].piece.piece_type == 22 :
					# check right diagonal up
					data_structure[element_name].append(False)

					if c != 7 and f != 0 :
						if self.check_movement(squares, f, c, f - 1, c + 1) == True :

							data_structure[element_name].append([f - 1, c + 1])
					
					if c != 0 and f != 0 :
						if self.check_movement(squares, f,c, f - 1, c - 1) == True :

							data_structure[element_name].append([f - 1, c - 1])

					if c != 7 and f != 7 :
						if self.check_movement(squares, f, c, f + 1, c + 1) == True :

							data_structure[element_name].append([f + 1, c + 1])

					if c != 0 and f != 7 :

						if self.check_movement(squares, f,c, f + 1, c - 1) == True :

							data_structure[element_name].append([f + 1, c - 1])

		return data_structure

	# check if any player has to capture and return a cond and the
	# pieces with their positions to capture

	def have_to_eat(self, data_structure, squares, player) :

		""" Check if the Pieces  have to capture
		return the cond and a dictionary with the position of the key
		as key and as value the position to capture
		"""

		# positions = {"position" : [moves]... }
		positions = {}
		pos = []
		cond = False
		for f in range(0, 8) :

			for c in range(0,8) :

				# asking if the piece is the kind of the player
				if self.convert_to_turn(squares[f][c].piece.piece_type) == player :

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

		"""
		Check if a Piece have where to capture.
		It Returns a cond a the positions the piece have to capture
		"""

		cond = False
		pos = []

		if (str(i) + str(j)) in comer_data_structure :

			pos = comer_data_structure[str(i) + str(j)]
			cond = True

		return cond, pos

	def become_king(self,turno, squares,i,j) :

		"""
		Converts a Normal Piece to a king piece
		"""
		if turno == 1 and squares[i][j].piece.isking == False :

			squares[i][j].piece.image = squares[i][j].piece.imagen_pieza_king1
			squares[i][j].piece.piece_type = 11
			squares[i][j].occupation = 11
			squares[i][j].piece.isking = True

		if turno == 2 and squares[i][j].piece.isking == False :

			squares[i][j].piece.image = squares[i][j].piece.imagen_pieza_king2
			squares[i][j].piece.piece_type = 22
			squares[i][j].occupation = 22
			squares[i][j].piece.isking = True

	def convert_to_turn(self, piece_type) :

		""" Returns the turn that a piece belong """

		if piece_type == 1 or piece_type == 11 :

			return 1

		if piece_type == 2 or piece_type == 22 :

			return 2

	def highlight_movement(self, squares, game_data_structure, i, j, turno) :

		aux = []

		for x in range(1,len(game_data_structure[str(i) + str(j)])) :

			for y in range(0, len(game_data_structure[str(i) + str(j)][x])) :

				aux.append(game_data_structure[str(i) + str(j)][x][y])

			if squares[aux[0]][aux[1]].piece.piece_type == 0 :
				squares[aux[0]][aux[1]].piece.image = squares[aux[0]][aux[1]].piece.imagen_highlight_none

			if squares[aux[0]][aux[1]].piece.piece_type == 1 :
				squares[aux[0]][aux[1]].piece.image = squares[aux[0]][aux[1]].piece.imagen_highlight_red

			if squares[aux[0]][aux[1]].piece.piece_type == 2 :
				squares[aux[0]][aux[1]].piece.image = squares[aux[0]][aux[1]].piece.imagen_highlight_black

			if squares[aux[0]][aux[1]].piece.piece_type == 11 :
				squares[aux[0]][aux[1]].piece.image = squares[aux[0]][aux[1]].piece.imagen_highlight_red_king

			if squares[aux[0]][aux[1]].piece.piece_type == 22 :
				squares[aux[0]][aux[1]].piece.image = squares[aux[0]][aux[1]].piece.imagen_highlight_black_king
			
			aux = []

	def deshighlight_movement(self, squares, game_data_structure, i, j, turno) :

		aux = []

		for x in range(1,len(game_data_structure[str(i) + str(j)])) :

			for y in range(0, len(game_data_structure[str(i) + str(j)][x])) :

				aux.append(game_data_structure[str(i) + str(j)][x][y])

			if squares[aux[0]][aux[1]].piece.piece_type == 0 :
				squares[aux[0]][aux[1]].piece.image = squares[aux[0]][aux[1]].piece.imagen_transparente
			aux = []

	def get_score(self, squares, player) :

		score = 0

		for i in range(0,8) :

			for j in range (0,8) :

				if player == self.convert_to_turn(squares[i][j].piece.piece_type) :

					if squares[i][j].piece.piece_type == 1 or squares[i][j].piece.piece_type == 2:

						score += 1

					if squares[i][j].piece.piece_type == 11 or squares[i][j].piece.piece_type == 22:

						score += 3
		return score

	def end_game(self, puntacion) :

		if puntacion == 0 :

			return True

		return False
