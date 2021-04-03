# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.5 (default, Sep  4 2020, 02:22:02) 
# [Clang 10.0.0 ]
# Embedded file name: /home/siwei/TA/ru-cs520-grading-sp21/assignment3/ans.py
# Compiled at: 2021-03-22 00:18:45
# Size of source mod 2**32: 4581 bytes


def _get_empty_state(n):
    state = []
    for i in range(0, n):
        row = []
        for j in range(0, n):
            row.append(' ')
        else:
            state.append(row)

    else:
        return state


def get_default_start_game_state_4():
    state = _get_empty_state(4)
    state[1][1] = state[2][2] = 'B'
    state[1][2] = state[2][1] = 'W'
    return state


def get_start_game_state_4_8():
    state = _get_empty_state(4)
    state[1][0] = state[1][1] = state[1][2] = state[1][3] = 'B'
    state[2][0] = state[2][1] = state[2][2] = state[2][3] = 'W'
    return state


def get_mid_start_game_state_4():
    state = _get_empty_state(4)
    state[0][2] = state[1][1] = state[1][2] = state[1][3] = state[2][2] = 'B'
    state[0][3] = state[2][1] = 'W'
    return state


def get_default_start_game_state_5():
    state = _get_empty_state(5)
    state[0][0] = state[1][1] = state[3][4] = state[4][3] = 'W'
    state[1][0] = state[0][1] = state[3][3] = state[4][4] = 'B'
    return state


def get_mid_start_game_state_5_1():
    state = _get_empty_state(5)
    state[2][0] = state[2][1] = state[2][2] = state[2][3] = state[2][4] = 'B'
    state[1][2] = state[3][0] = state[3][1] = state[3][2] = state[3][3] = state[3][4] = 'W'
    return state


def get_mid_start_game_state_5_2():
    state = _get_empty_state(5)
    state[2][0] = state[2][1] = state[3][2] = state[2][3] = state[2][4] = 'B'
    state[1][2] = state[3][0] = state[3][1] = state[2][2] = state[3][3] = state[3][4] = 'W'
    return state


def get_mid_start_game_state_8():
    return [
     [
      'B', 'B', 'B', 'B', 'B', 'B', 'B', 'W'], ['B', 'B', 'B', 'B', 'W', 'B', 'B', 'B'], [' ', 'B', 'W', 'W', 'B', 'W', 'B', 'B'], [' ', 'W', 'W', 'W', 'W', 'B', 'B', 'B'], [' ', ' ', 'W', 'W', 'W', 'W', 'W', 'W'], [' ', ' ', 'W', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]


def get_terminal_state_sample(n):
    if n == 0:
        return [
         [
          'B', 'W', 'W', 'W'], [' ', 'W', 'W', 'W'], [' ', 'W', 'W', 'W'], ['B', 'W', 'W', 'B']]
    if n == 1:
        return [
         [
          'B', 'B', 'B', 'W'], ['B', 'B', 'B', 'W'], ['B', 'W', 'B', 'W'], ['B', 'W', ' ', 'B']]
    if n == 2:
        return [
         [
          'B', 'B', 'B', 'W'], ['B', 'B', 'B', 'W'], ['B', 'B', 'B', 'W'], ['B', 'B', 'B', 'B']]
    if n == 3:
        return [
         [
          'W', 'W', 'W', ' ', ' '], ['W', 'W', ' ', ' ', ' '], ['W', ' ', ' ', ' ', 'B'], [' ', ' ', ' ', 'B', 'B'], [' ', ' ', 'B', 'B', 'B']]
    if n == 4:
        return [
         [
          'B', 'B', 'B', 'B', 'B'], ['W', 'W', 'B', 'B', 'B'], ['W', 'B', 'W', 'B', 'B'], ['W', 'W', 'W', 'B', 'B'], ['W', ' ', 'W', 'W', 'W']]
    if n == 5:
        return [
         [
          'B', 'B', 'B', 'B', 'B', 'B', 'B', 'W'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], ['B', ' ', 'W', 'B', 'B', 'B', 'B', 'B'], ['B', 'W', 'B', 'B', 'B', 'B', 'B', 'B'], ['W', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]
    if n == 6:
        return [
         [
          'W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'W', 'W'], ['W', 'W', 'W', 'W', 'B', 'B'], ['W', 'W', 'W', 'W', ' ', 'B']]


def get_move_value(state, player, row, column):
    flipped = 0
    size = len(state)
    for di, dj in ((1, 0), (1, 1), (0, 1), (-1, -1), (-1, 0), (0, -1), (-1, 1), (1, -1)):
        i = row + di
        j = column + dj
        count = 0
        while True:
            if j < size and j >= 0 and i >= 0 and i < size:
                if state[i][j] == ' ':
                    pass
                elif state[i][j] == player:
                    flipped += count
            else:
                i, j = i + di, j + dj
                count += 1

    else:
        return flipped


def execute_move(state, player, row, column):
    new_state = [list(i) for i in state]
    new_state[row][column] = player
    size = len(state)
    for di, dj in ((1, 0), (1, 1), (0, 1), (-1, -1), (-1, 0), (0, -1), (-1, 1), (1, -1)):
        i = row + di
        j = column + dj
        if j < size and j >= 0 and i >= 0:
            if i < size:
                if new_state[i][j] == ' ':
                    pass
                elif new_state[i][j] == player:
                    while True:
                        if (
                         i, j) != (row, column):
                            new_state[i][j] = player
                            i, j = i - di, j - dj

                else:
                    i, j = i + di, j + dj
        else:
            return new_state


def is_terminal_state(state, state_list=None):
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j] == ' ':
                get_move_value(state, 'W', i, j) > 0 or get_move_value(state, 'B', i, j) > 0
                return False
        else:
            return True
# okay decompiling ans.pyc
