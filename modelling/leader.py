from modelling.grid import Grid
from modelling.agent import Agent

import random


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
        # TODO: play the games!
        self._reproduce()

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
            agent = agent.change_payoff(base_pay)
            self._grid.set_agent(agent, agent_coordinate)

    def _reproduce(self):
        shuffled_agent_coordinates = self._grid.get_shuffled_occupied_tile_coordinates()

        for agent_coordinate in shuffled_agent_coordinates:
            agent = self._grid.get_agent(agent_coordinate)
            self._reproduce_agent(agent, agent_coordinate)

    def _reproduce_agent(self, agent, agent_coordinate):
        candidate_reproduction_coordinates = []
        if self._grid.is_tile_vacant((agent_coordinate[0] - 1, agent_coordinate[1])):
            candidate_reproduction_coordinates.append((agent_coordinate[0] - 1, agent_coordinate[1]))
        if self._grid.is_tile_vacant((agent_coordinate[0] + 1, agent_coordinate[1])):
            candidate_reproduction_coordinates.append((agent_coordinate[0] + 1, agent_coordinate[1]))
        if self._grid.is_tile_vacant((agent_coordinate[0], agent_coordinate[1] - 1)):
            candidate_reproduction_coordinates.append((agent_coordinate[0], agent_coordinate[1] - 1))
        if self._grid.is_tile_vacant((agent_coordinate[0], agent_coordinate[1] + 1)):
            candidate_reproduction_coordinates.append((agent_coordinate[0], agent_coordinate[1] + 1))

        if len(candidate_reproduction_coordinates) == 0:
            return

        fitness = Agent.get_fitness_from_payoff(agent.payoff)

        if random.random() > fitness:
            # It didn't work out today, sorry buddy. Better luck next time!
            return

        # Congratulations! you were fit enough to reproduce
        reproduction_coordinate_index = random.randrange(0, len(candidate_reproduction_coordinates))
        reproduction_coordinate = candidate_reproduction_coordinates[reproduction_coordinate_index]

        offspring = Agent(agent.coop_strategy, agent.punish_strategy, 0, 0)

        self._grid.set_agent(offspring, reproduction_coordinate)