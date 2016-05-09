import pygame

class Partida() :

	def __init__(self) :

		pass

	def mover(self,squares, f_actual, c_actual, f_prox, c_prox, data_structure) :

		aux_piece = squares[f_actual][c_actual].piece
		squares[f_actual][c_actual].piece = squares[f_prox][c_prox].piece
		squares[f_prox][c_prox].piece = aux_piece

		squares[f_prox][c_prox].occupation = squares[f_actual][c_actual].occupation
		squares[f_actual][c_actual].occupation = 0