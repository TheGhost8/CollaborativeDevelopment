from tkinter import *
import tkinter as tk
#from tkinter import messagebox
#import map.py


class Application(tk.Frame):
    #field = Map()

    def __init__(self, master=None, title="<application>", **kwargs):
        #tk.Tk.__init__(self, master)
        super().__init__(master, **kwargs) 
        #self.geometry('1000x600')
        #self.window_game = Game()
        self.master.title(title)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.restart = Button(text = "New game", command = self.new_game)
        self.restart.grid(column=0, row =2)
        self.info = Button(text = "Information", command = self.text_info)
        self.info.grid(column=1, row=2)
        self.exit = Button(text = "Exit", command = self.quit)
        self.exit.grid(column=2, row =2)
        self.map = tk.Canvas(bg='#fff', width=800, height=600)
        #id1 = self.map.create_rectangle(60, 60, 80, 80, fill='#000000')
        self.map.grid()
        self.new_game()


    def new_game(self):
        pass


    def text_info(self):
    	tk.messagebox.showinfo('informathoin', 'Игра для двоих пользователей.\nЕсть два игрока\n - небольшие квадратики разного цвета с выделенным ободком.\n Каждый игрок может двигаться влево/вправо/вверх/вниз и наискосок. Когда игрок идёт по нейтральной территории, за ним тянется полупрозрачный след из его цвета\nИгровые кнопки:\n "Esc" - выход из игры\n "p" - пауза\n "i" - показать окно информации\n Управление игроками:\n Первый игрок: "w", "a", "s", "d"\n Второй игрок: стрелочки))\n\n Правила игры - на игровом поле перемещать своего персонажа и захватывать территории\nпутем закрашивания пройденного следа персонажем и возможности закрашивать\nв свой цвет области, обведенные уже закрашенными областями поля\nЕсли до того, как игрок вернулся на свою закращенную область, соперник перешёл через его полупрозрачный след (разорвал связь игрока с его закрашенной областью), то игрок проигрывает - побеждает соперник.\n Цель игры - уничтожить соперника')


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



app = Application(title='Game')
#app.title('Game')
app.mainloop()
