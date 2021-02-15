"""
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 
주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

prices	return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]

- 깨달은 점 
    : next second에 가격이 하락할 때에도 1초가 걸리므로 1초를 고려해줘야하고, 그 뒤에 break 해 줘야 함. 해당 index에 대해거 
    : 근데 아래 풀이는 O(n^2)임. O(n) 풀이 고민하자. stack으로 풀면.  
"""

# solution
def solution(prices):
    res = [0]*len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                res[i] += 1 
            else : 
                res[i] +=1 
                break 
    return res