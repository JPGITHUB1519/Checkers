import pygame
import game

pygame.init()

def main() :

	juego = game.Game()

	while(juego.salir != True) :

		for event in pygame.event.get() :

			if event.type == pygame.QUIT :

				juego.salir = True


		juego.clock.tick(20)
		juego.pantalla.fill((255,255,255))
		pygame.display.update()

	pygame.quit()

main()