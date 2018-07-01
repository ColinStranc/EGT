import numpy as np
import random
from modelling.agent import Agent


class Grid:

    def __init__(self, size):
        self._size = size
        self._grid = np.zeros((size, size), int)
        self._occupied_tile_coordinates = []

    def has_empty_tiles(self):
        if len(self._occupied_tile_coordinates) >= self._size * self._size:
            return False
        return True

    def get_random_empty_square_coordinates(self):
        empty_square = None
        for i in range(0, 100):
            rand_x = random.randint(0, self._size-1)
            rand_y = random.randint(0, self._size-1)
            if self._grid[rand_x, rand_y] == 0:
                return rand_x, rand_y

        raise Exception('Could not find empty square, try threshold reached')

    def get_occupied_tile_coordinates(self):
        return list(self._occupied_tile_coordinates)

    def get_shuffled_occupied_tile_coordinates(self):
        return random.shuffle(self.get_occupied_tile_coordinates())

    def set_agent(self, agent, square):
        self._grid[square[0], square[1]] = agent.to_bitmap()
        if not self._occupied_tile_coordinates.__contains__((square[0], square[1])):
            self._occupied_tile_coordinates.append((square[0], square[1]))

    def get_agent(self, coordinates):
        agent_bits = self._grid[coordinates[0], coordinates[1]]
        return Agent.bits_to_agent(agent_bits)

    def __str__(self):
        sb = ''
        sb += '[\n'
        for x in range(0, self._size):
            for y in range(0, self._size):
                agent_bits = self._grid[x, y]
                if agent_bits == 0:
                    sb += ' <        EMPTY  TILE        > '
                else:
                    sb += ' <{0}> '.format(Agent.bits_to_agent(self._grid[x, y]))
            sb += '\n'
        sb += ']'

        return sb