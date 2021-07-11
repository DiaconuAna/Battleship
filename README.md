# Battleship
Small implementation of the famous game Battleship I did in my first semester of college.

Rules:
  One's fleet consists of: 
       - 1 Aircraft carrier: 5 squares
       - 1 Battleship: 4 squares
       - 1 Cruiser: 3 squares
       - 2 Destroyers: 2 squares each



 The game does not have a GUI as I did not know pyQT back then, but it is user-friendly nonetheless. 

At first, the player's ships have to be placed on a 10x10 board following the steps: 
    1. Input the ship's name. If the input is invalid, the player will be asked to try again and if the player tries to place a ship that has
       already been placed before, a message will be shown.
    2. Once the ship's name has been entered, the player will be asked to input a column (a letter between A and J), then a row (digit between 0 and 9). Options
       regarding the placement of the other extremity of the ship will be automatically generated and displayed. The player needs to choose the current number associated to each.
    3. The same steps are repeted until all player's ships are placed on the board. The computer ships' positions are generated automatically in a similar manner.
    
    The game starts, two boards being displayed simultaneously. 
    
    Board legend:
    * - square occupied by a ship
    0 - miss
    X - hit
    
    The user board comes first, followed by an initially empty board (the one in which the computer's ships are placed) on which the user has to guess. In order to pick a position,
    the player enters a row number and a column letter and presses enter. At the same time, the computer picks a random position on the player's board.
    
    Once a ship has been sunk, a corresponding message is displayed. (eg. "You sank computer's battleship", "You sank my battleship"). The game ends when either all computer's or 
    player's ships are sunk.
