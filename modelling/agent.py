COOPERATION = int('11111000000000000000', 2)
PUNISHMENT = int('00000111110000000000', 2)
FITNESS = int('00000000001111111111', 2)

COOPERATION_SHIFT = 15
PUNISHMENT_SHIFT = 10


class Agent:

    @staticmethod
    def create_agent(cooperation, punishment):
        cooperation_format = (cooperation << COOPERATION_SHIFT) & COOPERATION
        punishment_format = (punishment << PUNISHMENT_SHIFT) & PUNISHMENT
        return cooperation_format + punishment_format

    @staticmethod
    def unlock_cooperation_strategy(bitmap):
        return (bitmap & COOPERATION) >> COOPERATION_SHIFT

    @staticmethod
    def unlock_punishment_strategy(bitmap):
        return (bitmap & PUNISHMENT) >> PUNISHMENT_SHIFT

    @staticmethod
    def unlock_fitness(bitmap):
        return bitmap & FITNESS

    @staticmethod
    def to_string(bitmap):
        c_strat = Agent.unlock_cooperation_strategy(bitmap)
        p_strat = Agent.unlock_punishment_strategy(bitmap)
        fitness = Agent.unlock_fitness(bitmap)

        return "C:{0} P:{1} - Fitness: {2}".format(c_strat, p_strat, fitness)
