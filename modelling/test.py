from agent import Agent
from strategy.strategy_factory import StrategyFactory
from model import Model
from grid import Grid
from game import Game

	
print()
print("hola")
print()

base_pay = 10
contribution_cost = 1
punishment_cost = 1/2
punishment_fine = 3/2
multiplication_factor = 3
mutation_rate = 0.1
death_rate = 0.1
dimension = 10
rounds = 50

def testgame():
	sf = StrategyFactory(contribution_cost, punishment_fine)
	a1 = Agent(sf._contribution_strategies[0](), sf._punishment_strategies[0]())
	a1.initialize_round()
	a1.adjust_payoff(10)
	a2 = Agent(sf._contribution_strategies[0](), sf._punishment_strategies[3]())
	a2.initialize_round()
	a2.adjust_payoff(10)
	a3 = Agent(sf._contribution_strategies[2](), sf._punishment_strategies[2]())
	a3.initialize_round()
	a3.adjust_payoff(10)
	grid = Grid(dimension)

	grid.add_agent(a1, (0,0))
	grid.add_agent(a2, (0,1))
	grid.add_agent(a3, (1, 1))

	print(grid)

	game = Game(grid, multiplication_factor, contribution_cost, punishment_fine, punishment_cost)
	game.perform_game()

	print()
	print("-"*60)
	print()

	print(grid)


model = Model(dimension, base_pay, contribution_cost, multiplication_factor, punishment_cost, punishment_fine, mutation_rate, death_rate)
model.run(rounds)

print()
print("adios")
print()
