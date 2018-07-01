from modelling.grid import Grid
from modelling.agent import Agent


class Leader:
    def __init__(self):
        self._grid = Grid(5, 30, 3)

    def execute_simulation(self):
        self._execute_generation()
        print(self._grid)

    def _execute_generation(self):
        self._birth()
        self._grid.assign_base_payoffs()
        self._grid.apply_threat_level()

    def _birth(self):
        if not self._grid.has_empty_tiles:
            return

        new_tile_coordinates = self._grid.get_random_empty_square_coordinates()
        cooperation_strategy, punishment_strategy = Agent.get_random_strategies()

        agent = Agent(cooperation_strategy, punishment_strategy, 0, 0)
        self._grid.add_agent(agent, new_tile_coordinates)