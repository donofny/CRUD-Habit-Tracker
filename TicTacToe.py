import random
from enum import IntEnum


class TicTacToe:
    class STATES(IntEnum):
        CROSS_TURN = 0
        NAUGHT_TURN = 1
        DRAW = 2
        CROSS_WON = 3
        NAUGHT_WON = 4

    # Necessary variables to control and manipulate the flow of the Tic Tac Toe game
    board = [[]]
    count = 0
    game_result = 0
    list = list(STATES)

    # A board which contains all '0's is considered to be empty
    def __init__(self, size):
        self.board = [['0' for x in range(size)] for y in range(size)]
        self.game_result = int(random.randint(0, 1))
        self.count = 0

    # Displays game grid to the player, neatness of grid display begins to depreciate after 10x10(less aligned with col)
    def display_board(self):
        for y in range(len(self.board)):
            print("   ", y, end='')
        print()
        for count, row in enumerate(self.board):
            print(count, row)
        if self.game_result != self.list[2].value and\
           self.game_result != self.list[3].value and \
           self.game_result != self.list[4].value:

            if self.game_result == self.list[0].value:
                return "\nX's Turn\n"
            if self.game_result == self.list[1].value:
                return "\nO's Turn\n"

        else:
            print(self.check_winner())
            return "Game Over"

    # Use case which allows the user to insert their respective symbol on their given coordinates
    def place_marker(self, symbol, row, column):
        if symbol > 4 or symbol < 0:
            print("Input a proper symbol")
            return
        if (0 <= row < len(self.board)) and (0 <= column < len(self.board)):
            if self.board[row][column] != "x" and self.board[row][column] != "o":
                if symbol == self.list[0].value:
                    self.board[row][column] = "x"
                    self.game_result = 1
                    self.count += 1
                if symbol == self.list[1].value:
                    self.board[row][column] = "o"
                    self.game_result = 0
                    self.count += 1
                if symbol == self.list[2].value or\
                   symbol == self.list[3].value or \
                   symbol == self.list[4].value:
                    print("Can not place this, Game is Over")
                    return
                self.check_winner()
                print(self.display_board())
            else:
                print("Choose a spot which is not already taken.")
        else:
            print("failed input: stop trying to break the game")

    # Check horizontal cells connections
    def row_win(self):
        for x in range(len(self.board)):
            string_helper = ""
            for y in range(len(self.board)):
                if self.board[x][y].lower() == 'x':
                    string_helper += self.board[x][y].lower()
                if self.board[x][y].lower() == 'o':
                    string_helper += self.board[x][y].lower()

            if string_helper == "x" * len(self.board):
                self.game_result = self.list[3].value
                return True
            if string_helper == "o" * len(self.board):
                self.game_result = self.list[4].value
                return True
        return False

    # Check vertical cells connections
    def col_win(self):
        for x in range(len(self.board)):
            string_helper = ""
            for y in range(len(self.board)):
                if self.board[y][x].lower() == 'x':
                    string_helper += self.board[y][x].lower()
                if self.board[y][x].lower() == 'o':
                    string_helper += self.board[y][x].lower()

            if string_helper == "x" * len(self.board):
                self.game_result = self.list[3].value
                return True
            if string_helper == "o" * len(self.board):
                self.game_result = self.list[4].value
                return True
        return False

    # Check diagonal cells for connections
    def diagonal_win(self):
        string_helper = ""
        for x in range(len(self.board)):
            if self.board[x][x].lower() == 'x':
                string_helper += self.board[x][x].lower()
            if self.board[x][x].lower() == 'o':
                string_helper += self.board[x][x].lower()
        if string_helper == "x" * len(self.board):
            self.game_result = self.list[3].value
            return True
        if string_helper == "o" * len(self.board):
            self.game_result = self.list[4].value
            return True

        string_helper = ""
        for x in range(len(self.board)):
            y = len(self.board) - 1 - x
            if self.board[x][y].lower() == 'x':
                string_helper += self.board[x][y].lower()
            if self.board[x][y].lower() == 'o':
                string_helper += self.board[x][y].lower()
        if string_helper == "x" * len(self.board):
            self.game_result = self.list[3].value
            return True
        if string_helper == "o" * len(self.board):
            self.game_result = self.list[4].value
            return True
        return False

    # Checks for a game result (W,L,D) each time after the first move (less efficient but will work for every grid)
    # Ideally we would want to check how many turns before a player can win. Since we have no predetermined size;
    # Checking from zero accounts for all dynamic grid lengths, 1x1 and onward
    def check_winner(self):
        if self.count > 0:
            if self.row_win() or self.col_win() or self.diagonal_win():
                if self.game_result == self.list[4].value:
                    return "\nO IS VICTORIOUS!"
                if self.game_result == self.list[3].value:
                    return "\nX IS VICTORIOUS!"
        if self.count == (len(self.board) * len(self.board)):
            self.game_result = self.list[2].value
            return "Draw!"
        return "continue"

    # Checks which player is to go first
    def coin_flip_check(self):
        if self.game_result == 0:
            print("\nCoin lands on heads; x goes first!")
        if self.game_result == 1:
            print("\nCoin lands on tails; o goes first!")
