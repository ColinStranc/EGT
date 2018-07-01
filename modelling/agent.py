from collections import namedtuple

COOPERATION = int('111110000000000000000', 2)
PUNISHMENT = int('000001111100000000000', 2)
COOPERATED = int('000000000010000000000', 2)
FITNESS = int('000000000001111111111', 2)

COOPERATION_SHIFT = 16
PUNISHMENT_SHIFT = 11
COOPERATED_SHIFT = 10

MAX_FITNESS = 100


class Agent(namedtuple('Agent', 'coop_strategy punish_strategy fitness cooperated')):

    @staticmethod
    def bits_to_agent(bitmap):
        cooperation_strategy = (bitmap & COOPERATION) >> COOPERATION_SHIFT
        punishment_strategy = (bitmap & PUNISHMENT) >> PUNISHMENT_SHIFT
        cooperated = (bitmap & COOPERATED) >> COOPERATED_SHIFT
        fitness = bitmap & FITNESS

        return Agent(cooperation_strategy, punishment_strategy, fitness, cooperated)

    def set_cooperated(self, cooperated=True):
        return Agent(self.coop_strategy, self.punish_strategy, self.fitness, cooperated)

    def change_fitness(self, difference_in_fitness):
        old_fitness = self.fitness
        new_fitness = -1

        if old_fitness + difference_in_fitness < 0:
            # log that we aren't letting the fitness go lower than 0
            new_fitness = 0
        elif old_fitness + difference_in_fitness > MAX_FITNESS:
            # log that we are capping the fitness at 100 since it is a percentage
            new_fitness = 100
        else:
            new_fitness = old_fitness + difference_in_fitness

        return Agent(self.coop_strategy, self.punish_strategy, new_fitness, self.cooperated)

    def to_bitmap(self):
        cooperation_bits = self.coop_strategy << COOPERATION_SHIFT
        punishment_bits = self.punish_strategy << PUNISHMENT_SHIFT
        cooperated_bits = self.cooperated << COOPERATED_SHIFT
        fitness_bits = self.fitness

        return cooperation_bits + punishment_bits + cooperated_bits + fitness_bits

    def __str__(self):
        return "C:\"{0:2d}\" P:\"{1:2d}\" c:\"{2:d}\" F:\"{3:3d}\"".format(self.coop_strategy, self.punish_strategy,
                                                                           self.cooperated, self.fitness)
