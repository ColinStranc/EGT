import argparse

from model import Model

def setup_args():
	parser = argparse.ArgumentParser()

	parser.add_argument('--bp')
	parser.add_argument('--cc')
	parser.add_argument('--pc')
	parser.add_argument('--pf')
	parser.add_argument('--mf')
	parser.add_argument('--mr')
	parser.add_argument('--dr')
	parser.add_argument('-d')
	parser.add_argument('-r')

	args = parser.parse_args()

	return args


print("Starting...")

args = setup_args()

base_pay = double(args.bp) if args.bp else 30
contribution_cost = double(args.cc) if args.cc else 1
punishment_cost = double(args.pc) if args.pc else 1/2
punishment_fine = double(args.pf) if args.pf else 3/2
multiplication_factor = double(args.mf) if args.mf else 3
mutation_rate = double(args.mr) if args.mr else 0.1
death_rate = double(args.dr) if args.dr else 0.1
dimension = int(args.d) if args.d else 50
rounds = int(args.r) if args.r else 20

model = Model(dimension, base_pay, contribution_cost, multiplication_factor, punishment_cost, punishment_fine, mutation_rate, death_rate)

model.run(rounds)

print("Finished")
