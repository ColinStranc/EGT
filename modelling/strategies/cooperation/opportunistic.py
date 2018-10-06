import modelling.constants.cooperation_strategies as cs
import modelling.constants.punishement_strategies as ps


class Opportunistic:

    @staticmethod
    def contributes(neighbours, contribution_cost, punishment_fine):
        responsible_punishers = 0
        anti_social_punishers = 0

        for neighbour in neighbours:
            if neighbour.punish_strategy == ps.RESPONSIBLE:
                responsible_punishers += 1
            elif neighbour.punish_strategy == ps.ANTI_SOCIAL:
                anti_social_punishers += 1

        if responsible_punishers - anti_social_punishers > contribution_cost / punishment_fine:
            return True

        return False