import random

from strategy.contribution.cooperate import Cooperate
from strategy.contribution.defect import Defect 
from strategy.contribution.opportunistic import Opportunistic
from strategy.punishment.anti_social import AntiSocial
from strategy.punishment.non_punishing import NonPunishing 
from strategy.punishment.responsible import Responsible
from strategy.punishment.spiteful import Spiteful


class StrategyFactory:
	def __init__(self, contribution_cost, punishment_fine):
		self._contribution_strategies = [Cooperate, Opportunistic, Defect]
		self._punishment_strategies = [Responsible, AntiSocial, NonPunishing, Spiteful]

		self._cc = contribution_cost
		self._pf = punishment_fine

	def get_random_contribution_strategy(self):
		cs_index = random.randint(0, len(self._contribution_strategies)-1)

		cs_type = self._contribution_strategies[cs_index]
		if cs_type is Opportunistic:
			cs = cs_type(self._cc, self._pf)
		else:
			cs = cs_type()

		return cs

	def get_random_punishment_strategy(self):
		ps_index = random.randint(0, len(self._punishment_strategies)-1)

		ps_type = self._punishment_strategies[ps_index]
		ps = self._punishment_strategies[ps_index]()

		return ps

	def get_cstrat(self, agent):
		cstrat = type(agent._cstrat)

		if cstrat is Opportunistic:
			return cstrat(self._cc, self._pf)
		
		return cstrat()

	def get_pstrat(self, agent):
		return type(agent._pstrat)()
