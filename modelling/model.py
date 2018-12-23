from math import exp
import random

from agent import Agent
from game import Game
from grid import Grid
from strategy.strategy_factory import StrategyFactory


class Model:
	def __init__(self, dimension, base_pay, contribution_cost, multiplication_factor, punishment_cost, punishment_fine, mutation_rate, death_rate):
		self._bp = base_pay
		self._cc = contribution_cost
		self._mf = multiplication_factor
		self._pc = punishment_cost
		self._pf = punishment_fine
		self._mr = mutation_rate
		self._dr = death_rate

		self._g = Grid(dimension)
		self._sf = StrategyFactory(self._cc, self._pf)

	def run(self, rounds):
		for i in range(rounds):
			print("###### Round {} ######".format(i+1))
			self._run_round()
			self._summary()
			print(self._g)

			for agent in self._g.get_agents():
				agent.close_round()

	def _summary(self):
		op,co,de = 0,0,0
		ans,sp,np,re = 0,0,0,0

		for agent in self._g.get_agents():
			if agent._cstrat.code == "OP":
				op += 1
			elif agent._cstrat.code == "CO":
				co += 1
			elif agent._cstrat.code == "DE":
				de += 1

			if agent._pstrat.code == "AS":
				ans += 1
			elif agent._pstrat.code == "SP":
				sp += 1
			elif agent._pstrat.code == "NP":
				np += 1
			elif agent._pstrat.code == "RE":
				re += 1

		print("Contribution:\n {} Cooperaters\n {} Defecters\n {} Opportunistic".format(co, de, op))
		print("Punishment:\n {} Responsible\n {} Spiteful\n {} Non-Punishing\n {} Anti-Social".format(re, sp, np, ans))

	def _run_round(self):
		self._birth()
		self._calculate_fitness()
		self._reproduce()
		self._mutate()
		self._death()

	def _death(self):
		for agent in self._g.get_agents():
			if self._dies(agent):
				print("Agent {} died.".format(agent.uid))
				self._g.remove_agent(agent)

	def _dies(self, agent):
		return random.random() < self._dr

	def _mutate(self):
		for agent in self._g.get_agents():
			if self._mutates(agent):
				new_cstrat = self._sf.get_random_contribution_strategy()
				new_pstrat = self._sf.get_random_punishment_strategy()
				print("Agent {} mutates ({}, {}) -> ({}, {})".format(agent.uid, agent._cstrat.code, agent._pstrat.code, new_cstrat.code, new_pstrat.code))
				agent._cstrat = new_cstrat
				agent._pstrat = new_pstrat

	def _mutates(self, agent):
		return random.random() < self._mr

	def _reproduce(self):
		for agent in self._g.get_agents():
			if self._agent_reproduces(agent):
				coordinate = self._g.get_coordinates_of_agent(agent)
				empty_neighbour_coordinates = self._g.get_empty_neighbour_coordinates(coordinate)

				if len(empty_neighbour_coordinates) == 0:
					# no coordinates to reproduce into, sorry bud.
					pass
				else:
					c = empty_neighbour_coordinates[random.randint(0, len(empty_neighbour_coordinates)-1)]

					new_cstrat = self._sf.get_cstrat(agent)
					new_pstrat = self._sf.get_pstrat(agent)
					new_agent = Agent(new_cstrat, new_pstrat)

					print("Agent {} (f:{}) reproduced agent {} ({})".format(agent.uid, agent.get_fitness(), new_agent.uid, c))

					self._g.add_agent(new_agent, c)

	def _agent_reproduces(self, agent):
		return random.random() < agent.get_fitness()

	def _assign_base_payoffs(self):
		for agent in self._g.get_agents():
			agent.adjust_payoff(self._bp)

	def _calculate_fitness(self):
		self._assign_base_payoffs()
		game = Game(self._g, self._mf, self._cc, self._pf, self._pc)
		game.perform_game()
		self._assign_fitnesses()

	def _assign_fitnesses(self):
		for agent in self._g.get_agents():
			fitness = self._calculate_fitnesses(agent.get_payoff())
			agent.adjust_fitness(fitness)

	def _calculate_fitnesses(self, payoff):
		return 1 - exp(-0.1 * payoff)

	def _birth(self):
		possible_birth_coordinates = self._g.get_open_coordinates()

		if len(possible_birth_coordinates) == 0:
			# Grid appears full already, no space for births
			return

		birth_coordinate = possible_birth_coordinates[random.randint(0, len(possible_birth_coordinates)-1)]

		cs = self._sf.get_random_contribution_strategy()
		ps = self._sf.get_random_punishment_strategy()
		agent = Agent(cs, ps)

		print("Agent {} ({}, {}) was born.".format(agent.uid, agent._cstrat.code, agent._pstrat.code))

		self._g.add_agent(agent, birth_coordinate)
