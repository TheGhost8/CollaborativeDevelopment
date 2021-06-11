pers
===================
.. automodule:: pers
   :members:
   :private-members:


class Player:
	class that conteins player and its methods.

methods:
	def __init__(self, new_x=0, new_y=0, new_size=20, new_speed=5, new_color='#FFFFFF', new_transparent_color='#000000', start_direction='UP') - Create player.

	def check_win(self)  -  Check win.

	def change_win(self, new_win)  -  Change win.

	def check_vincible(new_win)  - Check_vincible.

	def get_color(self)  -  Get color.

	def get_transparent_color(self)  -  Get transparent color.

	def set_direction(self, new_new_direction)  -  Set direction.

	def set_coords(self, new_x, new_y)  -  Set coords.

	def get_x(self)  -  Get x.

	def set_x(self, new_x)  -  Set x.

	def player_size(self)  -  Player size.

	def move(self)  -  Move.
