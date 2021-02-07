"""
- 9. Palindrome Number

- solved in 2min (official: Easy / to me: ★☆☆☆☆)
    Runtime: 64 ms, faster than 60.69% of Python3 online submissions for Palindrome Number.
    Memory Usage: 14.3 MB, less than 52.66% of Python3 online submissions for Palindrome Number.
"""
# My solution 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i in range(int(len(x)/2)):
            if x[i] == x[-(i+1)]: 
                continue 
            else :
                return False 
        return True


# another solution 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x > 0:
            a = int(str(x)[::-1]) # inverse order of positive one 
        if x <= 0:
            a = int(str(x*-1)[::-1]) # inverse order of negative one
        if a == x:
            return True  # if same, true 
        else:
            return False # o/w false 