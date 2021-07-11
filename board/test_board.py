import unittest
from board.battleship_board import Board


class BoardTest(unittest.TestCase):
    def test_board(self):
        self._grid = Board()

        #testing the out of bounds function for out of bounds coordinates
        self.assertEqual(self._grid.out_of_bounds(10, 5), 1)
        self.assertEqual(self._grid.out_of_bounds(5, -1), 1)

        #placing the aircraft carrier and the cruiser on a row, each
        self.assertEqual(self._grid.test_if_possible_to_place_on_row('I', 'E', 2), 1)
        self.assertEqual(self._grid.test_if_possible_to_place_on_row('G', 'I', 4), 1)

        self._grid.place_ship({'row': 2, 'column': 'I'},{'row': 2, 'column': 'E'})
        self._grid.place_ship({'row': 4, 'column': 'G'},{'row': 4, 'column': 'I'})

        self.assertEqual(self._grid.test_if_possible_to_place_on_row('I', 'E', 2), 0)

        #placing the battleship on a column

        self.assertEqual(self._grid.test_if_possible_to_place_on_column(8, 5, 'D'), 1)
        self._grid.place_ship({'row': 5, 'column': 'D'},{'row': 8, 'column': 'D'})

        #placing the destroyers on two rows

        self.assertEqual(self._grid.test_if_possible_to_place_on_row('G', 'F', 0), 1)
        self._grid.place_ship({'row': 0, 'column': 'G'},{'row': 0, 'column': 'F'})

        self.assertEqual(self._grid.test_if_possible_to_place_on_row('G', 'H', 1), 1)
        self._grid.place_ship({'row': 1, 'column': 'G'},{'row': 1, 'column': 'H'})

        #sinking the aircraft carrier
        self._grid.set(2, 4, 'X')
        self._grid.set(2, 5, 'X')
        self._grid.set(2, 6, 'X')
        self._grid.set(2, 7, 'X')
        self._grid.set(2, 8, 'X')

        self.assertEqual(self._grid.check_if_ship_has_been_sunk([{'row': 2, 'column': 'I'},{'row': 2, 'column': 'E'}, 1]), 1)

        #sinking the two destroyers
        self._grid.set(0, 5, 'X')
        self._grid.set(0, 6, 'X')
        self.assertEqual(self._grid.check_if_ship_has_been_sunk([{'row': 0, 'column': 'G'},{'row': 0, 'column': 'F'}, 1, {'row': 1, 'column': 'G'}, {'row': 1, 'column': 'H'},  1]), 1)

        self._grid.set(1, 6, 'X')
        self._grid.set(1, 7, 'X')
        self.assertEqual(self._grid.check_if_ship_has_been_sunk([{'row': 0, 'column': 'G'},{'row': 0, 'column': 'F'}, '0', {'row': 1, 'column': 'G'}, {'row': 1, 'column': 'H'},  1]), 1)

        self._grid.set(1, 7, '*')
        self.assertEqual(self._grid.check_if_ship_has_been_sunk([{'row': 0, 'column': 'G'},{'row': 0, 'column': 'F'}, '0', {'row': 1, 'column': 'G'}, {'row': 1, 'column': 'H'},  1]), -1)



