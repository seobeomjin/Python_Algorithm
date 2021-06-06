
# implement binary search using recursive method 
# binary search 
def binary_search(arr, target, left, right) : 
    
    if left > right : 
        return 0 
    else : 
        mid = (left + right) // 2
        if target == arr[mid] : 
            return mid 
        else : 
            if arr[mid] < target : 
                return binary_search(arr, target, mid+1, right)
            else : 
                return binary_search(arr, target, left, mid-1)

arr =[1,3,5,6,7,9,10,14,17,19]        
target = 10 
pos = binary_search(arr, target, 0, len(arr)-1)
print(f"position is {pos}")

# error 
# 1. mid point setting error 
# 2. return mistype 
# 3. floor division 
    

 


