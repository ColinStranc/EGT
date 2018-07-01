import modelling.grid as g
from modelling.agent import Agent
import modelling.constants.cooperation_strategies as cs
import modelling.constants.punishement_strategies as ps

import logging


def get_random_agent():
    cooperation_strategy = cs.COOPERATOR
    punishment_strategy = ps.ANTI_SOCIAL
    return Agent(cooperation_strategy, punishment_strategy, 0, 0)


def birth(grid):
    target_square = grid.get_random_empty_square()
    born_agent = get_random_agent()
    grid.add_agent(born_agent, target_square)


logging.basicConfig(filename='../logging/egt.log', level='INFO')
logging.info('TEST')

grid = g.Grid(5, 30, -3)

for i in range(0,1):
    birth(grid)
    grid.assign_base_payoffs()
    grid.apply_threat_level()

print(grid)
