from tkinter import *
from tkinter import messagebox
import random
import time
import threading

game_over = False
class App:
    def __init__(self, master):
        self.game_over = False
        self.frame_bar = None
        self.frame_game = None
        self.label_time = None
        self.label_bombs = None
        self.button_smiley = None

        self.isbomb = []
        self.isflagged = []
        self.isempty = []
        self.button = []
        self.label = []
        self.label_text = []

        self.first_move = False
        self.flags = StringVar()
        self.flags.set('010')
        self.bombs_found = 0
        self.buttons_clicked = 0
        self.time = StringVar()
        self.time.set('000')

        master.title('DNA Minesweeper')
        master.iconbitmap('Ikon.ico')

        self.setup_menu(master)
        self.setup_game(master)


    def get_color(self, bombs):
        if bombs == 1:
            return '1', 'blue'
        elif bombs == 2:
            return '2', 'green'
        elif bombs == 3:
            return '3', 'red'
        elif bombs == 4:
            return  '4', '#00003f'
        elif bombs == 5:
            return '5', '#800000'
        elif bombs == 6:
            return '6', '#0dba86'
        elif bombs == 7:
            return '7', 'black'
        elif bombs == 8:
            return '8', '#d3d3d3'


    def setup_menu(self, master):
        self.frame_bar = Frame(master, bd=7, relief='ridge')
        self.frame_game = Frame(master, bd=7, relief='ridge')

        self.label_bombs = Label(self.frame_bar, height=1, width=3, textvariable=self.flags, fg='red', bg='black', font='DS 18 bold')
        self.button_smiley = Button(self.frame_bar, height=1, width=3, text='☻', fg='yellow', command= lambda: self.new_game(master))
        self.label_time = Label(self.frame_bar, height=1, width=3, textvariable=self.time, fg='red', bg='black', font='DS 18 bold')

        self.label_bombs.grid(row=0, column=0)
        self.button_smiley.grid(row=0, column=1)
        self.label_time.grid(row=0, column=2)

        self.frame_bar.grid_rowconfigure(0,weight=1)
        for i in range(3):
            self.frame_bar.grid_columnconfigure(i,weight=1)

        self.frame_bar.pack(fill=X)
        self.frame_game.pack(fill=BOTH)


    def setup_game(self, master):
        for i in range(9):
            A = []
            for j in range(9):
                A.append(False)
            self.isbomb.append(A)

        for i in range(9):
            A = []
            for j in range(9):
                A.append(False)
            self.isflagged.append(A)

        for i in range(9):
            A = []
            for j in range(9):
                A.append(False)
            self.isempty.append(A)

        for i in range(9):
            A = []
            for j in range(9):
                A.append(StringVar())
            self.label_text.append(A)

        for i in range(9):
            A = []
            for j in range(9):
                A.append(Label(self.frame_game, height=1, width=2, textvariable=self.label_text[i][j], font='Helvetica 11 bold', pady=2))
            self.label.append(A)

        for i in range(9):
            A = []
            self.button.append(A)
        self.button[0].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 0, 0)))
        self.button[0].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 0, 1)))
        self.button[0].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 0, 2)))
        self.button[0].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 0, 3)))
        self.button[0].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 0, 4)))
        self.button[0].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 0, 5)))
        self.button[0].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 0, 6)))
        self.button[0].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 0, 7)))
        self.button[0].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 0, 8)))
        self.button[1].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 1, 0)))
        self.button[1].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 1, 1)))
        self.button[1].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 1, 2)))
        self.button[1].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 1, 3)))
        self.button[1].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 1, 4)))
        self.button[1].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 1, 5)))
        self.button[1].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 1, 6)))
        self.button[1].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 1, 7)))
        self.button[1].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 1, 8)))
        self.button[2].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 2, 0)))
        self.button[2].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 2, 1)))
        self.button[2].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 2, 2)))
        self.button[2].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 2, 3)))
        self.button[2].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 2, 4)))
        self.button[2].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 2, 5)))
        self.button[2].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 2, 6)))
        self.button[2].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 2, 7)))
        self.button[2].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 2, 8)))
        self.button[3].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 3, 0)))
        self.button[3].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 3, 1)))
        self.button[3].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 3, 2)))
        self.button[3].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 3, 3)))
        self.button[3].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 3, 4)))
        self.button[3].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 3, 5)))
        self.button[3].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 3, 6)))
        self.button[3].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 3, 7)))
        self.button[3].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 3, 8)))
        self.button[4].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 4, 0)))
        self.button[4].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 4, 1)))
        self.button[4].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 4, 2)))
        self.button[4].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 4, 3)))
        self.button[4].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 4, 4)))
        self.button[4].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 4, 5)))
        self.button[4].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 4, 6)))
        self.button[4].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 4, 7)))
        self.button[4].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 4, 8)))
        self.button[5].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 5, 0)))
        self.button[5].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 5, 1)))
        self.button[5].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 5, 2)))
        self.button[5].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 5, 3)))
        self.button[5].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 5, 4)))
        self.button[5].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 5, 5)))
        self.button[5].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 5, 6)))
        self.button[5].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 5, 7)))
        self.button[5].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 5, 8)))
        self.button[6].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 6, 0)))
        self.button[6].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 6, 1)))
        self.button[6].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 6, 2)))
        self.button[6].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 6, 3)))
        self.button[6].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 6, 4)))
        self.button[6].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 6, 5)))
        self.button[6].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 6, 6)))
        self.button[6].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 6, 7)))
        self.button[6].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 6, 8)))
        self.button[7].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 7, 0)))
        self.button[7].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 7, 1)))
        self.button[7].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 7, 2)))
        self.button[7].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 7, 3)))
        self.button[7].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 7, 4)))
        self.button[7].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 7, 5)))
        self.button[7].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 7, 6)))
        self.button[7].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 7, 7)))
        self.button[7].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 7, 8)))
        self.button[8].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 8, 0)))
        self.button[8].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 8, 1)))
        self.button[8].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 8, 2)))
        self.button[8].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 8, 3)))
        self.button[8].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 8, 4)))
        self.button[8].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 8, 5)))
        self.button[8].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 8, 6)))
        self.button[8].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 8, 7)))
        self.button[8].append(Button(self.frame_game, height=1, width=2, command= lambda: self.game(master, 8, 8)))

        self.button[0][0].bind('<Button-3>', lambda x: self.flag(master, 0, 0))
        self.button[0][1].bind('<Button-3>', lambda x: self.flag(master, 0, 1))
        self.button[0][2].bind('<Button-3>', lambda x: self.flag(master, 0, 2))
        self.button[0][3].bind('<Button-3>', lambda x: self.flag(master, 0, 3))
        self.button[0][4].bind('<Button-3>', lambda x: self.flag(master, 0, 4))
        self.button[0][5].bind('<Button-3>', lambda x: self.flag(master, 0, 5))
        self.button[0][6].bind('<Button-3>', lambda x: self.flag(master, 0, 6))
        self.button[0][7].bind('<Button-3>', lambda x: self.flag(master, 0, 7))
        self.button[0][8].bind('<Button-3>', lambda x: self.flag(master, 0, 8))
        self.button[1][0].bind('<Button-3>', lambda x: self.flag(master, 1, 0))
        self.button[1][1].bind('<Button-3>', lambda x: self.flag(master, 1, 1))
        self.button[1][2].bind('<Button-3>', lambda x: self.flag(master, 1, 2))
        self.button[1][3].bind('<Button-3>', lambda x: self.flag(master, 1, 3))
        self.button[1][4].bind('<Button-3>', lambda x: self.flag(master, 1, 4))
        self.button[1][5].bind('<Button-3>', lambda x: self.flag(master, 1, 5))
        self.button[1][6].bind('<Button-3>', lambda x: self.flag(master, 1, 6))
        self.button[1][7].bind('<Button-3>', lambda x: self.flag(master, 1, 7))
        self.button[1][8].bind('<Button-3>', lambda x: self.flag(master, 1, 8))
        self.button[2][0].bind('<Button-3>', lambda x: self.flag(master, 2, 0))
        self.button[2][1].bind('<Button-3>', lambda x: self.flag(master, 2, 1))
        self.button[2][2].bind('<Button-3>', lambda x: self.flag(master, 2, 2))
        self.button[2][3].bind('<Button-3>', lambda x: self.flag(master, 2, 3))
        self.button[2][4].bind('<Button-3>', lambda x: self.flag(master, 2, 4))
        self.button[2][5].bind('<Button-3>', lambda x: self.flag(master, 2, 5))
        self.button[2][6].bind('<Button-3>', lambda x: self.flag(master, 2, 6))
        self.button[2][7].bind('<Button-3>', lambda x: self.flag(master, 2, 7))
        self.button[2][8].bind('<Button-3>', lambda x: self.flag(master, 2, 8))
        self.button[3][0].bind('<Button-3>', lambda x: self.flag(master, 3, 0))
        self.button[3][1].bind('<Button-3>', lambda x: self.flag(master, 3, 1))
        self.button[3][2].bind('<Button-3>', lambda x: self.flag(master, 3, 2))
        self.button[3][3].bind('<Button-3>', lambda x: self.flag(master, 3, 3))
        self.button[3][4].bind('<Button-3>', lambda x: self.flag(master, 3, 4))
        self.button[3][5].bind('<Button-3>', lambda x: self.flag(master, 3, 5))
        self.button[3][6].bind('<Button-3>', lambda x: self.flag(master, 3, 6))
        self.button[3][7].bind('<Button-3>', lambda x: self.flag(master, 3, 7))
        self.button[3][8].bind('<Button-3>', lambda x: self.flag(master, 3, 8))
        self.button[4][0].bind('<Button-3>', lambda x: self.flag(master, 4, 0))
        self.button[4][1].bind('<Button-3>', lambda x: self.flag(master, 4, 1))
        self.button[4][2].bind('<Button-3>', lambda x: self.flag(master, 4, 2))
        self.button[4][3].bind('<Button-3>', lambda x: self.flag(master, 4, 3))
        self.button[4][4].bind('<Button-3>', lambda x: self.flag(master, 4, 4))
        self.button[4][5].bind('<Button-3>', lambda x: self.flag(master, 4, 5))
        self.button[4][6].bind('<Button-3>', lambda x: self.flag(master, 4, 6))
        self.button[4][7].bind('<Button-3>', lambda x: self.flag(master, 4, 7))
        self.button[4][8].bind('<Button-3>', lambda x: self.flag(master, 4, 8))
        self.button[5][0].bind('<Button-3>', lambda x: self.flag(master, 5, 0))
        self.button[5][1].bind('<Button-3>', lambda x: self.flag(master, 5, 1))
        self.button[5][2].bind('<Button-3>', lambda x: self.flag(master, 5, 2))
        self.button[5][3].bind('<Button-3>', lambda x: self.flag(master, 5, 3))
        self.button[5][4].bind('<Button-3>', lambda x: self.flag(master, 5, 4))
        self.button[5][5].bind('<Button-3>', lambda x: self.flag(master, 5, 5))
        self.button[5][6].bind('<Button-3>', lambda x: self.flag(master, 5, 6))
        self.button[5][7].bind('<Button-3>', lambda x: self.flag(master, 5, 7))
        self.button[5][8].bind('<Button-3>', lambda x: self.flag(master, 5, 8))
        self.button[6][0].bind('<Button-3>', lambda x: self.flag(master, 6, 0))
        self.button[6][1].bind('<Button-3>', lambda x: self.flag(master, 6, 1))
        self.button[6][2].bind('<Button-3>', lambda x: self.flag(master, 6, 2))
        self.button[6][3].bind('<Button-3>', lambda x: self.flag(master, 6, 3))
        self.button[6][4].bind('<Button-3>', lambda x: self.flag(master, 6, 4))
        self.button[6][5].bind('<Button-3>', lambda x: self.flag(master, 6, 5))
        self.button[6][6].bind('<Button-3>', lambda x: self.flag(master, 6, 6))
        self.button[6][7].bind('<Button-3>', lambda x: self.flag(master, 6, 7))
        self.button[6][8].bind('<Button-3>', lambda x: self.flag(master, 6, 8))
        self.button[7][0].bind('<Button-3>', lambda x: self.flag(master, 7, 0))
        self.button[7][1].bind('<Button-3>', lambda x: self.flag(master, 7, 1))
        self.button[7][2].bind('<Button-3>', lambda x: self.flag(master, 7, 2))
        self.button[7][3].bind('<Button-3>', lambda x: self.flag(master, 7, 3))
        self.button[7][4].bind('<Button-3>', lambda x: self.flag(master, 7, 4))
        self.button[7][5].bind('<Button-3>', lambda x: self.flag(master, 7, 5))
        self.button[7][6].bind('<Button-3>', lambda x: self.flag(master, 7, 6))
        self.button[7][7].bind('<Button-3>', lambda x: self.flag(master, 7, 7))
        self.button[7][8].bind('<Button-3>', lambda x: self.flag(master, 7, 8))
        self.button[8][0].bind('<Button-3>', lambda x: self.flag(master, 8, 0))
        self.button[8][1].bind('<Button-3>', lambda x: self.flag(master, 8, 1))
        self.button[8][2].bind('<Button-3>', lambda x: self.flag(master, 8, 2))
        self.button[8][3].bind('<Button-3>', lambda x: self.flag(master, 8, 3))
        self.button[8][4].bind('<Button-3>', lambda x: self.flag(master, 8, 4))
        self.button[8][5].bind('<Button-3>', lambda x: self.flag(master, 8, 5))
        self.button[8][6].bind('<Button-3>', lambda x: self.flag(master, 8, 6))
        self.button[8][7].bind('<Button-3>', lambda x: self.flag(master, 8, 7))
        self.button[8][8].bind('<Button-3>', lambda x: self.flag(master, 8, 8))

        NOB = 0
        while NOB < 10:
            pos_i = random.randint(0, 8) 
            pos_j = random.randint(0, 8) 

            if self.isbomb[pos_i][pos_j] is False:
                self.label_text[pos_i][pos_j].set('●')
                self.isbomb[pos_i][pos_j] = True
                NOB += 1

        for i in range(9):
            for j in range(9):
                bombs = 0
                text = None
                color = None
                if self.isbomb[i][j] is False:
                    if i == 0 and j == 0:
                        if self.isbomb[i][j+1] is True:
                            bombs += 1
                        if self.isbomb[i+1][j] is True:
                            bombs += 1
                        if self.isbomb[i+1][j+1] is True:
                            bombs += 1
                    elif i == 0 and j == 8:
                        if self.isbomb[i+1][j] is True:
                            bombs += 1
                        if self.isbomb[i][j-1] is True:
                            bombs += 1
                        if self.isbomb[i+1][j-1] is True:
                            bombs += 1
                    elif i == 8 and j == 0:
                        if self.isbomb[i][j+1] is True:
                            bombs += 1
                        if self.isbomb[i-1][j] is True:
                            bombs += 1
                        if self.isbomb[i-1][j+1] is True:
                            bombs += 1
                    elif i == 8 and j == 8:
                        if self.isbomb[i][j-1] is True:
                            bombs += 1
                        if self.isbomb[i-1][j] is True:
                            bombs += 1
                        if self.isbomb[i-1][j-1] is True:
                            bombs += 1
                    elif i == 0:
                        if self.isbomb[i][j-1] is True:
                            bombs += 1
                        if self.isbomb[i][j+1] is True:
                            bombs += 1
                        if self.isbomb[i+1][j-1] is True:
                            bombs += 1
                        if self.isbomb[i+1][j+1] is True:
                            bombs += 1
                        if self.isbomb[i+1][j] is True:
                            bombs += 1
                    elif i == 8:
                        if self.isbomb[i][j-1] is True:
                            bombs += 1
                        if self.isbomb[i][j+1] is True:
                            bombs += 1
                        if self.isbomb[i-1][j-1] is True:
                            bombs += 1
                        if self.isbomb[i-1][j+1] is True:
                            bombs += 1
                        if self.isbomb[i-1][j] is True:
                            bombs += 1
                    elif j == 0:
                        if self.isbomb[i-1][j] is True:
                            bombs += 1
                        if self.isbomb[i+1][j] is True:
                            bombs += 1
                        if self.isbomb[i+1][j+1] is True:
                            bombs += 1
                        if self.isbomb[i-1][j+1] is True:
                            bombs += 1
                        if self.isbomb[i][j+1] is True:
                            bombs += 1
                    elif j == 8:
                        if self.isbomb[i-1][j] is True:
                            bombs += 1
                        if self.isbomb[i+1][j] is True:
                            bombs += 1
                        if self.isbomb[i+1][j-1] is True:
                            bombs += 1
                        if self.isbomb[i-1][j-1] is True:
                            bombs += 1
                        if self.isbomb[i][j-1] is True:
                            bombs += 1
                    else:
                        if self.isbomb[i][j+1] is True:
                            bombs += 1
                        if self.isbomb[i][j-1] is True:
                            bombs += 1
                        if self.isbomb[i+1][j+1] is True:
                            bombs += 1
                        if self.isbomb[i+1][j-1] is True:
                            bombs += 1
                        if self.isbomb[i-1][j+1] is True:
                            bombs += 1
                        if self.isbomb[i-1][j-1] is True:
                            bombs += 1
                        if self.isbomb[i-1][j] is True:
                            bombs += 1
                        if self.isbomb[i+1][j] is True:
                            bombs += 1

                    if bombs != 0:
                        text, color = self.get_color(bombs)
                        self.label[i][j].config(fg=color)
                        self.label_text[i][j].set(text)
                    else:
                        self.isempty[i][j] = True

        symbol = 'A'
        for i in range(9):
            for j in range(9):
                if self.isempty[i][j] is True:
                    if self.label_text[i][j].get() == '':
                        s = symbol
                        self.label_text[i][j].set(s)
                        symbol = chr(ord(symbol) + 1) 
                    else:
                        s = self.label_text[i][j].get()
                        
                    if i == 0 and j == 0:
                        if self.isempty[i][j+1] is True:
                            self.label_text[i][j+1].set(s)
                        if self.isempty[i+1][j] is True:
                            self.label_text[i+1][j].set(s)
                        if self.isempty[i+1][j+1] is True:
                            self.label_text[i+1][j+1].set(s)
                    elif i == 0 and j == 8:
                        if self.isempty[i+1][j] is True:
                            self.label_text[i+1][j].set(s)
                        if self.isempty[i][j-1] is True:
                            self.label_text[i][j-1].set(s)
                        if self.isempty[i+1][j-1] is True:
                            self.label_text[i+1][j-1].set(s)
                    elif i == 8 and j == 0:
                        if self.isempty[i][j+1] is True:
                            self.label_text[i][j+1].set(s)
                        if self.isempty[i-1][j] is True:
                            self.label_text[i-1][j].set(s)
                        if self.isempty[i-1][j+1] is True:
                            self.label_text[i-1][j+1].set(s)
                    elif i == 8 and j == 8:
                        if self.isempty[i][j-1] is True:
                            self.label_text[i][j-1].set(s)
                        if self.isempty[i-1][j] is True:
                            self.label_text[i-1][j].set(s)
                        if self.isempty[i-1][j-1] is True:
                            self.label_text[i-1][j-1].set(s)
                    elif i == 0:
                        if self.isempty[i][j-1] is True:
                            self.label_text[i][j-1].set(s)
                        if self.isempty[i][j+1] is True:
                            self.label_text[i][j+1].set(s)
                        if self.isempty[i+1][j-1] is True:
                            self.label_text[i+1][j-1].set(s)
                        if self.isempty[i+1][j+1] is True:
                            self.label_text[i+1][j+1].set(s)
                        if self.isempty[i+1][j] is True:
                            self.label_text[i+1][j].set(s)
                    elif i == 8:
                        if self.isempty[i][j-1] is True:
                            self.label_text[i][j-1].set(s)
                        if self.isempty[i][j+1] is True:
                            self.label_text[i][j+1].set(s)
                        if self.isempty[i-1][j-1] is True:
                            self.label_text[i-1][j-1].set(s)
                        if self.isempty[i-1][j+1] is True:
                            self.label_text[i-1][j+1].set(s)
                        if self.isempty[i-1][j] is True:
                            self.label_text[i-1][j].set(s)
                    elif j == 0:
                        if self.isempty[i-1][j] is True:
                            self.label_text[i-1][j].set(s)
                        if self.isempty[i+1][j] is True:
                            self.label_text[i+1][j].set(s)
                        if self.isempty[i+1][j+1] is True:
                            self.label_text[i+1][j+1].set(s)
                        if self.isempty[i-1][j+1] is True:
                            self.label_text[i-1][j+1].set(s)
                        if self.isempty[i][j+1] is True:
                            self.label_text[i][j+1].set(s)
                    elif j == 8:
                        if self.isempty[i-1][j] is True:
                            self.label_text[i-1][j].set(s)
                        if self.isempty[i+1][j] is True:
                            self.label_text[i+1][j].set(s)
                        if self.isempty[i+1][j-1] is True:
                            self.label_text[i+1][j-1].set(s)
                        if self.isempty[i-1][j-1] is True:
                            self.label_text[i-1][j-1].set(s)
                        if self.isempty[i][j-1] is True:
                            self.label_text[i][j-1].set(s)
                    else:
                        if self.isempty[i][j+1] is True:
                            self.label_text[i][j+1].set(s)
                        if self.isempty[i][j-1] is True:
                            self.label_text[i][j-1].set(s)
                        if self.isempty[i+1][j+1] is True:
                            self.label_text[i+1][j+1].set(s)
                        if self.isempty[i+1][j-1] is True:
                            self.label_text[i+1][j-1].set(s)
                        if self.isempty[i-1][j+1] is True:
                            self.label_text[i-1][j+1].set(s)
                        if self.isempty[i-1][j-1] is True:
                            self.label_text[i-1][j-1].set(s)
                        if self.isempty[i-1][j] is True:
                            self.label_text[i-1][j].set(s)
                        if self.isempty[i+1][j] is True:
                            self.label_text[i+1][j].set(s)

        for i in range(9):
            for j in range(9):
                self.label[i][j].grid(row=i, column=j)

        for i in range(9):
            for j in range(9):
                self.button[i][j].grid(row=i, column=j)

        master.resizable(0, 0)

    def update_time(self):
        while self.game_over is False and self.first_move is True:
            time.sleep(1)
            self.time.set('{:03}'.format(int(self.time.get()) + 1))
        self.time.set('000')


    def flag(self, master, i, j):
        if self.isflagged[i][j] is True:
            if self.isbomb[i][j] is True:
                self.bombs_found -= 1

            self.flags.set('{:03}'.format(int(self.flags.get()) + 1))
            self.button[i][j].config(text='')
            self.isflagged[i][j] = False
        else:
            if self.isbomb[i][j] is True:
                self.bombs_found += 1

            self.flags.set('{:03}'.format(int(self.flags.get()) - 1))
            self.button[i][j].config(text='|◤')
            self.isflagged[i][j] = True

    def new_game(self, master):
        self.frame_bar.destroy()
        self.frame_game.destroy()

        self.__init__(master)
        

    def game(self, master, i, j):
        if self.first_move is False:
            self.first_move = True

            self.thread = threading.Thread(target=self.update_time, args=())
            self.thread.daemon = True
            self.thread.start()

        if self.isbomb[i][j] is True:
            self.game_over = True
            for i in range(9):
                for j in range(9):
                    if self.isbomb[i][j] is True:
                        self.button[i][j].destroy()
                        self.buttons_clicked += 1
            messagebox.showwarning('GAME OVER!', f'You flagged {self.bombs_found} bombs!')
            master.quit()
        elif self.isempty[i][j] is True:
            s = self.label_text[i][j].get()
            self.label_text[i][j].set('')
            self.button[i][j].destroy()
            self.buttons_clicked += 1

            for a in range(9):
                for b in range(9):
                    if self.label_text[a][b].get() == s:
                        self.label_text[a][b].set('')
                        self.button[a][b].destroy()
                        self.buttons_clicked += 1

                        if a == 0 and b == 0:
                            if self.isempty[a][b+1] is False:
                                self.button[a][b+1].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a+1][b] is False:
                                self.button[a+1][b].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a+1][b+1] is False:
                                self.button[a+1][b+1].destroy()
                                self.buttons_clicked += 1
                        elif a == 0 and b == 8:
                            if self.isempty[a+1][b] is False:
                                self.button[a+1][b].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a][b-1] is False:
                                self.button[a][b-1].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a+1][b-1] is False:
                                self.button[a+1][b-1].destroy()
                                self.buttons_clicked += 1
                        elif a == 8 and b == 0:
                            if self.isempty[a][b+1] is False:
                                self.button[a][b+1].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a-1][b] is False:
                                self.button[a-1][b].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a-1][b+1] is False:
                                self.button[a-1][b+1].destroy()
                                self.buttons_clicked += 1
                        elif a == 8 and b == 8:
                            if self.isempty[a][b-1] is False:
                                self.button[a][b-1].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a-1][b] is False:
                                self.button[a-1][b].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a-1][b-1] is False:
                                self.button[a-1][b-1].destroy()
                                self.buttons_clicked += 1
                        elif a == 0:
                            if self.isempty[a][b-1] is False:
                                self.button[a][b-1].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a][b+1] is False:
                                self.button[a][b+1].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a+1][b-1] is False:
                                self.button[a+1][b-1].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a+1][b+1] is False:
                                self.button[a+1][b+1].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a+1][b] is False:
                                self.button[a+1][b].destroy()
                                self.buttons_clicked += 1
                        elif a == 8:
                            if self.isempty[a][b-1] is False:
                                self.button[a][b-1].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a][b+1] is False:
                                self.button[a][b+1].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a-1][b-1] is False:
                                self.button[a-1][b-1].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a-1][b+1] is False:
                                self.button[a-1][b+1].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a-1][b] is False:
                                self.button[a-1][b].destroy()
                                self.buttons_clicked += 1
                        elif b == 0:
                            if self.isempty[a-1][b] is False:
                                self.button[a-1][b].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a+1][b] is False:
                                self.button[a+1][b].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a+1][b+1] is False:
                                self.button[a+1][b+1].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a-1][b+1] is False:
                                self.button[a-1][b+1].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a][b+1] is False:
                                self.button[a][b+1].destroy()
                                self.buttons_clicked += 1
                        elif b == 8:
                            if self.isempty[a-1][b] is False:
                                self.button[a-1][b].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a+1][b] is False:
                                self.button[a+1][b].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a+1][b-1] is False:
                                self.button[a+1][b-1].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a-1][b-1] is False:
                                self.button[a-1][b-1].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a][b-1] is False:
                                self.button[a][b-1].destroy()
                                self.buttons_clicked += 1
                        else:
                            if self.isempty[a][b+1] is False:
                                self.button[a][b+1].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a][b-1] is False:
                                self.button[a][b-1].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a+1][b+1] is False:
                                self.button[a+1][b+1].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a+1][b-1] is False:
                                self.button[a+1][b-1].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a-1][b+1] is False:
                                self.button[a-1][b+1].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a-1][b-1] is False:
                                self.button[a-1][b-1].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a-1][b] is False:
                                self.button[a-1][b].destroy()
                                self.buttons_clicked += 1
                            if self.isempty[a+1][b] is False:
                                self.button[a+1][b].destroy()
                                self.buttons_clicked += 1
        else:
            self.buttons_clicked += 1
            self.button[i][j].destroy()
            self.buttons_clicked += 1

        if self.bombs_found == 10 or self.buttons_clicked == 71:
            messagebox.showinfo('YOU WIN!', f'You flagged {self.bombs_found} bombs!')

root = Tk()
Application = App(root)
root.mainloop()