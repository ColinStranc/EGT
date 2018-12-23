class Game:
	def __init__(self, grid, mf, cc, pf, pc):
		self._g = grid
		self._mf = mf
		self._cc = cc
		self._pf = pf
		self._pc = pc

	def perform_game(self):
		payoff_pool = self._handle_contributions()
		self._make_punishments()
		self._assign_payoffs(payoff_pool)

	def _assign_payoffs(self, pool):
                agents = self._g.get_agents()
                n = len(agents)

                agents_payoff = pool / n


                for agent in agents:
                        agent.adjust_payoff(agents_payoff)

	def _handle_contributions(self):
		payoff_pool = 0
		for agent in self._g.get_agents():
			if agent.contributes(self._g.get_neighbours_of_agent(agent)):
				print("Agent {} ({}) contributed.".format(agent.uid, agent._cstrat.code))
				payoff_pool += self._cc
				agent.adjust_payoff(-self._cc)
				agent.set_contributed(True)
			else:
				agent.set_contributed(False)

		return payoff_pool * self._mf

	def _make_punishments(self):
                for agent in self._g.get_agents():
                        neighbours = self._g.get_neighbours_of_agent(agent)

                        punishments = agent.punishes_neighbours(neighbours)

                        for neighbour, punishes in zip(neighbours, punishments):
                                if punishes:
                                        print("Agent {} ({}) punished agent {} ({}).".format(agent.uid, agent._pstrat.code, neighbour.uid, neighbour._cstrat.code))
                                        neighbour.adjust_payoff(-self._pf)
                                        agent.adjust_payoff(-self._pc)
