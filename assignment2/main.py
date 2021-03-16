import mp520 as mp
import numpy as np
import os
import pickle
import sys
import multiprocessing
import copy

VERBOSE = True


def run_function_with_timeout(func, parameters, timeout=1):
    try:
        pool = multiprocessing.Pool(1)
        solver = pool.apply_async(func, (parameters))
        ret_val = solver.get(timeout=timeout)
    except multiprocessing.TimeoutError:
        pool.terminate()
        print("Time Limit Exceed")
        raise multiprocessing.TimeoutError
    return ret_val


def _retrieve_solution(graph, goal_node_id):
    path = []
    cost = 0
    # Your code here #
    current_node = graph[goal_node_id]
    path.insert(0, current_node[0])
    while current_node[2] != 0:
        prev_node = graph[current_node[2]]
        current_node = prev_node
        path.insert(0, current_node[0])
    cost = graph[goal_node_id][3]
    return (cost, path)


def _heuristic_function(graph, node_id):
    return graph[node_id][4]


def _heuristic_zero(graph, node_id):
    return 0


"""
Generic graph search skeleton 
"""


def _graph_search(
    graph,
    start_node_id,
    goal_node_id,
    _add_to_queue,
    is_queue_empty,
    _pop,
    _heuristic,
    a=1,
    b=1,
):
    # Counting the expansion
    expansion_count = 0

    _add_to_queue(start_node_id, 0, 0 + _heuristic(graph, start_node_id) * b, True)
    # Go through the queue unless empty
    while is_queue_empty() == False:
        # Pop the first node (id) out of the queue
        (node_id, parent_node_id) = _pop()
        node = graph[node_id]
        # Check whether the node is already visited
        if node[1] == True:
            continue
        # Set node to be visited
        expansion_count = expansion_count + 1
        node[1] = True
        node[2] = parent_node_id
        if node_id != start_node_id:
            # print parent_node_id, node_id
            node[3] = graph[parent_node_id][3] + graph[parent_node_id][6][node_id]

        # Check whether we are at goal
        if node[0] == goal_node_id:
            (cost, path) = _retrieve_solution(graph, goal_node_id)
            return (expansion_count, cost, path)

        # Work with the neighbors
        for n in range(0, len(node[5])):
            nbr = node[5][n]
            if graph[nbr[0]][1] == False:
                _add_to_queue(
                    nbr[0],
                    node_id,
                    node[3]
                    + graph[node_id][6][nbr[0]] * a
                    + _heuristic(graph, nbr[0]) * b,
                    False,
                )

    return (-1, 0, 0)


