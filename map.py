"""module map."""

from pers import Player


class Map:
    """Class contein map of this game."""

    def coords_to_tiles(self, x, y):
        """Coords."""
        return (int(x / self.player1.player_size()), int(y / self.player1.player_size()))

    def __init__(self):
        """Create map."""
        self.PIXEL_SCREEN_WIDTH = 800
        self.PIXEL_SCREEN_HEIGHT = 600
        self.player1 = Player(new_color="#00FF00", new_transparent_color="#BBFFBB", start_direction='RIGHT')
        self.tiles_player1 = set()
        self.potential_tiles_player1 = set()
        self.player2 = Player(new_color="#FF0000", new_transparent_color="#FFBBBB", start_direction='LEFT')
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
        """Get tiles player1."""
        return self.tiles_player1

    def get_potential_tiles_player1(self):
        """Get potential tiles player1."""
        return self.potential_tiles_player1

    def get_tiles_player2(self):
        """Get tiles player2."""
        return self.tiles_player2

    def get_potential_tiles_player2(self):
        """Get potential tiles player2."""
        return self.potential_tiles_player2

    def update_player1(self):
        """Update player1."""
        invincible = (self.coords_to_tiles(self.player1.get_x(), self.player1.get_y()) in self.tiles_player1) or (self.coords_to_tiles(self.player1.get_x() + self.player1.player_size() - 1, self.player1.get_y()) in self.tiles_player1) or (self.coords_to_tiles(self.player1.get_x(), self.player1.get_y() + self.player1.player_size() - 1) in self.tiles_player1) or (self.coords_to_tiles(self.player1.get_x() + self.player1.player_size() - 1, self.player1.get_y() + self.player1.player_size() - 1) in self.tiles_player1)
        if (self.player1.check_vincible() and invincible):
            for y in range(0, int(self.PIXEL_SCREEN_HEIGHT / self.player1.player_size())):
                met_potential_tiles = 0
                met_colored_tiles = 0
                new_tiles_player1 = set()
                maybe_tiles_player1 = set()
                if (0, y) in self.tiles_player1:
                    met_colored_tiles += 1
                if (0, y) in self.potential_tiles_player1:
                    if ((1, y) not in self.potential_tiles_player1):
                        met_potential_tiles += 1
                    new_tiles_player1.add((0, y))
                for x in range(1, int(self.PIXEL_SCREEN_WIDTH / self.player1.player_size()) - 1):
                    if ((((x, y) in self.tiles_player1) and ((x - 1, y) not in self.tiles_player1)) or
                        (((x, y) in self.tiles_player1) and ((x + 1, y) not in self.tiles_player1))):
                        met_colored_tiles += 1
                        if (met_colored_tiles % 2 == 0):
                            new_tiles_player1 = new_tiles_player1 | maybe_tiles_player1
                            maybe_tiles_player1.clear()
                    if (((x, y) in self.potential_tiles_player1) and ((x - 1, y) in self.tiles_player1)):
                        met_colored_tiles = 0
                    if (((x, y) in self.tiles_player1) and ((x - 1, y) in self.potential_tiles_player1)):
                        met_potential_tiles = 0
                    if ((((x, y) in self.potential_tiles_player1) and ((x - 1, y) not in self.potential_tiles_player1) and ((x - 1, y) not in self.tiles_player1)) or
                        (((x, y) in self.potential_tiles_player1) and ((x + 1, y) not in self.potential_tiles_player1) and ((x + 1, y) not in self.tiles_player1) and
                                                                      ((x - 1, y) not in self.potential_tiles_player1))):
                        met_potential_tiles += 1
                        if ((met_colored_tiles > 0) and (met_colored_tiles % 2 == 0) and (met_potential_tiles == 1)):
                            new_tiles_player1 = new_tiles_player1 | maybe_tiles_player1
                            maybe_tiles_player1.clear()
                        if (met_potential_tiles % 2 == 0):
                            new_tiles_player1 = new_tiles_player1 | maybe_tiles_player1
                            maybe_tiles_player1.clear()
                    if ((met_colored_tiles > 0) and (met_colored_tiles % 2 == 0) and (met_potential_tiles == 0)):
                        maybe_tiles_player1.add((x, y))
                    if (((met_potential_tiles % 2 == 1) and (met_colored_tiles == 0)) or ((met_potential_tiles % 2 == 0) and (met_potential_tiles > 0) and (met_colored_tiles > 0))):
                        maybe_tiles_player1.add((x, y))
                    if ((x, y) in self.tiles_player1) or ((x, y) in self.potential_tiles_player1):
                        new_tiles_player1.add((x, y))

                if (((int(self.PIXEL_SCREEN_WIDTH / self.player1.player_size()) - 1, y) in self.potential_tiles_player1) or
                    ((int(self.PIXEL_SCREEN_WIDTH / self.player1.player_size()) - 1, y) in self.tiles_player1)):
                    new_tiles_player1 = new_tiles_player1 | maybe_tiles_player1
                    maybe_tiles_player1.clear()
                if ((int(self.PIXEL_SCREEN_WIDTH / self.player1.player_size()) - 1, y) in self.potential_tiles_player1):
                    new_tiles_player1.add((int(self.PIXEL_SCREEN_WIDTH / self.player1.player_size()) - 1, y))
                self.tiles_player1 = self.tiles_player1 | new_tiles_player1

            self.tiles_player2 = self.tiles_player2 - (self.tiles_player1 & self.tiles_player2)
            self.potential_tiles_player1.clear()
        self.player1.change_vincible(not invincible)
        if self.player1.check_vincible():
            self.potential_tiles_player1.add(self.coords_to_tiles(self.player1.get_x(), self.player1.get_y()))
            self.potential_tiles_player1.add(self.coords_to_tiles(self.player1.get_x() + self.player1.player_size() - 1, self.player1.get_y()))
            self.potential_tiles_player1.add(self.coords_to_tiles(self.player1.get_x(), self.player1.get_y() + self.player1.player_size() - 1))
            self.potential_tiles_player1.add(self.coords_to_tiles(self.player1.get_x() + self.player1.player_size() - 1, self.player1.get_y() + self.player1.player_size() - 1))
        if (len(self.tiles_player1 & self.potential_tiles_player2) != 0) or (len(self.potential_tiles_player1 & self.potential_tiles_player2) != 0):
            self.player1.change_win(True)

    def update_player2(self):
        """Update_player2."""
        invincible = (self.coords_to_tiles(self.player2.get_x(), self.player2.get_y()) in self.tiles_player2) or (self.coords_to_tiles(self.player2.get_x() + self.player2.player_size() - 1, self.player2.get_y()) in self.tiles_player2) or (self.coords_to_tiles(self.player2.get_x(), self.player2.get_y() + self.player2.player_size() - 1) in self.tiles_player2) or (self.coords_to_tiles(self.player2.get_x() + self.player2.player_size() - 1, self.player2.get_y() + self.player2.player_size() - 1) in self.tiles_player2)
        if (self.player2.check_vincible() and invincible):
            for y in range(0, int(self.PIXEL_SCREEN_HEIGHT / self.player2.player_size())):
                met_potential_tiles = 0
                met_colored_tiles = 0
                new_tiles_player2 = set()
                maybe_tiles_player2 = set()
                if (0, y) in self.tiles_player2:
                    met_colored_tiles += 1
                if (0, y) in self.potential_tiles_player2:
                    if ((1, y) not in self.potential_tiles_player2):
                        met_potential_tiles += 1
                    new_tiles_player2.add((0, y))
                for x in range(1, int(self.PIXEL_SCREEN_WIDTH / self.player2.player_size()) - 1):
                    if ((((x, y) in self.tiles_player2) and ((x - 1, y) not in self.tiles_player2)) or
                        (((x, y) in self.tiles_player2) and ((x + 1, y) not in self.tiles_player2))):
                        met_colored_tiles += 1
                        if (met_colored_tiles % 2 == 0):
                            new_tiles_player2 = new_tiles_player2 | maybe_tiles_player2
                            maybe_tiles_player2.clear()
                    if (((x, y) in self.potential_tiles_player2) and ((x - 1, y) in self.tiles_player2)):
                        met_colored_tiles = 0
                    if (((x, y) in self.tiles_player2) and ((x - 1, y) in self.potential_tiles_player2)):
                        met_potential_tiles = 0
                    if ((((x, y) in self.potential_tiles_player2) and ((x - 1, y) not in self.potential_tiles_player2) and ((x - 1, y) not in self.tiles_player2)) or
                        (((x, y) in self.potential_tiles_player2) and ((x + 1, y) not in self.potential_tiles_player2) and ((x + 1, y) not in self.tiles_player2) and
                                                                      ((x - 1, y) not in self.potential_tiles_player2))):
                        met_potential_tiles += 1
                        if ((met_colored_tiles > 0) and (met_colored_tiles % 2 == 0) and (met_potential_tiles == 1)):
                            new_tiles_player2 = new_tiles_player2 | maybe_tiles_player2
                            maybe_tiles_player2.clear()
                        if (met_potential_tiles % 2 == 0):
                            new_tiles_player2 = new_tiles_player2 | maybe_tiles_player2
                            maybe_tiles_player2.clear()
                    if ((met_colored_tiles > 0) and (met_colored_tiles % 2 == 0) and (met_potential_tiles == 0)):
                        maybe_tiles_player2.add((x, y))
                    if (((met_potential_tiles % 2 == 1) and (met_colored_tiles == 0)) or ((met_potential_tiles % 2 == 0) and (met_potential_tiles > 0) and (met_colored_tiles > 0))):
                        maybe_tiles_player2.add((x, y))
                    if ((x, y) in self.tiles_player2) or ((x, y) in self.potential_tiles_player2):
                        new_tiles_player2.add((x, y))

                if (((int(self.PIXEL_SCREEN_WIDTH / self.player2.player_size()) - 1, y) in self.potential_tiles_player2) or
                    ((int(self.PIXEL_SCREEN_WIDTH / self.player2.player_size()) - 1, y) in self.tiles_player2)):
                    new_tiles_player2 = new_tiles_player2 | maybe_tiles_player2
                    maybe_tiles_player2.clear()
                if ((int(self.PIXEL_SCREEN_WIDTH / self.player2.player_size()) - 1, y) in self.potential_tiles_player2):
                    new_tiles_player2.add((int(self.PIXEL_SCREEN_WIDTH / self.player2.player_size()) - 1, y))
                self.tiles_player2 = self.tiles_player2 | new_tiles_player2

            self.tiles_player1 = self.tiles_player1 - (self.tiles_player2 & self.tiles_player1)
            self.potential_tiles_player2.clear()
        self.player2.change_vincible(not invincible)
        if self.player2.check_vincible():
            self.potential_tiles_player2.add(self.coords_to_tiles(self.player2.get_x(), self.player2.get_y()))
            self.potential_tiles_player2.add(self.coords_to_tiles(self.player2.get_x() + self.player2.player_size() - 1, self.player2.get_y()))
            self.potential_tiles_player2.add(self.coords_to_tiles(self.player2.get_x(), self.player2.get_y() + self.player2.player_size() - 1))
            self.potential_tiles_player2.add(self.coords_to_tiles(self.player2.get_x() + self.player2.player_size() - 1, self.player2.get_y() + self.player2.player_size() - 1))
        if (len(self.tiles_player2 & self.potential_tiles_player1) != 0) or (len(self.potential_tiles_player2 & self.potential_tiles_player1) != 0):
            self.player2.change_win(True)

    def process_movement(self, key):
        """Process_movement."""
        if key == 'W':
            self.player1.set_direction('UP')
        elif key == 'D':
            self.player1.set_direction('RIGHT')
        elif key == 'S':
            self.player1.set_direction('DOWN')
        elif key == 'A':
            self.player1.set_direction('LEFT')
        elif key == 'ARROW_UP':
            self.player2.set_direction('UP')
        elif key == 'ARROW_RIGHT':
            self.player2.set_direction('RIGHT')
        elif key == 'ARROW_DOWN':
            self.player2.set_direction('DOWN')
        elif key == 'ARROW_LEFT':
            self.player2.set_direction('LEFT')

    def move_everything(self):
        self.player1.move()
        if (self.player1.get_x() < 0):
            self.player1.set_x(0)
        if (self.player1.get_x() + self.player1.player_size() > self.PIXEL_SCREEN_WIDTH):
            self.player1.set_x(self.PIXEL_SCREEN_WIDTH - self.player1.player_size())
        if (self.player1.get_y() < 0):
            self.player1.set_y(0)
        if (self.player1.get_y() + self.player1.player_size() > self.PIXEL_SCREEN_HEIGHT):
            self.player1.set_y(self.PIXEL_SCREEN_HEIGHT - self.player1.player_size())
        self.update_player1()

        self.player2.move()
        if (self.player2.get_x() < 0):
            self.player2.set_x(0)
        if (self.player2.get_x() + self.player2.player_size() > self.PIXEL_SCREEN_WIDTH):
            self.player2.set_x(self.PIXEL_SCREEN_WIDTH - self.player2.player_size())
        if (self.player2.get_y() < 0):
            self.player2.set_y(0)
        if (self.player2.get_y() + self.player2.player_size() > self.PIXEL_SCREEN_HEIGHT):
            self.player2.set_y(self.PIXEL_SCREEN_HEIGHT - self.player2.player_size())
        self.update_player2()
