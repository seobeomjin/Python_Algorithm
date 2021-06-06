
# - 다음 python 프로그램을 작성하여 하나의 파일에 담아 e-campus에 업로드
# - 프로그램 파일명은 hw3+이름+학번.py 로 설정
# -동일한 제출물은 마이너스 점수의 페널티 부과

# 실습강의동영상 실습p4_divide_conquer_quick_strassen.mp4 에서
# (1) 8쪽: [실습프로그램] 빠른정렬 프로그램을 python으로 완성하라
# (2) 30쪽: [실습프로그램] 큰 정수 곱셈 알고리즘을 python으로 완성하라. 여기서 threshold를 4로 설정한다.


############# page8 , quicksort #############
def quicksort(s, low, high):
    if low < high : 
        pivotPoint = partition(s, low, high)
        quicksort(s, low, pivotPoint-1)
        quicksort(s, pivotPoint+1, high)    

def partition(s, low, high): 
    j = low 
    pivotItem = s[low]
    for i in range(low+1, high+1): 
        if s[i] < pivotItem : 
            j +=1 
            tmp = s[j]
            s[j] = s[i]
            s[i] = tmp 
    pivotPoint = j 
    s[low] = s[pivotPoint]
    s[pivotPoint] = pivotItem
    return pivotPoint
    
############# page30 , big integer multiplication #############

def prod2(a,b): 
    # u = x*10^m + y / 
    # v = w*10^m + z / 
    n = max(len(str(a)), len(str(b)))
    if a == 0 or b == 0 : 
        return 0 
    elif n <= 4 : 
        return a*b
    else : 
        m = n//2 
        x = a//pow(10,m)
        y = a % pow(10,m)
        w = b//pow(10,m)
        z = b % pow(10,m)

        r = prod2(x+y, w+z)
        p = prod2(x,w)
        q = prod2(y,z) 
        return p*pow(10,2*m) + (r-p-q)*pow(10,m) + q 

if __name__ == "__main__": 
    # quick sort 
    s = [3,5,2,9,10,14,4,8]
    quicksort(s,0,7)
    print(s)

    # big interger multiplication 
    a=1234567812345678
    b=2345678923456789
    print(prod2(a,b))
    print(a*b)

