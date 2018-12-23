from strategy.contribution.contribution_strategy import ContributionStrategy


class Defect(ContributionStrategy):
	def __init__(self):
		self.name = "defect"
		self.code = "DE"

	def contributes(self, neighbours):
		return False
