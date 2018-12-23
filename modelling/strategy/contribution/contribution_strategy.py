from abc import ABC, abstractmethod


class ContributionStrategy(ABC):
	@abstractmethod
	def contributes(self, neighbours):
		pass
