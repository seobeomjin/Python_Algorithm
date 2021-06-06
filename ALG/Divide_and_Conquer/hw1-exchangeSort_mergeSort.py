# [보고서 작성 방법]

# - 보고서 파일명: 이름+학번+al_hw1.pdf 로 저장한 후 e-campus에 기한 내에 업로드
# - 구현된 알고리즘의 source 및 수행 결과 출력물을 포함
# - 시간 및 문제 크기의 추정 근거를 서술
# - 동일한 과제를 제출한 모든 학생들에게 페널티 부과

# 파이썬 프로그램을 이용하여 n개의 데이타 (키 값은 1~100 사이의 자연수)를 정렬하는 문제를 파이썬 프로그램을 이용하여 다음의 내용에 대해 수행한다.
# (1) n개의 데이타를 random으로 생성
# (2) O(n^2) 인 exchange sort 알고리즘(A)와 O(n log n) 알고리즘인 merge sort 알고리즘(B)를 구현
# (3) n=2,000, 4,000, 12,000에 대해 알고리즘 A, B가 종료될 때까지의 시간을 측정한다.
# (4) A, B 를 1분간 수행할 때 해결할 수 있는 문제의 크기 n' 를 (3)의 결과를 이용하여 추정한다. A와 B의 수행시간과 n의 관계를 고려해서 추정할 것.
# (5) n=5,000만일 때의 A, B의 수행시간을 (3)의 결과를 이용하여 추정한다.

# 비내림차순으로. 

# random data generate - 1-100 
    # 1. n 2000 
    # 2. n 4000
    # 3. n 12000 
    
    # 각 수행시간 측정 
    # 
    # n 5000만 일 때 각 알고리즘


import random 
import time

def exchange_sort(n): 
    length = len(n)
    for i in range(length):
        for j in range(i, length): 
            if n[i] > n[j] : 
                tmp = n[j]
                n[j] = n[i]
                n[i] = tmp
    # return n 

def merge_sort(n): 
    if len(n) == 1 : 
        return n
    
    mid = int(len(n)/2)
    l_list = merge_sort(n[:mid])
    r_list = merge_sort(n[mid:])
    result = merge(l_list, r_list)

    return result


def merge(l_list, r_list):
    if len(l_list) < 1 or len(r_list) <1 : 
        return l_list or r_list
    i,j,k = 0,0,0 
    result = []
    len_l = len(l_list)
    len_r = len(r_list)
    while i < len_l and j < len_r : 
        if(l_list[i] < r_list[j]) : 
            result.append(l_list[i])
            i +=1 
        else : 
            result.append(r_list[j])
            j +=1 
        k +=1 
    if i >= len_l : 
        result.extend(r_list[j:len_r])
    else : 
        result.extend(l_list[i:len_l])
    return result

n = [random.randrange(1,101) for _ in range(12000)]
# print(f"                n : {n}")
st_exsort = time.time()
exchange_sort(n)
print(f"exchange sort time : {time.time()-st_exsort}")
# print(f"exchange sorted n : {n}")

n = [random.randrange(1,101) for _ in range(2000)]
# print(f"                n : {n}")
st_mergesort = time.time()
n = merge_sort(n)
print(f"merge sort tiem : {time.time()-st_mergesort}")
# print(f"   merge sorted n : {n}")




