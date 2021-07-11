"""
Each player draws two 10 x 10 grids, labelled along the sides with letters and numbers.
On the left-hand grid the player secretly draws rectangles representing their fleet of ships.
The fleet
Each player's fleet consists of the following ships:

1 x Aircraft carrier - 5 squares
1 x Battleship - 4 squares
1 x Cruiser - 3 squares
2 x Destroyers - 2 squares each
Each ship occupies a number of adjacent squares on the grid, horizontally or vertically.

"""


class Board:
    def __init__(self):
        """
         A board is a list of rows, and each row is a list of cells with either '*' (marking a battleship)
         or a blank ' ' (water)
        """
        self._board = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]

    @property
    def board(self):
        return self._board

    def print_board_2(self):
        return self.board

    def get(self, row, column):
        """
        :param row:
        :param column:
        :return:
        ' ' if the square consists of water(is empty)
        'X' if a ship part has been hit
        '0' if miss
        '*' position of player's ship
        """
        return self.board[row][column]

    def set(self, row, column, symbol):
        self._board[row][column] = symbol

    @staticmethod
    def out_of_bounds(row, column):
        """
        Checks if a set of coordinates are withing the board
        :param row:
        :param column:
        :return: 1 if the square is out of the grid, else 0
        """
        if row < 0 or row > 9:
            return 1
        if column < 0 or column > 9:
            return 1
        return 0

    def mark_ship(self, row, column):
        """
        Mark a part of a ship's position on board
        :param row:
        :param column:
        :return:
        """
        self.board[row][column] = '*'

    def test_if_possible_to_place_on_row(self, start_column, end_column, row):
        """
        Make sure a ship does not overlap with another
        :param start_column:
        :param end_column:
        :param row:
        :return:
        """
        col_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
        start_col = col_dict[start_column]
        end_col = col_dict[end_column]
        if start_col > end_col:
            start_col, end_col = end_col, start_col
        for index in range(start_col, end_col):
            if self.get(row, index) == '*':
                return 0
        return 1

    def fill_row(self, start_column, end_column, row):
        """
        Fill a row with '*' (mark a ship placed on a certain row)
        :param start_column:
        :param end_column:
        :param row:
        :return:
        """
        col_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
        start_col = col_dict[start_column]
        end_col = col_dict[end_column]
        if start_col > end_col:
            start_col, end_col = end_col, start_col
        for index in range(start_col, end_col + 1):
            self.mark_ship(row, index)

    def test_if_possible_to_place_on_column(self, start_row, end_row, column):
        """
        Make sure a ship does not overlap with another
        :param start_row:
        :param end_row:
        :param column:
        :return:
        """
        col_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
        col = col_dict[column]
        if start_row > end_row:
            aux = start_row
            start_row = end_row
            end_row = aux
        for index in range(start_row, end_row):
            if self.get(index, col) == '*':
                return 0
        return 1

    def fill_column(self, start_row, end_row, column):
        """
        Fill a column with '*'(mark a ship placed on a certain column)
        :param start_row:
        :param end_row:
        :param column:
        :return:
        """
        col_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
        col = col_dict[column]
        if start_row > end_row:
            aux = start_row
            start_row = end_row
            end_row = aux
        for index in range(start_row, end_row + 1):
            self.mark_ship(index, col)

    def place_ship(self, extremity_one, extremity_two):
        """
        Mark a ship on the board based on the coordinates of its extremities
        :param extremity_one:
        :param extremity_two:
        :return:
        """
        if extremity_one['row'] == extremity_two['row']:
            self.fill_row(extremity_one['column'], extremity_two['column'], extremity_one['row'])

        if extremity_one['column'] == extremity_two['column']:
            self.fill_column(extremity_one['row'], extremity_two['row'], extremity_one['column'])

    def check_if_ship_has_been_sunk_on_column(self, start_row, end_row, column):
        """
        If a ship has been placed on a column, check if it has been sunk
        (all of its squares are marked with 'X')
        :param start_row:
        :param end_row:
        :param column:
        :return: 1 if the ship has been sunk, 0 otherwise
        """
        col_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
        col = col_dict[column]
        if start_row > end_row:
            aux = start_row
            start_row = end_row
            end_row = aux
        for index in range(start_row, end_row + 1):
            if self.get(index, col) == '*':
                return 0
        return 1

    def check_if_ship_has_been_sunk_on_row(self, start_column, end_column, row):
        """
        If a ship has been placed on a column, check if it has been sunk
        (all of its squares are marked with 'X')
        :param start_column:
        :param end_column:
        :param row:
        :return:
        """
        col_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
        start_col = col_dict[start_column]
        end_col = col_dict[end_column]
        if start_col > end_col:
            start_col, end_col = end_col, start_col
        for index in range(start_col, end_col + 1):
            if self.get(row, index) == '*':
                return 0
        return 1

    def check_if_ship_has_been_sunk(self, ship_coordinates):
        """
        Checks if a ship identified by its extremities' coordinates have been sunk
        (all of its squares are 'X' instead of '*')
        :param ship_coordinates:
        :return: 1 if the ship has been sunk, -1 if the ship has been sunk before, 0 if the ship has not been sunk
        """
        col_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}

        if len(ship_coordinates) == 3:
            if ship_coordinates[-1] == '0':
                return -1
            start = ship_coordinates[0]
            end = ship_coordinates[1]
            if start['row'] == end['row']:
                if self.check_if_ship_has_been_sunk_on_row(start['column'], end['column'], start['row']) == 1:
                    ship_coordinates[-1] = '0'
                    return 1
            elif start['column'] == end['column']:
                if self.check_if_ship_has_been_sunk_on_column(start['row'], end['row'], start['column']) == 1:
                    ship_coordinates[-1] = '0'
                    return 1
            return 0

        elif len(ship_coordinates) == 6:
            #in case of destroyers
            if ship_coordinates[2] != '0':
                start = ship_coordinates[0]
                end = ship_coordinates[1]

                if start['row'] == end['row']:
                    if self.check_if_ship_has_been_sunk_on_row(start['column'], end['column'], start['row']) == 1:
                        ship_coordinates[2] = '0'
                        return 1
                elif start['column'] == end['column']:
                    if self.check_if_ship_has_been_sunk_on_column(start['row'], end['row'], start['column']) == 1:
                        ship_coordinates[2] = '0'
                        return 1

            if ship_coordinates[5] == '0':
                return -1

            start = ship_coordinates[3]
            end = ship_coordinates[4]

            if start['row'] == end['row']:
                if self.check_if_ship_has_been_sunk_on_row(start['column'], end['column'], start['row']) == 1:
                    ship_coordinates[5] = '0'
                    return 1
            elif start['column'] == end['column']:
                if self.check_if_ship_has_been_sunk_on_column(start['row'], end['row'], start['column']) == 1:
                    ship_coordinates[5] = '0'
                    return 1

            if ship_coordinates[2] == '0':
                return -1

            return 0



