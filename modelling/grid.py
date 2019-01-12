import numpy as np

from agent import Agent


class Grid:
	def __init__(self, dimension):
		self._d = dimension

		self._grid = np.ndarray((self._d, self._d), Agent)

	def get_open_coordinates(self):
		open_coordinates = []

		for x in range(self._d):
			for y in range(self._d):
				if self._grid[x, y] is None:
					open_coordinates.append((x, y))

		return open_coordinates

	def add_agent(self, agent, coordinate, replace=False):
		if self._grid[coordinate] is not None and not replace:
			raise Exception("Agent already exists, cannot add new agent to coordinate")

		self._grid[coordinate] = agent

	def remove_agent(self, agent):
		c = self.get_coordinates_of_agent(agent)

		self._grid[c] = None

	def get_agents(self):
		agents = []

		for x in range(self._d):
			for y in range(self._d):
				if self._grid[x, y] is not None:
					agents.append(self.get_agent((x, y)))

		return agents

	def get_agent(self, coordinate):
		return self._grid[coordinate]

	def _get_occupied_coordinates(self):
		coordinates = []

		for x in range(self._d):
			for y in range(self._d):
				if self._grid[x, y] is not None:
					coordinates.append((x, y))

		return coordinates

	def _get_neighbouring_coordinates(self, coordinate):
		x = coordinate[0]
		y = coordinate[1]
		x_above = (x-1) % self._d
		x_below = (x+1) % self._d
		y_above = (y-1) % self._d
		y_below = (y+1) % self._d

		return list(set([(x_above, y), (x, y_below), (x_below, y), (x, y_above)]))

	def _get_neighbours_of_coordinate(self, coordinate):
		neighbour_coordinates = self._get_neighbouring_coordinates(coordinate)

		neighbours = [ self.get_agent(nc) for nc in neighbour_coordinates if self.get_agent(nc) is not None ]

		return neighbours

	def get_coordinates_of_agent(self, agent):
		target_uid = agent.uid

		occupied_coordinates = self._get_occupied_coordinates()

		for occupied_coordinate in occupied_coordinates:
			a = self.get_agent(occupied_coordinate)

			if a.uid == target_uid:
				return occupied_coordinate

		return None

	def get_empty_neighbour_coordinates(self, coordinate):
		neighbouring_coordinates = self._get_neighbouring_coordinates(coordinate)

		cs = [ c for c in neighbouring_coordinates if self.get_agent(c) is None ]

		return cs

	def get_neighbours_of_agent(self, agent):
		target_coordinates = self.get_coordinates_of_agent(agent)
		return self._get_neighbours_of_coordinate(target_coordinates)

	def __str__(self):
		text = ""

		for x in range(self._d):
			for y in range(self._d):
				a = self._grid[x, y]

				if a is None:
					text = text + "---------------------------  "
				else:
					text = text + a.__str__() + "  "

			text = text[:-2] + "\n"
		text = text[:-1]

		return text
