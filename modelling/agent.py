from collections import namedtuple
import modelling.constants.cooperation_strategies as cs
import modelling.constants.punishement_strategies as ps
from modelling.strategies.cooperation.cooperate import Cooperate
from modelling.strategies.cooperation.defect import Defect
from modelling.strategies.cooperation.opportunistic import Opportunistic
from modelling.strategies.punishment.non_punishing import NonPunishing
from modelling.strategies.punishment.anti_social import AntiSocial
from modelling.strategies.punishment.spiteful import Spiteful
from modelling.strategies.punishment.responsible import Responsible

import math
import random

COOPERATION = int('1111100000000000000000', 2)
PUNISHMENT = int('0000011111000000000000', 2)
COOPERATED = int('0000000000100000000000', 2)
PAYOFF = int('0000000000001111111111', 2)
NEW_AGENT = int('0000000000010000000000', 2)

COOPERATION_SHIFT = 17
PUNISHMENT_SHIFT = 12
COOPERATED_SHIFT = 11
NEW_AGENT_SHIFT = 10

PAYOFF_DECIMAL_COUNT = 3
MAX_PAYOFF = PAYOFF / 2**PAYOFF_DECIMAL_COUNT


class Agent(namedtuple('Agent', 'coop_strategy punish_strategy payoff cooperated new_agent')):

    @staticmethod
    def create_random_agent():
        strategies = Agent.get_random_strategies()
        return Agent.create_agent(strategies[0], strategies[1])

    @staticmethod
    # Only called when a new Agent is created, only way to have the "new_agent" bit set to 1
    #  during agent modifications you should call the methods designed for that modification instead
    def create_agent(coop_strategy, punish_strategy):
        return Agent(coop_strategy, punish_strategy, payoff=0.0, cooperated=0, new_agent=1)

    # This should not take for granted the magic numbers...
    @staticmethod
    def get_random_strategies():
        coop_random_number = random.randrange(0, 3)
        punish_random_number = random.randrange(0, 4)

        return coop_random_number + 1, punish_random_number + 1

    @staticmethod
    def get_fitness_from_payoff(payoff):
        return 1 - math.exp(-0.1 * payoff)

    @staticmethod
    def bits_to_agent(bitmap):
        cooperation_strategy = (bitmap & COOPERATION) >> COOPERATION_SHIFT
        punishment_strategy = (bitmap & PUNISHMENT) >> PUNISHMENT_SHIFT
        cooperated = (bitmap & COOPERATED) >> COOPERATED_SHIFT
        new_agent = (bitmap & NEW_AGENT) >> NEW_AGENT_SHIFT
        payoff = (bitmap & PAYOFF) / 2**PAYOFF_DECIMAL_COUNT

        return Agent(cooperation_strategy, punishment_strategy, payoff, cooperated, new_agent)

    def set_cooperated(self, cooperated=True):
        return Agent(self.coop_strategy, self.punish_strategy, self.payoff, cooperated, self.new_agent)

    def change_payoff(self, difference_in_payoff):
        old_payoff = self.payoff

        if old_payoff + difference_in_payoff < 0:
            # log that we aren't letting the payoff go lower than 0
            new_payoff = 0
        elif old_payoff + difference_in_payoff > MAX_PAYOFF:
            # log that we are capping the payoff at MAX_PAYOFFto avoid overflowing into other parts of the bitmap
            new_payoff = MAX_PAYOFF
        else:
            # find the nearest value whos decimal is a power of two that we can do
            difference_in_payoff = math.floor(difference_in_payoff * 2**PAYOFF_DECIMAL_COUNT) / 2**PAYOFF_DECIMAL_COUNT
            new_payoff = old_payoff + difference_in_payoff

        return Agent(self.coop_strategy, self.punish_strategy, new_payoff, self.cooperated, self.new_agent)

    def decide_contribution(self, neighbours, contribution_cost, punishment_fine):
        contributed = False

        if self.coop_strategy == cs.COOPERATOR:
            contributed = Cooperate.contributes(neighbours, contribution_cost, punishment_fine)
        elif self.coop_strategy == cs.DEFECTING:
            contributed = Defect.contributes(neighbours, contribution_cost, punishment_fine)
        elif self.coop_strategy == cs.OPPORTUNISTIC:
            contributed = Opportunistic.contributes(neighbours, contribution_cost, punishment_fine)

        return contributed

    def decide_punishment(self, neighbour):
        punishes = False

        if self.punish_strategy == ps.ANTI_SOCIAL:
            punishes = AntiSocial.punishes(self, neighbour)
        elif self.punish_strategy == ps.RESPONSIBLE:
            punishes = Responsible.punishes(self, neighbour)
        elif self.punish_strategy == ps.NON_PUNISHER:
            punishes = NonPunishing.punishes(self, neighbour)
        elif self.punish_strategy == ps.SPITEFUL:
            punishes = Spiteful.punishes(self, neighbour)

        return punishes

    def change_strategies(self, new_coop_strategy, new_punish_strategy):
        return Agent(new_coop_strategy, new_punish_strategy, self.payoff, self.cooperated, self.new_agent)

    def clear_payoff(self):
        return Agent(self.coop_strategy, self.punish_strategy, 0, self.cooperated, self.new_agent)

    def clear_new_status(self):
        return Agent(self.coop_strategy, self.punish_strategy, self.payoff, self.cooperated, 0)

    def to_bitmap(self):
        cooperation_bits = self.coop_strategy << COOPERATION_SHIFT
        punishment_bits = self.punish_strategy << PUNISHMENT_SHIFT
        cooperated_bits = self.cooperated << COOPERATED_SHIFT
        new_bits = self.new_agent << NEW_AGENT_SHIFT
        # Make decimals into int by shifting up the necessary bits. It should have been made rounded by change_payoff
        payoff_bits = int(self.payoff * 2**PAYOFF_DECIMAL_COUNT)

        return cooperation_bits + punishment_bits + cooperated_bits + new_bits + payoff_bits

    def __str__(self):
        novelty = "new" if self.new_agent else "old"
        return "C:\"{0:2d}\" P:\"{1:2d}\" c:\"{2:d}\" F:\"{3:6.3f}\", {4}".format(self.coop_strategy, self.punish_strategy,
                                                                           self.cooperated, self.payoff, novelty)
