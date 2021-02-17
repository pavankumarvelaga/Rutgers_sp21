

'''
GCD algorithm
'''
def gcd(a, b):
    gcd_dict = {'rem':[a,b],'x':[0,1],'y':[1,0]}
    while gcd_dict['rem'][0] != 0:
        f = gcd_dict['rem'][1]//gcd_dict['rem'][0]
        
#         Creating Function For GCD
        r_temp = gcd_dict['rem'][1] 
        gcd_dict['rem'][1] = gcd_dict['rem'][0]
        gcd_dict['rem'][0] =  r_temp - f*gcd_dict['rem'][1]
        
#         Creating funtion for first coeffiecient x in ax+by = GCD(a,b)
        x_temp = gcd_dict['x'][0]
        gcd_dict['x'][0] = gcd_dict['x'][1]
        gcd_dict['x'][1] = x_temp - gcd_dict['x'][0]*f

#         Creating funtion for first coeffiecient y in ax+by = GCD(a,b)
        y_temp = gcd_dict['y'][0]
        gcd_dict['y'][0] = gcd_dict['y'][1]
        gcd_dict['y'][1] = y_temp - gcd_dict['y'][0]*f
        
        
#         print(gcd_dict,f)
    return [gcd_dict['rem'][1],gcd_dict['x'][0],gcd_dict['y'][0]]
    
    
    
    

'''
Rectangles on a rubik's cube
'''
from math import comb
def rubiks(n):
    if n < 0:
        return(-1)
    return(comb(n+1,2)*comb(n+1,2)*6)


'''
Guessing a number
'''
def guess_unlimited(n, is_this_it):
    # The code here is only for illustrating how is_this_it() may be used 
    for i in range (1,n+1):
        if is_this_it(i) == True:
            return i
    return -1
    
        
'''
Guessing a number where you can only make two guesses that are larger
'''
def guess_limited(n, is_this_smaller):
  
    if n == 1:
        return(1)
    if is_this_smaller(n//2):
        if is_this_smaller(3*n//4):
            
            for i in range(int(3*n)//4,n+1,2):
                if not(is_this_smaller(i)):
                    if is_this_smaller(i-1):
                        return(i)
                    else: 
                        return(i-1)
        else:
            for i in range(n//2,(3*n)//4 + 1,2):
                if not(is_this_smaller(i)):
                    
                    if is_this_smaller(i-1):
                        return(i)
                    else: 
                        return(i-1) 

    else:
        for i in range(0,n//2 + 1,1):
            if not(is_this_smaller(i)):
                return(i)
                
    return(-1)
        
    
        

'''
Graph operations  
'''
def  add_vertex(graph):
    graph[len(graph.keys())+1] = []
    return graph

def  delete_vertex(graph, vid):
    del graph[vid]
    dict1 = {}
    for i in graph.keys():
        graph[i] = [i if i < vid else i-1 if i > vid else -1 for i in graph[i]]
        graph[i] = [i for i in graph[i] if i > 0]
        if i<vid:
            dict1[i] = graph[i]
        elif i > vid:
            dict1[i-1] = graph[i]
    return dict1


def  add_edge(graph, vid1, vid2):
    if ((vid1 in graph.keys()) and (vid2 in graph.keys())):
        if vid2 not in graph[vid1]:
            graph[vid1].append(vid2)
            graph[vid1] = sorted(graph[vid1])
            graph[vid2].append(vid1)
            graph[vid2] = sorted(graph[vid2])
    return graph

def  delete_edge(graph, vid1, vid2):
    if ((vid1 in graph.keys()) and (vid2 in graph.keys())):
        if vid2 in graph[vid1]:
            graph[vid1].remove(vid2)
        if vid1 in graph[vid2]:
            graph[vid2].remove(vid1)
    return graph

def dfs(g, node, visited):
    if node not in visited:
        visited.append(node)
        # print(1,visited)
        for neighbor in g[node]:
            dfs(g, neighbor, visited)
    # print(1,visited)
    return visited



def  is_connected(graph):
    visited = []
    vst = dfs(graph, 1, visited)
    
    if len(set(vst))!= len(graph.keys()):
        return False
    
    return True



def dfs_v1(g,node, visited,prevn):
    if node != prevn:
        visited.append(node)
        if len(set(visited)) != len(visited):
#                 print(neighbor, visited)
                return (True,visited)
        for neighbor in g[node]:
            # print(neighbor, visited)
            
            if neighbor != prevn:
                if dfs_v1(g, neighbor, visited, node)[0]:
                    return (True, visited)
            # print(neighbor, visited)
    return (False,visited)

def dfs_v2(g,v):
    lst = [i for i in g.keys() if i not in v]
    if not(lst):
        return False
    f,v = dfs_v1(g,lst[0], v,0)
    # print(lst[0],f,v)
    if f:
        return f

    else:
        return(dfs_v2(g,v))

def  has_cycle(graph):
   ret = dfs_v2(graph,[])
   return ret   
    


