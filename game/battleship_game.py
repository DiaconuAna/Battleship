from board.battleship_board import Board
from random import randrange, choice


class Game:
    def __init__(self):
        """
        self._board = User Board
        self._ships = Number of active user ships
        self._seen_computer_board = The board that the user sees and on which he makes guesses
        """
        self._board = Board()
        self._ships = 5
        self._computer_board = Board()
        self._computer_ships = 5
        self._seen_computer_board = Board()

    @property
    def ships(self):
        """
        Return how  many unsunk ships the user has left
        :return:
        """
        return self._ships

    @property
    def computer_ships(self):
        """
        Return how many unsunk ships the computer has left
        :return:
        """
        return self._computer_ships

    @property
    def board(self):
        """
        User's board
        :return:
        """
        return self._board

    @property
    def seen_computer_board(self):
        """
        The computer board that the user sees and on which he makes guesses
        :return:
        """
        return self._seen_computer_board

    def print_user_board(self):
        board = self.board.print_board_2()
        return board

    def print_opponent_board(self):
        board = self.seen_computer_board.print_board_2()
        return board

    def print_computer_board(self):
        board = self._computer_board.print_board_2()
        return board

    def generate_ship_positions(self, ship_type):
        """
        Randomly placing computer ships on its board
        :param ship_type: the type of ship placed at the current moment
        :return: ship's coordinates or 10,0 if it couldn't be placed in the current iteration
        (it overlapped other ships or it was outside the board)
        """
        ships = {'aircraft carrier': 5, 'battleship': 4, 'cruiser': 3, 'destroyer': 2, 'submarine': 1}
        squares = ships[ship_type] - 1
        rows = [0,1,2,3,4,5,6,7,8,9]
        columns = ['A','B','C','D','E','F','G','H','I','J']
        col_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
        reverse_dict = {'0': 'A', '1': 'B', '2':'C', '3':'D', '4':'E', '5':'F', '6':'G', '7':'H', '8':'I', '9':'J'}

        row = choice(rows)
        column = choice(columns)
        column_number = col_dict[column]
        if 0 <= row + squares <= 9:
            if self._computer_board.test_if_possible_to_place_on_column(row, row+squares, column):
                self._computer_board.fill_column(row, row+squares, column)
                return {'row': row, "column": column}, {'row': row+squares, 'column': column}
        elif 0 <= row - squares <= 9:
            if self._computer_board.test_if_possible_to_place_on_column(row, row-squares, column):
                self._computer_board.fill_column(row, row-squares, column)
                return {'row': row, "column": column}, {'row': row-squares, 'column': column}
        elif 0 <= column_number + squares <= 9:
            if self._computer_board.test_if_possible_to_place_on_row(column_number, column_number+squares, row):
                self._computer_board.fill_row(column, reverse_dict[str(column_number + squares)], row)
                return {'row': row, "column": column}, {'row': row, 'column': reverse_dict[str(column_number + squares)]}
        elif 0 <= column_number - squares <= 9:
            if self._computer_board.test_if_possible_to_place_on_row(column_number, column_number-squares, row):
                self._computer_board.fill_row(column, reverse_dict[str(column_number - squares)], row)
                return {'row': row, "column": column}, {'row': row, 'column': reverse_dict[str(column_number - squares)]}

        return 10, 0

    def generate_computer_ships(self):
        """
        Randomly generate all computer ships
        :return:
        """
        ships_coordinates = {'aircraft carrier': [], 'battleship': [], 'cruiser': [], 'destroyer': []}

        number1, number2 = self.generate_ship_positions('aircraft carrier')
        while number1 == 10:
            number1, number2 = self.generate_ship_positions('aircraft carrier')

        ships_coordinates['aircraft carrier'].append(number1)
        ships_coordinates['aircraft carrier'].append(number2)
        ships_coordinates['aircraft carrier'].append('1')

        number1, number2 = self.generate_ship_positions('battleship')
        while number1 == 10:
            number1, number2 = self.generate_ship_positions('battleship')

        ships_coordinates['battleship'].append(number1)
        ships_coordinates['battleship'].append(number2)
        ships_coordinates['battleship'].append('1')

        number1, number2 = self.generate_ship_positions('cruiser')
        while number1 == 10:
            number1, number2 = self.generate_ship_positions('cruiser')

        ships_coordinates['cruiser'].append(number1)
        ships_coordinates['cruiser'].append(number2)
        ships_coordinates['cruiser'].append('1')

        number1, number2 = self.generate_ship_positions('destroyer')
        while number1 == 10:
            number1, number2 = self.generate_ship_positions('destroyer')

        ships_coordinates['destroyer'].append(number1)
        ships_coordinates['destroyer'].append(number2)
        ships_coordinates['destroyer'].append('1')

        number1, number2 = self.generate_ship_positions('destroyer')
        while number1 == 10:
            number1, number2 = self.generate_ship_positions('destroyer')

        ships_coordinates['destroyer'].append(number1)
        ships_coordinates['destroyer'].append(number2)
        ships_coordinates['destroyer'].append('1')

        return ships_coordinates

    def user_move(self, row, column):
        """
        User makes a move by indicating a square on the board.
        If a part of a ship has been hit, it is marked by X
        If it is a miss, it is marked by 0
        :param row:
        :param column:
        :return: 1 if hit, 0 if missed
        """
        square = self._computer_board.get(row, column)
        if square == '*' or square == 'X':
            self._seen_computer_board.set(row, column, 'X')
            self._computer_board.set(row, column, 'X')
            return 1
        else:
            self._seen_computer_board.set(row, column, '0')
            return 0

    def computer_ship_sunk_check(self, coordinates):
        """
        Check if one or more computer ships have been sunk after the user's last move
        :param coordinates: list of coordinates of all computer ships
        :return:
        """
        number = self._computer_board.check_if_ship_has_been_sunk(coordinates['aircraft carrier'])
        if number == 1:
            self._computer_ships -= 1
            return("You sank computer's aircraft carrier")

        number = self._computer_board.check_if_ship_has_been_sunk(coordinates['battleship'])
        if number == 1:
            self._computer_ships -= 1
            return("You sank computer's battleship")

        number = self._computer_board.check_if_ship_has_been_sunk(coordinates['cruiser'])
        if number == 1:
            self._computer_ships -= 1
            return("You sank computer's cruiser")

        number = self._computer_board.check_if_ship_has_been_sunk(coordinates['destroyer'])
        if number == 1:
            self._computer_ships -= 1
            return("You sank one of computer's destroyers")

        return None

    def user_ship_sunk_check(self, coordinates):
        """
        Check if one or more user ships have been sunk after the computer's last move
        :param coordinates:
        :return:
        """

        number = self._board.check_if_ship_has_been_sunk(coordinates['aircraft carrier'])
        if number == 1:
            self._ships -= 1
            return("You sank my aircraft carrier")

        number = self._board.check_if_ship_has_been_sunk(coordinates['battleship'])
        if number == 1:
            self._ships -= 1
            return("You sank my battleship")

        number = self._board.check_if_ship_has_been_sunk(coordinates['cruiser'])
        if number == 1:
            self._ships -= 1
            return("You sank my cruiser")

        number = self._board.check_if_ship_has_been_sunk(coordinates['destroyer'])
        if number == 1:
            self._ships -= 1
            return("You sank one of my destroyers")
        return None

    def computer_move(self, prev_move):
        """
        Strategic move: if the last move was a hit, the computer seeks to attack the neighbouring squares that are
        within board's bound and have not been missed/hit before
        :param prev_move: if 1, computer seeks to attack nearby squares- list of previous coordinates and success rate
        :return:
        """
        rows = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        col_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
        reverse_dict = {'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H', '8': 'I',
                        '9': 'J'}

        if prev_move[1] == 1:
            row = prev_move[0]['row']
            column = prev_move[0]['column']
            column_number = col_dict[column]

            if self._board.out_of_bounds(row+1, column_number) == 0 and (self._board.get(row+1, column_number) != '0' and self._board.get(row+1, column_number) != 'X'):

                if self._board.get(row+1 , column_number) == '*':
                    self._board.set(row+1, column_number, 'X')
                    return [{'row': row+1, 'column': column}, 1]
                else:
                    self._board.set(row+1, column_number, '0')
                    return prev_move

            elif self._board.out_of_bounds(row-1, column_number) == 0 and (self._board.get(row-1, column_number) != '0' and self._board.get(row-1, column_number) != 'X'):

                if self._board.get(row-1 , column_number) == '*':
                    self._board.set(row - 1, column_number, 'X')
                    return [{'row': row - 1, 'column': column}, 1]
                else:
                    self._board.set(row - 1, column_number, '0')
                    return prev_move

            elif self._board.out_of_bounds(row, column_number - 1) == 0 and (self._board.get(row, column_number-1) !='0' and self._board.get(row, column_number-1) != 'X'):

                if self._board.get(row , column_number - 1) == '*':
                    self._board.set(row, column_number - 1, 'X')
                    return [{'row': row, 'column': reverse_dict[str(column_number - 1)]}, 1]
                else:
                    self._board.set(row, column_number - 1, '0')
                    return prev_move

            elif self._board.out_of_bounds(row, column_number + 1) == 0 and (self._board.get(row, column_number+1) !='0' and self._board.get(row, column_number+1)!='X'):

                if self._board.get(row , column_number+ 1) == '*':
                    self._board.set(row, column_number + 1, 'X')
                    return [{'row': row, 'column': reverse_dict[str(column_number + 1)]}, 1]
                else:
                    self._board.set(row, column_number + 1, '0')
                    return prev_move

        #if the computer doesn't have where to go,it makes a random choice
        row = choice(rows)
        column = choice(columns)
        column_number = col_dict[column]
        while self._board.out_of_bounds(row, column_number) == 1:
            row = choice(rows)
            column = choice(columns)
            column_number = col_dict[column]

        if self._board.get(row, column_number) == '*' or self._board.get(row, column_number) == 'X':
            self._board.set(row, column_number, 'X')
            return [{'row': row, 'column': column}, 1]
        else:
            self._board.set(row, column_number, '0')
            return [{'row': row, 'column': column}, 0]





