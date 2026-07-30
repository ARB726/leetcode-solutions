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
### Problem Analysis

#### Problem Type
The problem is related to a singly linked list and involves reordering its nodes.

#### Constraints and Edge Cases
- The length of the linked list is between 1 and 1000 (inclusive).
- The values of the nodes are between 1 and 1000 (inclusive).
- The linked list is non-empty.
- The values in the nodes cannot be modified; only the nodes themselves can be reordered.

#### Inputs and Outputs
- Input: The head of a singly linked list.
- Output: The reordered linked list with the same head, but with its nodes rearranged according to the specified pattern.

#### Data Structures
- A singly linked list, which can be represented using a ListNode class.
- To solve this problem efficiently, we can also use a list (or array) to temporarily store the nodes of the linked list, as well as two pointers (one at the start and one at the end of the list) to facilitate the reordering process.

### Suggested Approach
To reorder the linked list, follow these steps:
1. **Store the nodes in a list**: Traverse the linked list and store its nodes in a list.
2. **Initialize two pointers**: Initialize two pointers, one at the beginning of the list and one at the end.
3. **Reorder the nodes**: Reorder the nodes by iterating through the list and rearranging the nodes according to the specified pattern.
4. **Update the next pointers**: Update the next pointers of the nodes to reflect the new order.

Here is a sample code snippet in Python:

```python
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Base case: if the linked list has less than 2 nodes, return
        if not head or not head.next:
            return
        
        # Store the nodes in a list
        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next
        
        # Reorder the nodes
        for i in range(len(nodes) // 2):
            nodes[i].next = nodes[len(nodes) - 1 - i]
            nodes[len(nodes) - 1 - i].next = nodes[i + 1]
        
        # If the length of the linked list is odd, set the next pointer of the middle node to None
        if len(nodes) % 2 == 1:
            nodes[len(nodes) // 2].next = None
        else:
            nodes[-1].next = None
```

This solution has a time complexity of O(n), where n is the length of the linked list, and a space complexity of O(n), where n is the length of the linked list.

## Code Review
Here's a review of your solution:

### Bugs and Logical Errors
1.  Your solution seems to have an incomplete implementation. The code for finding the middle of the linked list and reversing the second half is present, but the final step of reordering the nodes by alternating between the first and second halves is not entirely correct.
2.  The `slow` and `fast` pointers are not correctly updated to find the middle of the linked list. The `while` loop condition should be `fast.next` and `fast.next.next` to correctly find the middle.
3.  You are incorrectly printing `slow.val` and `fast.val`. The `fast` pointer will reach the end of the linked list, so `fast.val` will throw an error. You should only print `slow.val` to verify that it reaches the middle of the linked list.

### Time Complexity
The time complexity of your solution is O(n), where n is the length of the linked list. This is because you are traversing the linked list to find the middle, reversing the second half, and then reordering the nodes.

### Space Complexity
The space complexity of your solution is O(1), which means the space used does not grow with the size of the input linked list, making it efficient for large inputs.

### Edge Cases
Your solution does not handle edge cases correctly. For example, it does not correctly handle the case when the length of the linked list is 1 or less. You should add a condition to return immediately if the length of the linked list is less than or equal to 1.

### Code Readability and Style
Your code can be improved for better readability and style:

1.  Use more descriptive variable names. For example, `dummy` can be renamed to `dummy_head`, `slow` can be renamed to `middle_pointer`, and `fast` can be renamed to `end_pointer`.
2.  Add comments to explain what each section of the code is doing. This will make it easier for others to understand your solution.
3.  Use consistent indentation and spacing between lines of code.

Here is the corrected version of your code:

```python
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Handle edge cases
        if not head or not head.next:
            return

        # Find the middle of the linked list
        dummy_head = ListNode(0)
        dummy_head.next = head
        middle_pointer = dummy_head
        end_pointer = dummy_head

        while end_pointer.next and end_pointer.next.next:
            middle_pointer = middle_pointer.next
            end_pointer = end_pointer.next.next

        # Reverse the second half of the linked list
        prev = None
        current = middle_pointer.next
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Reorder the nodes
        first_half = dummy_head.next
        second_half = prev
        while second_half:
            first_half_next = first_half.next
            second_half_next = second_half.next
            first_half.next = second_half
            second_half.next = first_half_next
            first_half = first_half_next
            second_half = second_half_next
```

