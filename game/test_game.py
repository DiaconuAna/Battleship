import unittest

from game.battleship_game import Game


class TestGame(unittest.TestCase):
    def test_game(self):
        self._game = Game()
        self._game._board._board = [
    ['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['*', '*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]

        ships_coordinates = {'aircraft carrier': [{'row': 0, 'column': 'A'}, {'row': 4, 'column': 'A'}, '1'],
                         'battleship': [{'row': 0, 'column': 'C'}, {'row': 3, 'column': 'C'}, '1'],
                         'cruiser': [{'row': 0, 'column': 'B'}, {'row': 2, 'column': 'B'}, '1'],
                         'destroyer': [{'row': 3, 'column': 'B'}, {'row': 4, 'column': 'B'}, '1', {'row': 5, 'column': 'A'}, {'row': 6, 'column': 'A'}, '1']}

        for index in range(5):
            self._game.generate_computer_ships()


        computer_coordinates = {'aircraft carrier': [{'row': 9, 'column': 'D'}, {'row': 5, 'column': 'D'}, '1'],
                                'battleship': [{'row': 0, 'column': 'B'}, {'row': 3, 'column': 'B'}, '1'],
                                'cruiser': [{'row': 2, 'column': 'A'}, {'row': 4, 'column': 'A'}, '1'],
                                'destroyer': [{'row': 5, 'column': 'H'}, {'row': 6, 'column': 'H'}, '1', {'row': 2, 'column': 'H'}, {'row': 3, 'column': 'H'}, '1']}

        self._game._computer_board._board = [
    [' ', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['*', '*', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' '],
    ['*', '*', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' '],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', '*', ' ', ' ', ' ', '*', ' ', ' '],
    [' ', ' ', ' ', '*', ' ', ' ', ' ', '*', ' ', ' '],
    [' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', ' '],
    ]
        user_board = self._game.board
        visibile_computer_board = self._game.seen_computer_board

        self._game.user_move(5, 7)
        square = visibile_computer_board.get(5, 7)
        self.assertEqual(square,'X')

        message = self._game.computer_ship_sunk_check(computer_coordinates)
        self.assertEqual(message, None)

        self._game.user_move(6, 7)
        square = visibile_computer_board.get(6, 7)
        self.assertEqual(square, 'X')

        message = self._game.computer_ship_sunk_check(computer_coordinates)
        self.assertEqual(message, "You sank one of computer's destroyers")

        self._game.user_move(5, 8)
        square = visibile_computer_board.get(5, 8)
        self.assertEqual(square, '0')

        self._game.user_move(5, 3)
        self._game.user_move(6, 3)
        self._game.user_move(7, 3)
        self._game.user_move(8, 3)
        self._game.user_move(9, 3)

        message = self._game.computer_ship_sunk_check(computer_coordinates)
        self.assertEqual(message, "You sank computer's aircraft carrier")

        self._game.user_move(2, 0)
        self._game.user_move(3, 0)
        self._game.user_move(4, 0)

        message = self._game.computer_ship_sunk_check(computer_coordinates)
        self.assertEqual(message, "You sank computer's cruiser")

        self._game.user_move(0, 1)
        self._game.user_move(1, 1)
        self._game.user_move(2, 1)
        self._game.user_move(3, 1)

        message = self._game.computer_ship_sunk_check(computer_coordinates)
        self.assertEqual(message, "You sank computer's battleship")

        self.assertEqual(self._game.computer_ships, 1)

        self._game.print_computer_board()
        self._game.print_user_board()
        self._game.print_opponent_board()

        """
        Computer move time :)
        """
        #Sinking the aircraft carrier
        user_board.set(0,0,'X')
        move = self._game.computer_move([{'row':0,'column':'A'}, 1])
        square = user_board.get(1, 0)
        self.assertEqual(square, 'X')

        move = self._game.computer_move(move)
        move = self._game.computer_move(move)
        move = self._game.computer_move(move)

        msg = self._game.user_ship_sunk_check(ships_coordinates)
        self.assertEqual(msg ,"You sank my aircraft carrier")

        #Sinking the battleship now

        user_board.set(0, 2, 'X')
        move = self._game.computer_move([{'row': 0, 'column': 'C'}, 1])
        square = user_board.get(1, 2)
        self.assertEqual(square, 'X')

        move = self._game.computer_move(move)
        move = self._game.computer_move(move)

        msg = self._game.user_ship_sunk_check(ships_coordinates)
        self.assertEqual(msg, "You sank my battleship")

        #A destroyer
        user_board.set(3, 1 ,'X')
        move = self._game.computer_move([{'row': 3, 'column': 'B'}, 1])
        square = user_board.get(4, 1)
        self.assertEqual(square, 'X')

        msg = self._game.user_ship_sunk_check(ships_coordinates)
        self.assertEqual(msg, "You sank one of my destroyers")

        #And the cruiser
        user_board.set(2, 1, 'X')
        move = self._game.computer_move([{'row': 2, 'column': 'B'}, 1])
        square = user_board.get(1, 1)
        self.assertEqual(square, 'X')

        move = self._game.computer_move(move)
        msg = self._game.user_ship_sunk_check(ships_coordinates)
        self.assertEqual(msg, "You sank my cruiser")

        user_board.set(1,0,' ')
        move = self._game.computer_move([{'row': 1, 'column': 'B'}, 1])
        square = user_board.get(1, 1)
        self.assertEqual(square, 'X')

        user_board.set(1, 2, ' ')
        move = self._game.computer_move([{'row': 1, 'column': 'B'}, 1])
        square = user_board.get(1, 1)
        self.assertEqual(square, 'X')

        user_board.set(1, 0, '*')
        move = self._game.computer_move([{'row': 1, 'column': 'B'}, 1])
        square = user_board.get(1, 1)
        self.assertEqual(square, 'X')

        user_board.set(1, 2, '*')
        move = self._game.computer_move([{'row': 1, 'column': 'B'}, 1])
        square = user_board.get(1, 1)
        self.assertEqual(square, 'X')

        user_board.set(0, 1, ' ')
        move = self._game.computer_move([{'row': 1, 'column': 'B'}, 1])
        square = user_board.get(1, 1)
        self.assertEqual(square, 'X')

        user_board.set(2, 1, ' ')
        move = self._game.computer_move([{'row': 1, 'column': 'B'}, 1])
        square = user_board.get(1, 1)
        self.assertEqual(square, 'X')

        #Sinking the 2nd destroyer

        user_board.set(5, 0 ,'X')
        move = self._game.computer_move([{'row': 5, 'column': 'A'}, 1])
        square = user_board.get(6, 0)
        self.assertEqual(square, 'X')

        msg = self._game.user_ship_sunk_check(ships_coordinates)
        self.assertEqual(self._game.ships, 0)
        self.assertEqual(msg, "You sank one of my destroyers")


        #now we let the computer do a random move
        move = [0,0]
        move = self._game.computer_move(move)
        msg = self._game.user_ship_sunk_check(ships_coordinates)
        while move[1] != 1:
            move = self._game.computer_move(move)





