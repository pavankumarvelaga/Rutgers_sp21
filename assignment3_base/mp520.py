"""
Compute the value brought by a given move by placing a new token for player
at (row, column). The value is the number of opponent pieces getting flipped
by the move. 

A move is valid if for the player, the location specified by (row, column) is
(1) empty and (2) will cause some pieces from the other player to flip. The
return value for the function should be the number of pieces hat will be moved.
If the move is not valid, then the value 0 (zero) should be returned. Note
here that row and column both start with index 0. 
"""

from copy import deepcopy
import numpy as np

def is_bounded(state,row, column):
    return row >= 0 and row < len(state) and column >= 0 and column <len(state)

def get_move_value(state, player, row, column):
    flipped = 0
    flips = []
    moves = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    opponent =  'B' if player == 'W' else 'W'
    
    for row_move, col_move in moves:
        x,y = row,column
        x += row_move
        y += col_move
        # print(x,y)
        if is_bounded(state,x, y) and state[x][y] == opponent: 
            x += row_move
            y += col_move
            if not is_bounded(state,x, y):
                continue
            while state[x][y] == opponent:
                x += row_move
                y += col_move
                if not is_bounded(state,x, y): 
                    break
            if not is_bounded(state,x, y):
                continue
            if state[x][y] == player:
                while True:
                    x -= row_move
                    y -= col_move
                    if x == row and y == column:
                        break
                    flips.append([x, y])
    print(f"state:{state},player:{player},(row,column):{(row, column)}")
    print(flips)
    flipped = len(flips)
    return flipped


"""
Execute a move that updates the state. A new state should be crated. The move
must be valid. Note that the new state should be a clone of the old state and
in particular, should not share memory with the old state. 
"""


def execute_move(state, player, row, column):
    # if get_move_value(state, player, row, column):
    new_state = deepcopy(state)
    new_state[row][column] = player
    return new_state


"""
A method for counting the pieces owned by the two players for a given state. The
return value should be two tuple in the format of (blackpeices, white pieces), e.g.,

    return (4, 3)

"""

def get_counts(state):
    state_counts = [(i[0],i[1]) for i in np.array(np.unique(state , return_counts=True)).T]
    dict_counts = dict(zip([i[0] for i in state_counts],[i[1] for i in state_counts]))
    return(dict_counts)

def count_pieces(state):
    blackpieces = 0
    whitepieces = 0
    # Your implementation goes here
    dict_counts = get_counts(state)
    blackpieces = dict_counts.get('B',0)
    whitepieces = dict_counts.get('W',0)
    return (blackpieces,whitepieces )


"""
Check whether a state is a terminal state. 
"""


def is_terminal_state(state, state_list=None):
    terminal = True
    counts = get_counts(state)
    if counts.get(' ',0) == 0:
        return True 
    # Your implementation goes here
    for i in range(len(state)):
        for j in range(len(state)):
            for k in ['B','W']:
                if get_move_value(state,k,i,j) > 0:
                    return False

            

    return terminal


"""
The minimax algorithm. Your implementation should return the best value for the
given state and player, as well as the next immediate move to take for the player. 
"""


def minimax(state, player):
    value = 0
    row = -1
    column = -1
    # Your implementation goes here
    return (value, row, column)


"""
This method should call the minimax algorithm to compute an optimal move sequence
that leads to an end game. 
"""


def full_minimax(state, player):
    value = 0
    move_sequence = []
    # Your implementation goes here
    return (value, move_sequence)


"""
The minimax algorithm with alpha-beta pruning. Your implementation should return the
best value for the given state and player, as well as the next immediate move to take
for the player. 
"""


def minimax_ab(state, player, alpha=-10000000, beta=10000000):
    value = 0
    row = -1
    column = -1
    # Your implementation goes here
    return (value, row, column)


"""
This method should call the minimax_ab algorithm to compute an optimal move sequence
that leads to an end game, using alpha-beta pruning.
"""


def full_minimax_ab(state, player):
    value = 0
    move_sequence = []
    # Your implementation goes here
    return (value, move_sequence)
