

# Q1
# page 6 - DFS  
# output = (visit sequence, visited node)
# first visit sequence is set as 1 
# 1 0
# 2 1
# 3 2
# 4 3
# 5 4
# 6 6
# 7 7
# 8 5

import utility
e = {0:[1,2,3], 1:[2,5], 2:[3,4,5,6], 3:[4,6], 4:[6,7]}
n = 8 
a = [ [0 for j in range(0,n)] for i in range(0,n)]
# index는 nlgn만큼만 보고(반만 보고), 값은 연결된 모든 index에 넣어준 matrix  
for i in range(0,n-1): # 0에서 6까지 . 7번째는 어차피 돌 필요 없음. identity는 검사 안하니까 
    for j in range(i+1, n):  #1에서 7까지  # [6][7]까지 다 도는 것. #upper triangular matrix만 검사  
        if i in e : 
            if j in e[i] :
                a[i][j]=1
                a[j][i]=1 
utility.printMatrix(a)
#    0    1    1    1    0    0    0    0
#    1    0    1    0    0    1    0    0
#    1    1    0    1    1    1    1    0
#    1    0    1    0    1    0    1    0
#    0    0    1    1    0    0    1    1
#    0    1    1    0    0    0    0    0
#    0    0    1    1    1    0    0    0
#    0    0    0    0    1    0    0    0

visited = n*[0]
n = len(a)
seq = 1

# 왜 n 과 visited는 global로 지정도 안해줬는데 DFS에서 쓸 수 있고, 
# k 는 global로 지정해줘야 쓰이는가?  

def DFS(a, v): 
    global seq, n, visited

    if v == 0 : 
        print(seq, 0)
        seq +=1

    for i in range(v+1, n): 
        if a[v][i] == 1 and visited[i]!=1:
            print(seq,i)  # sequence, node idx / 방문순서는 카운트하면 되고, 노드번호는 계속 트래킹 
            visited[i] = 1
            seq += 1
            DFS(a, v+1) 

print(f"----------------- DFS -----------------")        
DFS(a,0) # visit from node 0

#-----------------------------------------------------#
# + BFS 

seq_, n_ = 1, len(a)
visited_ = [0]*n_ 

def BFS(a, v): 
    global seq_, n_, visited_ 
    
    q = []
    q.append(v)

    while q : 
        node = q.pop(0)  # 0 node first 
        visited_[node]=1  # 0 node visited
        print(seq_, node) # print
        seq_ +=1 
        for i in range(node+1, n_): # 1,2,3 node will be inserted to the queue orderly   
            if a[node][i] == 1 and visited_[i]!=1 :
                if i not in q : 
                    q.append(i) 
            # print(f"q : {q}")
print(f"----------------- BFS -----------------")      
BFS(a, 0)

#-----------------------------------------------------#
# Q2
# page 18 - n Queens, n=7
# print => "# of total solution" and "third solution"

# i번째가 유망한지를 확인하고, 그리고 그 i가 마지막인 n번째 칼럼이면 
# 그 이전은 모두 유망하기 때문에 n번째까지 온거니까 답을 출력할 수 있게 됨. 

# queens의 맨 마지막 else 부분에서, 이 부분이 일종의 DFS 처럼 굴러가는 듯. 
# 그리고 if i==n 이 stopping point 

def promising(i, col) : 
    k = 0 
    switch = True 
    while k<i and switch : 
        if col[i]==col[k] or abs(col[i]-col[k])==i-k : 
            switch = False
        k +=1 
    return switch

def queens(n, i, col): 
    global count, third_solution
    if promising(i, col):
        if i == n-1 :
            count +=1 
            print(col)
            if count == 3 : 
                third_solution[:] = col[:]
        else : 
            for j in range(0,n):
                col[i+1] = j 
                queens(n, i+1, col)
            
print(f"----------------- 7 Queens -----------------") 
n = 7
col = n*[0]
count = 0 
third_solution = []
queens(n, -1, col)
print(f"\nnumber of solutions : {count} \n3rd solution : {third_solution}")