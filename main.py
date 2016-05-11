import pygame
import game
import piece
import board
import partida

pygame.init()

def main() :

    juego = game.Game()
    partida_object = partida.Partida()
    data_structure = {}
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
                                
                                if juego.seleccionado == False :

                                	if juego.turno == juego.tablero.squares[i][j].piece.piece_type :
	                                    data_structure = partida_object.check_all_pieces_movement(juego.tablero.squares)
	                                    #print juego.partida.have_to_eat(data_structure, juego.tablero.squares, 2)
	                                    juego.dic_elemento = str(i) + str(j)
	                                    juego.seleccionado = True
	                                    juego.factual = i
	                                    juego.cactual = j
	                                    #print data_structure["45"]
	                                    #print "\n"
	                                    continue

                            if juego.seleccionado == True :
                                # recorrer saber si la posicion a mover esta en la estructura de datos
                                if len(data_structure[juego.dic_elemento]) > 1 :

                                    for moves in range(0, len(data_structure[juego.dic_elemento])) :

                                        if data_structure[juego.dic_elemento][0] == True :
                                        	if data_structure[juego.dic_elemento][moves] == [i,j] :
                                        			juego.partida.capture_piece(juego.tablero.squares, juego.factual, juego.cactual, i, j)
                                        			break
                                        if data_structure[juego.dic_elemento][moves] == [i,j] :
                                            juego.partida.mover(juego.tablero.squares, juego.factual, juego.cactual, i,j, juego.game_data_structure)
                               
                                juego.seleccionado = False

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