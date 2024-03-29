import csv
import os
import random
import sys


# The Three Musketeers Game

# In all methods,
#   A 'location' is a two-tuple of integers, each in the range 0 to 4.
#        The first integer is the row number, the second is the column number.
#   A 'direction' is one of the strings "up", "down", "left", or "right".
#   A 'board' is a list of 5 lists, each containing 5 strings: "M", "R", or "-".
#        "M" = Musketeer, "R" = Cardinal Richleau's man, "-" = empty.
#        Each list of 5 strings is a "row"
#   A 'player' is one of the strings "M" or "R" (or sometimes "-").
#
# For brevity, Cardinal Richleau's men are referred to as "enemy".
# 'pass' is a no-nothing Python statement. Replace it with actual code.
def create_board():
    global board
    """Creates the initial Three Musketeers board and makes it globally
       available (That is, it doesn't have to be passed around as a
       parameter.) 'M' represents a Musketeer, 'R' represents one of
       Cardinal Richleau's men, and '-' denotes an empty space."""
    m = 'M'
    r = 'R'
    board =  [[r, r, r, r, m],
              [r, r, r, r, r],
              [r, r, m, r, r],
              [r, r, r, r, r],
              [m, r, r, r, r]]

def set_board(new_board):
    """Replaces the global board with new_board."""
    global board
    board = new_board
    return board

def get_board():
    """Just returns the board. Possibly useful for unit tests."""
    return board

def string_to_location(s):
    """Given a two-character string (such as 'A5'), returns the designated
       location as a 2-tuple (such as (0, 4)).
       The function should raise ValueError exception if the input
       is outside of the correct range (between 'A' and 'E' for s[0] and
       between '1' and '5' for s[1]
       """
    rows = {"A":0,"B":1, "C":2, "D":3, "E":4}
    columns = {"1":0, "2":1,"3":2, "4":3, "5":4}
    try:
        loc_row = rows[s[0]]
        loc_col = columns[s[1]]
        return (loc_row, loc_col)
    except KeyError:
        raise ValueError ("That location is not on the board.")


def location_to_string(location):
    """Returns the string representation of a location.
    Similarly to the previous function, this function should raise
    ValueError exception if the input is outside of the correct range
    """
    rows = {0:"A",1:"B", 2:"C", 3:"D", 4:"E"}
    columns = {0:"1", 1:"2",2:"3", 3:"4", 4:"5"}
    try:
        loc_row = rows[location[0]]
        loc_col = columns[location[1]]
        return loc_row + loc_col
    except KeyError:
        raise ValueError ("That location is not on the board.")


def at(location):
    """Returns the contents of the board at the given location.
    You can assume that input will always be in correct range."""
    if is_legal_location(location):
        return board[location[0]][location[1]]
    else:
        return False


def all_locations():
    """Returns a list of all 25 locations on the board."""
    all_locations = [[],[],[],[],[]]
    for i in range(5):
        for j in range(5):
            all_locations[i].append((i,j))
    return all_locations

def adjacent_location(location, direction):
    """Return the location next to the given one, in the given direction.
       Does not check if the location returned is legal on a 5x5 board.
       You can assume that input will always be in correct range."""
    (row, column) = location
    if direction == 'up':
        row -=1
    elif direction == 'down':
        row +=1
    elif direction == 'left':
        column -=1
    else:
        column +=1

    return (row,column)

def is_legal_move_by_musketeer(location, direction):
    """Tests if the Musketeer at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'M'"""
    new_location = adjacent_location(location, direction)
    if is_within_board(location, direction):
        if at(location) == 'M':
            if at(new_location) == "R":
                return True
            else:
                return False
        else:
            raise ValueError ("You have to move a musketeer piece")
    else:
        return False

def is_legal_move_by_enemy(location, direction):
    """Tests if the enemy at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'R'"""
    new_location = adjacent_location(location, direction)
    if is_within_board(location, direction):
        if at(location) == "R":
            if at(new_location) == "-" :
                return True
            else:
                return False
        else:
            raise ValueError ("You have to move an Enemy piece")
    else:
        return False

