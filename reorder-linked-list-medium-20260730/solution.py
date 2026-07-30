# Problem
"""
Reorder Linked List
Medium
Topics
Company Tags
Hints
You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

Example 1:

Input: head = [2,4,6,8]

Output: [2,8,4,6]
Example 2:

Input: head = [2,4,6,8,10]

Output: [2,10,4,8,6]
Constraints:

1 <= Length of the list <= 1000.
1 <= Node.val <= 1000


Topics

Recommended Time & Space Complexity

Hint 1

Hint 2

Hint 3

Company Tags
Seen this question in a real interview?
Yes
No
Acceptance Rate
71.8%

Solution 1
+

NeetBot
|

Hint
|
|
Ln 44, Col 4

Ask NeetBot


131421363738151617181920222324252627352829303132333439407814class Solution:    def reorderList(self, head: Optional[ListNode]) -> None:        while fast and fast.next:
Wrong Answer


Suggest Fix
Passed test cases: 0 / 2


Input:


head=[2,4,6,8]
stdout:


4
8
6
8
Your Output:


[2,4]
Expected output:


[2,8,4,6]

"""

# My Solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        print(slow.val)
        print(fast.val)

        prev = None
        current = slow.next

        while current.next:
            Next = slow.next
            current.next = prev
            prev = current
            current = Next


        firstHalf = dummy.next
        secondHalf = prev

        while secondHalf:

            firstHalfNext = firstHalf.next
            secondHalfNext = secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = firstHalfNext
            firstHalf = firstHalfNext
            secondHalf = secondHalfNext




"""

-> First Take fast pointer to the end of the list
-> Reverse the pointers after fast goes to the end so I mean second half
"""