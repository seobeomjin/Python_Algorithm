"""
- 7. Reverse Integer
    a signed 32 bit integer가 주어졌을 때, 이를 거꾸로 뒤집은 값을 return하라. 
    만약 reversed value의 범위가 [-2^31, 2^31-1] 을 넘으면 return 0 하라. 

- solved in 25min (official Easy / for me: ★☆☆☆☆))
    36 ms / 14.4 MB
    분명 더 효율적인 방법이 있을텐데.. 

"""

# My solution
class Solution:
    def reverse(self, x: int) -> int:
        
        neg = False
        if x < 0 :
            x_ = str(x)[1:]
            neg = True
        else : 
            x_ = str(x)
        Len = len(str(x_))
        
        reverse_x = 0
        for i, item in enumerate(x_[::-1]):
            reverse_x += int(item)*(pow(10,Len-1-i))
        if neg : 
            reverse_x *=(-1)
        
        if pow(-2,31) <= reverse_x <= pow(2,31)-1 : 
            return reverse_x
        else : 
            return 0

# effective solution via another coder 
class Solution:
    def reverse(self, x: int) -> int:
        numstr=str(abs(x))
        result=numstr[::-1]
        if x<0:
            result="-"+result
        if abs(int(result))< 2**31:
            return int(result)
        else:
            return 0