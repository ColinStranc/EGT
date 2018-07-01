from modelling.grid import Grid
from modelling.agent import Agent


class Leader:
    def __init__(self, grid_size, base_pay, threat_level):
        self._grid = Grid(grid_size)

        self._base_pay = base_pay
        self._threat_level = threat_level

    def execute_simulation(self):
        self._execute_generation()

        print(self._grid)

    def _execute_generation(self):
        self._birth()
        self._assign_payoffs()

    def _birth(self):
        if not self._grid.has_empty_tiles:
            return

        new_tile_coordinates = self._grid.get_random_empty_square_coordinates()
        cooperation_strategy, punishment_strategy = Agent.get_random_strategies()

        agent = Agent(cooperation_strategy, punishment_strategy, 0, 0)
        self._grid.set_agent(agent, new_tile_coordinates)

    def _assign_payoffs(self):
        self._assign_base_payoffs()

    def _assign_base_payoffs(self):
        base_pay = self._base_pay - self._threat_level

        agent_coordinates = self._grid.get_occupied_tile_coordinates()

        for agent_coordinate in agent_coordinates:
            agent = self._grid.get_agent(agent_coordinate)
            agent = agent.change_fitness(base_pay)
            self._grid.set_agent(agent, agent_coordinate)