This corrected version should pass all test cases and correctly reorder the nodes in the linked list.

## Optimized Solution
### Optimized Solution

The provided solution can be optimized by finding the middle of the linked list and then reversing the second half of the list. This approach avoids storing all nodes in a list and reduces the space complexity to O(1).

Here's the optimized code:

```python
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Base case: if the linked list has less than 2 nodes, return
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
        
        # Reorder the nodes
        first = head
        second = prev
        while second.next:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        
        # Set the next pointer of the last node to None
        if second:
            second.next = None
```

### Explanation

1.  We start by finding the middle of the linked list using the slow and fast pointer approach.
2.  We then reverse the second half of the linked list.
3.  Next, we reorder the nodes by iterating through the first half and the reversed second half simultaneously, swapping their next pointers.
4.  Finally, we set the next pointer of the last node to None to complete the reordering process.

### Time and Space Complexity

*   **Time Complexity:** O(n), where n is the length of the linked list.
*   **Space Complexity:** O(1), as we only use a constant amount of space to store the slow and fast pointers, and the previous and current nodes during the reversal and reordering process.

### Step-by-Step Walkthrough

1.  Initialize the slow and fast pointers to the head of the linked list.
2.  Move the fast pointer two steps at a time until it reaches the end of the linked list, and move the slow pointer one step at a time.
3.  When the fast pointer reaches the end, the slow pointer will be at the middle of the linked list.
4.  Reverse the second half of the linked list by iterating through it and swapping the next pointers of each node with the previous node.
5.  Initialize two pointers, `first` and `second`, to the head of the linked list and the reversed second half, respectively.
6.  Iterate through the first half and the reversed second half simultaneously, swapping their next pointers to complete the reordering process.

Example Use Cases:

*   Input: `head = [2,4,6,8]`
    *   Output: `[2,8,4,6]`
*   Input: `head = [2,4,6,8,10]`
    *   Output: `[2,10,4,8,6]`

Note: The provided solution has been optimized for time and space complexity while maintaining readability and understandability.

## Lesson & Pattern
Let's break this down together.

### 1. Core Algorithmic Pattern:
The core algorithmic pattern in this problem is a combination of **Two Pointers** and **Reversal** of a Linked List. The two pointers are used to divide the list into two halves, and then the second half is reversed. Finally, the two halves are interleaved to achieve the desired order.

### 2. Why This Pattern Fits This Problem:
This pattern fits this problem because it allows us to efficiently reorder the nodes in the linked list without modifying their values. By dividing the list into two halves and reversing the second half, we can interleave the nodes from the start and end of the list to achieve the desired order.

### 3. Similar LeetCode Problems:
Here are three similar LeetCode problems that use the same pattern:

* **Reverse Linked List** (LeetCode 206): This problem involves reversing a singly linked list, which is a crucial step in the solution to the Reorder Linked List problem.
* **Partition List** (LeetCode 86): This problem involves partitioning a linked list around a given value, which requires a similar approach to dividing the list into two halves.
* **Find the Middle Element of a Linked List** (LeetCode 876): This problem involves finding the middle element of a linked list, which is a necessary step in dividing the list into two halves.

### 4. Simple Mental Framework:
To recognize this pattern in future problems, here's a simple mental framework:

* **Two halves**: Divide the problem into two halves, either literally (like in the case of a linked list) or conceptually (like in the case of an array or a string).
* **Reversal**: Look for opportunities to reverse one or both halves to achieve the desired order or transformation.
* **Interleaving**: Consider how to interleave the elements from the two halves to achieve the desired result.

### 5. Key Takeaway:
One key takeaway from this problem is the importance of **breaking down complex problems into smaller sub-problems**. In this case, breaking down the reordering problem into smaller sub-problems like finding the middle element, reversing the second half, and interleaving the two halves made the solution much more manageable. This approach can be applied to a wide range of problems in computer science and programming.
