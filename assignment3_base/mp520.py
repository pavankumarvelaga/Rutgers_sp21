"""
Compute the value brought by a given move by placing a new token for player
at (row, column). The value is the number of opponent pieces getting flipped
by the move. 

A move is valid if for the player, the location specified by (row, column) is
(1) empty and (2) will cause some pieces from the other player to flip. The
return value for the function should be the number of pieces that will be moved.
If the move is not valid, then the value 0 (zero) should be returned. Note
here that row and column both start with index 0. 
"""
from copy import deepcopy
from pprint import pprint
def is_bounded(state, x, y):
	if x < len(state) > y and x >= 0 and y >= 0:
		return True
	else:
		return False

def is_valid_move(state, player, row, column):
	moves = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
	opponent = 'B' if player == 'W' else 'W'
	flip_tiles = []
	for x_move,y_move in moves:
		x = row
		y = column
		x += x_move
		y += y_move
		if is_bounded(state, x, y) and state[x][y] == opponent:
			x += x_move
			y += y_move
			if not is_bounded(state, x, y):
				continue
			while state[x][y] == opponent:
				x += x_move
				y += y_move
				if not is_bounded(state, x, y): 
					# break out of while loop, then continue in for loop
					break
			if not is_bounded(state, x, y): 
				continue
			if state[x][y] == player:
				while True:

					x -= x_move
					y -= y_move
					if x == row and y == column:
						break

					flip_tiles.append([x,y])
	if len(flip_tiles) == 0:
		return False
	return flip_tiles


def get_move_value(state, player, row, column):
	flipped = 0
	# Your implementation goes here
	valid_move = is_valid_move(state, player, row, column)
	if valid_move:
		flipped = len(valid_move)
	return flipped


"""
Execute a move that updates the state. A new state should be crated. The move
must be valid. Note that the new state should be a clone of the old state and
in particular, should not share memory with the old state. 
"""


def execute_move(state, player, row, column):
	new_state = None
	# Your implementation goes here
	new_state = deepcopy(state)
	new_state[row][column] = player
	valid_move = is_valid_move(state, player, row, column)
	if valid_move:
		for i,j in valid_move:
			new_state[i][j] = player
	return new_state


"""
A method for counting the pieces owned by the two players for a given state. The
return value should be two tuple in the format of (blackpeices, white pieces), e.g.,

	return (4, 3)

"""
def count_pieces(state):
	blackpieces = 0
	whitepieces = 0
	# Your implementation goes here
	for i in range(len(state)):
		for j in range(len(state)):
			if state[i][j] == 'B':
				blackpieces += 1
			elif state[i][j] == 'W':
				whitepieces += 1

	return (blackpieces, whitepieces)
"""

Check whether a state is a terminal state. 

"""
def is_terminal_state(state, state_list=None): 
	terminal = True 
	b , w = count_pieces(state)
	if len(state[0])**2 - (b + w) == 0:
		return True
	for k in ['B','W']: 
		moves = get_valid_moves(state,k) 
        # print(moves) 
		if len(moves) > 0: 
			terminal = False 
	return terminal

def get_valid_moves(state, player):
	valid_moves = []
	for i in range(len(state)):
		for j in range(len(state)):
			if state[i][j] == ' ' and is_valid_move(state, player, i ,j):
				valid_moves.append([i,j])

	return valid_moves

"""
The minimax algorithm. Your implementation should return the best value for the
given state and player, as well as the next immediate move to take for the player. 
"""


"""
def minimax(state, player):
	value = 0
	row = -1
	column = -1
	# Your implementation goes here
	row, column, value = max_value(state)

	return (value, row, column )

def max_value(state):
	row , col = -1, -1
	if is_terminal_state(state):
		b, w = count_pieces(state)
		return -1, -1, b - w
	max_val = float('-inf')
	available_moves = get_valid_moves(state, 'B')
	if len(available_moves) == 0:
		return min_value(state)
	for x , y in available_moves:
		new_state = execute_move(state, 'B', x, y)
		_, _, mini_val = min_value(new_state)
		if mini_val	> max_val:
			row = x
			col = y
			max_val = mini_val
			
	return row, col, max_val

def min_value(state):
	row , col = -1, -1
	if is_terminal_state(state):
		b, w = count_pieces(state)
		return  -1, -1, b - w
	min_val = float('inf')
	available_moves = get_valid_moves(state, 'W')
	if len(available_moves) == 0:
		return max_value(state)
	for x , y in available_moves:
		new_state = execute_move(state, 'W', x, y)
		_, _, maxi_val = max_value(new_state)
		if maxi_val	< min_val:
			row = x
			col = y
			min_val = maxi_val
	return row, col, min_val
"""

