"""
- 8. String to Integer (atoi)
    문자열로 주어진 숫자데이터를 int형 데이터 타입으로 변환하는 문제. 
    공백, 부호, 숫자외의 문자 등 숫자가 될 수 있는 조건을 충족시켜야 함. 

- solved in 45min (official: Medium / for me: ★★★☆☆)
    Runtime: 28 ms, faster than 94.52% of Python3 online submissions for String to Integer (atoi).
    Memory Usage: 14.3 MB, less than 29.26% of Python3 online submissions for String to Integer (atoi).

    th) 시간 더 단축해야 한다. 
    th) 문제 자체가 어려웠다기 보다는, 예외들을 잡는 데에 더 많은 신경을 썼던 거 같다 
        
- 배운 점 
    str[idx].isalpha() -> returns True if all the characters are alphabet letters (a-z).
    str[idx].isdigit() -> returns True if all the characters are digits, otherwise False.
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        
        dig = ''
        sign = ''
        for i in range(len(s)):
            
            if s[i] == ' ' : 
                continue
            elif s[i] == '-' or s[i]=='+': 
                if i!=0 and ('0' <= s[i-1] <= '9') : 
                    return 0
                if i!= len(s)-1 and ('0' > s[i+1] or s[i+1] > '9')  : 
                    break
                sign = s[i]
                continue
            
            if '0' <= s[i] <= '9' : 
                dig += s[i]
                if i!= len(s)-1 and ('0' > s[i+1] or s[i+1] > '9')  : 
                    break
            else : 
                break
        
        if dig : 
            if sign == '-' : 
                dig = int(dig)*(-1)
                if abs(dig) > 2**31 : 
                    return -1*(2**31)
                else : 
                    return dig
            else :
                dig = int(dig)
                if dig > (2**31)-1 :
                    return 2**31-1
                else : 
                    return dig     
        else:
            return 0
        
# "   -42"
# "-91283472332"
# "00000-42a1234"
# "4193 with words"