"""head module - interface."""

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from map import Map
from clock import Clock
import gettext

gettext.install('interface', localedir='po')
"""Localization."""
# def _(a):
# return a


class Application(tk.Tk):
    """Class conteined all."""

    def __init__(self, master=None, title="Paper.io", **kwargs):
        """Create class."""
        self.field = Map()
        self.pause = False
        super().__init__(master, **kwargs)
        self.frame = tk.Frame(self)
        self.frame.pack()
        self.restart = tk.Button(self.frame, text=_("New game"), command=self.new_game, width=28, height=2).pack(side=tk.LEFT)
        self.info = tk.Button(self.frame, text=_("Information"), command=self.text_info, width=27, height=2).pack(side=tk.LEFT)
        self.exit = tk.Button(self.frame, text=_("Exit"), command=self.quit, width=28, height=2).pack(side=tk.LEFT)
        self.clock = Clock(self.frame).pack(side=tk.LEFT)

        self.buttons = [False for i in range(9)]
        self.click()
        self.window = tk.Frame(self)
        self.window.pack()
        self.canv = tk.Canvas(self.window, bg='#fff', width=800, height=600)
        self.canv.pack(side=tk.LEFT)
        self.new_game()

    def movement(self):
        """Movement."""
        if not self.pause:
            self.field.move_everything()
            self.draw_everything()
            self.after(33, self.movement)
            if (self.field.player1.check_win()):
                self.won()
            if (self.field.player2.check_win()):
                self.lose()

    def click(self):
        """Click some buttons."""
        self.bind_all('<KeyPress-p>', self.__p_handler)
        self.bind_all('<KeyPress-i>', self.text_info)
        self.bind_all('<KeyPress-n>', self.new_game)
        self.bind_all('<KeyPress-Escape>', self.escape_handler)

        self.bind_all('<KeyPress-a>', self.__a_handler)
        self.bind_all('<KeyPress-w>', self.__w_handler)
        self.bind_all('<KeyPress-s>', self.__s_handler)
        self.bind_all('<KeyPress-d>', self.__d_handler)
        self.bind_all('<KeyPress-Left>', self.__arrow_left_handler)
        self.bind_all('<KeyPress-Up>', self.__arrow_up_handler)
        self.bind_all('<KeyPress-Down>', self.__arrow_down_handler)
        self.bind_all('<KeyPress-Right>', self.__arrow_right_handler)

        self.bind_all('<KeyRelease-a>', self.__a_release)
        self.bind_all('<KeyRelease-w>', self.__w_release)
        self.bind_all('<KeyRelease-s>', self.__s_release)
        self.bind_all('<KeyRelease-d>', self.__d_release)
        self.bind_all('<KeyRelease-Left>', self.__arrow_left_release)
        self.bind_all('<KeyRelease-Up>', self.__arrow_up_release)
        self.bind_all('<KeyRelease-Down>', self.__arrow_down_release)
        self.bind_all('<KeyRelease-Right>', self.__arrow_right_release)

    def new_game(self, event=None):
        """Start new game."""
        self.field = Map()
        self.pause = False
        self.draw_everything()
        self.after(33, self.movement)

    def draw_everything(self):
        """Draw everything."""
        self.canv.delete('all')

        for i in self.field.get_tiles_player1():
            self.canv.create_rectangle(i[0] * self.field.player1.player_size(), i[1] * self.field.player1.player_size(), i[0] * self.field.player1.player_size() + self.field.player1.player_size(), i[1] * self.field.player1.player_size() + self.field.player1.player_size(), fill=self.field.player1.get_color(), outline=self.field.player1.get_color())
        for i in self.field.get_tiles_player2():
            self.canv.create_rectangle(i[0] * self.field.player2.player_size(), i[1] * self.field.player2.player_size(), i[0] * self.field.player2.player_size() + self.field.player2.player_size(), i[1] * self.field.player2.player_size() + self.field.player2.player_size(), fill=self.field.player2.get_color(), outline=self.field.player2.get_color())

        for i in self.field.get_potential_tiles_player1():
            self.canv.create_rectangle(i[0] * self.field.player1.player_size(), i[1] * self.field.player1.player_size(), i[0] * self.field.player1.player_size() + self.field.player1.player_size(), i[1] * self.field.player1.player_size() + self.field.player1.player_size(), fill=self.field.player1.get_transparent_color(), outline=self.field.player1.get_transparent_color())
        for i in self.field.get_potential_tiles_player2():
            self.canv.create_rectangle(i[0] * self.field.player2.player_size(), i[1] * self.field.player2.player_size(), i[0] * self.field.player2.player_size() + self.field.player2.player_size(), i[1] * self.field.player2.player_size() + self.field.player2.player_size(), fill=self.field.player2.get_transparent_color(), outline=self.field.player2.get_transparent_color())

        self.canv.create_rectangle(self.field.player1.get_x(), self.field.player1.get_y(), self.field.player1.get_x() + self.field.player1.player_size(), self.field.player1.get_y() + self.field.player1.player_size(), fill=self.field.player1.get_color())
        self.canv.create_rectangle(self.field.player2.get_x(), self.field.player2.get_y(), self.field.player2.get_x() + self.field.player2.player_size(), self.field.player2.get_y() + self.field.player2.player_size(), fill=self.field.player2.get_color())

    def escape_handler(self, event):
        """Escape handler."""
        self.quit()

    def __p_handler(self, event):
        """Pause control."""
        self.pause = not self.pause
        if not self.pause:
            self.after(33, self.movement)

        self.buttons[8] = not self.buttons[8]
        if self.buttons[8]:
            messagebox.showinfo(_('Pause'), _('Press <p> to continue'))
        self.check_buttons()

    def __a_handler(self, event):
        """A_handler."""
        self.buttons[0] = True
        self.check_buttons()

    def __w_handler(self, event):
        """W handler."""
        self.buttons[1] = True
        self.check_buttons()

    def __s_handler(self, event):
        """S handler."""
        self.buttons[2] = True
        self.check_buttons()

    def __d_handler(self, event):
        """D handler."""
        self.buttons[3] = True
        self.check_buttons()

    def __arrow_left_handler(self, event):
        """Left handler."""
        self.buttons[4] = True
        self.check_buttons()

    def __arrow_up_handler(self, event):
        """Up handler."""
        self.buttons[5] = True
        self.check_buttons()

    def __arrow_down_handler(self, event):
        """Down handler."""
        self.buttons[6] = True
        self.check_buttons()

    def __arrow_right_handler(self, event):
        """Right handler."""
        self.buttons[7] = True
        self.check_buttons()

    def __a_release(self, event):
        """A_release."""
        self.buttons[0] = False
        self.check_buttons()

    def __w_release(self, event):
        """W release."""
        self.buttons[1] = False
        self.check_buttons()

    def __s_release(self, event):
        """S release."""
        self.buttons[2] = False
        self.check_buttons()

    def __d_release(self, event):
        """D release."""
        self.buttons[3] = False
        self.check_buttons()

    def __arrow_left_release(self, event):
        """Left release."""
        self.buttons[4] = False
        self.check_buttons()

    def __arrow_up_release(self, event):
        """Up release."""
        self.buttons[5] = False
        self.check_buttons()

    def __arrow_down_release(self, event):
        """Down release."""
        self.buttons[6] = False
        self.check_buttons()

    def __arrow_right_release(self, event):
        """Right release."""
        self.buttons[7] = False
        self.check_buttons()

    def check_buttons(self):
        """Check buttons."""
        # print(self.buttons)
        if not self.buttons[8]:
            if self.buttons[0]:
                self.a_press()
            if self.buttons[1]:
                self.w_press()
            if self.buttons[2]:
                self.s_press()
            if self.buttons[3]:
                self.d_press()
            if self.buttons[4]:
                self.left_press()
            if self.buttons[5]:
                self.up_press()
            if self.buttons[6]:
                self.down_press()
            if self.buttons[7]:
                self.right_press()

    def a_press(self):
        """Press A."""
        self.field.process_movement('A')
        if (self.field.player1.check_win()):
            self.won()
        self.draw_everything()

    def w_press(self):
        """Press W."""
        self.field.process_movement('W')
        if (self.field.player1.check_win()):
            self.won()
        self.draw_everything()

    def s_press(self):
        """Press S."""
        self.field.process_movement('S')
        if (self.field.player1.check_win()):
            self.won()
        self.draw_everything()

    def d_press(self):
        """Press D."""
        self.field.process_movement('D')
        if (self.field.player1.check_win()):
            self.won()
        self.draw_everything()

    def left_press(self):
        """Press left."""
        self.field.process_movement('ARROW_LEFT')
        if (self.field.player2.check_win()):
            self.lose()
        self.draw_everything()

    def up_press(self):
        """Press Up."""
        self.field.process_movement('ARROW_UP')
        if (self.field.player2.check_win()):
            self.lose()
        self.draw_everything()

    def down_press(self):
        """Press down."""
        self.field.process_movement('ARROW_DOWN')
        if (self.field.player2.check_win()):
            self.lose()
        self.draw_everything()

    def right_press(self):
        """Press right."""
        self.field.process_movement('ARROW_RIGHT')
        if (self.field.player2.check_win()):
            self.lose()
        self.draw_everything()

    def text_info(self, event=None):
        """Text info."""
        messagebox.showinfo(_('Information'), _('"Esc" - exit the game.\n"p" - pause.\n"i" - show information window.\n"n" - new game.\nFirst player controls: "w", "a", "s", "d".\nSecond player controls: arrows.\n'))

    def won(self):
        """Win game."""
        self.pause = True
        messagebox.showinfo(_('End_game'), _('First player win!'))
        self.new_game()

    def lose(self):
        """Lose game."""
        self.pause = True
        messagebox.showinfo(_('End_game'), _('Second player win!'))
        self.new_game()


app = Application()
app.title('paper.io')
app.resizable(width=False, height=False)
app.mainloop()
