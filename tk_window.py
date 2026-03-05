import tkinter as tk
from game_of_life import Grid, GameOfLife
import time
import copy


class Window():
    def __init__(self, board):
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=500, height=500)
        self.canvas.grid(column = 0, row=0, padx=50, pady=50)
        self.game_grid_width = 500
        self.game = GameOfLife(board)
        self.sim_is_running = False
        # self.board = self.game.board
        self.blocks = 3
        self.block_width = self.game_grid_width / len(self.game.board.get_grid())
        self.start_board = copy.deepcopy(self.game.board.get_grid())
        

        self.rects = [[None for i in range(len(self.game.board.get_grid()[0]))] for j in range(len(self.game.board.get_grid()))]
        self.canvas.create_rectangle(0, 0, 500, 500, width=0, fill='black')
        
        self.canvas.bind("<Button-1>",self.clicked_1)
        self.place_squares()

        self.button_frame = tk.Frame(self.window, width=350, height=150)
        self.button_frame.grid(row=2, column=0)
        self.button_frame.grid_propagate(False)

        self.run_round_button = tk.Button(self.button_frame, text="Simulate a round")
        self.run_round_button.bind("<Button-1>", self.run_round_1)

        self.round_var = tk.StringVar()
        self.round_num_label = tk.Label(self.window, textvariable=self.round_var)
        self.round_num = 0
        self.round_var.set(f'Round: {self.round_num}')

        self.start_stop_var = tk.StringVar()
        self.start_stop_button = tk.Button(self.button_frame, textvariable=self.start_stop_var)
        self.start_stop_var.set(self.start_or_stop())
        self.start_stop_button.bind("<Button-1>", self.on_start_or_stop)

        self.reset_clear_var = tk.StringVar()
        self.reset_clear_button = tk.Button(self.button_frame, textvariable=self.reset_clear_var)
        self.reset_clear_var.set(self.reset_or_clear())
        self.reset_clear_button.bind("<Button-1>", self.on_reset_or_clear)

        self.round_speed_slider = tk.Scale(self.button_frame, orient='horizontal', command=self.change_round_speed, length="350", from_=1, to=100)
        self.round_speed_slider.set(50)
        self.round_speed = int(self.round_speed_slider.get()) * 10
        self.round_num_label.grid(column=0, row=1)
        self.run_round_button.grid(column=0, row=0)
        self.start_stop_button.grid(column=1, row=0)
        self.reset_clear_button.grid(column=2, row=0)
        self.round_speed_slider.grid(column=1, row=1)

        self.button_frame.grid_columnconfigure(1, weight=2)
        
        self.window.protocol("WM_DELETE_WINDOW", self.window.quit)
        self.window.mainloop()

    def place_squares(self):
        for i, row in enumerate(self.game.board.get_grid()):
            for j, val in enumerate(row):
                if val==1 and self.rects[i][j] == None:
                    self.rects[i][j] = self.canvas.create_rectangle(self.block_width * j, self.block_width * i, self.block_width * (j+1), self.block_width * (i+1), width=1, fill='yellow', outline='light grey')
                #     self.canvas.tag_bind(rect,"<Button-1>",self.clicked)
                elif val==0 and self.rects[i][j]:
                    self.canvas.delete(self.rects[i][j])
                    self.rects[i][j] = None
        
    def clicked_1(self, event):
        col = int((event.x - (event.x % self.block_width)) / self.block_width)
        row = int((event.y - (event.y % self.block_width)) / self.block_width)

        if self.game.board.get_value(row, col) == 0:
            self.game.board.set_value(row, col, 1)
            self.rects[row][col] = self.canvas.create_rectangle(col * self.block_width, row * self.block_width, (col+1) * self.block_width, (row+1) * self.block_width, fill='yellow', width=1, outline='light grey')
            
        else:
            self.game.board.set_value(row, col, 0)
            self.canvas.delete(self.rects[row][col])
            self.rects[row][col] = None
    
    def run_round_1(self, *args):
        self.round_num += 1
        if self.round_num == 1:
            self.reset_clear_var.set(self.reset_or_clear())
            self.start_board = copy.deepcopy(self.game.board.get_grid())
            
        
        self.game.run_round()
        self.place_squares()
        self.round_var.set(f'Round: {self.round_num}')
        
    
    def start_or_stop(self):
        if self.sim_is_running == True:
            return 'Stop'
        return 'Start'

    def reset_or_clear(self):
        if self.round_num > 0:
            return 'Reset'
        return 'Clear'

    def run_simulation(self):
        if self.sim_is_running:
            self.run_round_1()
            self.window.after(self.round_speed, self.run_simulation)

    def on_start_or_stop(self, event):
        if self.sim_is_running == False:
            self.sim_is_running = True
            self.start_stop_var.set(self.start_or_stop())
            self.run_simulation()
        else:
            self.sim_is_running = False
            self.start_stop_var.set(self.start_or_stop())
    
    def on_reset_or_clear(self, event):
        if self.reset_clear_var.get() == 'Reset':
            self.game.board.set_grid(copy.deepcopy(self.start_board))
            self.place_squares()
            self.round_num = 0 
            self.round_var.set(f'Round: {self.round_num}')
        elif self.reset_clear_var.get() == 'Clear':
            self.game.board.reset_grid()
            self.place_squares()
        self.reset_clear_var.set(self.reset_or_clear())
    
    def change_round_speed(self, scroll_value):
        self.round_speed = int(scroll_value) * 10

board = Grid(30, 30)
# board.set_value(2, 3, 1)
# board.set_value(2, 2, 1)
app = Window(board)
