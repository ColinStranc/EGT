from modelling.agent import Agent
import modelling.constants.cooperation_strategies as coop_strat
import modelling.constants.punishement_strategies as punish_strat


class PublicGoodsGame:
    @staticmethod
    def get_agent_cooperation(agent, neighbours):
        if agent.coop_strategy == coop_strat.COOPERATOR:
            return -1
        elif agent.coop_strategy == coop_strat.DEFECTING:
            return 0
        else:
            responsible_punishers = 0
            anti_social_punishers = 0
            
            for neighbour in neighbours:
                if neighbour.punish_strategy == punish_strat.RESPONSIBLE:
                    responsible_punishers += 1
                elif neighbour.punish_strategy == punish_strat.ANTI_SOCIAL:
                    anti_social_punishers += 1

            if responsible_punishers > anti_social_punishers:
                return -1
            else:
                return 0

    @staticmethod
    def resolve_agent_punishment(agent, neighbours):
        agent_punishment = 0
        for neighbour in neighbours:
            if PublicGoodsGame.__is_agent_punished(agent, neighbour):
                agent_punishment += 3
            
            if PublicGoodsGame.__is_agent_punished(neighbour, agent):
                agent_punishment += 1
        
        return agent_punishment

    @staticmethod
    def __is_agent_punished(agent, punisher):
        agent_contributed = agent.cooperated
        punisher_strat = punisher.punish_strategy

        agent_punished_for_contributing = agent_contributed and punisher_strat in [punish_strat.ANTI_SOCIAL, punish_strat.SPITEFUL]
        agent_punished_for_not_contributing = not agent_contributed and punisher_strat in [punish_strat.RESPONSIBLE, punish_strat.SPITEFUL]
        
        return agent_punished_for_contributing or agent_punished_for_not_contributing
