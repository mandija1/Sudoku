from random import randint, shuffle
import numpy as np
import pygame
pygame.font.init()

class Sudoku():
    def __init__(self):
        self.possible_numbers = [1,2,3,4,5,6,7,8,9]
        grid = []
        for i in range(9):
            grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.grid = grid

    def checkGrid(self):
        for row in range(0,9):
            for col in range(0,9):
                if self.grid[row][col]==0:
                    return False
        return True

    def possible(self, row, col, n):
        for i in range(9):
            if self.grid[row][i] == n:
                return False
        for i in range(9):
            if self.grid[i][col] == n:
                return False
        square_x = (col // 3) * 3
        square_y = (row // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.grid[square_y + i][square_x + j] == n:
                    return False
        return True

    def fill_grid(self):
        for i in range(81):
            row = i // 9
            col = i % 9
            if self.grid[row][col]==0:
                shuffle(self.possible_numbers)
                for n in self.possible_numbers:
                    if self.possible(row, col, n):
                        self.grid[row][col]=n
                        if self.checkGrid():
                            return True
                        else:
                            if self.fill_grid():
                                return True
                break
        self.grid[row][col]=0

    def hide_numbers(self):
        len_to_hide = 45
        for n in range(len_to_hide):
            row = randint(0, 8)
            col = randint(0, 8)
            self.grid[row][col] = 0

    def draw_board(self):
        # Draw Grid Lines
        gap = 9 / 9
        for i in range(self.rows+1):
            pygame.draw.line(win, (0,0,0), (0, i*gap), (self.width, i*gap), thick)
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)


game_1 = Sudoku()
game_1.fill_grid()
game_1.hide_numbers()
print(np.matrix(game_1.grid))
