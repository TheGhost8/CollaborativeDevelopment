"""module clock."""

import tkinter
import time


class Clock(tkinter.Label):
    """Class that contains the clock widget and clock refresh."""

    def __init__(self, parent=None, seconds=True, colon=False):
        """Create and place the clock widget into the parent element."""
        tkinter.Label.__init__(self, parent)
        self.display_seconds = seconds
        if self.display_seconds:
            self.time = time.strftime('%H:%M:%S')
        else:
            self.time = time.strftime('%I:%M %p').lstrip('0')
        self.display_time = self.time
        self.configure(text=self.display_time)

        if colon:
            self.blink_colon()

        self.after(200, self.tick)

    def tick(self):
        """Update the display clock every 200 milliseconds."""
        if self.display_seconds:
            new_time = time.strftime('%H:%M:%S')
        else:
            new_time = time.strftime('%I:%M %p').lstrip('0')
        if new_time != self.time:
            self.time = new_time
            self.display_time = self.time
            self.config(text=self.display_time)
        self.after(200, self.tick)

    def blink_colon(self):
        """Blink the colon every second."""
        if ':' in self.display_time:
            self.display_time = self.display_time.replace(':', ' ')
        else:
            self.display_time = self.display_time.replace(' ', ':', 1)
        self.config(text=self.display_time)
        self.after(1000, self.blink_colon)
