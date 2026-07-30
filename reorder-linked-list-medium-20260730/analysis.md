# Reorder Linked List — Medium

## Problem
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


## Problem Analysis
**Problem Analysis**

1. **Problem Type**: Linked List
2. **Constraints and Edge Cases**:
	* Length of the list: 1 <= n <= 1000
	* Node values: 1 <= Node.val <= 1000
	* Reorder the nodes in the list without modifying their values
3. **Inputs and Outputs**:
	* Input: Head of a singly linked list
	* Output: Reordered linked list (in-place modification)
4. **Recommended Data Structures**:
	* LinkedList nodes
	* Stacks or arrays to store the middle and second half of the list

**Solution Approach**

To solve this problem, you can:

1. Find the middle of the linked list.
2. Reverse the second half of the list.
3. Merge the first half and the reversed second half in an alternating manner.

**Example Use Case**

Input: `head = [2,4,6,8]`
Output: `[2,8,4,6]`

Note: The input and output are represented as linked lists, where each node contains a value (`Node.val`) and a pointer to the next node (`Node.next`).

## Code Review
**Code Review**

The provided solution attempts to solve the "Reorder Linked List" problem. Here's a review of the code:

### Bugs or Logical Errors:

1. The current implementation does not correctly reorder the linked list. The `while` loop that reverses the second half of the list only updates the `slow` pointer, but it does not correctly connect the reversed nodes to the first half of the list.
2. The second `while` loop that attempts to merge the first half and the reversed second half has an incorrect assignment: `dummy.next.next = slow`. This line does not correctly connect the nodes in an alternating manner.
3. The `fast` pointer is not used correctly. After finding the middle of the list, the `fast` pointer should be used to reverse the second half of the list, but this is not done in the current implementation.

### Time Complexity (Big O):

The time complexity of the current implementation is O(n), where n is the length of the linked list. This is because the code iterates through the list twice: once to find the middle and reverse the second half, and once to attempt to merge the first half and the reversed second half.

### Space Complexity (Big O):

The space complexity of the current implementation is O(1), as it only uses a constant amount of space to store the `dummy`, `slow`, and `fast` pointers.

### Edge Cases:

The current implementation does not handle edge cases, such as:

* An empty linked list (i.e., `head` is `None`)
* A linked list with only one node
* A linked list with an even number of nodes

### Code Readability and Style:

The code is not well-organized, and the variable names are not descriptive. For example, `slow` and `fast` are not clear indicators of the purpose of these pointers. Additionally, the code uses `print` statements, which are not necessary and can be removed.

### Suggestions for Improvement:

1. Use more descriptive variable names to improve code readability.
2. Correctly implement the reversal of the second half of the list using the `fast` pointer.
3. Implement a correct merge of the first half and the reversed second half in an alternating manner.
4. Handle edge cases, such as an empty linked list or a linked list with only one node.

Here is a corrected implementation:
```python
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Find the middle of the linked list
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        prev = None
        current = slow.next
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        slow.next = None  # Break the list into two halves

        # Merge the first half and the reversed second half
        first = head
        second = prev
        while second:
            next_first = first.next
            next_second = second.next
            first.next = second
            second.next = next_first
            first = next_first
            second = next_second
```
This implementation correctly reorders the linked list in an alternating manner and handles edge cases.

## Optimized Solution
## Optimized Solution

The provided solution has some issues with implementing the reordering logic. A correct approach would be to:

1.  Find the middle of the linked list using the slow and fast pointer technique.
2.  Reverse the second half of the linked list.
3.  Merge the first half and the reversed second half in an alternating manner.

Here is the optimized solution in Python:

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Find the middle of the linked list
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        prev = None
        current = slow.next
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        slow.next = None

        # Merge the first half and the reversed second half
        first = head
        second = prev
        while second:
            next_first = first.next
            next_second = second.next
            first.next = second
            second.next = next_first
            first = next_first
            second = next_second

