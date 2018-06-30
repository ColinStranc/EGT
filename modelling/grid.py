import numpy as np
import random
import modelling.agent as agnt


class Grid:

    def __init__(self, size):
        self._size = size
        self._grid = np.zeros((size, size), int)

    def get_random_empty_square(self):
        empty_square = None
        for i in range(0, 100):
            rand_x = random.randint(0, self._size-1)
            rand_y = random.randint(0, self._size-1)
            if self._grid[rand_x, rand_y] == 0:
                return rand_x, rand_y

        raise Exception('Could not find empty square, try threshold reached')

    def add_agent(self, agent, square):
        self._grid[square[0], square[1]] = agent

    def to_string(self):
        sb = ''
        sb += '[\n'
        for x in range(0, self._size):
            for y in range(0, self._size):
                sb += ' <{0}> '.format(agnt.Agent.to_string(self._grid[x, y]))
            sb += '\n'
        sb += ']'

        return sb