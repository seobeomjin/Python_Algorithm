# 실습강의 실습p12_BB에서 다음 데이터를 이용하려 (1), (2)를 해결하라. 
# W=8
#   pi wi pi/wi
# 1 $48 4 12
# 2 $55 5 11
# 3 $16 4 4
# 4 $16 8 2
# (1) 10,11쪽: [실습프로그램] 분기한정 가지치기 깊이우선검색 방법으로 0-1 배낭문제를
# 해결하는 알고리즘을 python으로 완성하라.
# (2) 24,25쪽: [실습프로그램] 분기한정 가지치기 최고우선검색 방법으로 0-1 배낭문제를
# 해결하는 알고리즘을 python으로 완성하라. 



# solve the 0-1 KnapSack Problem  
# BB-DFS 

############################################
# knapsack function : 
#     1. current status check 
#         if weight <=W and profit > max profit : 
#             bestset = include 
#             num_items = i
#             max profit = profit 
#     2. if next status is also promising, keep going 
#         promising check function have to be developed. 
#         if promising : 
#             knapsack(i+1, profit, weight)
#             knapsack(i+1, progit+1, weight+1)

# promising function : 
    # check weight 
    # check bound 
############################################

def knapsack(i, profit, weight): 
    # global parameter setting 
    global max_profit, best_set, include, W, w

    # current status check 
    if (weight <= W and profit > max_profit) : 
        max_profit = profit 
        num_items = i 
        best_set = include[:]

    # if next status is also promising, keep going! 
    if promising(i, profit, weight):
        include[i+1] = 1 
        knapsack(i+1, profit+p[i+1], weight+w[i+1]) # put i-th item
        include[i+1] = 0 
        knapsack(i+1, profit, weight) # not put i-th item  

def promising(i, profit, weight): 
    global max_profit, W, w
    j, k, bound, totweight = 0, 0, 0, 0 

    # weight check 
    if weight >=W : 
        return False 
    # whether bound is larger than max_profit 
    else : 
        j = i+1 
        bound = profit 
        totweight = weight 
        while(j<=n-1 and totweight + w[j] <= W):
            totweight = totweight + w[j]
            bound = bound + p[j]
            j +=1 
        k = j 
        if k <=n-1 : 
            bound = bound + (W-totweight)*(p[k]/w[k])
        return bound > max_profit
############################################    ############################################    ############################################ 






# solve the 0-1 KnapSack Problem  
# BB-Best First Search 

############################################
# Node class 
    #level , weight , profit, bound , include 
# Knapsack BestFS BB Function
    # v = Node()
    # PQ.put(v)
    # while not PQ.empty(): 
    #     v = PQ.get()
    #     if v.bound > max rpofit : 
    #         # add next item case 
    #         u = Node(level+1, weight+= w[i+1], ~)
    #         if (w <= W and max < current profit): 
    #             max = profit 
    #         u.bound = bound(u)

    #         # not add next item case 
# Bound Function
############################################

import queue 

class Node : 
    def __init__(self, level=None, weight=None, profit=None, bound=None, include=None):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.bound = bound
        self.include = include 

    def __cmp__(self, other) :
        return cmp(self.bound, other.bound)

    def __lt__(self, other): ##################
        return self.bound < other.bound

    def info(self):
        print(f"level : {self.level}\nweight : {self.weight}\nprofit : {self.profit}\nbound : {self.bound}\n include : {self.include}")

def knapsack_BestFS_BB():
    global max_profit, best_set, include
    num_nodes = 0
    v = Node(-1, 0, 0, 0.0, include) #level, weight, profit, bound, include
    v.bound = compBound(v) #negative 
    
    # num_nodes += 1 
    # print(f"num_node : {num_nodes}")
    # v.info()

    q = queue.PriorityQueue()
    q.put(v)
    # q.put((v.bound, v))
    
    while not q.empty() :  ##############  
        v = q.get()
        if v.bound < -max_profit :  # ex. -115 < -(40) -> keep going 
        # min heap!!(not maxheap) , bound의 절댓값이 가장큰 음수가 가장 위에 옴.  
        # each profit : positive / # each bound : negative
        # bound 랑 max profit 비교할 때만 음수 비교

        # case 1) that add next item 
            # u is children node of v  
            u = Node(
                v.level +1, 
                v.weight + w[v.level +1], 
                v.profit + p[v.level +1], 
                None, 
                None)
            u.include = v.include[:] 
            u.include[u.level] = 1

            # if it is valid, update current max profit   
            if u.weight <= W and u.profit > max_profit : # 양수, 양수 비교.  # 타당하니 update 
                max_profit = u.profit 
                best_set = u.include[:]

            # update its bound  
            u.bound = compBound(u) # it's negative 

            # just check 
            # num_nodes += 1 
            # print(f"num_node : {num_nodes}")
            # v.info()

            if u.bound < -max_profit : # ex. -115 < -(90)  # 더 발전할 여지가 있는가 ? 
                q.put(u) 
                # u.info()

        # case 2) that not add next item
            u = Node(
                v.level+1, 
                v.weight, 
                v.profit, 
                None, 
                None) 
            u.include = v.include[:]

            # update its bound 
            u.bound = compBound(u)

            # just check 
            # num_nodes += 1 
            # print(f"num_node : {num_nodes}")
            # v.info()

            if u.bound < -max_profit : #ex. -110 < -90 # 발전할 여지가 있는가? 
                q.put(u)
                # u.info()

def compBound(u):
    global W, w, p
    j, k, total_weight, bound = 0, 0, 0, 0

    if u.weight >= W : 
        return 0
    else : 
        bound = u.profit 
        j = u.level+1 
        total_weight = u.weight 
        while j<=n-1 and total_weight + w[j] <= W:
            total_weight += w[j]
            bound += p[j]
            j +=1 
        k = j 
        if k<=n-1 : 
            bound += (W-total_weight)*(p[k]/w[k])
        return -bound   ########### -1*
    
if __name__ == "__main__": 
    n = 4 

    # homework 
    W = 8 
    p = [48, 55, 16, 16]   
    w = [4, 5, 4, 8]    
    
    # practice
    # W = 16
    # p = [40, 30, 50, 10]
    # w = [2, 5, 10, 5]

    p_over_w = [12, 11, 4, 2]
    max_profit = 0 
    include = [0]*n
    best_set = [0]*n

    print()
    print("Q1) 0-1 knapsack problem via BB-DFS method")
    knapsack(-1, 0, 0)
    print(f"max profit: {max_profit}\tbset set: {best_set}")     
    
    print()
    print("Q2) 0-1 knapsack problem via BB-Best First Search method")
    knapsack_BestFS_BB()
    print(f"max profit: {max_profit}\tbset set: {best_set}")     

    

