import pygame
import game
import piece
import board

pygame.init()

def main() :

	juego = game.Game()
	cond_game = True
	stri = ""
	while(juego.salir != True) :

		for event in pygame.event.get() :

			if event.type == pygame.QUIT :

				juego.salir = True

			if event.type == pygame.MOUSEBUTTONDOWN :

				if juego.cursor1.colliderect(juego.tablero.squares[0][0]) :
					
					print juego.tablero.squares[0][2]

		juego.clock.tick(20)
		
		if juego.cond_main_game == True : 
			juego.main_game()

		if cond_game == True :
			for i in range(0,8) :

				for j in range(0,8) :

					stri += " " + str(juego.tablero.squares[i][j].occupation)
				stri+= "\n"

			print stri
			cond_game = False

		pygame.display.update()

	pygame.quit()

main()