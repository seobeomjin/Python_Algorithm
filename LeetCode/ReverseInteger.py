"""
- 7. Reverse Integer
    a signed 32 bit integer가 주어졌을 때, 이를 거꾸로 뒤집은 값을 return하라. 
    만약 reversed value의 범위가 [-2^31, 2^31-1] 을 넘으면 return 0 하라. 

- solved in 25min (official Easy / for me: ★☆☆☆☆))
    28 ms / 14.2 MB
    faster than 89.27% of Python3 online submissions

- 깨달은 점 
    > str 을 list로 wapping하면 index별로 쪼개서 들어감 
    > list의 거꾸로 꺼내는 것은 list[::-1] 임. 
    > abs를 활용하면 연산에서 더 빠름 

"""
# My developed solution 
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0 : 
            rev_x = str(x)[1:][::-1]
        else : 
            rev_x = str(x)[::-1]
            
        if x < 0 :
            rev_x = int("-"+rev_x)
            if (-2)**31 <= rev_x <= 2**31-1 : return rev_x
            else : return 0
            
        else : 
            rev_x = int(rev_x)
            if (-2)**31 <= rev_x <= 2**31-1 : return rev_x
            else : return 0



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



# effective solution by another coder 
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