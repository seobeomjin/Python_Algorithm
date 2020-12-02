'''
#TwoSum #Easy #Array 
nums 배열과 target이 주어지면 target을 맞출 수 있는 두 개의 index를 return하는 문제.

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Runtime: 40 ms, faster than 96.97% of Python3 online submissions for Two Sum.
Memory Usage: 14.4 MB, less than 88.52% of Python3 online submissions for Two Sum.
'''
# O(NlogN) 풀이 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for e1 in range(len(nums)): 
            for e2 in range(e1+1,len(nums)): 
                if nums[e1] + nums[e2] == target: 
                    return [e1, e2]
                else : continue 


# 다른 방법 풀이 (해쉬테이블 이용)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            elem = target - nums[i] 
            if elem not in d : 
                d[nums[i]] = i
            else : return [i, d[elem]]   