# Reverse Linked List — Easy

## Problem
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

## Problem Analysis
### Problem Analysis: Reverse Linked List

**1. Problem Type:** 
- Linked List
- Reversal

**2. Constraints and Edge Cases:**
- Length of the list: 0 <= length <= 1000
- Node values: -1000 <= Node.val <= 1000
- Edge cases:
  - Empty list
  - List with one node
  - List with multiple nodes

**3. Inputs and Outputs:**
- Input: Head of a singly linked list
- Output: Head of the reversed linked list

**4. Recommended Data Structures:**
- Node (to represent the linked list node)
- Linked list (to store and reverse the nodes)

**Additional Notes:**
- This problem requires a simple iterative or recursive solution to reverse the linked list.
- The time complexity should be O(n), where n is the number of nodes in the list.
- The space complexity should be O(1), as we are only using a constant amount of space to store the previous, current, and next nodes during the reversal process.

## Code Review
**Code Review: Reverse Linked List**

### 1. Checking for Bugs or Logical Errors

Your solution looks correct. You're properly reversing the linked list by iterating through each node and updating the `next` pointers. The algorithm is sound, and there are no obvious bugs or logical errors.

### 2. Evaluating Time Complexity (Big O)

The time complexity of your solution is **O(n)**, where n is the number of nodes in the linked list. This is because you're iterating through each node once, performing a constant amount of work for each node.

### 3. Evaluating Space Complexity (Big O)

The space complexity of your solution is **O(1)**, which is correct. You're only using a constant amount of space to store the `prev`, `current`, and `Next` pointers, regardless of the size of the input linked list.

### 4. Checking for Edge Cases that are Not Handled

You're handling the following edge cases:

* Empty list: If `head` is `None`, the function will simply return `None`, which is the correct behavior.
* List with one node: If `head` has only one node, the function will correctly return that node, since there's nothing to reverse.
* List with multiple nodes: Your solution will correctly reverse the linked list with multiple nodes.

However, it's worth noting that you're not checking for `None` values in the `next` pointer of each node. But in this case, it's not necessary because the `while` loop condition already checks if `current` is `None`.

### 5. Commenting on Code Readability and Style

Your code is generally well-structured and easy to read. Here are some minor suggestions for improvement:

* Consider adding a brief comment to explain the purpose of the function and the algorithm used.
* The variable name `Next` could be changed to `next_node` to follow Python's naming conventions (lowercase with underscores).
* The variable name `prev` could be changed to `previous_node` for clarity.
* Consider adding type hints for the `current`, `prev`, and `Next` variables to make the code more explicit.

Here's an updated version of your code with these suggestions:
```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse a singly linked list in-place
        current: ListNode = head
        previous_node: ListNode = None
        
        while current:
            # Store the next node in the list
            next_node: ListNode = current.next
            # Reverse the link
            current.next = previous_node
            # Move to the next node
            previous_node = current
            current = next_node

        return previous_node
```
Overall, your solution is correct, efficient, and easy to understand. With these minor suggestions, it can be even more readable and maintainable.

## Optimized Solution
### Optimized Solution
The original solution provided is already optimal for reversing a singly linked list. It has a time complexity of O(n) and a space complexity of O(1), where n is the number of nodes in the list. The solution uses a simple iterative approach to reverse the list.

Here's the same solution with some additional comments to help understand the process:

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize pointers for the current node and the previous node
        current = head
        prev = None
        
        # Traverse the list until the end is reached
        while current:
            # Store the next node before reversing the link
            next_node = current.next
            
            # Reverse the link
            current.next = prev
            
            # Move the pointers one step forward
            prev = current
            current = next_node

        # At this point, 'prev' points to the new head of the reversed list
        return prev
```

### Explanation
This solution iterates through the linked list, keeping track of the current node and the previous node. It reverses the link of each node by setting `current.next` to `prev`. The process continues until the end of the list is reached.

The time complexity is O(n) because each node is visited once. The space complexity is O(1) because only a constant amount of extra memory is used to store the `current`, `prev`, and `next_node` pointers.

### Time and Space Complexity
- Time Complexity: **O(n)**
- Space Complexity: **O(1)**

### Step-by-Step Walkthrough
1. Initialize `current` to the head of the list and `prev` to `None`.
2. Traverse the list. While `current` is not `None`:
   - Store the next node in `next_node`.
   - Reverse the link of the current node by setting `current.next` to `prev`.
   - Move the pointers one step forward: `prev` becomes `current`, and `current` becomes `next_node`.
3. When the loop ends, `prev` points to the new head of the reversed list.
4. Return `prev` as the new head of the reversed list.

### Why It Is Already Optimal
This solution is already optimal because it only requires a single pass through the list and uses a constant amount of extra memory. Any solution to reverse a linked list must at least visit each node once, resulting in a time complexity of O(n). The space complexity of O(1) is the best possible for this problem because we do not need to store any additional data that scales with the input size.

## Lesson & Pattern
Let's break down the problem and solution.

**1. Core algorithmic pattern:**
The core pattern in this problem is a simple iteration, but more specifically, it's a variation of the **Two Pointers** technique. In this case, we're using three pointers: `prev`, `current`, and `Next`. However, this problem is more closely related to the **Iterative Traversal** pattern, as we're traversing the linked list and modifying it in-place.

**2. Why this pattern fits:**
This pattern fits this problem because we need to traverse the linked list and reverse the direction of the pointers. By using the `prev`, `current`, and `Next` pointers, we can efficiently reverse the list by updating the `next` pointer of each node. This approach allows us to avoid using extra space (like an array or stack) to store the nodes, making it a space-efficient solution.

**3. Similar LeetCode problems:**
Here are three similar problems that use the same pattern:

* **Remove Duplicates from Sorted List**: This problem requires you to remove duplicates from a sorted linked list. You can use a similar two-pointer approach to iterate through the list and remove duplicates.
* **Merge Two Sorted Lists**: This problem involves merging two sorted linked lists into one sorted list. You can use a two-pointer technique to compare nodes from both lists and add them to the merged list.
* **Delete Node in a Linked List**: In this problem, you need to delete a node from a linked list given only access to that node. You can use a similar approach to update the `next` pointer of the previous node to skip the node to be deleted.

**4. Mental framework:**
To recognize this pattern in future problems, ask yourself:
* Am I dealing with a linked list or a sequence of nodes?
* Do I need to traverse the list and modify it in-place?
* Can I use a few pointers to keep track of nodes and update the structure?
If you answer "yes" to these questions, you might be able to apply an iterative traversal or two-pointer technique to solve the problem.

**5. Key takeaway:**
The key takeaway from this problem is that when dealing with linked lists, it's often efficient to use iterative traversal and update the structure in-place, rather than using extra space to store nodes. This approach can help you solve problems like reversing a linked list, removing duplicates, or merging lists in a space-efficient manner.

Now, go ahead and practice some similar problems to reinforce your understanding of this pattern!
