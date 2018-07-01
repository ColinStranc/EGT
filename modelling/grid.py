import numpy as np
import random
from modelling.agent import Agent


class Grid:

    def __init__(self, size, base_pay, threat_level):
        self._size = size
        self._grid = np.zeros((size, size), int)

        self._base_pay = base_pay
        self._threat_level = threat_level

    def get_random_empty_square(self):
        empty_square = None
        for i in range(0, 100):
            rand_x = random.randint(0, self._size-1)
            rand_y = random.randint(0, self._size-1)
            if self._grid[rand_x, rand_y] == 0:
                return rand_x, rand_y

        raise Exception('Could not find empty square, try threshold reached')

    def add_agent(self, agent, square):
        self._grid[square[0], square[1]] = agent.to_bitmap()

    def assign_base_payoffs(self):
        self.assign_equal_payoffs_to_all(self._base_pay)

    def apply_threat_level(self):
        self.assign_equal_payoffs_to_all(self._threat_level)

    def assign_equal_payoffs_to_all(self, amount):
        for x in range(0, self._size):
            for y in range(0, self._size):
                if self._grid[x, y] == 0:
                    continue
                agent = Agent.bits_to_agent(self._grid[x, y])
                agent = agent.change_fitness(amount)
                self._grid[x, y] = agent.to_bitmap()

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