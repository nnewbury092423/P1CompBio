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
        
        # create ancestor set
        ancestor = set()
        
        # create dictionary
        if not u in LCA:
            LCA[u] = {}
          
        if v not in LCA[u]:
            LCA[u][v] = set()
        
            
        # base cases    
        if u == v:  
            LCA[u][v] = {u}
            return LCA[u][v]
        
        if parent[u] == set() or parent[u] == []:
            LCA[u][v] = {u}
            return LCA[u][v]

        if parent[v] == set() or parent[v] == []:
            LCA[u][v] = {v}
            return LCA[u][v]
        
        # recursive formula
        for pu in parent[u]:
            #print(type(pu))
            #print(type(v))
            #print(LCA[pu][v])
            if not LCA[pu][v] == set():
                ancestor = ancestor|LCA[pu][v] 
            
        for pv in parent[v]:
            if not LCA[u][pv] == set():
                ancestor = ancestor|LCA[u][pv] 
        
         # remove the ancestors that are not LCA
        for n1 in ancestor:
            for n2 in ancestor:
                if n1!=n2:
                    #print(LCA[n1][n2])
                    ancestor = ancestor - LCA[n1][n2]


      
        
        # save ancestor, which is now LCA into our LCA dictionary
        LCA[u][v] = ancestor
        return LCA[u][v] # TODO replace this with your code


    # Now, we will call your recursive "lca" function on all pairs of nodes to populate the "LCA" dictionary
    for u in parent:
        for v in parent:
            lca(u,v)
    return LCA
