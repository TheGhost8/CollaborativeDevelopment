from tkinter import *
import tkinter as tk
from tkinter import messagebox
from map import Map


class Application(tk.Tk):
    def __init__(self, master=None, title="Paper.io", **kwargs):
        self.field = Map()
        super().__init__(master, **kwargs)
        self.frame = Frame(self)
        self.frame.pack()
        self.restart = Button(self.frame ,text = "New game", command = self.new_game, width=30, height=2).pack(side=LEFT)
        self.info = Button(self.frame , text = "Information", command = self.text_info, width=30, height=2).pack(side=LEFT)
        self.exit = Button(self.frame ,  text = "Exit", command = self.quit, width=30, height=2).pack(side=LEFT)

        self.bind_all('<KeyPress-a>', self.__a_handler)
        self.bind_all('<KeyPress-w>', self.__w_handler)
        self.bind_all('<KeyPress-s>', self.__s_handler)
        self.bind_all('<KeyPress-d>', self.__d_handler)
        self.bind_all('<KeyPress-Left>', self.__arrow_left_handler)
        self.bind_all('<KeyPress-Up>', self.__arrow_up_handler)
        self.bind_all('<KeyPress-Down>', self.__arrow_down_handler)
        self.bind_all('<KeyPress-Right>', self.__arrow_right_handler)

        self.window = Frame(self)
        self.window.pack()
        self.canv = tk.Canvas(self.window, bg='#fff', width=800, height=600)
        self.canv.pack(side=LEFT)
        self.new_game()
        

    def new_game(self):
        self.draw_everything()


    def draw_everything(self):
        self.canv.delete('all')

        for i in self.field.get_tiles_player1():
            self.canv.create_rectangle(i[0]*self.field.player1.player_size(), i[1]*self.field.player1.player_size(), i[0]*self.field.player1.player_size() + self.field.player1.player_size(), i[1]*self.field.player1.player_size() + self.field.player1.player_size(), fill=self.field.player1.get_color(), outline=self.field.player1.get_color())
        for i in self.field.get_potential_tiles_player1():
            self.canv.create_rectangle(i[0]*self.field.player1.player_size(), i[1]*self.field.player1.player_size(), i[0]*self.field.player1.player_size() + self.field.player1.player_size(), i[1]*self.field.player1.player_size() + self.field.player1.player_size(), fill=self.field.player1.get_transparent_color(), outline=self.field.player1.get_transparent_color())
        self.canv.create_rectangle(self.field.player1.get_x(), self.field.player1.get_y(), self.field.player1.get_x() + self.field.player1.player_size(), self.field.player1.get_y() + self.field.player1.player_size(), fill=self.field.player1.get_color())

        for i in self.field.get_tiles_player2():
            self.canv.create_rectangle(i[0]*self.field.player2.player_size(), i[1]*self.field.player2.player_size(), i[0]*self.field.player2.player_size() + self.field.player2.player_size(), i[1]*self.field.player2.player_size() + self.field.player2.player_size(), fill=self.field.player2.get_color(), outline=self.field.player2.get_color())
        for i in self.field.get_potential_tiles_player2():
            self.canv.create_rectangle(i[0]*self.field.player2.player_size(), i[1]*self.field.player2.player_size(), i[0]*self.field.player2.player_size() + self.field.player2.player_size(), i[1]*self.field.player2.player_size() + self.field.player2.player_size(), fill=self.field.player2.get_transparent_color(), outline=self.field.player2.get_transparent_color())
        self.canv.create_rectangle(self.field.player2.get_x(), self.field.player2.get_y(), self.field.player2.get_x() + self.field.player2.player_size(), self.field.player2.get_y() + self.field.player2.player_size(), fill=self.field.player2.get_color())

    def __a_handler(self, event):
        self.field.process_movement('A')
        self.draw_everything()

    def __w_handler(self, event):
        self.field.process_movement('W')
        self.draw_everything()

    def __s_handler(self, event):
        self.field.process_movement('S')
        self.draw_everything()

    def __d_handler(self, event):
        self.field.process_movement('D')
        self.draw_everything()

    def __arrow_left_handler(self, event):
        self.field.process_movement('ARROW_LEFT')
        self.draw_everything()

    def __arrow_up_handler(self, event):
        self.field.process_movement('ARROW_UP')
        self.draw_everything()

    def __arrow_down_handler(self, event):
        self.field.process_movement('ARROW_DOWN')
        self.draw_everything()

    def __arrow_right_handler(self, event):
        self.field.process_movement('ARROW_RIGHT')
        self.draw_everything()

    def text_info(self):
    	messagebox.showinfo('information', 'Игра для двоих пользователей.\nЕсть два игрока\n - небольшие квадратики разного цвета с выделенным ободком.\n Каждый игрок может двигаться влево/вправо/вверх/вниз и наискосок. Когда игрок идёт по нейтральной территории, за ним тянется полупрозрачный след из его цвета\nИгровые кнопки:\n "Esc" - выход из игры\n "p" - пауза\n "i" - показать окно информации\n Управление игроками:\n Первый игрок: "w", "a", "s", "d"\n Второй игрок: стрелочки))\n\n Правила игры - на игровом поле перемещать своего персонажа и захватывать территории\nпутем закрашивания пройденного следа персонажем и возможности закрашивать\nв свой цвет области, обведенные уже закрашенными областями поля\nЕсли до того, как игрок вернулся на свою закращенную область, соперник перешёл через его полупрозрачный след (разорвал связь игрока с его закрашенной областью), то игрок проигрывает - побеждает соперник.\n Цель игры - уничтожить соперника')


    def won(self):
    	messagebox.showinfo('You win!')
    	self.end_game()


    def lose(self):
    	messagebox.showinfo('You lose!')
    	self.end_game()


    def end_game(self):
    	combo = Combobox(self)
    	combo['values'] = ('Yes', 'No')
    	combo.current('No')
    	if combo.current == 1:
    		self.new_game
    	else:
    		self.quit


app = Application()
app.title('paper.io')
app.resizable(width=False, height=False)
app.mainloop()
