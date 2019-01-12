from strategy.contribution.contribution_strategy import ContributionStrategy


class Cooperate(ContributionStrategy):
	def __init__(self):
		self.name = "cooperate"
		self.code = "CO"

	def contributes(self, neighbours):
		return True
