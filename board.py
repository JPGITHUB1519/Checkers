import pygame


class Board() :

	def __init__ (self, color1, color2, x, y,width, height) :

		self.color1 = color1
		self.color2 = color2
		self.squares = [[],[],[],[],[],[],[],[]]
		self.width = width
		self.height = height
		self.xpos = x
		self.ypos = y	

		# initialize square

		for i in range(0,8) :

			for j in range(0,8) :

				self.squares[i].append(pygame.Rect(self.xpos, self.ypos, width, height))
				self.xpos += 65
			self.xpos = 0
			self.ypos += 65

		"""
		self.squares.append(pygame.Rect(x,y,width, height))
		self.squares.append(pygame.Rect(x + 65,y,width, height))
		self.squares.append(pygame.Rect(x,y + 65,width, height))
		"""
	def update(self, pantalla) :

		#pygame.draw.rect(pantalla,self.color1, self.squares[0])

		for i in range(0,8) :

			for j in range(0,8) :

				if i % 2 == 0 :

					if j % 2 == 0 :

						pygame.draw.rect(pantalla,self.color1, self.squares[i][j])

					else :

						pygame.draw.rect(pantalla, self.color2, self.squares[i][j])

				else :

					if j % 2 == 0 :

						pygame.draw.rect(pantalla, self.color2, self.squares[i][j])

					else :

						pygame.draw.rect(pantalla, self.color1, self.squares[i][j])







		

