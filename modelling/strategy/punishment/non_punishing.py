from strategy.punishment.punishment_strategy import PunishmentStrategy


class NonPunishing(PunishmentStrategy):
	def __init__(self):
		self.name = "non-punishing"
		self.code = "NP"

	def punishes(self, punishment_target):
		return False
