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
		print squares[f_prox][c_prox].piece.piece_type
		print squares[f_prox][c_prox].occupation

		squares[f_prox][c_prox].piece.image = squares[f_actual][c_actual].piece.image
		squares[f_actual][c_actual].piece.image = squares[f_actual][c_actual].piece.imagen_transparente
	
		squares[f_prox][c_prox].occupation = squares[f_actual][c_actual].occupation
		squares[f_actual][c_actual].occupation = 0

		squares[f_prox][c_prox].piece.piece_type = squares[f_actual][c_actual].piece.piece_type
		squares[f_actual][c_actual].piece.piece_type = 0

		print squares[f_prox][c_prox].piece.piece_type
		print squares[f_prox][c_prox].occupation
	





		