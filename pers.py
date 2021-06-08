"""module player."""


class Player():
    """class that conteins player and its methods."""

    def __init__(self, new_x=0, new_y=0, new_size=20, new_speed=5, new_color='#FFFFFF', new_transparent_color='#000000'):
        """Create player."""
        self.x = new_x
        self.y = new_y
        self.size = new_size
        self.speed = new_speed
        self.color = new_color
        self.transparent_color = new_transparent_color
        self.vincible = False
        self.win = False

    def check_win(self):
        """Check win."""
        return self.win

    def change_win(self, new_win):
        """Change win."""
        self.win = new_win

    def check_vincible(self):
        """Check vincible."""
        return self.vincible

    def change_vincible(self, new_vincible):
        """Change vincible."""
        self.vincible = new_vincible

    def get_color(self):
        """Get color."""
        return self.color

    def get_transparent_color(self):
        """Get transparent color."""
        return self.transparent_color

    def set_coords(self, new_x, new_y):
        """Set coords."""
        self.x = new_x
        self.y = new_y

    def get_x(self):
        """Get x."""
        return self.x

    def set_x(self, new_x):
        """Set x."""
        self.x = new_x

    def get_y(self):
        """Get y."""
        return self.y

    def set_y(self, new_y):
        """Set y."""
        self.y = new_y

    def player_size(self):
        """Player size."""
        return self.size

    def move(self, command):
        """Move."""
        if command == 'LEFT':
            self.x = self.x - self.speed
        if command == 'RIGHT':
            self.x = self.x + self.speed
        if command == 'UP':
            self.y = self.y - self.speed
        if command == 'DOWN':
            self.y = self.y + self.speed