def main():
    get_random_state_point = 0
    compute_attacking_pairs_point = 0
    hill_descending_point = 0
    n_queens_point = 0

    ### Get random states
    for n in [8, 12, 16, 20, 24]:
        try:
            state1 = run_function_with_timeout(mp.get_random_state, [n])
            state2 = run_function_with_timeout(mp.get_random_state, [n])
            state3 = run_function_with_timeout(mp.get_random_state, [n])
            if state1 == state2 and state2 == state3:
                if VERBOSE:
                    print("Getting exactly same answer for multiple runs")
            elif len(state1) == n and len(state2) == n and len(state3) == n:
                get_random_state_point += 1
        except Exception as e:
            if VERBOSE:
                print(e)

    for state_num in range(1, 6):
        with open(
            os.path.join("testcases", "state_" + str(state_num)), "rb"
        ) as file_obj:
            state, num_attacking_pair, is_local_min = pickle.load(file_obj)
            ### Compute attacking pairs
            # Note, the state is 1-index, i.e. state[i] is between 1 and len(state)
            try:
                ### deepcopy in case people modify state in the function
                result1 = run_function_with_timeout(
                    mp.compute_attacking_pairs, [copy.deepcopy(state)]
                )
                if result1 == num_attacking_pair:
                    compute_attacking_pairs_point += 1
            except Exception as e:
                if VERBOSE:
                    print(e)

            ### hill_descending
            try:
                ### Note: the "mp.compute_attacking_pairs" will be
                ### replaced during the grading
                ### with an implementation by grader for grading purpose
                result2 = run_function_with_timeout(
                    mp.hill_descending_n_queens,
                    (copy.deepcopy(state), mp.compute_attacking_pairs),
                )
                
                if is_local_min and (result2 == state):
                    hill_descending_point += 1
                # else: print(state,hill_descending_point)
                if not is_local_min:
                    if num_attacking_pair > mp.compute_attacking_pairs(
                        copy.deepcopy(result2)
                    ):
                        hill_descending_point += 1
                # print(state,hill_descending_point)
            except Exception as e:
                if VERBOSE:
                    print(e)

    ### n_queens
    for n in [4, 8, 10,9,14,6,7,13,11,14,11,11,11,11,13,12,15]:
        try:
            ### Note: the "mp.compute_attacking_pairs" will be
            ### replaced during the grading
            ### with an implementation by grader for grading purpose
            result3 = run_function_with_timeout(
                mp.n_queens,
                [
                    n,
                    mp.get_random_state,
                    mp.compute_attacking_pairs,
                    mp.hill_descending_n_queens,
                ],
                timeout=3,
            )
            if mp.compute_attacking_pairs(result3) == 0:
                n_queens_point += 1
            print(n,n_queens_point)
        except Exception as e:
            if VERBOSE:
                print(e)

    print("get_random_state passed: %d/5" % get_random_state_point)
    print("compute_attacking_pairs passed: %d/5" % compute_attacking_pairs_point)
    print("hill_descending passed: %d/5" % hill_descending_point)
    print("n_queens passed: %d/5" % n_queens_point)

    ### Search Problems

    dfs_points = 0
    bfs_points = 0
    uc_points = 0
    astar_points = 0

    for graph_num in range(1, 6):
        with open(
            os.path.join("testcases", "graph_" + str(graph_num)), "rb"
        ) as file_obj:
            (graph, start, goal, dfs_ret, bfs_ret, uc_ret, astar_ret) = pickle.load(
                file_obj
            )
            try:
                result1 = run_function_with_timeout(
                    _graph_search,
                    [
                        copy.deepcopy(graph),
                        start,
                        goal,
                        mp.add_to_queue_DFS,
                        mp.is_queue_empty_DFS,
                        mp.pop_front_DFS,
                        _heuristic_zero,
                    ],
                )
                if result1 == dfs_ret:
                    dfs_points += 1
            except Exception as e:
                if VERBOSE:
                    print(e)
            try:
                result2 = run_function_with_timeout(
                    _graph_search,
                    [
                        copy.deepcopy(graph),
                        start,
                        goal,
                        mp.add_to_queue_BFS,
                        mp.is_queue_empty_BFS,
                        mp.pop_front_BFS,
                        _heuristic_zero,
                    ],
                )
                if result2 == bfs_ret:
                    bfs_points += 1
            except Exception as e:
                if VERBOSE:
                    print(e)
            try:
                result3 = run_function_with_timeout(
                    _graph_search,
                    [
                        copy.deepcopy(graph),
                        start,
                        goal,
                        mp.add_to_queue_UC,
                        mp.is_queue_empty_UC,
                        mp.pop_front_UC,
                        _heuristic_zero,
                    ],
                )
                ### check cost
                if result3[1] == uc_ret[1]:
                    uc_points += 2
            except Exception as e:
                if VERBOSE:
                    print(e)
            try:
                result4 = run_function_with_timeout(
                    _graph_search,
                    [
                        copy.deepcopy(graph),
                        start,
                        goal,
                        mp.add_to_queue_ASTAR,
                        mp.is_queue_empty_ASTAR,
                        mp.pop_front_ASTAR,
                        _heuristic_function,
                    ],
                )
                ### check cost
                if result4[1] == astar_ret[1]:
                    astar_points += 2
            except Exception as e:
                if VERBOSE:
                    print(e)
    print("dfs search %d / 5" % dfs_points)
    print("bfs search %d / 5" % bfs_points)
    print("uc search %d / 10" % uc_points)
    print("astar search %d / 10" % astar_points)
    print(
        "Total %d / 50"
        % (
            get_random_state_point
            + compute_attacking_pairs_point
            + hill_descending_point
            + n_queens_point
            + dfs_points
            + bfs_points
            + uc_points
            + astar_points
        )
    )


if __name__ == "__main__":
    main()