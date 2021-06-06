
class Bot():
	def __init__(self, master=None, number, characters):
		self.coords = [random.randint(0, characters[0]), random.randint(0, characters[1])]
		self.number = number
		self.size = 20
		self.speed = 2  #замени
		self.last_coords = self.coords
		self.step = 1
		self.current = 0
		self.direction = 'rigth'
		self.flag = False


	def move():
		if self.flag:
			self.coords = self.last_coords
			self.flag = !self.flag
			return 'down'
		if self.current < self.step:
			if self.last_coords[0] == self.coords[0] and self.last_coords[1] == self.coords[1] + 1:
				self.last_coords, self.coords = self.coords , self.last_coords
				self.flag = True
				return 'up'
			self.current += 1
			if self.direction == 'rigth':
				self.coords[0] += self.size * self.speed
			if self.direction == 'up':
				self.coords[1] += self.size * self.speed
			if self.direction == 'left':
				self.coords[0] -= self.size * self.speed
			if self.direction == 'down':
				self.coords[1] -= self.size * self.speed
		else:
			self.current = 0
			if self.direction == 'rigth':
				self.coords[1] += self.size * self.speed
				self.direction = 'up'
			if self.direction == 'up':
				self.coords[0] -= self.size * self.speed
				self.direction = 'left'
			if self.direction == 'left':
				self.coords[1] -= self.size * self.speed
				self.direction = 'down'
			if self.direction == 'down':
				self.coords[0] += self.size * self.speed
				self.direction = 'rigth'
			return self.direction


	def return_color():
		if number == 1:
			return 'F00000'
		if number == 2:
			return '0F0000'
		if number == 3:
			return '00F000'
		if number == 4:
			return '000F00'
		if number == 5:
			return '0000F0'
		if number == 6:
			return '00000F'
