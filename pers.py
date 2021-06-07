class Player():
	x = 0
	y = 0
	size = 20
	speed = 5
	color = '#FF0000'
	vincible = False

	def __init__(self, new_x=0, new_y=0, new_size=20, new_speed=5, new_color='#FF0000'):
		x = new_x
		y = new_y
		size = new_size
		speed = new_speed
		color = new_color

	def set_coords(new_x, new_y):
		x = new_x
		y = new_y

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

	def move(self, command):
		if command is 'LEFT':
			x = x - speed

		if command is 'RIGHT':
			x = x + speed

		if command is 'UP':
			y = y - speed

		if command is 'DOWN':
			y = y + speed