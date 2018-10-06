import unittest
from modelling.grid import Grid
from modelling.agent import Agent
import modelling.constants.cooperation_strategies as cs
import modelling.constants.punishement_strategies as ps
from modelling.strategies.cooperation.cooperate import Cooperate
from modelling.strategies.cooperation.defect import Defect
from modelling.strategies.cooperation.opportunistic import Opportunistic
from modelling.strategies.punishment.non_punishing import NonPunishing
from modelling.strategies.punishment.anti_social import AntiSocial
from modelling.strategies.punishment.spiteful import Spiteful
from modelling.strategies.punishment.responsible import Responsible
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

    # spiteful, antisocial, responsible, nonpunishing
    def test_punishment_strategy_non_punishing_does_not_punish_contributor(self):
        punisher = Agent.create_agent(cs.COOPERATOR, ps.NON_PUNISHER)
        punishee = Agent.create_agent(cs.COOPERATOR, ps.RESPONSIBLE).set_cooperated(True)

        did_punish = NonPunishing.punishes(punisher, punishee)

        self.assertFalse(did_punish)

    def test_punishment_strategy_non_punishing_does_not_punish_non_contributor(self):
        punisher = Agent.create_agent(cs.COOPERATOR, ps.NON_PUNISHER)
        punishee = Agent.create_agent(cs.DEFECTING, ps.RESPONSIBLE).set_cooperated(False)

        did_punish = NonPunishing.punishes(punisher, punishee)

        self.assertFalse(did_punish)

    def test_punishment_strategy_spiteful_does_punish_contributor(self):
        punisher = Agent.create_agent(cs.COOPERATOR, ps.ANTI_SOCIAL)
        punishee = Agent.create_agent(cs.COOPERATOR, ps.RESPONSIBLE).set_cooperated(True)

        did_punish = Spiteful.punishes(punisher, punishee)

        self.assertTrue(did_punish)

    def test_punishment_strategy_spiteful_does_punish_non_contributor(self):
        punisher = Agent.create_agent(cs.COOPERATOR, ps.ANTI_SOCIAL)
        punishee = Agent.create_agent(cs.DEFECTING, ps.RESPONSIBLE).set_cooperated(False)

        did_punish = Spiteful.punishes(punisher, punishee)

        self.assertTrue(did_punish)

    def test_punishment_strategy_responsible_does_not_punish_contributor(self):
        punisher = Agent.create_agent(cs.COOPERATOR, ps.RESPONSIBLE)
        punishee = Agent.create_agent(cs.COOPERATOR, ps.RESPONSIBLE).set_cooperated(True)

        did_punish = Responsible.punishes(punisher, punishee)

        self.assertFalse(did_punish)

    def test_punishment_strategy_responsible_does_punish_non_contributor(self):
        punisher = Agent.create_agent(cs.COOPERATOR, ps.RESPONSIBLE)
        punishee = Agent.create_agent(cs.DEFECTING, ps.RESPONSIBLE).set_cooperated(False)

        did_punish = Responsible.punishes(punisher, punishee)

        self.assertTrue(did_punish)

    def test_punishment_strategy_anti_social_does_punish_contributor(self):
        punisher = Agent.create_agent(cs.COOPERATOR, ps.ANTI_SOCIAL)
        punishee = Agent.create_agent(cs.COOPERATOR, ps.RESPONSIBLE).set_cooperated(True)

        did_punish = AntiSocial.punishes(punisher, punishee)

        self.assertTrue(did_punish)

    def test_punishment_strategy_anti_social_does_not_punish_non_contributor(self):
        punisher = Agent.create_agent(cs.COOPERATOR, ps.ANTI_SOCIAL)
        punishee = Agent.create_agent(cs.DEFECTING, ps.RESPONSIBLE).set_cooperated(False)

        did_punish = AntiSocial.punishes(punisher, punishee)

        self.assertFalse(did_punish)