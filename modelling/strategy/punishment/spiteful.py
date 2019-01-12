from strategy.punishment.punishment_strategy import PunishmentStrategy


class Spiteful(PunishmentStrategy):
	def __init__(self):
		self.name = "spiteful"
		self.code = "SP"

	def punishes(self, punishment_target):
		return True
