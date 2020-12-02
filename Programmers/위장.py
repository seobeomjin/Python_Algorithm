'''
#위장 #Hash #
스파이가 위장을 하며 매일 다른 옷을 입어야 하는 경우의 수 문제 
'''
import collections
def solution(clothes):
    items = []
    for cloth in clothes : 
        items.append(cloth[1])
    counter = collections.Counter(items) # list에 있는 요소들이 각각 몇개씩 있는지를 딕형태로 돌려줌
    if len(counter.keys())!= 1 : 
        whole = 1
        for i in counter.values() : 
            whole *= (i+1)
    else : 
        sum_ = len(items)
        return sum_
    return whole-1