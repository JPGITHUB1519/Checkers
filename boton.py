import pygame

class Boton(pygame.sprite.Sprite) :

	def __init__(self, imagen1, imagen2, x = 200, y = 200) :

		self.imagen_normal = imagen1
		self.imagen_seleccion = imagen2
		self.rect = self.imagen_normal.get_rect()
		self.rect.left, self.rect.top = x,y 
		self.imagen_actual = self.imagen_normal

	def update(self, pantalla, cursor) :

		if cursor.colliderect(self.rect) :

			self.imagen_actual = self.imagen_seleccion

		else :

			self.imagen_actual = self.imagen_normal

		pantalla.blit(self.imagen_actual, self.rect)