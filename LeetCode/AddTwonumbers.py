"""
- 2. Add Two Numbers  <Linked List>
    non empty linked list에 각 값이 거꾸로 저장되어 있고 두 개의 Linked List의 
    거꾸로 저장된 값들을 더해 다시 거꾸로 저장하는 문제.  
    https://leetcode.com/problems/add-two-numbers/

- fail to solve (난이도 : ★★★☆☆)
    부족했던 부분 : 
        1) python에서 linked list 처음 다루어 본 점. 
        2) call by object-refernce에 대한 개념이 불명확했음. 

- 배운 점 
    1) function annotation
    2) while any([])
    3) _ , __ = divmod( , )
    4) Linked List implementation in python 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    # : expression >>> function annotation으로, 변수의 타입을 명시
    # -> expression >>> function annotation으로, 함수의 리턴타입을 명시 
    # 파이썬 언어의 유연성을 보존하면서, 좀 더 명식적으로 만들어주기 위함.
     
        result  = ListNode(0)
        result_tail = result
        carry = 0 

        while any([l1, l2, carry]):
            val1 = (l1.val if l1 else None)
            val2 = (l2.val if l2 else None)
            carry, out = divmod(val1+val2+carry, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next

        # 풀며 들었던 의문
        # 파이썬은 모든 객체 타입 앞에 auto가 생략되어 있다고 생각하자. 
        # 파이썬에서의 = 는 값의 복사일까, 주소의 복사일까?
        # 파이썬에서는 포인터 개념이 없는데, 어떻게 linked 를 표현하지? 
        # >>> 그러니 call by object-reference 개념을 정확히 이해하고 있어야 하는 거구나
        
        