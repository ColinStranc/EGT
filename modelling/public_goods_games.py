from modelling.agent import Agent
import modelling.constants.cooperation_strategies as coop_strat
import modelling.constants.punishement_strategies as punish_strat


# Should not be static, we need to pass in punishment amount.
class PublicGoodsGame:
    @staticmethod
    def get_agent_cooperation(agent, neighbours):
        cooperated = agent.decide_contribution(neighbours, 1, 3)

        return -1 if cooperated else 0

    @staticmethod
    def resolve_agent_punishment(agent, neighbours):
        agent_punishment = 0

        for neighbour in neighbours:
            agent_punished = agent.decide_punishment(neighbour)
            agent_punishes = neighbour.decide_punishment(agent)

            if agent_punished:
                agent_punishment += 3
            
            if agent_punishes:
                agent_punishment += 1
        
        return agent_punishment
