import random
from collections import deque
from queue import PriorityQueue
import numpy as np
import time 
bfs_q = deque()
dfs_q = []
ucs_q = PriorityQueue()
as_q = PriorityQueue()


''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For Search Algorithms 
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''

'''
BFS add to queue 
'''
def add_to_queue_BFS(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    if initialize == True:
        global bfs_q 
        bfs_q = deque()
    bfs_q.append((node_id, parent_node_id))
    return

'''
BFS add to queue 
'''
def is_queue_empty_BFS():
    # Your code here
    global bfs_q
    if len(bfs_q) == 0:
        return True
    return False


'''
BFS pop from queue
'''
def pop_front_BFS():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    global bfs_q
    (node_id, parent_node_id) = bfs_q.popleft()
    return (node_id, parent_node_id)


'''
DFS add to queue 
'''
def add_to_queue_DFS(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    
    if initialize == True:
        global dfs_q
        dfs_q = [] 
    dfs_q.append((node_id, parent_node_id))
    # print dfs_q
    return


'''
DFS add to queue 
'''
def is_queue_empty_DFS():
    # Your code here
    global dfs_q
    if len(dfs_q) == 0:
        return True
    return False


'''
DFS pop from queue
'''
def pop_front_DFS():
    (node_id, parent_node_id) = (0, 0)
    # # Your code here
    global dfs_q
    (node_id, parent_node_id) = dfs_q.pop()
    return (node_id, parent_node_id)


'''
UC add to queue 
'''
def add_to_queue_UC(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    if initialize == True:
        global ucs_q
        ucs_q = PriorityQueue()
    ucs_q.put((cost, (node_id, parent_node_id)))
    return


'''
UC add to queue 
'''
def is_queue_empty_UC():
    # Your code here
    global ucs_q
    if ucs_q.empty():
        return True
    return False



'''
UC pop from queue
'''
def pop_front_UC():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    (_,(node_id, parent_node_id)) = ucs_q.get()
    return (node_id, parent_node_id)


'''
A* add to queue 
'''
def add_to_queue_ASTAR(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    if initialize == True:
        global as_q
        as_q = PriorityQueue()
    as_q.put((cost, (node_id, parent_node_id)))
    return


'''
A* add to queue 
'''
def is_queue_empty_ASTAR():
    # Your code here
    global as_q
    if as_q.empty():
        return True
    return False


'''
A* pop from queue
'''
def pop_front_ASTAR():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    (_,(node_id, parent_node_id)) = as_q.get()
    return (node_id, parent_node_id)


''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For n-queens problem 
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''


'''
Compute a random state 
'''
def get_random_state(n):
    state = []
    # Your code here 
    for i in range(n):
        state.append(random.randint(1,n))
    # state = list(np.random.randint(0,n-1,n))
    return state

'''
Compute pairs of queens in conflict 
'''
def compute_attacking_pairs(state):
    number_attacking_pairs = 0
    # Your code here 
    n = len(state)
    for i in range(n):
        for j in range(i+1,n):
            if state[i] == state[j]:
                number_attacking_pairs += 1
            elif abs(state[i] - state[j]) == abs(i - j):
                number_attacking_pairs += 1
    return number_attacking_pairs

'''
The basic hill-climing algorithm for n queens
'''
def hill_descending_n_queens(state,comp_att_pairs):
    n = (len(state))
    min_cost = compute_attacking_pairs(state)
    # print(f"min_cost:{min_cost}")
    min_state = state
    min_prv = 0
    while min_cost !=  min_prv:
        state = min_state[:]
        min_prv = min_cost
        for i in range(n):
            current = state[:]
            for j in range(1,n+1):
                if j != current[i]:
                    current[i] = j
                    cst = comp_att_pairs(current)
                    if cst  <  min_cost:
                        min_cost = cst
                        min_state = current[:]
                        if cst == 0:
                            return min_state
            if min_cost == 0:
                return min_state
        if min_cost == 0:
            return min_state

    
    return min_state

'''
Hill-climing algorithm for n queens with restart
'''
def n_queens(n, get_rand_st, comp_att_pairs, hill_descending):
    if n <= 2:
        final_state = []
    else:
        cst = float('inf')
        while cst != 0: 
            state = get_random_state(n)
            # start = time.time()
            final_state = hill_descending(state,comp_att_pairs)
            # end = time.time()
            cst = comp_att_pairs(final_state)
            # print(final_state,cst,(end - start))
    return final_state






