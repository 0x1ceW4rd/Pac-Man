import unittest
from maze import Maze


class TestMaze(unittest.TestCase):

    def setUp(self):
        # 3 columns, 2 rows
        # All cells have no walls initially
        self.cells = [
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.maze = Maze(3, 2, self.cells)

    def test_cell_inside_maze(self):
        self.assertTrue(self.maze.cell_checker((0, 0)))
        self.assertTrue(self.maze.cell_checker((2, 1)))

    def test_cell_outside_maze(self):
        self.assertFalse(self.maze.cell_checker((-1, 0)))
        self.assertFalse(self.maze.cell_checker((0, -1)))
        self.assertFalse(self.maze.cell_checker((3, 0)))
        self.assertFalse(self.maze.cell_checker((0, 2)))

    def test_direction(self):
        self.assertEqual(self.maze.direction((0, 0), (1, 0)), "RIGHT")
        self.assertEqual(self.maze.direction((1, 0), (0, 0)), "LEFT")
        self.assertEqual(self.maze.direction((0, 0), (0, 1)), "DOWN")
        self.assertEqual(self.maze.direction((0, 1), (0, 0)), "UP")

    def test_invalid_direction(self):
        # Diagonal, too far, and same cell
        self.assertEqual(self.maze.direction((0, 0), (1, 1)), "invalid")
        self.assertEqual(self.maze.direction((0, 0), (2, 0)), "invalid")
        self.assertEqual(self.maze.direction((0, 0), (0, 0)), "invalid")

    def test_move_when_no_walls(self):
        self.assertTrue(self.maze.mv_checker((0, 0), (1, 0)))
        self.assertTrue(self.maze.mv_checker((1, 0), (1, 1)))

    def test_move_blocked_by_current_cell_wall(self):
        # East wall on cell (0, 0)
        self.cells[0][0] = 2
        self.assertFalse(self.maze.mv_checker((0, 0), (1, 0)))

    def test_move_blocked_by_destination_cell_wall(self):
        # West wall on cell (1, 0)
        self.cells[0][1] = 8
        self.assertFalse(self.maze.mv_checker((0, 0), (1, 0)))

    def test_move_invalid_coordinates(self):
        self.assertFalse(self.maze.mv_checker((-1, 0), (0, 0)))
        self.assertFalse(self.maze.mv_checker((0, 0), (3, 0)))

    def test_move_non_adjacent_cells(self):
        self.assertFalse(self.maze.mv_checker((0, 0), (2, 0)))
        self.assertFalse(self.maze.mv_checker((0, 0), (1, 1)))

    def test_move_blocked_by_either_wall(self):
        # Current cell has an East wall; destination has a West wall
        self.cells[0][0] = 2
        self.cells[0][1] = 8
        self.assertFalse(self.maze.mv_checker((0, 0), (1, 0)))


if __name__ == "__main__":
    unittest.main()
