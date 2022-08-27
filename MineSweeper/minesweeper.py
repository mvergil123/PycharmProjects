import random
import math


class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        self.board = self.make_new_board()

        self.dug = set()

    def make_new_board(self):

        board = []

        for i in range(self.dim_size):
            row = [SafeSpot(i, board)] * self.dim_size
            board.append(row)
    
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            new_bomb = Bomb(loc, self)
            row = math.floor(loc / self.dim_size)
            column = int(str(loc)[-1:])
            #column = int(column_arr[len(column_arr)-1])
            print(f"trying to add new bomb in row {row} and column {column}")
            board[row][column] = new_bomb
            bombs_planted += 1
        return board

    def print_board(self):
        position = 0
        for column in self.board:
            for row_item in column:
                row_item.print_item(position)
                position += 1


    def game_over(self):
        pass

    def game_continue(self):
        pass


    def play(dim_size=10, num_bombs=10):
        pass


class Bomb:
    def __init__(self, loc, board ):
        self.loc = loc
        self.board = board
   
    def user_has_chosen(self):
        self.board.game_over()

    def print_item(self, at_postion):
        if at_postion % 9 == 0 and at_postion != 0:
            print("| $ |")
        else:
            print("| $ |", end="")           

class SafeSpot:
    def __init__(self, loc, board):
        self.loc = loc
        self.board = board
    
    def print_item(self, at_postion):
        if at_postion % 9 == 0 and at_postion != 0:
            print("| $ |")
        else:
            print("| $ |", end="")      
              
    def user_has_chosen(self):
        self.board.game_continue()


def main():
    board1 = Board(10,10)
    board1.print_board()

main()


