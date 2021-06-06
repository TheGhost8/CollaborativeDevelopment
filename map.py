import tkinter as tk
import pers.py


class Map:
	PIXEL_SCREEN_WIDTH = 800
	PIXEL_SCREEN_HEIGHT = 600
	player1 = player()
	tiles_player1 = set()
	potential_tiles_player1 = set()
	player2 = player()
	tiles_player2 = set()
	potential_tiles_player2 = set()

	def coords_to_tiles(x, y)
		return (x / player1.size(), y / player1.size())

	def __init__(self):
		player1.set_coords(player1.size() * 3, player1.size() * 3)
		player1_tile = coords_to_tiles(player1.get_x(), player1.get_y())
		for i in range(player1_tile[0] - 1, player1_tile[0] + 2):
			for j in range(player1_tile[1] - 1, player1_tile[1] + 2):
				tiles_player1.add((i, j))

		player2.set_coords(player2.size() * 12, player2.size() * 12)
		player2_tile = coords_to_tiles(player2.get_x(), player2.get_y())
		for i in range(player2_tile - 1, player2_tile + 2):
			for j in range(player2_tile - 1, player2_tile + 2):
				tiles_player2.add((i, j))

	def refresh_tiles_player1(self):
		if player1.vincible():
			potential_tiles_player1.add(coords_to_tiles(player1.get_x(), player1.get_y()))
			potential_tiles_player1.add(coords_to_tiles(player1.get_x() + player1.size() - 1, player1.get_y()))
			potential_tiles_player1.add(coords_to_tiles(player1.get_x(), player1.get_y() + player1.size() - 1))
			potential_tiles_player1.add(coords_to_tiles(player1.get_x() + player1.size() - 1, player1.get_y() + player1.size() - 1))

	def refresh_tiles_player2(self):
		if player2.vincible():
			potential_tiles_player2.add(coords_to_tiles(player2.get_x(), player2.get_y()))
			potential_tiles_player2.add(coords_to_tiles(player2.get_x() + player2.size() - 1, player2.get_y()))
			potential_tiles_player2.add(coords_to_tiles(player2.get_x(), player2.get_y() + player2.size() - 1))
			potential_tiles_player2.add(coords_to_tiles(player2.get_x() + player2.size() - 1, player2.get_y() + player2.size() - 1))		

	def process_movement(self, key):
		if key == 'W':
			player1.move('UP')
			if (player1.get_y() < 0):
				player1.set_y(0)
			refresh_tiles_player1()
		elif key == 'D':
			player1.move('RIGHT')
			if (player1.get_x() + player1.size() > PIXEL_SCREEN_WIDTH):
				player1.set_x(PIXEL_SCREEN_WIDTH - player1.size())
			refresh_tiles_player1()
		elif key == 'S':
			player1.move('DOWN')
			if (player1.get_y() + player1.size() > PIXEL_SCREEN_HEIGHT):
				player1.set_y(PIXEL_SCREEN_HEIGHT - player1.size())
			refresh_tiles_player1()
		elif key == 'A':
			player1.move('LEFT')
			if (player1.get_x() < 0):
				player1.set_x(0)
			refresh_tiles_player1()
		elif key == 'ARROW_UP':
			player2.move('UP')
			if (player2.get_y() < 0):
				player2.set_y(0)
			refresh_tiles_player2()
		elif key == 'ARROW_RIGHT':
			player2.move('RIGHT')
			if (player2.get_x() + player2.size() > PIXEL_SCREEN_WIDTH):
				player2.set_x(PIXEL_SCREEN_WIDTH - player2.size())
			refresh_tiles_player2()
		elif key == 'ARROW_DOWN':
			player2.move('DOWN')
			if (player2.get_y() + player2.size() > PIXEL_SCREEN_HEIGHT):
				player2.set_y(PIXEL_SCREEN_HEIGHT - player2.size())
			refresh_tiles_player2()
		elif key == 'ARROW_LEFT':
			if (player2.get_x() < 0):
				player2.set_x(0)
			player2.move('LEFT')
			refresh_tiles_player2()