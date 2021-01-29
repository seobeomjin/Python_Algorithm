"""
- 6. ZigZag Conversion

- solved in 35min (official: Medium / for me: ★★★☆☆)
    Runtime: 84 ms, faster than 21.83% of Python3 online submissions for ZigZag Conversion.
    Memory Usage: 14.4 MB, less than 47.15% of Python3 online submissions for ZigZag Conversion.

- 배운 점
    다른 코드들을 읽어보니, character가 진행됨에 따라, down/up 등의 방향이 바뀌기 때문에 
    그 방향성을 *(-1) 을 해주어 구현하였다. 그렇게 해주면 확실히 불필요한 연산이 줄어들 거 같기는 하다.

"""

# 내 풀이 
# 각 row마다 순서대로 문자들이 들어가야 하므로 각 row에 들어갈 인덱스를 규칙적으로 
# 찾을 수 있는 방법에 대해 생각해 보았음. 
# row-1 번째 row를 기준으로 다시 찍고 올라가기 때문에 
# 내려가는 부분과 올라가는 부분에 대해 넣어줘야 하는 인덱스의 경우를 찾아 넣어주게 함

# res list 에 넣어주는 과정은 O(n) 인데, 마지막에 이중포문.. 
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 :
            return s
        
        res = [[] for _ in range(numRows)]
        
        for i in range(len(s)): #O(n)
            if i%(numRows+numRows-2) > numRows-1: #O(1)
                idx = i%(numRows+numRows-2) - (numRows-1)
                res[numRows-1-idx].append(s[i]) #O(1)
            else :
                res[i%(numRows+numRows-2)].append(s[i])
        
        result = ""
        for i in range(len(res)): 
            for j in range(len(res[i])):
                result += res[i][j]
        return result


# 내 풀이 (저장 방법만 dict으로)
# 살짝 더 나은 정도 
# Runtime: 80 ms, faster than 24.44% of Python3 online submissions for ZigZag Conversion.

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 :
            return s
    
        d = {}
        for i in range(len(s)):
            if i%(numRows+numRows-2) > numRows-1:
                idx = i%(numRows+numRows-2) - (numRows-1)
                if d.get(numRows-1-idx,None) == None : 
                    d[numRows-1-idx] = s[i]
                else : 
                    d[numRows-1-idx] +=s[i]
            else :
                if d.get(i%(numRows+numRows-2),None) == None : 
                    d[i%(numRows+numRows-2)] = s[i]
                else : 
                    d[i%(numRows+numRows-2)] +=s[i]

        rest = ''.join(d.values()
        return rest



# 다른 사람의 python 풀이 (beats 95%)
# 방향 전환이 관건이었음. 
# 이것 외의 다픈 풀이들도 이 부분이 핵심인 듯.
class Solution:
    def convert(self, s:str, numRows:int): -> str
        lin = 0
        pl = 1
        outp = [""] * numRows
        for i in range(len(s)):
            outp[lin] += s[i]
            if numRows > 1:
                lin += pl # +1이나 -1씩 더해줌 방향에 따라
                if lin == 0 or lin == numRows -1:
                    pl *= -1 # 0번째 이거나, 마지막이면 방향을 바꾸어주어야 함.
        outputStr = ""
        for j in range(numRows):
            outputStr += outp[j]
        return outputStr