# (1) 9쪽: [실습프로그램] 부분집합의 합 문제 해결 알고리즘을 python으로 완성하라. 모
# 든 해를 출력하도록 작성할 것. 데이터는 S={1,2,3,4,5,6}, W=9 로 할 것.
# (2) 15쪽: [실습프로그램] m-coloring 문제 해결 알고리즘을 python으로 완성하라. 모든
# 해를 출력하도록 작성할 것.


# page 9 - sum of subsets  

def ss_promising(i, weight, total): 
    return (weight+total >=W) and (weight==W or weight+w[i+1] <=W)

def sum_of_subsets(i, weight, total, include): 
    global W
    if ss_promising(i, weight, total):
        if (weight == W) : 
            print(f"sol : {include}")
        else : 
            if i < n-1 :  
                include[i+1] = 1
                sum_of_subsets(i+1, weight+w[i+1], total-w[i+1], include)
                include[i+1] = 0 
                sum_of_subsets(i+1, weight, total-w[i+1], include)
            else : 
                print("out of index.")
                exit(100)
                    
n = 6 
w = [1,2,3,4,5,6]
w.sort()
W = 9 
print(f"items : {w} ,W : {W}")
include = n*[0]  # sum of n 
total = 0 
for k in w : 
    total += k 

###### ======================================================= ######

# page 15 - m coloring : print all soutions 
def color(i, vcolor): 
    global W_
    if col_promising(i, vcolor):
        if (i == n_-1): 
            print(vcolor)
        else : 
            for col in range(1,m+1): 
                if i < n_-1:
                    vcolor[i+1] = col 
                    color(i+1, vcolor)
                else :  
                    print("out of index")
                    exit(100)
                

def col_promising(i, vcolor) : 
    switch = True 
    j = 0 
    while (j<i and switch) : 
        if W_[i][j] and vcolor[i]==vcolor[j]: # if connected and same color   
            switch = False 
        j += 1 
    return switch 

n_ = 4  # number of nodes 
W_=[[0,1,1,1],[1,0,1,0],[1,1,0,1],[1,0,1,0]]
vcolor=n_*[0] # assigns a color to each node
m =  3 # number of colors
# color(-1, vcolor)

if __name__ == "__main__":
    sum_of_subsets(-1, 0, total, include)
    color(-1, vcolor)



            