def max_value(state):
	# nonlocal moves_seq
	row , col, path = -1, -1, None
	if is_terminal_state(state):
		b, w = count_pieces(state)		
		return  b - w, [('B', -1, -1)]
	max_val = float('-inf')
	available_moves = get_valid_moves(state, 'B')
	if len(available_moves) == 0:
		return min_value(state)
	for x , y in available_moves:
		new_state = execute_move(state, 'B', x, y)
		mini_val, path_ = min_value(new_state)		
		if mini_val	> max_val:
			row = x
			col = y
			max_val = mini_val
			path = path_
			
	return max_val, [('B', row, col)] + path

def min_value(state):
	row , col, path = -1, -1, None
	if is_terminal_state(state):
		b, w = count_pieces(state)		
		return   b - w, [("W",-1,-1)]
	min_val = float('inf')
	available_moves = get_valid_moves(state, 'W')
	if len(available_moves) == 0:
		return max_value(state)
	for x , y in available_moves:
		new_state = execute_move(state, 'W', x, y)
		maxi_val, path_ = max_value(new_state)
		if maxi_val	< min_val:
			row = x
			col = y		
			min_val = maxi_val
			path = path_
	
	return min_val, [('W', row, col)] + path

def minimax(state, player):
	value = 0
	row = -1
	column = -1
	# Your implementation goes here
	if player == 'B':
		value, path = max_value(state)
	else:
		value, path = min_value(state)
	row = path[0][1]
	column = path[0][2]
	return value, row, column 
	# return value, *path[1:]

"""
This method should call the minimax algorithm to compute an optimal move sequence
that leads to an end game. 
"""

def full_minimax(state, player):

	value = 0
	move_sequence = []
	# Your implementation goes here
	if player == 'B':
		value, move_sequence = max_value(state)
	else:
		value, move_sequence = min_value(state)
	
	return (value, move_sequence)


"""
The minimax algorithm with alpha-beta pruning. Your implementation should return the
best value for the given state and player, as well as the next immediate move to take
for the player. 
"""

def max_value_ab(state, alpha, beta):
	# nonlocal moves_seq
	row , col, path = -1, -1, None
	if is_terminal_state(state):
		b, w = count_pieces(state)		
		return  b - w, [('B', -1, -1)]

	max_val = float('-inf')
	available_moves = get_valid_moves(state, 'B')
	if len(available_moves) == 0:
		return min_value_ab(state, alpha, beta)
	for x , y in available_moves:
		new_state = execute_move(state, 'B', x, y)
		mini_val, path_ = min_value_ab(new_state, alpha, beta)		
		if mini_val	> max_val:
			row = x
			col = y
			max_val = mini_val
			path = path_
	
		if max_val >= beta:
			return 	max_val, [('B', row, col)] + path
		alpha = max(alpha, max_val)
	return max_val, [('B', row, col)] + path

def min_value_ab(state, alpha, beta):
	row , col, path = -1, -1, None
	if is_terminal_state(state):
		b, w = count_pieces(state)		
		return   b - w, [("W",-1,-1)]
	min_val = float('inf')
	available_moves = get_valid_moves(state, 'W')
	if len(available_moves) == 0:
		return max_value_ab(state, alpha, beta)
	for x , y in available_moves:
		new_state = execute_move(state, 'W', x, y)
		maxi_val, path_ = max_value_ab(new_state, alpha, beta)
		if maxi_val	< min_val:
			row = x
			col = y		
			min_val = maxi_val
			path = path_
		if min_val <= alpha:
			return min_val, [('W', row, col)] + path
		beta = min(beta, min_val)
	return min_val, [('W', row, col)] + path

def minimax_ab(state, player, alpha=-10000000, beta=10000000):
	value = 0
	row = -1
	column = -1
	# Your implementation goes here
	if player == 'B':
		value, path = max_value_ab(state, alpha, beta)
	else:
		value, path = min_value_ab(state, alpha, beta)

	row = path[0][1]
	column = path[0][2]
	return (value, row, column)

"""
This method should call the minimax_ab algorithm to compute an optimal move sequence
that leads to an end game, using alpha-beta pruning.
"""

def full_minimax_ab(state, player):
	value = 0
	move_sequence = []
	alpha=-10000000
	beta=10000000
	# Your implementation goes here
	if player == 'B':
		value, move_sequence = max_value_ab(state, alpha, beta)
	else:
		value, move_sequence = min_value_ab(state, alpha, beta)

	return (value, move_sequence)
