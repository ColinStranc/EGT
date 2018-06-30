import modelling.grid as g
from modelling.agent import Agent

import logging


def get_random_agent():
    cooperation_strategy = 2
    punishment_strategy = 1
    return Agent.create_agent(cooperation_strategy, punishment_strategy)


def birth(grid):
    target_square = grid.get_random_empty_square()
    born_agent = get_random_agent()
    grid.add_agent(born_agent, target_square)


logging.basicConfig(filename='../logging/egt.log', level='INFO')
logging.info('TEST')

grid = g.Grid(5, 30)

for i in range(0,1):
    birth(grid)
    grid.assign_base_payoffs()

print(grid.to_string())
