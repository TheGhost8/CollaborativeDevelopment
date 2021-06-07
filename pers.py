class Player():
	def __init__(self, new_x=0, new_y=0, new_size=20, new_speed=5, new_color='#FFFFFF', new_transparent_color='#000000'):
		self.x = new_x
		self.y = new_y
		self.size = new_size
		self.speed = new_speed
		self.color = new_color
		self.transparent_color = new_transparent_color
		self.vincible = False

	def set_coords(self, new_x, new_y):
		self.x = new_x
		self.y = new_y

	def check_vincible(self):
		return self.vincible

	def change_vincible(self, new_vincible):
		self.vincible = new_vincible

	def get_color(self):
		return self.color

	def get_transparent_color(self):
		return self.transparent_color

	def get_x(self):
		return self.x

	def set_x(self, new_x):
		self.x = new_x

	def get_y(self):
		return self.y

	def set_y(self, new_y):
		self.y = new_y

	def player_size(self):
		return self.size

	def move(self, command):
		if command == 'LEFT':
			self.x = self.x - self.speed

		if command == 'RIGHT':
			self.x = self.x + self.speed

		if command == 'UP':
			self.y = self.y - self.speed

		if command == 'DOWN':
			self.y = self.y + self.speed