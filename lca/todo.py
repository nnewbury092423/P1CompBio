def find_LCAs(parent):
    LCA = dict() # This is the nested dictionary you will be modifying
  
    # TODO You will fill in the following "lca" function
    def lca(u, v):
        '''
        This function computes the Least Common Ancestor between nodes u and v
        :param u: node u
        :param v: node v
        :return: A set containing the LCAs of u and v
        '''
        #print(type(u)) string
        #print(type(v)) string
        testset = set()
        if not u in LCA:
            LCA[u] = {}
          
        if v not in LCA[u]:
            LCA[u][v] = set()
            
        if u == v:
            LCA[u][v] = {u}
            return LCA[u][v]
        
        if parent[u] == set() or parent[u] == []:
            LCA[u][v] = {u}
            return LCA[u][v]

        if parent[v] == set() or parent[v] == []:
            LCA[u][v] = {v}
            return LCA[u][v]
        

        for pu in parent[u]:
            #print(type(pu))
            #print(type(v))
            #print(LCA[pu][v])
            if not LCA[pu][v] == set():
                testset = testset|LCA[pu][v] 
            
        for pv in parent[v]:
            if not LCA[u][pv] == set():
                testset = testset|LCA[u][pv] 
        
        for n1 in testset:
            for n2 in testset:
                if n1!=n2:
                    #print(LCA[n1][n2])
                    testset = testset - LCA[n1][n2]


        #if len(testset) > 1:
         #   for elem in testset:
        #subtract = set()
        #for a in testset:
         #   for b in testset:
         #       if a != b and LCA[a][b] != set():
          #          subtract = subtract | LCA[a][b]
        #print( u + v)      
        
        # need optimal test set
        LCA[u][v] = testset
       # LCA[u][v] -= subtract 
        return LCA[u][v] # TODO replace this with your code


    # Now, we will call your recursive "lca" function on all pairs of nodes to populate the "LCA" dictionary
    for u in parent:
        for v in parent:
            lca(u,v)
    return LCA
