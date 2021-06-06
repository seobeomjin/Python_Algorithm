# merge sort 2 - using less additional space, +n

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

data = [3,16,13,1 ,9,2,7,5, 8,4,11,6, 15,14,10,12]
mergesort2(data, 0, len(data)-1)
print(data)
# print(add_sp_2)
