import pygame
import game
import piece
import board
import partida

pygame.init()

def main() :

	juego = game.Game()
	partida_object = partida.Partida()
	cond = False

	while(juego.salir != True) :

		for event in pygame.event.get() :

			if event.type == pygame.QUIT :

				juego.salir = True

			if event.type == pygame.MOUSEBUTTONDOWN :

				for i in range(0,8) :

					for j in range(0,8) :

						if juego.cursor1.colliderect(juego.tablero.squares[i][j]) :

							# check if clic a piece
							if partida_object.check_is_occupied(juego.tablero.squares, i, j) == True :
								
								# save all posibles movements
								juego.game_data_structure = partida_object.check_all_pieces_movement(juego.tablero.squares)
								juego.cond_comer, juego.comer_data_structure = juego.partida.have_to_eat(juego.game_data_structure, juego.tablero.squares, juego.turno)
					
								#print juego.comer_data_structure

								# si hay alguna pieza que le toca comer multiple
								if juego.cond_comer_multiple == True :
									# si la pieza seleccionada es la que tiene que comer
									if i == juego.f_comer_multiple and j == juego.c_comer_multiple :

										if juego.seleccionado == False :

											if juego.turno == juego.partida.convert_to_turn(juego.tablero.squares[i][j].piece.piece_type) :

												#print juego.partida.have_to_eat(data_structure, juego.tablero.squares, 2)
												em
												juego.seleccionado = True
												juego.factual = i
												juego.cactual = j
												juego.dic_elemento = str(i) + str(j)

												#print juego.game_data_structure["45"]
												#print "\n"
												continue 


								# hay alguna pieza que tenga que comer?
								if juego.cond_comer == True  :

									if (str(i) + str(j)) in juego.comer_data_structure :

										if juego.seleccionado == False :

											if juego.turno == juego.partida.convert_to_turn(juego.tablero.squares[i][j].piece.piece_type) :

												#print juego.partida.have_to_eat(data_structure, juego.tablero.squares, 2)
												
												juego.seleccionado = True
												juego.factual = i
												juego.cactual = j
												juego.dic_elemento = str(i) + str(j)

												#print juego.game_data_structure["45"]
												#print "\n"
												continue 

								# si no tiene que comer juega normal
								else : 
								# if the piece click is in the data structure
									if (str(i) + str(j)) in juego.game_data_structure :

										if juego.seleccionado == False :

											if juego.turno == juego.partida.convert_to_turn(juego.tablero.squares[i][j].piece.piece_type) :

												#print juego.partida.have_to_eat(data_structure, juego.tablero.squares, 2)
												
												juego.seleccionado = True
												juego.factual = i
												juego.cactual = j
												juego.dic_elemento = str(i) + str(j)

												#print juego.game_data_structure["45"]
												#print "\n"
												continue 

							# to see if click a piece no has movement
							# clickeo en un cuadro vacio?
							if juego.tablero.squares[i][j].piece.piece_type == 0 :
							#if len(juego.game_data_structure[str(i) + str(j)]) == 0 :

								if juego.seleccionado == True :

									#print juego.game_data_structure
									#print "\n"
									juego.cond_play_well = False
									# recorrer saber si la posicion a mover esta en la estructura de datos
									if len(juego.game_data_structure[juego.dic_elemento]) > 1 :

										for moves in range(0, len(juego.game_data_structure[juego.dic_elemento])) :

											# preguntar si le toca comer
											if juego.game_data_structure[juego.dic_elemento][0] == True :

												if juego.game_data_structure[juego.dic_elemento][moves] == [i,j] :

														print juego.comer_multiple_cond
														if juego.cond_comer_multiple == False :
															juego.partida.capture_piece(juego.tablero.squares, juego.factual, juego.cactual, i, j)
														else :
															juego.partida.capture_piece(juego.tablero.squares, juego.f_comer_multiple, juego.c_comer_multiple, i, j, True)

														juego.cond_play_well = True

														# here ask if the same pieza have to eat again
														# here i can ask as king
														juego.aux_game_data_structure = juego.partida.check_all_pieces_movement(juego.tablero.squares, True)
														juego.aux_comer_data_structure = juego.partida.have_to_eat(juego.aux_game_data_structure, juego.tablero.squares, juego.turno)[1]
														print juego.aux_comer_data_structure
														# ver si la pieza actual puede capturar
														juego.comer_multiple_cond = juego.partida.piece_have_to_eat(juego.aux_comer_data_structure,juego.tablero.squares,i,j)[0]
														juego.f_comer_multiple = i
														juego.c_comer_multiple = j
														
														#if have to eat again cannot change of turn
														if juego.comer_multiple_cond == True :

															juego.cond_play_well = False
  
														break

											if juego.game_data_structure[juego.dic_elemento][moves] == [i,j] :
												juego.partida.mover(juego.tablero.squares, juego.factual, juego.cactual, i,j, juego.game_data_structure)
								   				juego.cond_play_well = True

								   	# become the player 1 piece  king
					   				if juego.tablero.squares[i][j].piece.piece_type == 1 and juego.tablero.squares[i][j].piece.isking == False :

						   				if i == 0 :

						   					juego.partida.become_king(juego.turno, juego.tablero.squares, i, j)
						   					
					   				# become the player 2 piece  king
					   				if juego.tablero.squares[i][j].piece.piece_type == 2 and juego.tablero.squares[i][j].piece.isking == False :

					   					if i == 7 :
						   					juego.partida.become_king(juego.turno, juego.tablero.squares, i, j)


						   			#print juego.tablero.get_string_data_structure() + "\n"

									juego.seleccionado = False

									if juego.cond_play_well  == True :

										# change the turns

										if juego.turno == 1 :

											juego.turno = 2
											continue

										if juego.turno == 2 :

											juego.turno = 1

							else :

								if juego.turno == juego.partida.convert_to_turn(juego.tablero.squares[i][j].piece.piece_type) :

									if juego.cond_comer == True  :

										if str(i) + str(j) in juego.comer_data_structure  :

											# if clicked a valid piece assign it as selected
											juego.seleccionado = True
											juego.factual, juego.cactual = i, j
											juego.dic_elemento = str(i) + str(j)

									else :
										juego.seleccionado = True
										juego.factual, juego.cactual = i, j
										juego.dic_elemento = str(i) + str(j)

		juego.clock.tick(20)
		if juego.cond_main_game == True : 
			juego.main_game()

		pygame.display.update()

	pygame.quit()

main()