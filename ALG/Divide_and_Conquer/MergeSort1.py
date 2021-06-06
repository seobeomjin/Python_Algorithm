# merge sort 1 - using additional space +2n 

# global additional_space_1 
# global additional_space_2 

# additional_space_1 = 0 
# additional_space_2 = 0

def mergesort1(n, s) :

    if n <=1 : 
        return s
    else :  
        h = n//2 
        m = n-h
    
        u = s[:h]
        v = s[h:]
        
        mergesort1(h,u)
        mergesort1(m,v)
        merge1(h,m,u,v,s)

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

data = [3,16,13,1 ,9,2,7,5, 8,4,11,6, 15,14,10,12]

mergesort1(len(data), data)
print(data)

# error 
# index 문제였음 :h , h: