import modelling.grid as g

import numpy as np
import logging


def get_random_agent():
    return 1


def birth(grid):
    target_square = grid.get_random_empty_square()
    born_agent = get_random_agent()
    grid.add_agent(born_agent, target_square)


logging.basicConfig(filename='../logging/egt.log', level='INFO')
logging.info('TEST')

grid = g.Grid(5)

for i in range(0,10):
    birth(grid)
print(grid.to_string())