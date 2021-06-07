from tkinter import *
import tkinter as tk
from tkinter import messagebox


class Application(tk.Tk):
    def __init__(self, master=None):
        tk.Tk.__init__(self, master)
        self.geometry('800x700')
        #self.window_game = Game()
        self.restart = Button(text = "New game", command = self.new_game, width = 30)
        self.restart.grid(column=0, row =2)
        self.info = Button(text = "Informathoin", command = self.text_info, width = 30)
        self.info.grid(column=1, row=2)
        self.exit = Button(text = "exit", command = self.quit, width = 30)
        self.exit.grid(column=2, row =2)
        self.new_game()


    def new_game(self):
        '''
    	'''


    def text_info(self):
    	messagebox.showinfo('informathoin', 'Игра для двоих пользователей.\nЕсть два игрока\n - небольшие квадратики разного цвета с выделенным ободком.\n Каждый игрок может двигаться влево/вправо/вверх/вниз и наискосок. Когда игрок идёт по нейтральной территории, за ним тянется полупрозрачный след из его цвета\nИгровые кнопки:\n "Esc" - выход из игры\n "p" - пауза\n "i" - показать окно информации\n Управление игроками:\n Первый игрок: "w", "a", "s", "d"\n Второй игрок: стрелочки))\n\n Правила игры - на игровом поле перемещать своего персонажа и захватывать территории\nпутем закрашивания пройденного следа персонажем и возможности закрашивать\nв свой цвет области, обведенные уже закрашенными областями поля\nЕсли до того, как игрок вернулся на свою закращенную область, соперник перешёл через его полупрозрачный след (разорвал связь игрока с его закрашенной областью), то игрок проигрывает - побеждает соперник.\n Цель игры - уничтожить соперника')


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
app.title('Game')
app.resizable(width=False, height=False)
app.mainloop()
