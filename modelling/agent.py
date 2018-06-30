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
    def get_cooperation_strategy(bitmap):
        return (bitmap & COOPERATION) >> COOPERATION_SHIFT

    @staticmethod
    def get_punishment_strategy(bitmap):
        return (bitmap & PUNISHMENT) >> PUNISHMENT_SHIFT

    @staticmethod
    def get_fitness(bitmap):
        return bitmap & FITNESS

    @staticmethod
    def add_fitness(bitmap, amount):
        current_fitness = bitmap & FITNESS

        # We can't go negative, so if we are subtracting more than exists, just move it to 0
        if amount < 0 and current_fitness < abs(amount):
            return bitmap - current_fitness

        new_fitness = current_fitness + amount

        if new_fitness > FITNESS:
            raise Exception("Fitness exceeded limit")

        return bitmap + amount

    @staticmethod
    def _subtract_fitness(bitmap, amount):
        current_fitness = bitmap & FITNESS

        # We can't go negative, so 5 - 10 = 0
        if current_fitness < amount:
            return bitmap - current_fitness

        return bitmap - amount

    @staticmethod
    def to_string(bitmap):
        if bitmap == 0:
            return "Empty Hub"

        c_strat = Agent.get_cooperation_strategy(bitmap)
        p_strat = Agent.get_punishment_strategy(bitmap)
        fitness = Agent.get_fitness(bitmap)

        return "{0:2d} {1:2d} {2:3d}".format(c_strat, p_strat, fitness)
