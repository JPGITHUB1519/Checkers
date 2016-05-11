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
								

								juego.game_data_structure = partida_object.check_all_pieces_movement(juego.tablero.squares)
								juego.cond_comer, juego.comer_data_structure = juego.partida.have_to_eat(juego.game_data_structure, juego.tablero.squares, juego.turno)

								# if the piece click is in the data structure
								if (str(i) + str(j)) in juego.game_data_structure :

									# si le toca comer y
									if juego.cond_comer == True :
										juego.comer_data_structure_element = str(i) + str(j)
										# comio?
										if juego.comer_data_structure_element in juego.comer_data_structure :

											juego.comio = True

									# si no le toca comer no pregunta sobre eso
									if juego. cond_comer == False :

										if juego.seleccionado == False :

											if juego.turno == juego.tablero.squares[i][j].piece.piece_type :

												juego.comio = False
												#print juego.partida.have_to_eat(data_structure, juego.tablero.squares, 2)
												
												juego.seleccionado = True
												juego.factual = i
												juego.cactual = j
												juego.dic_elemento = str(i) + str(j)

												#print juego.game_data_structure["45"]
												#print "\n"
												continue
									else :
										# si comio -> juega
										if juego.seleccionado == False and juego.comio == True :

											if juego.turno == juego.tablero.squares[i][j].piece.piece_type :

												juego.comio = False
												#print juego.partida.have_to_eat(data_structure, juego.tablero.squares, 2)
												
												juego.seleccionado = True
												juego.factual = i
												juego.cactual = j
												juego.dic_elemento = str(i) + str(j)

												#print juego.game_data_structure["45"]
												#print "\n"
												continue


							if juego.seleccionado == True :

								juego.cond_play_well = False
								# recorrer saber si la posicion a mover esta en la estructura de datos
								if len(juego.game_data_structure[juego.dic_elemento]) > 1 :

									for moves in range(0, len(juego.game_data_structure[juego.dic_elemento])) :

										# preguntar si le toca comer
										if juego.game_data_structure[juego.dic_elemento][0] == True :
											if juego.game_data_structure[juego.dic_elemento][moves] == [i,j] :
													juego.partida.capture_piece(juego.tablero.squares, juego.factual, juego.cactual, i, j)
													juego.cond_play_well = True
													break

										if juego.game_data_structure[juego.dic_elemento][moves] == [i,j] :
											juego.partida.mover(juego.tablero.squares, juego.factual, juego.cactual, i,j, juego.game_data_structure)
							   				juego.cond_play_well = True
								juego.seleccionado = False

								if juego.cond_play_well  == True :
									# change the turns

									if juego.turno == 1 :

										juego.turno = 2
										break

									if juego.turno == 2 :

										juego.turno = 1


		juego.clock.tick(20)
		if juego.cond_main_game == True : 
			juego.main_game()

				
		pygame.display.update()

	pygame.quit()

main()