import modelling.agent as g
import modelling.constants.cooperation_strategies as coop_strat
import modelling.constants.punishement_strategies as punish_strat


class public_goods_games

    def get_agent_cooperation(agent, neighbours):
        if g.Agent.get_cooperation_strategy(agent) == coop_start.COOPERATOR
            return -1
        else if g.Agent.get_cooperation_strategy(agent) == coop_start.DEFECTING
            return 0
        else
            responsible_punishers = 0
            anti_social_punishers = 0
            
            for neighbour in neighbours
                if g.Agent.get_punishment_strategy(neighbour) == punish_strat.RESPONSIBLE
                    responsible_punishers++
                else if g.Agent.get_punishment_strategy(neighbour) == punish_strat.ANTI_SOCIAL
                    anti_social_punishers++

            if responsible_punishers > anti_social_punishers
                return -1
            else
                return 0