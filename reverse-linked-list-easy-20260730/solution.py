# Problem
"""
Reverse Linked List
Easy
Topics
Company Tags
Hints
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:

Input: head = [0,1,2,3]

Output: [3,2,1,0]
Example 2:

Input: head = []

Output: []
Constraints:

0 <= The length of the list <= 1000.
-1000 <= Node.val <= 1000


Topics

Recommended Time & Space Complexity

Hint 1

Hint 2

Hint 3

Hint 4

Company Tags
Seen this question in a real interview?
Yes
No
Acceptance Rate
82.0%

Solution 1
+

NeetBot
|

Hint
|
|
Ln 1, Col 1

12345678910111213141516171819





























"""

# My Solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        
        while current:

            Next = current.next
            current.next = prev
            prev = current
            current = Next

        return prev