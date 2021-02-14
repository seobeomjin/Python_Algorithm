"""
- 11. Container With Most Water
    각 height가 주어진 array에서 두 개의 height 를 뽑아 물을 담을 수 있는 가장 큰 container의 크기를 return하는 문제 
    https://leetcode.com/problems/container-with-most-water/

- fail to solve (official: Medium / for me: ★★★☆☆)

    1) Brute Force한 방법으로는 풀었으나, 이는 time compexity를 만족하지 못한 solution이었다. 

    2) width가 크고, height가 높아야 한다는 관점에서 linear time에 해결할 수 있었다. 
        아래 Optimal solution 참고
        
- 깨달은 점 
    연습을 더 많이 해야겠다. 왜 width 관점에서 줄여야 한다고 보이지 않았을까. 
    #Array #Two Pointers
    
"""

# Optimal solution 
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l,r = 0, len(height)-1  

        
        while l <= r : # width가 가장 긴 조건에서 시작 
            ar = (r-l) * min(height[l], height[r])
            res = max(ar, res)   
            
            if height[l] > height[r] : # height가 더 작은 부분을 하나씩 변경해 나간다. 
                r -= 1 
            else : 
                l += 1 
                
        return res


# My solution - Brute Force , O(n^2)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # n * logn 을 계산하는 것보다 더 효율적인 방법이 있을텐데. 
        # 처음부터 계산을 하는데, 다음 바의 높이차이가 더 많이 나야 계산할 가치가 있지 
        
        max_area = 0
    
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                ar = (j-i)*min(height[i], height[j])
                max_area = max(ar, max_area)
                
        return max_area
                    
                    
                                
                
                
                 
                
                
            
        