# Example usage
# Create a sample linked list: 2 -> 4 -> 6 -> 8
head = ListNode(2, ListNode(4, ListNode(6, ListNode(8))))

# Reorder the linked list
solution = Solution()
solution.reorderList(head)

# Print the reordered linked list
while head:
    print(head.val)
    head = head.next
```

## Explanation

1.  **Time Complexity:** O(n), where n is the number of nodes in the linked list. This is because we traverse the list three times: once to find the middle, once to reverse the second half, and once to merge the two halves.
2.  **Space Complexity:** O(1), which means the space required does not change with the size of the input linked list. This is because we only use a constant amount of space to store the slow and fast pointers.
3.  **Step-by-Step Walkthrough:**

    *   We first check if the linked list has less than two nodes. If so, we return immediately because there's nothing to reorder.
    *   We then find the middle of the linked list using the slow and fast pointer technique. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. When the fast pointer reaches the end of the list, the slow pointer will be at the middle.
    *   Next, we reverse the second half of the linked list. We do this by keeping track of the previous node and the current node. We update the next pointer of the current node to point to the previous node, effectively reversing the link.
    *   Finally, we merge the first half and the reversed second half. We do this by iterating through both halves and updating the next pointers to alternate between nodes from the two halves.

The optimized solution ensures that we correctly reorder the linked list in-place without using any additional data structures that scale with the input size.

## Lesson & Pattern
Now, let's break down the solution to the "Reorder Linked List" problem.

**1. Identify the core algorithmic pattern:**
The core algorithmic pattern in this problem is a combination of **Two Pointers** (specifically, the slow and fast pointer technique) and **List Reversal**.

**2. Explain why this pattern fits this problem:**
The two-pointer technique is used to find the middle of the linked list, which is essential to divide the list into two halves. The fast pointer moves twice as fast as the slow pointer, allowing us to find the middle of the list efficiently. Once we've found the middle, we reverse the second half of the list using a simple iterative approach. Finally, we merge the two halves in an alternating manner to achieve the desired reordered list.

**3. List 3 similar LeetCode problems that use the same pattern:**
Here are three similar problems that use the two-pointer technique and/or list reversal:

* **Remove Duplicates from Sorted List** (LeetCode 83): This problem involves removing duplicates from a sorted linked list, which can be achieved using a two-pointer technique.
* **Partition List** (LeetCode 86): This problem requires partitioning a linked list around a given value, which can be done using a two-pointer technique and list reversal.
* **Reverse Linked List** (LeetCode 206): This problem is a straightforward example of list reversal, which is a fundamental technique used in many linked list problems, including the "Reorder Linked List" problem.

**4. Give a simple mental framework to recognize this pattern:**
To recognize the two-pointer technique and list reversal pattern in future problems, ask yourself:

* Does the problem involve a linked list or an array?
* Is there a need to find the middle or a specific point in the list/array?
* Does the problem require reversing a part of the list/array?
* Can the problem be solved by dividing the list/array into two or more parts and processing them separately?

If you answer "yes" to any of these questions, you might be dealing with a problem that involves the two-pointer technique and/or list reversal.

**5. One key takeaway:**
One key takeaway from this problem is the importance of understanding the **two-pointer technique** and how to apply it to find the middle of a linked list or array. This technique is widely used in many algorithms, including sorting, searching, and linked list problems. Mastering the two-pointer technique will help you solve a wide range of problems more efficiently and effectively.

In the context of the provided solution, the code is attempting to find the middle of the linked list using the slow and fast pointer technique. However, the code has a few issues, such as incorrect pointer updates and a missing merge step. To fix these issues, you can modify the code as follows:
```python
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle of the linked list
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        prev = None
        current = slow.next
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        slow.next = None  # Set the next pointer of the middle node to None

        # Merge the two halves in an alternating manner
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
```
This modified code correctly finds the middle of the linked list, reverses the second half, and merges the two halves in an alternating manner to achieve the desired reordered list.
