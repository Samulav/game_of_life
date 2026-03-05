import time

class Grid():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for i in range(cols)] for k in range(rows)]
    
    def get_value(self, row, col):
        return self.grid[row][col]

    def get_grid(self):
        return self.grid

    def set_value(self, row, col, val):
        self.grid[row][col] = val

    def set_grid(self, grid):
        self.grid = grid
    
    def log_grid(self):
        for row in self.grid:
            print(''.join(['x' if val == 1 else 'o' for val in row]))

    def reset_grid(self):
        self.grid = [[0 for i in range(self.cols)] for k in range(self.rows)]
            
class GameOfLife():
    def __init__(self, grid):
        """
        grid: Grid object
        """
        self.board = grid
        self.M, self.N = self.board.rows, self.board.cols

    #Helper checks all neighbours of a point on an x,y coordinate (0 indexed)
    def helper(self, row, col):
        points = [(0,1), (1,1), (1,0), (1,-1), (0, -1), (-1,-1), (-1, 0), (-1, 1)]
        counter = 0
        for x,y in points:
            if 0<= row + y < self.M and 0<= col + x < self.N and self.board.get_value(row + y, col + x) > 0:
                counter += 1
        
        #Rules of game
        if self.board.get_value(row, col) > 0:
            if counter < 2:
                return 2
            elif 2 <= counter <=3:
                return 1
            else: 
                return 2
        else:
            if counter == 3:
                return -1 #Terug naar leven
            else:
                return 0

    def run_round(self):
        self.tmp = [[None]*self.N for _ in range(self.M)] #Reset the temporary
        for row in range(self.M):
            for col in range(self.N):
                self.board.set_value(row, col, self.helper(row, col))
        for row in range(self.M):
            for col in range(self.N):
                if self.board.get_value(row, col) == 2:
                    self.board.set_value(row, col, 0)
                elif self.board.get_value(row, col) == -1:
                    self.board.set_value(row, col, 1)



def run_simulation(grid, sleep_time=0,  rounds=30):
    game = GameOfLife(grid)
    for round_num in range(1, rounds+1):
        game.run_round()
        print(f"Current round: {round_num}")
        game.board.log_grid()
        print('')
        time.sleep(sleep_time)

def run_interface():
    print("Welcome to this game of life simulator! ")
    print("In the following steps we will set up the starting configuration.")
    print("Height of the board (rows): ")
    rows = int(input())
    print("Width of the board (collumns): ")
    cols = int(input())
    print("How much delay should there be between each round (s): ")
    sleep_time_round = float(input())
    print("How many rounds should the simulation last?")
    rounds = int(input())
    print('')

    print('The following configuration has been set: ')
    print(f'Rows: {rows}')
    print(f'Collumns: {cols}')
    print(f'Sleep time round: {sleep_time_round}')
    print(f'Rounds: {rounds}')

    grid = Grid(rows, cols)
    
    print('In the following steps the starting configuration of the grid can be set: ')
    grid.log_grid()
    print('')

    ##Hier nog startconfiguratie kunnen instellen
    start_conf_done = False
    while not start_conf_done:
        print("Select a piece to to change that value in the following form: x y (0-indexed). Leave empty to start the simulation.")
        tile = input()
        if tile == '':
            start_conf_done = True
        else:
            try:
                co = tile.split(' ')
                row, col = int(co[0]), int(co[1])
            except IndexError: 
                print('Error: Make sure that the row and collumn are seperated by a space. Example: 12 14')
                continue
            except ValueError:
                print('Error: Make sure the row and collumn are integers.')
                continue
            if grid.get_value(row, col) == 0:
                grid.set_value(row, col, 1)
            else:
                grid.set_value(row, col, 0)
            print('The value at row {row} and collumn {col} has been changed')
            print('The grid has been changed to: ')
            grid.log_grid()
    print("The simulation will be started in the following start-configuration.")
    print(f'Rows: {rows}')
    print(f'Collumns: {cols}')
    print(f'Sleep time round: {sleep_time_round}')
    print(f'Rounds: {rounds}')
    grid.log_grid()
    print('')
    print('Press any key to start the simulation: ')
    input()
    run_simulation(grid, sleep_time_round, rounds)

if __name__=='__main__':
    run_interface()