def is_legal_move(location, direction):
    """Tests whether it is legal to move the piece at the location
    in the given direction.
    You can assume that input will always be in correct range."""

    if at(location) == "M":
        return is_legal_move_by_musketeer(location, direction)
    elif at(location) == "R":
        return is_legal_move_by_enemy(location, direction)
    else:
        return False

def can_move_piece_at(location):
    """Tests whether the player at the location has at least one move available.
    You can assume that input will always be in correct range."""
    directions = ["up","down","left","right"]
    for i in range(len(directions)):
        if is_legal_move(location, directions[i]):
            return True
    else:
        return False

def has_some_legal_move_somewhere(who):
    """Tests whether a legal move exists for player "who" (which must
    be either 'M' or 'R'). Does not provide any information on where
    the legal move is.
    You can assume that input will always be in correct range."""
    for location in all_locations():
        for i in range(5):
            if at(location[i]) == who:
                if can_move_piece_at(location[i]):
                    return True
    else:
        return False


def possible_moves_from(location):
    """Returns a list of directions ('left', etc.) in which it is legal
       for the player at location to move. If there is no player at
       location, returns the empty list, [].
       You can assume that input will always be in correct range."""
    directions = ["up","down","left","right"]
    moves = []
    if at(location) != "-":
        for i in range(len(directions)):
            if is_legal_move(location, directions[i]):
                moves.append(directions[i])
    return moves

def is_legal_location(location):
    """Tests if the location is legal on a 5x5 board.
    You can assume that input will always be in correct range."""
    (row, column) = location
    if row >= 0 and row <=4 and column >=0 and column <=4:
        return True
    else:
        return False

def is_within_board(location, direction):
    """Tests if the move stays within the boundaries of the board.
    You can assume that input will always be in correct range."""
    return is_legal_location((adjacent_location(location, direction)))

def all_possible_moves_for(player):
    """Returns every possible move for the player ('M' or 'R') as a list
     (location, direction) tuples. You can assume that input will always be in correct range.
     Checks all locations, if the location matches the player, checks each move in all_possible_moves
     and if the move is legal, adds it to a list which moves can be chosen from"""
    all_possible_moves = []
    for location in all_locations():
        for i in range(5):
            for move in possible_moves_from(location[i]):
                if at(location[i]) == player:
                    if is_legal_move(location[i], move):
                        if is_within_board(location[i], move):
                            all_possible_moves.append((location[i],move))
    return all_possible_moves

def make_move(location, direction):
    """Moves the piece in location in the indicated direction.
    Doesn't check if the move is legal. You can assume that input will always
    be in correct range."""
    player = at(location)
    if (location, direction) in all_possible_moves_for(player):
        (row, column) = adjacent_location(location, direction)
        board[location[0]][location[1]] = "-"
        board[row][column] = player
    return board

def choose_computer_move(who):
    """The computer chooses a move for a Musketeer (who = 'M') or an
    enemy (who = 'R') and returns it as the tuple (location, direction),
    where a location is a (row, column) tuple as usual.
    You can assume that input will always be in correct range.

    Uses random library to make a choice of moves from all possible_moves. If only
    one move is possible it makes this move"""
    all_possible_moves = all_possible_moves_for(who)
    if len(all_possible_moves)>1:
        return random.choice(all_possible_moves)
    else:
        return all_possible_moves[0]

def is_enemy_win():
    """checks the board for the location of the musketeers and returns their locations to a list
    checks this list to see if the first index of the location of each matches (all in same row)
    and checks if second index of location in each matches (all in same column)"""
    locations_of_musketeers = []
    for location in all_locations():
        for i in range(5):
            if at(location[i])=="M":
                locations_of_musketeers.append(location[i])

    if locations_of_musketeers[0][0]==locations_of_musketeers[1][0]==locations_of_musketeers[2][0]:
        return True
    elif locations_of_musketeers[0][1]==locations_of_musketeers[1][1]==locations_of_musketeers[2][1]:
        return True
    else:
        return False

