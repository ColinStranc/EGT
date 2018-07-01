from collections import namedtuple
import modelling.constants.cooperation_strategies as cs
import modelling.constants.punishement_strategies as ps

import math
import random

COOPERATION = int('111110000000000000000', 2)
PUNISHMENT = int('000001111100000000000', 2)
COOPERATED = int('000000000010000000000', 2)
PAYOFF = int('000000000001111111111', 2)

COOPERATION_SHIFT = 16
PUNISHMENT_SHIFT = 11
COOPERATED_SHIFT = 10

MAX_PAYOFF = PAYOFF


class Agent(namedtuple('Agent', 'coop_strategy punish_strategy payoff cooperated')):

    # This should not take for granted the magic numbers...
    @staticmethod
    def get_random_strategies():
        coop_random_number = random.randrange(0, 3)
        punish_random_number = random.randrange(0, 4)

        return coop_random_number + 1, punish_random_number + 1

    @staticmethod
    def get_fitness_from_payoff(payoff):
        # exponent = -0.1*payoff
        # exponential = math.exp()

        return 1 - math.exp(-0.1 * payoff)

    @staticmethod
    def bits_to_agent(bitmap):
        cooperation_strategy = (bitmap & COOPERATION) >> COOPERATION_SHIFT
        punishment_strategy = (bitmap & PUNISHMENT) >> PUNISHMENT_SHIFT
        cooperated = (bitmap & COOPERATED) >> COOPERATED_SHIFT
        payoff = bitmap & PAYOFF

        return Agent(cooperation_strategy, punishment_strategy, payoff, cooperated)

    def set_cooperated(self, cooperated=True):
        return Agent(self.coop_strategy, self.punish_strategy, self.payoff, cooperated)

    def change_payoff(self, difference_in_payoff):
        old_payoff = self.payoff
        new_payoff = -1

        if old_payoff + difference_in_payoff < 0:
            # log that we aren't letting the payoff go lower than 0
            new_payoff = 0
        elif old_payoff + difference_in_payoff > MAX_PAYOFF:
            # log that we are capping the payoff at 100 since it is a percentage
            new_payoff = 100
        else:
            new_payoff = old_payoff + difference_in_payoff

        return Agent(self.coop_strategy, self.punish_strategy, new_payoff, self.cooperated)

    def clear_payoff(self):
        return Agent(self.coop_strategy, self.punish_strategy, 0, self.cooperated)

    def to_bitmap(self):
        cooperation_bits = self.coop_strategy << COOPERATION_SHIFT
        punishment_bits = self.punish_strategy << PUNISHMENT_SHIFT
        cooperated_bits = self.cooperated << COOPERATED_SHIFT
        payoff_bits = self.payoff

        return cooperation_bits + punishment_bits + cooperated_bits + payoff_bits

    def __str__(self):
        return "C:\"{0:2d}\" P:\"{1:2d}\" c:\"{2:d}\" F:\"{3:3d}\"".format(self.coop_strategy, self.punish_strategy,
                                                                           self.cooperated, self.payoff)
