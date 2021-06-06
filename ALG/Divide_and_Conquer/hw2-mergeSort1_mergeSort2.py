# 실습동영상 p3_divide_conquer_mergesort 에서 
# 16쪽: [실습프로그램] 합병정렬
# 22쪽: [실습프로그램] 합병정렬2에 대해

# 각 합병정렬 알고리즘 수행에 필요한 추가적인 저장공간(합병정렬 ≒2n, 합병정렬2=n)을 계산할 수 있도록 기능을 추가하여 구현하라. 
# 수행 종료 후 필요한 추가적인 저장공간의 개수 및 정렬된 데이터를 출력
# 사용한 공간을 반납하는 과정을 고려하여야 함.
# 하나의 프로그램으로 작성
# 데이터 = [3,16,13,1 ,9,2,7,5, 8,4,11,6, 15,14,10,12]를 이용하여 프로그램을 검증한다.

# class for counting
class Count : 
    def __init__(self): 
        self.current_space = 0 
        self.used_space = 0 
    def add(self, l): 
        self.current_space += len(l)
    def sub(self, l): 
        self.current_space -= len(l)
    def compare(self):
        self.used_space = max(self.current_space, self.used_space)
    def look_at_me(self): 
        print(f"curr : {self.current_space}  /  used : {self.used_space}")

# page 16 합병정렬
# using additional space, 2n
def mergesort1(n, s) :
    if n <=1 : 
        return s
    else :  
        h = n//2 
        m = n-h
    
        u = s[:h] 
        v = s[h:] 

        count1.add(u)
        count1.add(v)
        count1.compare()
        # count1.look_at_me()

        mergesort1(h,u) 
        mergesort1(m,v)
        merge1(h,m,u,v,s)

        count1.sub(u) # 합병 후 반환  
        count1.sub(v) # 합병 후 반환 
        
def merge1(h,m,u,v,s) : 
    i, j, k = 0,0,0 
    while i<h and j<m: 
        if u[i] < v[j] : 
            s[k] = u[i]
            i +=1 
        else : 
            s[k] = v[j]
            j +=1 
        k +=1 
    if (i>=h): 
        while j < m : 
            s[k] = v[j]
            k +=1 
            j +=1 
    else : 
        while i < h : 
            s[k] = u[i]
            k +=1 
            i +=1 

# page 22 합병정렬2
# using less additional space, n 
def mergesort2(s, low, high) : 
    if low >= high: 
        return s 
    else : 
        mid = (low+high)//2
        mergesort2(s, low, mid) # index 다 포함시키는. 
        mergesort2(s, mid+1, high)
        merge2(s, low, mid, high)

def merge2(s, low, mid, high):
    i = low # iterative index 1
    j = mid+1 # iterative index 2 
    k = 0 # u 시작하는 첫 원소 
    u = [0]*(high-low+1) # u 배열 크기 

    count2.add(u) # merge 시, 공간 추가 
    count2.compare() 
    # count2.look_at_me()

    while i<=mid and j<=high : 
        if s[i] < s[j] : 
            u[k] = s[i]
            i +=1 
        else : 
            u[k] = s[j]
            j +=1 
        k +=1 
    if i > mid : 
        while j <=high : 
            u[k] = s[j]
            j +=1
            k +=1 
    else : 
        while i <= mid: 
            u[k] = s[i]
            i +=1 
            k +=1 
    s[low:high+1] = u[:] # ★★★★★ s 배열의 low에서 high까지 들어가야 함
    count2.sub(u) # merge 이후 반환 


data1 = [3,16,13,1 ,9,2,7,5, 8,4,11,6, 15,14,10,12]
data2 = data1[:]

count1 = Count()
count2 = Count()

mergesort1(len(data1), data1)
print(f"merge sort 1 : {data1}")
print(f"additional space : {count1.used_space}")

mergesort2(data2, 0, len(data2)-1)
print(f"merge sort 2 : {data2}")
print(f"additional space : {count2.used_space}")

