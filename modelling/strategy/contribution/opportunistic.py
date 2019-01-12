from strategy.contribution.contribution_strategy import ContributionStrategy


class Opportunistic(ContributionStrategy):
	def __init__(self, contribution_cost, punishment_fine):
		self.name = "opportunistic"
		self.code = "OP"

		self._c = contribution_cost
		self._p = punishment_fine

	def contributes(self, neighbours):
		responsible_punishers = 0
		anti_social_punishers = 0

		for neighbour in neighbours:
			if neighbour.punishment_code() == "RE":
				responsible_punishers += 1
			elif neighbour.punishment_code() == "AS":
				anti_social_punishers += 1

		return (responsible_punishers - anti_social_punishers) > (self._c / self._p)
