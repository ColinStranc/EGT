from modelling.grid import Grid
from modelling.agent import Agent
from modelling.public_goods_games import PublicGoodsGame

import math
import random
import timeit


class Leader:
    def __init__(self, grid_size, reps, base_pay, threat_level, mutation_rate, death_rate, contribution_multiplication_factor):
        self._grid = Grid(grid_size)

        self._reps = reps
        self._base_pay = base_pay
        self._threat_level = threat_level
        self._mutation_rate = mutation_rate
        self._death_rate = death_rate
        self._contribution_multiplication_factor = contribution_multiplication_factor

        self._record_name = "record.egt"

    def execute_simulation(self):
        self._create_record()

        for i in range(0,self._reps):
            self._execute_generation()

            self._add_generation_to_record(i)

            # TODO: clear cooperated as well -- AFTER BEING SAVED --
            self._clear_generation_agent_details()

            print("finished {0}/{1}".format(i+1, self._reps))

    def _execute_generation(self):
        self._birth()
        self._assign_base_payoffs()
        self._play_game()
        self._reproduce()
        self._mutations()
        self._death()

        print(self._grid)

    def _birth(self):
        if not self._grid.has_empty_tiles:
            return

        new_tile_coordinates = self._grid.get_random_empty_square_coordinates()
        cooperation_strategy, punishment_strategy = Agent.get_random_strategies()

        agent = Agent.create_agent(cooperation_strategy, punishment_strategy)
        self._grid.set_agent(agent, new_tile_coordinates)

    def _assign_base_payoffs(self):
        base_pay = self._base_pay - self._threat_level

        agent_coordinates = self._grid.get_occupied_tile_coordinates()

        for agent_coordinate in agent_coordinates:
            agent = self._grid.get_agent(agent_coordinate)
            agent = agent.change_payoff(base_pay)
            self._grid.set_agent(agent, agent_coordinate)

    def _play_game(self):
        # TODO: Turns out this is supposed to be done multiple times each generation? Not sure how that works, will ask Alec!
        cooperation_count = self._choose_cooperations()
        self._choose_punishments()
        self._distribute_contributions(cooperation_count)

    def _choose_cooperations(self):
        cooperation_count = 0

        for agent_coordinate in self._grid.get_occupied_tile_coordinates():
            agent = self._grid.get_agent(agent_coordinate)

            # Get occupied neighbours
            neighbour_agents = []
            neighbour_coordinates = self._grid.get_occupied_neighbour_tile_coordinates(agent_coordinate)
            for neighbour_coordinate in neighbour_coordinates:
                neighbour_agents.append(self._grid.get_agent(neighbour_coordinate))


            # TODO: if the return is the cost, then the naming here should reflect that.
            #       if this naming sticks, then an enumeration should be returned
            agent_cooperation_choice = PublicGoodsGame.get_agent_cooperation(agent, neighbour_agents)

            agent = agent.change_payoff(agent_cooperation_choice)
            if agent_cooperation_choice < 0:
                agent = agent.set_cooperated(True)
                cooperation_count += 1

            self._grid.set_agent(agent, agent_coordinate)

        return cooperation_count

    def _choose_punishments(self):
        for agent_coordinate in self._grid.get_occupied_tile_coordinates():
            agent = self._grid.get_agent(agent_coordinate)

            neighbour_agents = []
            neighbour_coordinates = self._grid.get_occupied_neighbour_tile_coordinates(agent_coordinate)
            for neighbour_coordinate in neighbour_coordinates:
                neighbour_agents.append(self._grid.get_agent(neighbour_coordinate))

            agent_punishment_size = PublicGoodsGame.resolve_agent_punishment(agent, neighbour_agents)

            # TODO: we probably don't want to have this random -1 here
            agent = agent.change_payoff(-1*agent_punishment_size)

            self._grid.set_agent(agent, agent_coordinate)

    def _distribute_contributions(self, contributions):
        contribution_total = contributions * self._contribution_multiplication_factor

        agent_coordinates = self._grid.get_occupied_tile_coordinates()

        # TODO: This can be an arbitrary fraction, right now we can't deal with any fractions so we are rounding it (up) to the nearest appropriate integer
        reward_per_agent = math.ceil(contribution_total/len(agent_coordinates))

        for agent_coordinate in agent_coordinates:
            agent = self._grid.get_agent(agent_coordinate)
            agent = agent.change_payoff(reward_per_agent)
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

        offspring = Agent.create_agent(agent.coop_strategy, agent.punish_strategy)

        self._grid.set_agent(offspring, reproduction_coordinate)

    def _mutations(self):
        agent_coordinates = self._grid.get_occupied_tile_coordinates()
        for agent_coordinate in agent_coordinates:

            if random.random() <= self._mutation_rate:
                new_coop_strategy, new_punish_strategy = Agent.get_random_strategies()
                agent = self._grid.get_agent(agent_coordinate)
                agent = agent.change_strategies(new_coop_strategy, new_punish_strategy)
                self._grid.set_agent(agent, agent_coordinate)

    def _death(self):
        agent_coordinates = self._grid.get_occupied_tile_coordinates()
        for agent_coordinate in agent_coordinates:

            if random.random() <= self._death_rate:
                self._grid.remove_agent(agent_coordinate)

    def _clear_generation_agent_details(self):
        agent_coordinates = self._grid.get_occupied_tile_coordinates()
        for agent_coordinate in agent_coordinates:
            agent = self._grid.get_agent(agent_coordinate)
            agent = agent.clear_payoff()
            agent = agent.set_cooperated(False)
            agent = agent.clear_new_status()
            self._grid.set_agent(agent, agent_coordinate)

    def _create_record(self):
        record = open(self._record_name, 'wb')

        agent_header_length = 1
        agent_record_length = 7
        parameter_length = 2
        header_length = agent_header_length + parameter_length

        record.write(bytearray([header_length, agent_record_length, self._threat_level, 0]))

        record.close()

    def _add_generation_to_record(self, generation):
        record = open(self._record_name, 'ab')

        gen_1 = 0
        gen_2 = generation

        agent_coordinates = self._grid.get_occupied_tile_coordinates()
        for agent_coordinate in agent_coordinates:
            agent = self._grid.get_agent(agent_coordinate)

            record.write(bytearray([gen_1, gen_2, agent_coordinate[0], agent_coordinate[1], agent.coop_strategy, agent.punish_strategy, agent.cooperated]))

        record.close()