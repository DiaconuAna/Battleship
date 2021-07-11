import pygame

from constants.constants import *

WIN = pygame.display.set_mode((WIDTH,  HEIGHT))
pygame.display.set_caption("BATTLESHIP")


def main():
    battle = True
    while battle:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                battle = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

    pygame.quit()

class PCBoard:
    pass

class UserBoard:
    pass

class Display:
    """Class to handle PyGame input and output"""
    colours = {
        "water": pygame.color.Color("blue"),
        "ship": pygame.color.Color("orange"),
        "hit": pygame.color.Color("red"),
        "miss": pygame.color.Color("lightcyan"),
        "background": pygame.color.Color("navy"),
        "text": pygame.color.Color("white")
    }

    def __init__(self, board_size=10, cell_size=30, margin=15):
        self.board_size = board_size
        self.cell_size = cell_size
        self.margin = margin

        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont("Helvetica", 14)

        screen_width = self.cell_size * board_size + 2 * margin
        screen_height = 2 * self.cell_size * board_size + 3 * margin
        self.screen = pygame.display.set_mode(
            [screen_width, screen_height])
        pygame.display.set_caption("Battleships")

    def show(self, upper_board, lower_board, include_top_ships=False):
        """Requests appropriate COlour Grids from boards, and draws them"""
        if upper_board is not None:
            upper_colours = upper_board.colour_grid(
                self.colours, include_top_ships)

        if lower_board is not None:
            lower_colours = lower_board.colour_grid(
                self.colours)

        self.screen.fill(Display.colours["background"])
        for y in range(self.board_size):
            for x in range(self.board_size):

                if upper_board is not None:
                    pygame.draw.rect(self.screen, upper_colours[y][x],
                                     [self.margin + x * self.cell_size,
                                      self.margin + y * self.cell_size,
                                      self.cell_size, self.cell_size])

                if lower_board is not None:
                    offset = self.margin * 2 + self.board_size * self.cell_size
                    pygame.draw.rect(self.screen, lower_colours[y][x],
                                     [self.margin + x * self.cell_size,
                                      offset + y * self.cell_size,
                                      self.cell_size, self.cell_size])

    def get_input(self):
        """Converts MouseEvents into board corrdinates, for input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Display.close()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                y = y % (self.board_size * self.cell_size + self.margin)
                x = (x - self.margin) // self.cell_size
                y = (y - self.margin) // self.cell_size
                if x in range(self.board_size) and y in range(self.board_size):
                    return x, y
        return None, None

    def show_text(self, text, upper=False, lower=False):
        """Displays text on the screen, either upper or lower """
        x = self.margin
        y_up = x
        y_lo = self.board_size * self.cell_size + self.margin
        label = self.font.render(text, True, Display.colours["text"])
        if upper:
            self.screen.blit(label, (x, y_up))
        if lower:
            self.screen.blit(label, (x, y_lo))

    @classmethod
    def flip(cls):
        pygame.display.flip()
        pygame.time.Clock().tick(60)

    @classmethod
    def close(cls):
        pygame.display.quit()
        pygame.quit()

class Game:
    def __init__(self, display, size = 10, game):
        self._display = display
        self._board_size = size
        self._game = game

    def battle(self):
        prev_move = [0, 0]
        is_it_over_yet = False
        user_turn = True

        while not is_it_over_yet:
            try:
                if user_turn:



"""
class Game:
    The overall class to control the game

    def __init__(self, display, size=10, ship_sizes=[6, 4, 3, 3, 2]):
        Sets up the game by generating two Boards
        self.display = display
        self.board_size = size
        self.ai_board = AIBoard(size, ship_sizes)
        self.player_board = PlayerBoard(display, size, ship_sizes)

    def play(self):
        The main game loop, alternating shots until someone wins
        print("Play starts")
        while not self.gameover:
            if self.player_shot():
                self.ai_shot()
            self.display.show(self.ai_board, self.player_board)
            self.display.show_text("Click to guess:")
            Display.flip()

"""

main()