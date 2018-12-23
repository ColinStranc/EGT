from strategy.punishment.punishment_strategy import PunishmentStrategy


class Responsible(PunishmentStrategy):
	def __init__(self):
		self.name = "responsible"
		self.code = "RE"

	def punishes(self, punishment_target):
		if not punishment_target.get_contributed():
			return True 

		return False 
