import pygame
import abc
import numpy as np
import numba as nb


class BasicValues(metaclass=abc.ABCMeta):
    def __init__(self, caption='Game of life', width=600, height=400):
        self._width = width
        self._height = height
        self._size = width, height
        self._caption = caption


class PyGame(BasicValues):
    """sets up and terminates the game"""
    def __init__(self):
        super().__init__()
        pygame.init()
        self.screen = pygame.display.set_mode(self._size)
        pygame.display.set_caption(self._caption)

        self.__running = None

    def set_up(self):
        self.__running = True

    def terminate(self):
        self.__running = False

    def is_running(self):
        return self.__running


class Board(BasicValues):
    """updates the board"""
    def __init__(self, screen):
        super().__init__()
        self.__black = (0, 0, 0)
        self.__green = (0, 255, 0)
        self.ON = 1
        self.OFF = 0
        self.vals = [self.ON, self.OFF]
        self.screen = screen
        self.board = np.random.choice(self.vals, self._width*self._height, p=[0.2, 0.8]).reshape(self._size)


    def update_screen(self):
        for row in range(self._height):
            for cul in range(self._width):
                if self.is_alive(cul, row):
                    self.screen.set_at((cul, row), self.__green)
                else:
                    self.screen.set_at((cul, row), self.__black)

    def is_alive(self, cul, row):
        return self.board[cul][row] == 1


    def update_board(self):
        board = self.board[:]
        for row in range(self._height):
            for cul in range(self._width):
                neighbors = self.count_neighbors(row, cul, self.board)
                state = self.board[cul][row]
                board[cul][row] = self.change_state(neighbors, state)
        self.board = board

    def update(self):
        self.update_board()
        self.update_screen()


    @staticmethod
    @nb.njit
    def change_state(neighbors, state):
        if state == 1:
            if neighbors < 2:
                return 0
            elif 2 < neighbors < 4:
                return 1
            else:
                return 0
        else:
            if neighbors == 3:
                return 1
            else:
                return 0


    @staticmethod
    @nb.njit
    def count_neighbors(row, cul, board):
        neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if j == cul and i == row:
                    continue
                neighbors += board[cul+j][row+i]
        return neighbors
