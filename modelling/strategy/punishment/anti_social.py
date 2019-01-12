from strategy.punishment.punishment_strategy import PunishmentStrategy


class AntiSocial(PunishmentStrategy):
	def __init__(self):
		self.name = "anti-social"
		self.code = "AS"

	def punishes(self, punishment_target):
		if punishment_target.get_contributed():
			return True

		return False
