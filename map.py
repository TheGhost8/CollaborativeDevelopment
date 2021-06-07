import tkinter as tk
from pers import Player


class Map:
	def coords_to_tiles(self, x, y):
		return (int(x / self.player1.player_size()), int(y / self.player1.player_size()))

	def __init__(self):
		self.PIXEL_SCREEN_WIDTH = 800
		self.PIXEL_SCREEN_HEIGHT = 600
		self.player1 = Player(new_color="#00FF00", new_transparent_color="#BBFFBB")
		self.tiles_player1 = set()
		self.potential_tiles_player1 = set()
		self.player2 = Player(new_color="#FF0000", new_transparent_color="#FFBBBB")
		self.tiles_player2 = set()
		self.potential_tiles_player2 = set()

		self.player1.set_coords(new_x=self.player1.player_size() * 3, new_y=self.player1.player_size() * 3)
		player1_tile = self.coords_to_tiles(self.player1.get_x(), self.player1.get_y())
		for i in range(player1_tile[0] - 1, player1_tile[0] + 2):
			for j in range(player1_tile[1] - 1, player1_tile[1] + 2):
				self.tiles_player1.add((i, j))

		self.player2.set_coords(self.player2.player_size() * ((self.PIXEL_SCREEN_WIDTH / self.player1.player_size()) - 3), self.player2.player_size() * ((self.PIXEL_SCREEN_HEIGHT / self.player1.player_size()) - 3))
		player2_tile = self.coords_to_tiles(self.player2.get_x(), self.player2.get_y())
		for i in range(player2_tile[0] - 1, player2_tile[0] + 2):
			for j in range(player2_tile[1] - 1, player2_tile[1] + 2):
				self.tiles_player2.add((i, j))

	def get_tiles_player1(self):
		return self.tiles_player1

	def get_potential_tiles_player1(self):
		return self.potential_tiles_player1

	def get_tiles_player2(self):
		return self.tiles_player2

	def get_potential_tiles_player2(self):
		return self.potential_tiles_player2

	def update_player1(self):
		invincible = (self.coords_to_tiles(self.player1.get_x(), self.player1.get_y()) in self.tiles_player1) or (self.coords_to_tiles(self.player1.get_x() + self.player1.player_size() - 1, self.player1.get_y()) in self.tiles_player1) or (self.coords_to_tiles(self.player1.get_x(), self.player1.get_y() + self.player1.player_size() - 1) in self.tiles_player1) or (self.coords_to_tiles(self.player1.get_x() + self.player1.player_size() - 1, self.player1.get_y() + self.player1.player_size() - 1) in self.tiles_player1)
		if (self.player1.check_vincible() == True and invincible == True):
			min_tile = min(self.potential_tiles_player1)
			max_tile = max(self.potential_tiles_player1)
			for x in range(min_tile[0], max_tile[0] + 1):
				for y in range(min_tile[1], max_tile[1] + 1):
					self.tiles_player1.add((x, y))
					if ((x,y) in self.potential_tiles_player1):
						self.potential_tiles_player1.remove((x, y))
		self.player1.change_vincible(not invincible)
		if self.player1.check_vincible():
			self.potential_tiles_player1.add(self.coords_to_tiles(self.player1.get_x(), self.player1.get_y()))
			self.potential_tiles_player1.add(self.coords_to_tiles(self.player1.get_x() + self.player1.player_size() - 1, self.player1.get_y()))
			self.potential_tiles_player1.add(self.coords_to_tiles(self.player1.get_x(), self.player1.get_y() + self.player1.player_size() - 1))
			self.potential_tiles_player1.add(self.coords_to_tiles(self.player1.get_x() + self.player1.player_size() - 1, self.player1.get_y() + self.player1.player_size() - 1))
		if (len(self.tiles_player1 & self.potential_tiles_player2) != 0) or (len(self.potential_tiles_player1 & self.potential_tiles_player2) != 0):
			self.player1.change_win(True)


	def update_player2(self):
		invincible = (self.coords_to_tiles(self.player2.get_x(), self.player2.get_y()) in self.tiles_player2) or (self.coords_to_tiles(self.player2.get_x() + self.player2.player_size() - 1, self.player2.get_y()) in self.tiles_player2) or (self.coords_to_tiles(self.player2.get_x(), self.player2.get_y() + self.player2.player_size() - 1) in self.tiles_player2) or (self.coords_to_tiles(self.player2.get_x() + self.player2.player_size() - 1, self.player2.get_y() + self.player2.player_size() - 1) in self.tiles_player2)
		if (self.player2.check_vincible() == True and invincible == True):
			min_tile = min(self.potential_tiles_player2)
			max_tile = max(self.potential_tiles_player2)
			for x in range(min_tile[0], max_tile[0] + 1):
				for y in range(min_tile[1], max_tile[1] + 1):
					self.tiles_player2.add((x, y))
					if ((x,y) in self.potential_tiles_player2):
						self.potential_tiles_player2.remove((x, y))
		self.player2.change_vincible(not invincible)
		if self.player2.check_vincible():
			self.potential_tiles_player2.add(self.coords_to_tiles(self.player2.get_x(), self.player2.get_y()))
			self.potential_tiles_player2.add(self.coords_to_tiles(self.player2.get_x() + self.player2.player_size() - 1, self.player2.get_y()))
			self.potential_tiles_player2.add(self.coords_to_tiles(self.player2.get_x(), self.player2.get_y() + self.player2.player_size() - 1))
			self.potential_tiles_player2.add(self.coords_to_tiles(self.player2.get_x() + self.player2.player_size() - 1, self.player2.get_y() + self.player2.player_size() - 1))
		if (len(self.tiles_player2 & self.potential_tiles_player1) != 0) or (len(self.potential_tiles_player2 & self.potential_tiles_player1) != 0):
			self.player2.change_win(True)

	def process_movement(self, key):
		if key == 'W':
			self.player1.move('UP')
			if (self.player1.get_y() < 0):
				self.player1.set_y(0)
			self.update_player1()
		elif key == 'D':
			self.player1.move('RIGHT')
			if (self.player1.get_x() + self.player1.player_size() > self.PIXEL_SCREEN_WIDTH):
				self.player1.set_x(self.PIXEL_SCREEN_WIDTH - self.player1.player_size())
			self.update_player1()
		elif key == 'S':
			self.player1.move('DOWN')
			if (self.player1.get_y() + self.player1.player_size() > self.PIXEL_SCREEN_HEIGHT):
				self.player1.set_y(self.PIXEL_SCREEN_HEIGHT - self.player1.player_size())
			self.update_player1()
		elif key == 'A':
			self.player1.move('LEFT')
			if (self.player1.get_x() < 0):
				self.player1.set_x(0)
			self.update_player1()
		elif key == 'ARROW_UP':
			self.player2.move('UP')
			if (self.player2.get_y() < 0):
				self.player2.set_y(0)
			self.update_player2()
		elif key == 'ARROW_RIGHT':
			self.player2.move('RIGHT')
			if (self.player2.get_x() + self.player2.player_size() > self.PIXEL_SCREEN_WIDTH):
				self.player2.set_x(self.PIXEL_SCREEN_WIDTH - self.player2.player_size())
			self.update_player2()
		elif key == 'ARROW_DOWN':
			self.player2.move('DOWN')
			if (self.player2.get_y() + self.player2.player_size() > self.PIXEL_SCREEN_HEIGHT):
				self.player2.set_y(self.PIXEL_SCREEN_HEIGHT - self.player2.player_size())
			self.update_player2()
		elif key == 'ARROW_LEFT':
			self.player2.move('LEFT')
			if (self.player2.get_x() < 0):
				self.player2.set_x(0)
			self.update_player2()