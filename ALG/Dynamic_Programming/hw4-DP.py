
# page 21 Floyd

def printMatrix(d:"Matrix") -> "print Matrix":
    n = len(d[0])
    for i in range(n):
        for j in range(n):
            print(d[i][j], end=" ")
        print()

def allShortestPath(g: "connection info", n: "size of mat") -> "arr" :
    
    # Floyd2 Algorithm  
    
    p = [[0 for j in range(n)] for i in range(n)]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if g[i][k] + g[k][j] < g[i][j] : 
                    p[i][j] = k+1 # it means there exists a conncection , update it as the largest node number
                    g[i][j] = g[i][k]+g[k][j] # set it as the shortest path 

                # g[i][j] = min(g[i][j], g[i][k]+g[k][j])
    return g, p 


# page 25 shortest path 

def path(p, q, r): 
    if p[q-1][r-1]!=0 : 
        path(p, q, p[q-1][r-1]) 
        print(f"v{p[q-1][r-1]}", end=" ")
        path(p, p[q-1][r-1],r)


# infinite 
inf=1000

# connection info
g=[[0,1,inf, 1,5],
   [9,0,3,2,inf],
   [inf,inf,0,4,inf],
   [inf,inf,2,0,3],
   [3,inf,inf,inf,0]]

d, p = allShortestPath(g,5)
print()
printMatrix(d)
print()
printMatrix(p) 

path(p ,5, 3)