import unittest
from modelling.constants import cooperation_strategies as cs
from modelling.constants import punishement_strategies as ps
from modelling.agent import Agent


class TestAgent(unittest.TestCase):
    def test_can_fetch_all_input_data(self):
        cooperation_strategy = cs.COOPERATOR
        punishment_strategy = ps.ANTI_SOCIAL
        fitness = 0
        cooperated = 0

        agent = Agent(cooperation_strategy, punishment_strategy, fitness, cooperated)

        self.assertEqual(cooperation_strategy, agent.coop_strategy)
        self.assertEqual(punishment_strategy, agent.punish_strategy)
        self.assertEqual(fitness, agent.fitness)
        self.assertEqual(cooperated, agent.cooperated)

    def test_bitmap_keeps_all_data(self):
        cooperation_strategy = cs.COOPERATOR
        punishment_strategy = ps.ANTI_SOCIAL
        fitness = 0
        cooperated = 0

        agent = Agent(cooperation_strategy, punishment_strategy, fitness, cooperated)
        bitmap = agent.to_bitmap()
        agent_clone = Agent.bits_to_agent(bitmap)

        self.assertEqual(agent, agent_clone, "clone is not identical to original")

    def test_can_increase_fitness(self):
        cooperation_strategy = cs.COOPERATOR
        punishment_strategy = ps.ANTI_SOCIAL
        fitness = 0
        cooperated = 0

        fitness_change = 5

        agent = Agent(cooperation_strategy, punishment_strategy, fitness, cooperated)
        new_agent = agent.change_fitness(fitness_change)

        self.assertEqual(fitness_change + fitness, new_agent.fitness)

    def test_can_decrease_fitness(self):
        cooperation_strategy = cs.COOPERATOR
        punishment_strategy = ps.ANTI_SOCIAL
        fitness = 0
        cooperated = 0

        fitness_change = 5
        fitness_change_2 = -2

        agent = Agent(cooperation_strategy, punishment_strategy, fitness, cooperated)
        agent = agent.change_fitness(fitness_change)
        new_agent = agent.change_fitness(fitness_change_2)

        print(new_agent.fitness)
        self.assertEqual(fitness_change_2 + fitness_change + fitness, new_agent.fitness)

    def test_fitness_does_not_go_negative(self):
        cooperation_strategy = cs.COOPERATOR
        punishment_strategy = ps.ANTI_SOCIAL
        fitness = 0
        cooperated = 0

        fitness_change = -5

        agent = Agent(cooperation_strategy, punishment_strategy, fitness, cooperated)
        new_agent = agent.change_fitness(fitness_change)

        self.assertEqual(0, new_agent.fitness)

    def test_fitness_does_not_go_above_100(self):
        cooperation_strategy = cs.COOPERATOR
        punishment_strategy = ps.ANTI_SOCIAL
        fitness = 0
        cooperated = 0

        fitness_change = 105

        agent = Agent(cooperation_strategy, punishment_strategy, fitness, cooperated)
        new_agent = agent.change_fitness(fitness_change)

        self.assertEqual(100, new_agent.fitness)

    def test_fitness_can_have_fractions(self):
        cooperation_strategy = cs.COOPERATOR
        punishment_strategy = ps.ANTI_SOCIAL
        fitness = 10.125
        cooperated = 0

        agent = Agent(cooperation_strategy, punishment_strategy, fitness, cooperated)

        self.assertEqual(fitness, agent.fitness)

    def test_fitness_with_fractions_can_marshal(self):
        cooperation_strategy = cs.COOPERATOR
        punishment_strategy = ps.ANTI_SOCIAL
        fitness = 10.125
        cooperated = 0

        agent = Agent(cooperation_strategy, punishment_strategy, fitness, cooperated)
        bitmap = agent.to_bitmap()
        agent_clone = Agent.bits_to_agent(bitmap)

        self.assertEqual(fitness, agent_clone.fitness)

    def test_can_set_cooperated_true(self):
        cooperation_strategy = cs.COOPERATOR
        punishment_strategy = ps.ANTI_SOCIAL
        fitness = 0
        cooperated = 0

        agent = Agent(cooperation_strategy, punishment_strategy, fitness, cooperated)
        new_agent = agent.set_cooperated(True)

        self.assertEqual(1, new_agent.cooperated)

    def test_can_set_cooperated_false(self):
        cooperation_strategy = cs.COOPERATOR
        punishment_strategy = ps.ANTI_SOCIAL
        fitness = 0
        cooperated = 0

        agent = Agent(cooperation_strategy, punishment_strategy, fitness, cooperated)
        new_agent = agent.set_cooperated(False)

        self.assertEqual(0, new_agent.cooperated)

    def test_cooperated_set_defaults_true(self):
        cooperation_strategy = cs.COOPERATOR
        punishment_strategy = ps.ANTI_SOCIAL
        fitness = 0
        cooperated = 0

        agent = Agent(cooperation_strategy, punishment_strategy, fitness, cooperated)
        new_agent = agent.set_cooperated()

        self.assertEqual(1, new_agent.cooperated)
