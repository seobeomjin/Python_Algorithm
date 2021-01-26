"""
- 1695. Maximum Erasure Value 
    서브어레이를 유니크하게 만들면서 그 summation이 가장 큰 값을 retrun하는 문제. 

- solved in 37min? (official: Medium / for me: ★★☆☆☆)
    Runtime: 1284 ms, faster than 73.00% of Python3 online submissions for Maximum Erasure Value.
    Memory Usage: 27.6 MB, less than 83.23% of Python3 online submissions for Maximum Erasure Value.

    th) 시간 더 단축해야 한다. 
    th) 자료구조 + 알고리즘 응용 문제들이 나오는 듯. 
        그 개념들을 명확히 알아야 응용할 수 있을 듯. 
        
- 배운 점 
    <presum + sliding window>
    sliding window를 활용해야 겠다는 것  (left position, right position) 은 알고 있었으나, 
    sliging window만 사용하니, time error가 떴다. 그래서 pre-summation 을 함께 사용함. 
    매 번 summation을 적용하는 것이 아니라 변화가 있을 때마다 더하고 빼주면서 전자보다 연산을 줄일 수 있다. 

"""

class Solution:
    """
    an array of positive integers nums 
    erase a subarray containing unique elements
    equal to the sum of its elements

    그러니까, 배열 안에서, 겹치지 않는 연속되는 값들의 최고 합을 구하라는 말 
    """
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        win = set()
        pre_res, res, l = 0, 0, 0
        
        for r in range(len(nums)): 
            while nums[r] in win : 
                pre_res -= nums[l]
                win.remove(nums[l])
                l += 1
            win.add(nums[r])
            pre_res += nums[r]
            res = max(res, pre_res)

        return res