from game.battleship_game import Game


class UI:
    def __init__(self):
        self._game = Game()

    @staticmethod
    def battleships():
        print("Your fleet consists of: ")
        print("1 Aircraft carrier: 5 squares")
        print("1 Battleship: 4 squares")
        print("1 Cruiser: 3 squares")
        print("2 Destroyers: 2 squares each")
        print("*****---------*********")
        print("Pick your positions wisely!")
        print("*****---------*********")

    def place_battleship(self, type):
        """
        Place a battleship given by type on board (user's)
        You pick the coordinates of an extremity and the computer
        offers you the alternatives for the other extremity so that the ship
        does not overlap with other ships and it's placed within the board
        :param type: ship type
        :return: the coordinates of the ship
        """
        possible_positions = []
        ships = {'aircraft carrier': 5, 'battleship': 4, 'cruiser': 3,'destroyer': 2}
        col_dict = {'A': 0, 'B': 1, 'C': 2, 'D':3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
        reverse_dict = {'0': 'A', '1': 'B', '2':'C', '3':'D', '4':'E', '5':'F', '6':'G', '7':'H', '8':'I', '9':'J'}
        if type not in ships:
            raise ValueError("Invalid ship type.")
        ship = ships[type]

        #Establishing one extremity of the ship
        print("Where do you want to place ", type, "?")
        column = input("column (A to J): ")
        if column not in col_dict:
            raise ValueError("Invalid column input")
        column_number = col_dict[column]
        row = int(input("row (0 to 9): "))
        if not (0 <= row <= 9):
            raise ValueError("Invalid row input")

        if self._game.board.out_of_bounds(row, column_number):
            raise ValueError("Out of bounds!")

        #Now we need to place the entire ship
        possible_row = row + ship - 1
        if 0 <= possible_row <= 9:
            if self._game.board.test_if_possible_to_place_on_column(row, possible_row, column):
                possible_positions.append({'row': possible_row, 'column': column})

        possible_row = row - ship + 1
        if 0 <= possible_row <= 9:
            if self._game.board.test_if_possible_to_place_on_column(row, possible_row, column):
                possible_positions.append({'row': possible_row, 'column': column})

        possible_column = column_number + ship - 1
        if 0 <= possible_column <= 9:
            if self._game.board.test_if_possible_to_place_on_row(column, reverse_dict[str(possible_column)], row):
                possible_positions.append({'row': row, 'column': reverse_dict[str(possible_column)]})

        possible_column = column_number - ship + 1
        if 0 <= possible_column <= 9:
            if self._game.board.test_if_possible_to_place_on_row(column, reverse_dict[str(possible_column)], row):
                possible_positions.append({'row': row, 'column': reverse_dict[str(possible_column)]})

        if len(possible_positions) == 0:
            print("Your ships are overlaping... please pick another position...")
            return 10, 0
        print("Where would you like to place the other extremity of the ship? ")
        for index in range(len(possible_positions)):
            print(index, end='. ')
            position = possible_positions[index]
            print(position['column'], position['row'])

        option_number = int(input("Enter number of option: "))
        if not (0 <= option_number <= len(possible_positions)):
            raise ValueError("Invalid option number!")

        new_row = possible_positions[option_number]['row']
        new_column = possible_positions[option_number]['column']

        self._game.board.place_ship({'row': row, "column": column}, {'row': new_row, 'column': new_column})
        return {'row': row, "column": column}, {'row': new_row, 'column': new_column}

    def unplaced_ships(self, ships):
        """
        Checks how many ships are there yet to be placed
        :param ships:-
        :return: number of ships that haven't been placed yet
        """
        index = 0
        if ships["aircraft carrier"] != 0:
            print("1 Aircraft Carrier")
            index += 1

        if ships["battleship"] != 0:
            print("1 Battleship")
            index += 1

        if ships["cruiser"] != 0:
            print("1 Cruiser")
            index += 1

        if ships["destroyer"] != 0:
            print(ships["destroyer"], "Destroyer(s)")
            index += ships['destroyer']

        return index

    def place_battleships(self):
        """
        We place the battleships on our board
        For each placed ship we save its coordinates and a flag that marks that the ship has not been sunk yet( is 1)
        :return: list of coordinates and sink status for each ship
        """
        self.battleships()
        ships = {'aircraft carrier': 1, 'battleship': 1, 'cruiser': 1, 'destroyer': 2}
        ships_coordinates = {'aircraft carrier': [], 'battleship': [], 'cruiser': [], 'destroyer': []}
        over = 0
        while not over:
            index = self.unplaced_ships(ships)
            if index == 0:
                return ships_coordinates
            self.print_user_board()
            ship = input("Which ship would you like to place? >>> ")
            if ship.lower() in ships:
                if ships[ship.lower()] == 0:
                    print(ship, "has already been placed. Please place an unplaced ship. ")
                else:
                    number1, number2 = self.place_battleship(ship.lower())
                    while number1 == 10:
                        number1, number2 = self.place_battleship(ship.lower())

                    ships_coordinates[ship.lower()].append(number1)
                    ships_coordinates[ship.lower()].append(number2)
                    ships_coordinates[ship.lower()].append('1')
                    ships[ship.lower()] -= 1

                    index -= 1

    def user_move(self, computer_coordinates):
        """
        Inputting coordinates for the user move
        :return:
        """
        col_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
        row = int(input("Input row(0 to 9)>>"))
        column = input("Input column(A to J)>>")

        if 0 <= row <= 9 and column in col_dict:
            result = self._game.user_move(row, col_dict[column])
            if result == 1:
                print("HIT!")
                message = self._game.computer_ship_sunk_check(computer_coordinates)
                if message is not None:
                    print(message)
            elif result == 0:
                print("MISS!")
        else:
            raise ValueError("Invalid input. Try again, this time WITHIN the board :)")

    def print_user_board(self):
        board = self._game.print_user_board()
        self.print_board(board)

    def print_opponent_board(self):
        board = self._game.print_opponent_board()
        self.print_board(board)

    @staticmethod
    def print_row(row):
        for square in row:
            print(square, end=' ')
        print("|", end='')

    def print_board(self, board):
        # Show the board, one row at a time
        print("  A B C D E F G H I J ")
        print("  -------------------- ")
        row_number = 1
        for row in board:
            print(row_number-1, end = "|")
            self.print_row(row)
            print()
            row_number = row_number + 1
        print("  -------------------- ")

    def start(self):
        computer_coordinates = self._game.generate_computer_ships()
        print(computer_coordinates['aircraft carrier'])
        print(computer_coordinates['battleship'])
        print(computer_coordinates['cruiser'])
        print(computer_coordinates['destroyer'])

        try:
            user_coordinates = self.place_battleships()
        except ValueError as err:
            print(str(err))
            return 0

        prev_move = [0,0]
        is_it_over_yet = False
        user_turn = True

        while not is_it_over_yet:
            try:
                if user_turn:
                    # Printing user's board and computer's user-visible board
                    print("This is your board for the time being: ")
                    self.print_user_board()
                    print("And you guess here.")
                    self.print_opponent_board()

                    self.user_move(computer_coordinates)
                    if self._game.computer_ships == 0:
                        print("You win!")
                        is_it_over_yet = True
                else:
                    prev_move = self._game.computer_move(prev_move)
                    if prev_move[1] == 1:
                        message = self._game.user_ship_sunk_check(user_coordinates)
                        if message is not None:
                            print(message)

                    if self._game.ships == 0:
                        print("Computer wins!")
                        is_it_over_yet = True
                user_turn = not user_turn
            except ValueError as error:
                print(str(error))


if __name__ == '__main__':
    game = UI()
    game.start()

