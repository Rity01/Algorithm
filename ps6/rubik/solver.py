import rubik
from rubik import perm_apply
def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    if start == end:
        return []

    levels = 7
    nodesDict1 = {start:0}
    nodesDict2 = {end:0}
    nodes1 = [start]
    nodes2 = [end]
    exit_flag = False
    middle = ()
    for i in range(7):
        newnodes = []
        for node in nodes1:
            for twist in rubik.quarter_twists:
                newnode = perm_apply(twist, node)
                
                if nodesDict1.has_key(newnode) == False:
                    newnodes.append(newnode)
                    nodesDict1[newnode] = (twist,node)
                    if nodesDict2.has_key(newnode):
                        middle = newnode
                        exit_flag = True
                        break
            if exit_flag:
                break
        nodes1 = newnodes
        if exit_flag:
            break

        
        
        newnodes = []
        for node in nodes2:
            for twist in rubik.quarter_twists:
                newnode = perm_apply(twist, node)
                
                if nodesDict2.has_key(newnode) == False:
                    newnodes.append(newnode)
                    nodesDict2[newnode] = (twist,node)
                    if nodesDict1.has_key(newnode):
                        middle = newnode
                        exit_flag = True
                        break
            if exit_flag:
                break
        nodes2 = newnodes
        if exit_flag:
            break

    

    if middle == ():
        return None
    
    res = []
    nodetravel = middle
    while nodesDict1[nodetravel] != 0:
        res.insert(0,nodesDict1[nodetravel][0])
        nodetravel = nodesDict1[nodetravel][1]
    nodetravel = middle
    while nodesDict2[nodetravel] != 0:
        res.append(rubik.perm_inverse(nodesDict2[nodetravel][0]))
        nodetravel = nodesDict2[nodetravel][1]
    
    print(res)
    print("===============",len(res),"============")
    # print([rubik.F])
    print([rubik.F, rubik.L])
    
    return res
