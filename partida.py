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

	def check_movement(self,piece, f_actual, c_actual, f_prox, c_prox) :

		if self.check_ispiece(piece) :

			if self.check_piece_type(piece) == 1 :
				
				if not(f_prox == f_actual - 1 and c_prox in self.check_diagonal(f_actual, c_actual)) :

					return False

			if self.check_piece_type(piece) == 2 :

				if not(f_prox == f_actual + 1 and c_prox in self.check_diagonal(f_actual, c_actual)) :

					return False
		else :

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






		