from agent_round import AgentRound

import uuid


class Agent:
	# cooperates(self, neighbours) returns Boolean
	# punishes(self, neighbour) returns Boolean
	# should there be a punishes all neighbours?
	def __init__(self, contribution_strategy, punishment_strategy):
		self._cstrat = contribution_strategy
		self._pstrat = punishment_strategy

		self.results = []
		self.result = AgentRound() 

		self.uid = uuid.uuid4()

	def close_round(self):
		self.results.append(self.result)

		self.result = AgentRound()

	def adjust_fitness(self, amount, absolute_value=False):
		cur = self.result.fitness

		self.result.fitness = amount if absolute_value else cur + amount

	def get_fitness(self):
		return self.result.fitness

	def get_payoff(self):
		return self.result.payoff

	def adjust_payoff(self, amount, absolute_value=False):
		cur = self.result.payoff

		self.result.payoff = amount if absolute_value else cur + amount

	def set_contributed(self, contributed):
		self.result.contributed = contributed

	def get_contributed(self):
		return self.result.contributed

	def contributes(self, neighbours):
		return self._cstrat.contributes(neighbours)

	def punishes_neighbour(self, neighbour):
		return self._pstrat.punishes(neighbour)

	def punishes_neighbours(self, neighbours):
		return [ self.punishes_neighbour(neighbour) for neighbour in neighbours ]

	def punishment_code(self):
		return self._pstrat.code

	def __str__(self):
		f = -1 if not self.result else self.result.fitness
		p = -1 if not self.result else self.result.payoff
		c = -1 if not self.result else int(self.result.contributed)
		return "({},{}) f:{:5.2f} p:{:4.1f} c:{:2.0f}".format(self._cstrat.code, self._pstrat.code, f, p, c)
