from fractions import Fraction


class Settings:
	def __init__(self, dimension, base_pay, contribution_cost, multiplication_factor, punishment_cost, punishment_fine, mutation_rate, death_rate, threat_level, rounds):
		self.base_pay = base_pay
		self.contribution_cost, self.contribution_cost_num, self.contribution_cost_dn = self._frac(contribution_cost)
		self.multiplication_factor = multiplication_factor
		self.punishment_cost, self.punishment_cost_num, self.punishment_cost_dn = self._frac(punishment_cost)
		self.punishment_fine, self.punishment_fine_num, self.punishment_fine_dn = self._frac(punishment_fine)
		self.mutation_rate, self.mutation_rate_num, self.mutation_rate_dn = self._frac(mutation_rate)
		self.death_rate, self.death_rate_num, self.death_rate_dn = self._frac(death_rate)
		self.threat_level = threat_level
		self.dimension = dimension
		self.rounds = rounds

	def _frac(self, r):
		f = Fraction(r).limit_denominator(64)

		# Fractions _may_ lose accuracy. We start using the result of the fraction so everything will stay in sync from now on
		return f.numerator / f.denominator, f.numerator, f.denominator
