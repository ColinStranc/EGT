import unittest
from modelling.grid import Grid
from modelling.agent import Agent
import modelling.constants.cooperation_strategies as cs
import modelling.constants.punishement_strategies as ps
from modelling.strategies.cooperate import Cooperate
from modelling.strategies.defect import Defect
from modelling.strategies.opportunistic import Opportunistic
from modelling.public_goods_games import PublicGoodsGame


class TestPublicGoodsGame(unittest.TestCase):

    def test_contribution_strategy_coop_contributes_given_no_neighbours(self):
        contribution_cost = 1
        punishment_fine = 3

        neighbours = []

        did_contribute = Cooperate.contributes(neighbours, contribution_cost, punishment_fine)

        self.assertTrue(did_contribute)

    # TODO: this should be a "parameterized" test which goes through each combination of strategies for the neighbour
    def test_contribution_strategy_coop_contributes_given_neighbour(self):
        contribution_cost = 1
        punishment_fine = 3

        neighbour = [Agent.create_agent(cs.COOPERATOR, ps.NON_PUNISHER)]

        did_contribute = Cooperate.contributes(neighbour, contribution_cost, punishment_fine)

        self.assertTrue(did_contribute)

    def test_contribution_strategy_coop_contributes_given_neighbours(self):
        contribution_cost = 1
        punishment_fine = 3

        neighbours = [Agent.create_agent(cs.DEFECTING, ps.SPITEFUL),
                      Agent.create_agent(cs.COOPERATOR, ps.NON_PUNISHER),
                      Agent.create_agent(cs.OPPORTUNISTIC, ps.RESPONSIBLE)]

        did_contribute = Cooperate.contributes(neighbours, contribution_cost, punishment_fine)

        self.assertTrue(did_contribute)

    def test_contribution_strategy_defecting_does_not_contribute_given_no_neighbours(self):
        contribution_cost = 1
        punishment_fine = 3

        neighbours = []

        did_contribute = Defect.contributes(neighbours, contribution_cost, punishment_fine)

        self.assertFalse(did_contribute)

    # TODO: this should be a "parameterized" test which goes through each combination of strategies for the neighbour
    def test_contribution_strategy_defecting_does_not_contribute_given_neighbour(self):
        contribution_cost = 1
        punishment_fine = 3

        neighbour = [Agent.create_agent(cs.COOPERATOR, ps.NON_PUNISHER)]

        did_contribute = Defect.contributes(neighbour, contribution_cost, punishment_fine)

        self.assertFalse(did_contribute)

    def test_contribution_strategy_defecting_does_not_contribute_given_neighbours(self):
        contribution_cost = 1
        punishment_fine = 3

        neighbours = [Agent.create_agent(cs.DEFECTING, ps.SPITEFUL),
                      Agent.create_agent(cs.COOPERATOR, ps.NON_PUNISHER),
                      Agent.create_agent(cs.OPPORTUNISTIC, ps.RESPONSIBLE)]

        did_contribute = Defect.contributes(neighbours, contribution_cost, punishment_fine)

        self.assertFalse(did_contribute)

    def test_contribution_strategy_opportunistic_does_not_contribute_given_no_neighbours(self):
        contribution_cost = 1
        punishment_fine = 3

        neighbours = []

        did_contribute = Opportunistic.contributes(neighbours, contribution_cost, punishment_fine)

        self.assertFalse(did_contribute)

    def test_contribution_strategy_opportunistic_does_not_contribute_given_anti_social_neighbour(self):
        contribution_cost = 1
        punishment_fine = 3

        neighbour = [Agent.create_agent(cs.OPPORTUNISTIC, ps.ANTI_SOCIAL)]

        did_contribute = Opportunistic.contributes(neighbour, contribution_cost, punishment_fine)

        self.assertFalse(did_contribute)

    def test_contribution_strategy_opportunistic_does_not_contribute_given_spiteful_neighbour(self):
        contribution_cost = 1
        punishment_fine = 3

        neighbour = [Agent.create_agent(cs.OPPORTUNISTIC, ps.SPITEFUL)]

        did_contribute = Opportunistic.contributes(neighbour, contribution_cost, punishment_fine)

        self.assertFalse(did_contribute)

    def test_contribution_strategy_opportunistic_does_not_contribute_given_responsible_neighbour_and_high_contribution_cost(self):
        contribution_cost = 4
        punishment_fine = 3

        neighbour = [Agent.create_agent(cs.OPPORTUNISTIC, ps.RESPONSIBLE)]

        did_contribute = Opportunistic.contributes(neighbour, contribution_cost, punishment_fine)

        self.assertFalse(did_contribute)

    def test_contribution_strategy_opportunistic_contributes_given_responsible_neighbour(self):
        contribution_cost = 1
        punishment_fine = 3

        neighbour = [Agent.create_agent(cs.OPPORTUNISTIC, ps.RESPONSIBLE)]

        did_contribute = Opportunistic.contributes(neighbour, contribution_cost, punishment_fine)

        self.assertTrue(did_contribute)

    def test_contribution_strategy_opportunistic_contributes_given_more_responsible_neighbours_than_anti_social_neighbours(self):
        contribution_cost = 1
        punishment_fine = 3

        neighbours = [Agent.create_agent(cs.OPPORTUNISTIC, ps.RESPONSIBLE),
                     Agent.create_agent(cs.COOPERATOR, ps.RESPONSIBLE),
                     Agent.create_agent(cs.COOPERATOR, ps.ANTI_SOCIAL),
                     Agent.create_agent(cs.DEFECTING, ps.SPITEFUL)]

        did_contribute = Opportunistic.contributes(neighbours, contribution_cost, punishment_fine)

        self.assertTrue(did_contribute)
