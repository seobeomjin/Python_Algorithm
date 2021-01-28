"""
- 5. Longest Palindromic Substring
    substring 중에 가장 긴 palindrom 을 찾아 return 하는 문제  
    https://leetcode.com/problems/longest-palindromic-substring/

- fail to solve (official: Medium / for me: ★★★★★)
    부족했던 부분 : 
        
        1) Brute force 한 접근 방법은 아예 배제를 하고 생각을 했었다. 
        Brute force로 풀면 palindrom check를 위한 linear scan O(n) * 모든 case의 substring O(n^2) = O(n^3) 
        의 연산이 소요 된다. 

        2) (비효율적 방법) 멍청한 방법이지만, 양 끝에서부터 같음을 확인하면서 내려가면 어떨까라고 생각을 했다. 
        하지만 left가 시작이라면, right는 항상 반대편 끝에서 부터 시작을 했어야 했고, 그러면 Brute Force 와 
        다를 게 없었다.

- 배운 점 
    palindrom의 가운데를 시작으로 left,right가 같으면 하나씩 위치를 증가해 나가는 방법을 사용할 수 있었다. 
    이는 palindrom을 확장하는 데에 O(n) * 모든 index 시작점을 기준으로 O(n) = O(n^2) 의 연산이 든다. 
    (th 왜 생각을 못했을까) 
"""
# solution 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        resLen = 0
        
        for i in range(len(s)):
            
            # ood palindrom 
            l, r = i, i 
            while l >= 0 and r <=len(s)-1 and s[l] == s[r]: 
                if (r-l+1) > resLen : 
                    res =  s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1
            
            # even palindrom 
            l, r = i, i+1
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]: 
                if (r-l+1) > resLen : 
                    res =  s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1
        return res
                