#---------- Communicating with the user ----------
#----you do not need to modify code below unless you find a bug
#----a bug in it before you move to stage 3

def print_board():
    print("    1  2  3  4  5")
    print("  ---------------")
    ch = "A"
    for i in range(0, 5):
        print(ch, "|", end = " ")
        for j in range(0, 5):
            print(board[i][j] + " ", end = " ")
        print()
        ch = chr(ord(ch) + 1)
    print()

def print_instructions():
    print()
    print("""To make a move, enter the location of the piece you want to move,
and the direction you want it to move. Locations are indicated as a
letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
Directions are indicated as left, right, up, or down (or simply L, R,
U, or D). For example, to move the Musketeer from the top right-hand
corner to the row below, enter 'A5 left' (without quotes).
For convenience in typing, you may use lowercase letters.""")
    print()

def choose_users_side():
    """Returns 'M' if user is playing Musketeers, 'R' otherwise."""
    user = ""
    while user != 'M' and user != 'R':
        answer = input("Would you like to play Musketeer (M) or enemy (R)? ")
        answer = answer.strip()
        if answer != "":
            user = answer.upper()[0]
    return user

def get_users_move():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple.
       The user can also enter S to save a game or Q to quit"""
       
    directions = {'L':'left', 'R':'right', 'U':'up', 'D':'down'}
    move = input("Enter your move or enter(S) to save game or enter(Q) to quit. ").upper().replace(' ', '')
    if move.upper() == 'S':
        save_game(board)
    elif move.upper() == "Q":
        print("Goodbye, thanks for playing. ")
        sys.exit()
    else:
        if (len(move) >= 3
                and move[0] in 'ABCDE'
                and move[1] in '12345'
                and move[2] in 'LRUD'):
            location = string_to_location(move[0:2])
            direction = directions[move[2]]
            if is_legal_move(location, direction):
                return (location, direction)
        print("Illegal move--'" + move + "'")
        return get_users_move()

def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        (location, direction) = get_users_move()
        if at(location) == 'M':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Musketeer", location, direction)
        else:
            print("You can't move there!")
            return move_musketeer(users_side)
    else: # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')
        make_move(location, direction)
        describe_move("Musketeer", location, direction)

def move_enemy(users_side):
    """Gets the enemy's move (from either the user or the computer)
       and makes it."""
    if users_side == 'R':
        (location, direction) = get_users_move()
        if at(location) == 'R':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Enemy", location, direction)
        else:
            print("You can't move there!")
            return move_enemy(users_side)
    else: # Computer plays enemy
        (location, direction) = choose_computer_move('R')
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board

def describe_move(who, location, direction):
    """Prints a sentence describing the given move."""
    new_location = adjacent_location(location, direction)
    print(who, 'moves', direction, 'from',\
          location_to_string(location), 'to',\
          location_to_string(new_location) + ".\n")

def save_game(board):
    """Asks the user for their file/user name and playing side and saves this information in a csv file to load later.
       If player saves game as existing game file, it is over written. Maximum number of saved games is 10, I have limited the number
       to avoid an infinite number of games being saved.
       Gives the player the option to keep playing or quit after save is performed"""
    clear()
    # count the number of games already saved
    count = 0
    with open('saved_games.csv') as myFile:
        csv_reader = csv.reader(myFile, delimiter=',')
        for row in csv_reader:
            count +=1

    # If count <=11 allows 10 games plus table headers to be saved.
    if count <11:
        #prints the names of all the current saved files so user will not overwrite in error
       with open('saved_games.csv') as myFile:
           csv_reader = csv.reader(myFile, delimiter=',')
           for row in csv_reader:
               print(row[0])
       print("Enter one of the file names above to overwrite the previously saved game with this one, or enter a new file name. ")
       name = input("Enter name to save game: ")

    else:
        #if more than 10 files are saved then the user will have to choose a file to overwrite
      with open('saved_games.csv') as myFile:
          csv_reader = csv.reader(myFile, delimiter=',')
          for row in csv_reader:
              print(row[0])
      name = input("Choose file from above to overwrite: ")

    user = ""
    # asks the user who they are playing and saves this in the file (user can choose to save as opponent)
    while user != "M" and user != "R":
        user = input("Which side are you playing (M or R): ").upper()
        user = user.strip()

    #The code below goes through the current saved_games.csv file and appends all saved games to myNewData list. Files of the same names are skipped
    #and therefore overwritten with the new data. The table headers are skipped too. The result is a list of lists called myNewData
    #containing names, boards and users. This list is later written to file as saved_games.csv.

    myNewData = [["Name", "Board", "Playing as"],[name, board, user]]
    with open('saved_games.csv') as myFile:
        csv_reader = csv.reader(myFile, delimiter=',')
        for row in csv_reader:
            if row[0] == name or row[0] == "Name":
                continue
            else:
                myNewData.append(row)

    #writes the new file data created above to a file called saved_games.csv
    with open('saved_games.csv', 'w', newline='') as myFile:
        writer = csv.writer(myFile)
        writer.writerows(myNewData)

    #the code below gives the user the option to quit after saving the game or go back to the board and continue their game
    while True:
        keep_playing = input("Would you like to keep playing(P) or Quit now(Q): ")
        if keep_playing.upper() == "Q":
            # tells the user where to find their game and exits game
            print("Thanks for playing.")
            print("You can play game " +name+ " later.")
            sys.exit()
        elif keep_playing.upper() == 'P':
            # sets the board and user as it was before save and game continues
            board = myNewData[1][1]
            user = myNewData[1][2]
            clear()
            start(board, user)
    else:
        keep_playing = input("Would you like to keep playing(P) or Quit(Q) now: ").upper()


def load_game():
    """ Go through the saved games and print the name of each game. Ask the user for
    the name of the game they want to load and get the board from the file and save it as the board for the game. The user must Enter
    an existing file name. """

    clear()
    # prints the names of all the saved games
    with open('saved_games.csv') as myFile:
        csv_reader = csv.reader(myFile, delimiter=',')
        for row in csv_reader:
            print(row[0])

    # ensures the user enters an existing file name or else reasks user to enter file name
    while True:
        name = input("Enter name of game you want to load: ")
        with open('saved_games.csv') as myFile:
            csv_reader = csv.reader(myFile, delimiter=',')
            for row in csv_reader:
                if name == row[0]:
                    # eval converts board string which is saved in file back into list of lists which can be printed by print_board()
                    board = eval(row[1])
                    users_side = row[2]
                    start(board, users_side)
            print("You must enter one of the file names above. ")

def start(board, users_side):
    """ Start the users game with the board and side they have just selected from load_game
    or else starts a new game. Clears the screen and prints the instructions """
    clear()
    set_board(board)
    print_instructions()
    print()

    # if it's a new game lets the user choose sides
    if users_side != "M" and users_side != "R":
        users_side = choose_users_side()
        print_board()

    else:
        #reminds the user who they are playing as, prints the board and waits for move
        print("Welcome back, you are playing as "+users_side)
        print()
        print_board()

        # stops computer taking extra move after the game is loaded if player is R
        if users_side == "R":
            board = move_enemy(users_side)
            print_board()

    while True:
        # plays the game
        if has_some_legal_move_somewhere('M'):
            board = move_musketeer(users_side)
            print_board()
            if is_enemy_win():
                print("Cardinal Richleau's men win!")
                sys.exit()
        else:
            print("The Musketeers win!")
            sys.exit()

        if has_some_legal_move_somewhere('R'):
            board = move_enemy(users_side)
            print_board()
        else:
            print("The Musketeers win!")
            sys.exit()

def play_or_load():
    "Asks the user if they want to start a new game or load a saved game."
    clear()
    load = ""
    while load  != 'L' or load != 'N':
        load= input("Do you want to play a new game (N) or load a saved game (L): ")
        load = load.strip().upper()
        if load == 'L':
            load_game()
        if load == 'N':
            create_board()
            users_side = ""
            start(board, users_side)

def clear():
    """Clears the screen"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

play_or_load()
