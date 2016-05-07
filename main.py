import pygame
import game
import piece
import board

pygame.init()

def main() :

	juego = game.Game()

	while(juego.salir != True) :

		for event in pygame.event.get() :

			if event.type == pygame.QUIT :

				juego.salir = True

			if event.type == pygame.MOUSEBUTTONDOWN :

				if juego.cursor1.colliderect(juego.tablero.squares[0][5]) :
					pass

		juego.clock.tick(20)
		
		if juego.cond_main_game == True : 
			juego.main_game()

		pygame.display.update()

	pygame.quit()

main()