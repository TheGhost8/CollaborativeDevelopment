import random

#подается номер игрока и размеры окна

class player():
	x = 0
	y = 0
	size = 20
	speed = 5
	color = '#FF0000'
	vincible = False

	def __init__(self, master=None, number, characters):
		pass
		#self.coords = [random.randint(0, characters[0]), random.randint(0, characters[1])]
		#self.number = number
		#self.size = 20
		#self.speed = 2  #замени


	def move(self, command):
		'''Знаки посмотри'''
		if command is 'LEFT':
			#self.coords[0] = self.coords[0] - self.speed
			x = x - speed

		if command is 'RIGHT':
			#self.coords[0] = self.coords[0] + self.speed
			x = x + speed

		if command is 'UP':
			#self.coords[1] = self.coords[1] - self.speed
			y = y - speed

		if command is 'DOWN':
			#self.coords[1] = self.coords[1] + self.speed
			y = y + speed


	def get_color(self):
		return color

	
	def get_x(self):
		return x

	def set_x(self, new_x):
		x = new_x

	def get_y(self):
		return y

	def set_y(self, new_y):
		y = new_y

	def size(self):
		return size