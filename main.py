import pygame
import game
import piece
import board
import partida

pygame.init()

def main() :

	juego = game.Game()
	partida_object = partida.Partida()


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

									juego.pos_comer = partida_object.check_can_eat(juego.tablero.squares, i, j)
									if len(juego.pos_comer) > 0 :
										juego.cond_comer = True
										print "Puede Comer! " + str(juego.pos_comer[0]) + str(juego.pos_comer[1])
									#print ("[" + str(i) + "][" + str(j) + "]")
									juego.seleccionado = True
									juego.factual = i
									juego.cactual = j
									continue

							if juego.seleccionado == True :
								
								if juego.partida.check_movement(juego.tablero.squares,juego.factual, juego.cactual,i,j) == True :
									juego.partida.mover(juego.tablero.squares, juego.factual, juego.cactual, i,j, juego.game_data_structure)
									print "exito"
								juego.seleccionado = False
								#print str(juego.factual) + " " + str(juego.cactual)
								#print str(i) + " " + str(j)
								#juego.tablero.squares[juego.factual][juego.cactual].piece.image = juego.tablero.squares[juego.factual][juego.cactual].piece.imagen_transparente
								#juego.tablero.squares[i][j].piece.image = juego.tablero.squares[juego.factual][juego.cactual].piece.imagen_pieza_roja

		juego.clock.tick(20)
		
		if juego.cond_main_game == True : 
			juego.main_game()

		pygame.display.update()

	pygame.quit()

main()