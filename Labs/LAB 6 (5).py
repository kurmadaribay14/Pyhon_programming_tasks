## Tic-tac-toe game by Mateon1

try:
    raw_input
except NameError:
    import sys
    print >> sys.stderr, "This program supports Python 2 only."
    sys.exit(1)

def prompt(question, check_func=lambda i: i.lower() == "y"):
    """Prompts the user with `question`
Awaits until check_func(<user_input>) returns a non-None value and returns it"""
    while True:
        value = check_func(raw_input(question))
        if value is not None:
            return value

def check_win(board):
    "Checks if there is a win condition, returns who won or False"
    width = len(board[0])
    height = len(board)

    # Horizontal
    for y in xrange(height):
        if board[y][0] != 0 and all(board[y][i] == board[y][0] for i in xrange(1, width)):
            return board[y][0]

    # Vertical
    for x in xrange(width):
        if board[0][x] != 0 and all(board[i][x] == board[0][x] for i in xrange(1, height)):
            return board[0][x]

    if width == height:  # Diagonals only work if the board is square
        # \ diagonal
        if board[0][0] != 0 and all(board[i][i] == board[0][0] for i in xrange(1, width)):
            return board[0][0]

        # / diagonal
        if board[0][-1] != 0 and all(board[i][-1 - i] == board[0][-1] for i in xrange(1, width)):
            return board[0][-1]
    return False


def f_positive(string):
    try:
        val = int(string)
        if val > 0: return val
    except ValueError:
        pass
    # Implicit `return None` at the end of the function

def f_coords(board):
    "Returns function handling user input for board coordinates"
    def f(i):
        i = i.split(" ")
        if len(i) != 2: return
        x = f_positive(i[0])
        y = f_positive(i[1])
        if x is None or y is None: return
        if board[y - 1][x - 1] != 0: return
        return (x - 1, y - 1)
    return f

def print_board(board):
    """Prints the game board.
Output example:

      1  2  3
    +--+--+--+
  1 |<>|  |<>|
    +--+--+--+
  2 |<>|><|  |
    +--+--+--+
  3 |><|  |  |
    +--+--+--+"""

    def cell(value):
        "Returns a 2-character representation of the cell"
        if value == 0:
            return "  "
        elif value == 1:
            return "<>" # circle
        elif value == 2:
            return "><" # cross
        raise ValueError("Invalid cell value: %r" % value)

    width = len(board[0])
    height = len(board)
    text = [] # Print is annoying, build a buffer instead

    text.append("     ")
    for i in xrange(width):
        text.append("%2d " % (i + 1,))
    text.append("\n")

    for y in xrange(height):
        text.append("    " + "+--" * width + "+\n") # separator
        text.append("%3d " % (y + 1,))
        for x in xrange(width):
            text.append("|" + cell(board[y][x]))
        text.append("|\n")
    text.append("    " + "+--" * width + "+")

    print " ".join(text)


def play(board_size=(3, 3)):
    board = [[0 for x in xrange(board_size[0])] for y in xrange(board_size[1])]
    # board[y][x]:
    # * 0 - empty
    # * 1 - <> // circle
    # * 2 - >< // cross
    turn = 0
    while turn < board_size[0] * board_size[1] and not check_win(board):
        print "Player %d's (%s) turn!" % (turn % 2 + 1, ("circle", "cross")[turn % 2])
        print_board(board)
        (x, y) = prompt("Please enter board coordinates to place your piece on.\n(example: `2 3` for 2nd column 3rd row): ", f_coords(board))
        board[y][x] = turn % 2 + 1
        turn += 1

    print "=== Game over! ==="
    print_board(board)

    winning_player = check_win(board)
    if not winning_player:
        print "The game was a tie!"
    else:
        print "Player %d (%s) won!" % (winning_player, ("circle", "cross")[winning_player - 1])


if __name__ == "__main__":
    # Python needs a damn do..while construct
    # Can't avoid repeating myself here.
    board_size = (prompt("Please enter tic-tac-toe board width:  ", f_positive),
                  prompt("Please ented tic-tac-toe board height: ", f_positive))
    play(board_size=board_size)
    while prompt("Would you like to play again? (y/N) "):
        board_size = (prompt("Please enter tic-tac-toe board width:  ", f_positive),
                      prompt("Please ented tic-tac-toe board height: ", f_positive))
        play(board_size=board_size)
