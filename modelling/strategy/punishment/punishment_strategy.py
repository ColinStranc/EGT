from abc import ABC, abstractmethod


class PunishmentStrategy(ABC):
	@abstractmethod
	def punishes(self, punishment_target):
		pass
