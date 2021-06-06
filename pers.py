import random

#подается номер игрока и размеры окна

class player():
	def __init__(self, master=None, number, characters):
		self.coords = [random.randint(0, characters[0]), random.randint(0, characters[1])]
		self.number = number
		#self.size = 20
		self.speed = 2  #замени


	def move(command):
		'''Знаки посмотри'''
		if command is 'left':
			self.coords[0] = self.coords[0] - self.speed

		if command is 'rigth':
			self.coords[0] = self.coords[0] + self.speed

		if command is 'up':
			self.coords[1] = self.coords[1] - self.speed

		if command is 'down':
			self.coords[1] = self.coords[1] + self.speed


	def return_color():
		if self.number == 1:
			return 'FF0000'
		else:
			return '00FF00'

	
	def return_coords():
		return self.coords


	def __del__(self):
