import unittest
from modelling.constants import cooperation_strategies as cs
from modelling.constants import punishement_strategies as ps
from modelling.agent import Agent
from modelling.agent import MAX_PAYOFF


class TestAgent(unittest.TestCase):
    def test_can_fetch_all_input_data(self):
        cooperation_strategy = cs.COOPERATOR
        punishment_strategy = ps.ANTI_SOCIAL
        payoff = 0
        cooperated = 0

        agent = Agent.create_agent(cooperation_strategy, punishment_strategy)

        self.assertEqual(cooperation_strategy, agent.coop_strategy)
        self.assertEqual(punishment_strategy, agent.punish_strategy)
        self.assertEqual(payoff, agent.payoff)
        self.assertEqual(cooperated, agent.cooperated)

    def test_bitmap_keeps_all_data(self):
        cooperation_strategy = cs.COOPERATOR
        punishment_strategy = ps.ANTI_SOCIAL

        agent = Agent.create_agent(cooperation_strategy, punishment_strategy)
        bitmap = agent.to_bitmap()
        agent_clone = Agent.bits_to_agent(bitmap)

        self.assertEqual(agent, agent_clone, "clone is not identical to original")

    def test_newly_created_agent_has_new_flag(self):
        cooperation_strategy = cs.COOPERATOR
        punishment_strategy = ps.ANTI_SOCIAL

        agent = Agent.create_agent(cooperation_strategy, punishment_strategy)

        self.assertEqual(1, agent.new_agent)

    def test_can_turn_new_flag_off(self):
        cooperation_strategy = cs.COOPERATOR
        punishment_strategy = ps.ANTI_SOCIAL

        agent = Agent.create_agent(cooperation_strategy, punishment_strategy)
        agent = agent.clear_new_status()

        self.assertEqual(0, agent.new_agent)

    def test_can_increase_payoff(self):
        cooperation_strategy = cs.COOPERATOR
        punishment_strategy = ps.ANTI_SOCIAL
        payoff = 0

        payoff_change = 5

        agent = Agent.create_agent(cooperation_strategy, punishment_strategy)
        new_agent = agent.change_payoff(payoff_change)

        self.assertEqual(payoff_change + payoff, new_agent.payoff)

    def test_can_decrease_payoff(self):
        cooperation_strategy = cs.COOPERATOR
        punishment_strategy = ps.ANTI_SOCIAL
        payoff = 0

        payoff_change = 5
        payoff_change_2 = -2

        agent = Agent.create_agent(cooperation_strategy, punishment_strategy)
        agent = agent.change_payoff(payoff_change)
        new_agent = agent.change_payoff(payoff_change_2)

        self.assertEqual(payoff_change_2 + payoff_change + payoff, new_agent.payoff)

    def test_payoff_does_not_go_negative(self):
        cooperation_strategy = cs.COOPERATOR
        punishment_strategy = ps.ANTI_SOCIAL

        payoff_change = -5

        agent = Agent.create_agent(cooperation_strategy, punishment_strategy)
        new_agent = agent.change_payoff(payoff_change)

        self.assertEqual(0, new_agent.payoff)

    def test_payoff_does_not_go_above_max_payoff(self):
        cooperation_strategy = cs.COOPERATOR
        punishment_strategy = ps.ANTI_SOCIAL

        payoff_change = MAX_PAYOFF+1

        agent = Agent.create_agent(cooperation_strategy, punishment_strategy)
        new_agent = agent.change_payoff(payoff_change)

        self.assertEqual(MAX_PAYOFF, new_agent.payoff)

    def test_payoff_does_not_cause_overflows_at_max_value(self):
        cooperation_strategy = cs.COOPERATOR
        punishment_strategy = ps.ANTI_SOCIAL

        payoff_change = MAX_PAYOFF + 1

        agent = Agent.create_agent(cooperation_strategy, punishment_strategy)
        agent = agent.change_payoff(payoff_change)
        agent_clone = Agent.bits_to_agent(agent.to_bitmap())

        self.assertEqual(agent, agent_clone)

    def test_payoff_can_have_fractions(self):
        cooperation_strategy = cs.COOPERATOR
        punishment_strategy = ps.ANTI_SOCIAL
        payoff = 10.25

        agent = Agent.create_agent(cooperation_strategy, punishment_strategy)
        agent = agent.change_payoff(payoff)

        self.assertEqual(payoff, agent.payoff)

    def test_payoff_with_fractions_can_marshal(self):
        cooperation_strategy = cs.COOPERATOR
        punishment_strategy = ps.ANTI_SOCIAL
        payoff = 10.125

        agent = Agent.create_agent(cooperation_strategy, punishment_strategy)
        agent = agent.change_payoff(payoff)
        bitmap = agent.to_bitmap()
        agent_clone = Agent.bits_to_agent(bitmap)

        self.assertEqual(payoff, agent_clone.payoff)

    def test_payoff_with_complicated_fractions_marshals_to_something_close(self):
        cooperation_strategy = cs.COOPERATOR
        punishment_strategy = ps.ANTI_SOCIAL
        payoff = 10.15
        close_payoff = 10.125

        agent = Agent.create_agent(cooperation_strategy, punishment_strategy)
        agent = agent.change_payoff(payoff)
        bitmap = agent.to_bitmap()
        agent_clone = Agent.bits_to_agent(bitmap)

        self.assertEqual(close_payoff, agent_clone.payoff)

    def test_can_set_cooperated_true(self):
        cooperation_strategy = cs.COOPERATOR
        punishment_strategy = ps.ANTI_SOCIAL

        agent = Agent.create_agent(cooperation_strategy, punishment_strategy)
        new_agent = agent.set_cooperated(True)

        self.assertEqual(1, new_agent.cooperated)

    def test_can_set_cooperated_false(self):
        cooperation_strategy = cs.COOPERATOR
        punishment_strategy = ps.ANTI_SOCIAL

        agent = Agent.create_agent(cooperation_strategy, punishment_strategy)
        new_agent = agent.set_cooperated(False)

        self.assertEqual(0, new_agent.cooperated)

    def test_cooperated_set_defaults_true(self):
        cooperation_strategy = cs.COOPERATOR
        punishment_strategy = ps.ANTI_SOCIAL

        agent = Agent.create_agent(cooperation_strategy, punishment_strategy)
        new_agent = agent.set_cooperated()

        self.assertEqual(1, new_agent.cooperated)
