import mp520 as mp
from ans import *
import time


if __name__ == "__main__":
    p1 = "B"
    p2 = "W"
    points = 0
    total_t = 0

    # get_move_value
    _p1 = 5
    state = get_start_game_state_4_8()
    for i in range(4):
        for j in range(4):
            if state[i][j] == " ":
                if mp.get_move_value(state, p1, i, j) != get_move_value(
                    state, p1, i, j
                ):
                    _p1 -= 1
    state = get_mid_start_game_state_4()
    for i in range(4):
        for j in range(4):
            if state[i][j] == " ":
                if mp.get_move_value(state, p2, i, j) != get_move_value(
                    state, p2, i, j
                ):
                    _p1 -= 1
    state = get_default_start_game_state_5()
    for i in range(5):
        for j in range(5):
            if state[i][j] == " ":
                if mp.get_move_value(state, p1, i, j) != get_move_value(
                    state, p1, i, j
                ):
                    _p1 -= 1
    state = get_mid_start_game_state_8()
    for i in range(8):
        for j in range(8):
            if state[i][j] == " ":
                if mp.get_move_value(state, p2, i, j) != get_move_value(
                    state, p2, i, j
                ):
                    _p1 -= 1
    _p1 = max(0, _p1)

    # execute_move
    _p2 = 2.5
    state = get_start_game_state_4_8()
    for i in range(4):
        for j in range(4):
            if state[i][j] == " ":
                if get_move_value(state, p1, i, j) > 0:
                    new_state = mp.execute_move(state, p1, i, j)
                    state[i][j] = " "
                    if new_state != execute_move(state, p1, i, j):
                        _p2 -= 0.5
    state = get_mid_start_game_state_4()
    for i in range(4):
        for j in range(4):
            if state[i][j] == " ":
                if get_move_value(state, p2, i, j) > 0:
                    new_state = mp.execute_move(state, p2, i, j)
                    state[i][j] = " "
                    if new_state != execute_move(state, p2, i, j):
                        _p2 -= 0.5
    state = get_default_start_game_state_5()
    for i in range(5):
        for j in range(5):
            if state[i][j] == " ":
                if get_move_value(state, p1, i, j) > 0:
                    new_state = mp.execute_move(state, p1, i, j)
                    state[i][j] = " "
                    if new_state != execute_move(state, p1, i, j):
                        _p2 -= 0.5
    state = get_mid_start_game_state_8()
    for i in range(8):
        for j in range(8):
            if state[i][j] == " ":
                if get_move_value(state, p2, i, j) > 0:
                    new_state = mp.execute_move(state, p2, i, j)
                    state[i][j] = " "
                    if new_state != execute_move(state, p2, i, j):
                        _p2 -= 0.5
    _p2 = max(0, _p2)

    # is_terminal_state         5
    _p3 = 2.5
    for i in range(7):
        state = get_terminal_state_sample(i)
        if is_terminal_state(state) != mp.is_terminal_state(state):
            _p3 -= 0.5
    _p3 = max(0, _p2)

    # minimax
    _p4 = 7.5
    state = get_default_start_game_state_4()
    if mp.minimax(state, p1) != (-8, 0, 2):
        _p4 -= 2.5

    state = get_start_game_state_4_8()
    if mp.minimax(state, p1) != (10, 3, 0):
        _p4 -= 2.5

    state = get_mid_start_game_state_4()
    if mp.minimax(state, p2) != (-8, 0, 1):
        _p4 -= 2.5

    _p4 = max(0, _p4)

    # full_minimax
    _p5 = 7.5
    state = get_default_start_game_state_4()
    (_, seq) = mp.full_minimax(state, p1)
    if seq != [
        ("B", 0, 2),
        ("W", 0, 3),
        ("B", 1, 3),
        ("W", 0, 1),
        ("B", 3, 0),
        ("W", 2, 3),
        ("B", 0, 0),
        ("W", 3, 2),
        ("B", 3, 3),
        ("W", 3, 1),
    ]:
        _p5 -= 2.5

    state = get_start_game_state_4_8()
    (_, seq) = mp.full_minimax(state, p1)
    if seq != [
        ("B", 3, 0),
        ("W", 0, 3),
        ("B", 3, 3),
        ("W", 0, 1),
        ("B", 0, 2),
        ("W", 3, 1),
        ("B", 0, 0),
        ("B", 3, 2),
    ]:
        _p5 -= 2.5

    state = get_mid_start_game_state_4()
    (_, seq) = mp.full_minimax(state, p1)
    if seq != [
        ("B", 3, 0),
        ("W", 0, 1),
        ("W", 2, 3),
        ("W", 2, 0),
        ("B", 1, 0),
        ("B", 3, 2),
        ("W", 3, 1),
        ("W", 3, 3),
    ]:
        _p5 -= 2.5

    # minimax_ab, full_minimax_ab

    _p7 = 5
    state = get_default_start_game_state_4()
    if mp.minimax_ab(state, p1) != (-8, 0, 2):
        _p7 -= 1
    state = get_start_game_state_4_8()
    if mp.minimax_ab(state, p1) != (10, 3, 0):
        _p7 -= 1
    state = get_default_start_game_state_5()
    if mp.minimax_ab(state, p1) != (0, 2, 4):
        _p7 -= 1
    state = get_mid_start_game_state_5_1()
    if mp.minimax_ab(state, p2) != (23, 1, 1):
        _p7 -= 1
    state = get_mid_start_game_state_5_2()
    if mp.minimax_ab(state, p1) != (17, 4, 0):
        _p7 -= 1
    _p7 = max(_p7, 0)

    _p8 = 5
    state = get_default_start_game_state_4()
    (v, seq) = mp.full_minimax_ab(state, p1)
    if v != -8:
        _p8 -= 1

    state = get_start_game_state_4_8()
    t = time.time()
    (v, seq) = mp.full_minimax_ab(state, p1)
    if v != 10:
        _p8 -= 1

    state = get_default_start_game_state_5()
    (v, seq) = mp.full_minimax_ab(state, p1)
    if v != 0:
        _p8 -= 1

    state = get_mid_start_game_state_5_1()
    (v, seq) = mp.full_minimax_ab(state, p2)
    if v != 23:
        _p8 -= 1

    state = get_mid_start_game_state_5_2()
    (v, seq) = mp.full_minimax_ab(state, p1)
    if v != 17:
        _p8 -= 1
    _p8 = max(0, _p8)

    print(
        "".join(
            [
                "get_move_value: ",
                str(_p1),
                " / 5\n",
                "execute_move: ",
                str(_p2),
                " / 2.5\n",
                "is_terminal_move: ",
                str(_p3),
                " / 2.5\n",
                "minimax: ",
                str(_p4),
                " / 7.5\n",
                "full_minimax: ",
                str(_p5),
                " / 7.5\n",
                "minimax_ab: ",
                str(_p7),
                " / 5\n",
                "full_minimax_ab: ",
                str(_p8),
                " / 5\n",
                "Total points: ",
                str(min(35, _p1 + _p2 + _p3 + _p4 + _p5 + _p7 + _p8)),
                " / 35\n",
            ]
        )
    )
