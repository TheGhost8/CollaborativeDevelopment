import tkinter as tk
from pers import Player


class Map:
	def coords_to_tiles(self, x, y):
		return (int(x / self.player1.player_size()), int(y / self.player1.player_size()))

	def __init__(self):
		self.PIXEL_SCREEN_WIDTH = 800
		self.PIXEL_SCREEN_HEIGHT = 600
		self.player1 = Player(new_color="#00FF00")
		self.tiles_player1 = set()
		self.potential_tiles_player1 = set()
		self.player2 = Player(new_color="#FF0000")
		self.tiles_player2 = set()
		self.potential_tiles_player2 = set()

		self.player1.set_coords(new_x=self.player1.player_size() * 3, new_y=self.player1.player_size() * 3)
		player1_tile = self.coords_to_tiles(self.player1.get_x(), self.player1.get_y())
		for i in range(player1_tile[0] - 1, player1_tile[0] + 2):
			for j in range(player1_tile[1] - 1, player1_tile[1] + 2):
				self.tiles_player1.add((i, j))

		self.player2.set_coords(self.player2.player_size() * 12, self.player2.player_size() * 12)
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

	def refresh_tiles_player1(self):
		if self.player1.vincible():
			self.potential_tiles_player1.add(coords_to_tiles(self.player1.get_x(), self.player1.get_y()))
			self.potential_tiles_player1.add(coords_to_tiles(self.player1.get_x() + self.player1.player_size() - 1, self.player1.get_y()))
			self.potential_tiles_player1.add(coords_to_tiles(self.player1.get_x(), self.player1.get_y() + self.player1.player_size() - 1))
			self.potential_tiles_player1.add(coords_to_tiles(self.player1.get_x() + self.player1.player_size() - 1, self.player1.get_y() + self.player1.player_size() - 1))

	def refresh_tiles_player2(self):
		if self.player2.vincible():
			self.potential_tiles_player2.add(coords_to_tiles(self.player2.get_x(), self.player2.get_y()))
			self.potential_tiles_player2.add(coords_to_tiles(self.player2.get_x() + self.player2.player_size() - 1, self.player2.get_y()))
			self.potential_tiles_player2.add(coords_to_tiles(self.player2.get_x(), self.player2.get_y() + self.player2.player_size() - 1))
			self.potential_tiles_player2.add(coords_to_tiles(self.player2.get_x() + self.player2.player_size() - 1, self.player2.get_y() + self.player2.player_size() - 1))		

	def process_movement(self, key):
		if key == 'W':
			self.player1.move('UP')
			if (self.player1.get_y() < 0):
				self.player1.set_y(0)
			self.refresh_tiles_player1()
		elif key == 'D':
			self.player1.move('RIGHT')
			if (self.player1.get_x() + self.player1.player_size() > self.PIXEL_SCREEN_WIDTH):
				self.player1.set_x(self.PIXEL_SCREEN_WIDTH - self.player1.player_size())
			self.refresh_tiles_player1()
		elif key == 'S':
			self.player1.move('DOWN')
			if (self.player1.get_y() + self.player1.player_size() > self.PIXEL_SCREEN_HEIGHT):
				self.player1.set_y(self.PIXEL_SCREEN_HEIGHT - self.player1.player_size())
			self.refresh_tiles_player1()
		elif key == 'A':
			self.player1.move('LEFT')
			if (self.player1.get_x() < 0):
				self.player1.set_x(0)
			self.refresh_tiles_player1()
		elif key == 'ARROW_UP':
			self.player2.move('UP')
			if (self.player2.get_y() < 0):
				self.player2.set_y(0)
			self.refresh_tiles_player2()
		elif key == 'ARROW_RIGHT':
			self.player2.move('RIGHT')
			if (self.player2.get_x() + self.player2.player_size() > self.PIXEL_SCREEN_WIDTH):
				self.player2.set_x(self.PIXEL_SCREEN_WIDTH - self.player2.player_size())
			self.refresh_tiles_player2()
		elif key == 'ARROW_DOWN':
			self.player2.move('DOWN')
			if (self.player2.get_y() + self.player2.player_size() > self.PIXEL_SCREEN_HEIGHT):
				self.player2.set_y(self.PIXEL_SCREEN_HEIGHT - self.player2.player_size())
			self.refresh_tiles_player2()
		elif key == 'ARROW_LEFT':
			self.player2.move('LEFT')
			if (self.player2.get_x() < 0):
				self.player2.set_x(0)
			self.refresh_tiles_player2()