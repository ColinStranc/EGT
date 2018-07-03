import unittest
from modelling.grid import Grid
import modelling.grid as g
from modelling.agent import Agent


class TestGrid(unittest.TestCase):
    def test_grid_can_be_created_and_it_is_empty(self):
        size = 5
        grid = Grid(size)

        self.assertIsNotNone(grid)
        self.assertEqual(size, grid._size)
        self.assertEqual(0, len(grid.get_occupied_tile_coordinates()))

    def test_default_grid_size(self):
        default_size = g.DEFAULT_GRID_SIZE
        grid = Grid()

        # grid size should be public
        self.assertEqual(default_size, grid._size)

    def test_can_add_agent_to_grid(self):
        grid = Grid()
        agent = Agent.create_random_agent()
        coordinates = (0, 0)

        grid.set_agent(agent, coordinates)
        received_agent = grid.get_agent(coordinates)

        occupied_tiles = grid.get_occupied_tile_coordinates()

        self.assertEqual(1, len(occupied_tiles))
        self.assertEqual(coordinates, occupied_tiles[0])

        self.assertEqual(agent, received_agent)

    def test_can_update_agent_at_grid_location(self):
        grid = Grid()
        first_agent = Agent.create_agent(0, 0)
        agent = Agent.create_agent(0, 1)
        coordinates = (0, 0)

        grid.set_agent(first_agent, coordinates)
        grid.set_agent(agent, coordinates)
        received_agent = grid.get_agent(coordinates)

        occupied_tiles = grid.get_occupied_tile_coordinates()

        self.assertEqual(1, len(occupied_tiles))
        self.assertEqual(coordinates, occupied_tiles[0])

        self.assertEqual(agent, received_agent)

    def test_can_remove_agent(self):
        grid = Grid()
        agent = Agent.create_random_agent()
        coordinates = (0, 0)

        grid.set_agent(agent, coordinates)
        grid.remove_agent(coordinates)
        received_agent = grid.get_agent(coordinates)

        occupied_tiles = grid.get_occupied_tile_coordinates()

        self.assertEqual(0, len(occupied_tiles))
        self.assertIs(None, received_agent)

    def test_grid_can_be_full(self):
        grid = Grid(1)
        grid.set_agent(Agent.create_random_agent(), (0, 0))

        self.assertFalse(grid.has_empty_tiles())
        self.assertFalse(grid.is_tile_vacant((0, 0)))
        self.assertTrue(grid.is_tile_occupied((0, 0)))

    def test_grid_can_have_empty_tiles(self):
        grid = Grid(1)

        self.assertTrue(grid.has_empty_tiles())
        self.assertTrue(grid.is_tile_vacant((0, 0)))
        self.assertFalse(grid.is_tile_occupied((0, 0)))

    def test_grid_can_find_empty_tile_in_empty_grid(self):
        grid = Grid(1)
        empty_tile = grid.get_random_empty_square_coordinates()

        self.assertIsNotNone(empty_tile)

    def test_grid_can_find_empty_tiles_multiple_times(self):
        grid = Grid(2)
        first_empty_tile = grid.get_random_empty_square_coordinates()
        grid.set_agent(Agent.create_random_agent(), first_empty_tile)

        second_empty_tile = grid.get_random_empty_square_coordinates()

        self.assertIsNotNone(second_empty_tile)

    def test_raises_when_trying_to_find_empty_square_in_full_grid(self):
        grid = Grid(1)

        grid.set_agent(Agent.create_random_agent(), (0, 0))

        self.assertRaises(Exception, grid.get_random_empty_square_coordinates)

    def test_raises_when_creating_0_by_0_grid(self):
        self.assertRaises(Exception, Grid, 0)

    def test_fetches_neighbour_agent(self):
        grid = Grid(2)

        agent_coordinates = (0, 0)
        neighbour = Agent.create_random_agent()
        neighbour_coordinates = (1, 0)

        grid.set_agent(neighbour, neighbour_coordinates)

        received_neighbour_coordinates = grid.get_occupied_neighbour_tile_coordinates(agent_coordinates)

        self.assertEqual(1, len(received_neighbour_coordinates))
        self.assertEqual(neighbour_coordinates, received_neighbour_coordinates[0])

    def test_fetches_multiple_neighbour_agents(self):
        grid = Grid(3)

        agent_coordinates = (1, 1)
        neighbour1 = Agent.create_random_agent()
        neighbour1_coordinates = (1, 0)
        neighbour2 = Agent.create_random_agent()
        neighbour2_coordinates = (1, 2)
        neighbour3 = Agent.create_random_agent()
        neighbour3_coordinates = (0, 1)
        neighbour4 = Agent.create_random_agent()
        neighbour4_coordinates = (2, 1)

        grid.set_agent(neighbour1, neighbour1_coordinates)
        grid.set_agent(neighbour2, neighbour2_coordinates)
        grid.set_agent(neighbour3, neighbour3_coordinates)
        grid.set_agent(neighbour4, neighbour4_coordinates)

        neighbour_coordinates = grid.get_occupied_neighbour_tile_coordinates(agent_coordinates)

        self.assertEqual(4, len(neighbour_coordinates))

        self.assertTrue(neighbour1_coordinates in neighbour_coordinates)
        self.assertTrue(neighbour2_coordinates in neighbour_coordinates)
        self.assertTrue(neighbour3_coordinates in neighbour_coordinates)
        self.assertTrue(neighbour4_coordinates in neighbour_coordinates)

    def test_fetches_empty_list_when_no_neighbour(self):
        grid = Grid(2)

        agent_coordinates = (0, 0)

        received_neighbour_coordinates = grid.get_occupied_neighbour_tile_coordinates(agent_coordinates)

        self.assertEqual(0, len(received_neighbour_coordinates))

    def test_does_not_fetch_agent_who_is_not_neighbour(self):
        grid = Grid(2)

        agent_coordinates = (0, 0)
        not_neighbour = Agent.create_random_agent()
        not_neighbour_coordinates = (1, 1)

        grid.set_agent(not_neighbour, not_neighbour_coordinates)

        received_neighbour_coordinates = grid.get_occupied_neighbour_tile_coordinates(agent_coordinates)

        self.assertEqual(0, len(received_neighbour_coordinates))
