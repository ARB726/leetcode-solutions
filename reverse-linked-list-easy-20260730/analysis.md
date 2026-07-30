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






























## Problem Analysis
**Problem Analysis**

* **Problem Type**: Linked List
* **Constraints and Edge Cases**:
	+ List length: 0 <= length <= 1000
	+ Node values: -1000 <= Node.val <= 1000
	+ Empty list (head = []) is a valid input
* **Inputs and Outputs**:
	+ Input: head of a singly linked list
	+ Output: head of the reversed linked list
* **Recommended Data Structures**: Singly Linked List Node, Pointer variables to keep track of current, previous, and next nodes.

This problem can be solved using a iterative or recursive approach. The key is to keep track of the current node and its previous node, and update the next pointer of the current node to point to the previous node.

## Code Review
**Code Review**

### Bugs or Logical Errors

The provided solution appears to be correct and does not contain any logical errors. The iteration through the linked list and the reversal of the links between the nodes are properly implemented.

### Time Complexity (Big O)

The time complexity of the solution is **O(n)**, where n is the number of nodes in the linked list. This is because the solution iterates through the linked list once, reversing the links between the nodes.

### Space Complexity (Big O)

The space complexity of the solution is **O(1)**, which means the space required does not change with the size of the input linked list. This is because the solution only uses a constant amount of space to store the `current`, `prev`, and `Next` variables.

### Edge Cases

The solution correctly handles the following edge cases:

*   Empty linked list (head = []): The solution returns `None`, which is the correct result for an empty linked list.
*   Linked list with one node: The solution returns the same node, which is the correct result since a linked list with one node is already reversed.

However, it's worth noting that the solution does not explicitly handle the case where the input `head` is `None`. Although it still works correctly in this case (returning `None`), a comment or a check to explicitly handle this case could improve readability and maintainability.

### Code Readability and Style

The code is generally well-organized and easy to follow. The variable names `current`, `prev`, and `Next` clearly indicate their purpose in the algorithm.

However, there are a few improvements that can be made:

*   The variable name `Next` should be `next` (lowercase) to follow the conventional naming style in Python.
*   A comment or docstring explaining the purpose of the function and the algorithm used would be helpful for readability and maintainability.
*   The type hint `Optional[ListNode]` is correctly used to indicate that the function can return `None`.

Here's the updated code with these improvements:

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly linked list and returns the new head of the reversed list.
        
        :param head: The head of the linked list to be reversed.
        :return: The head of the reversed linked list.
        """
        
        # Initialize current node and previous node
        current = head
        prev = None
        
        # Iterate through the linked list and reverse the links
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # Return the new head of the reversed list
        return prev
```

Overall, the solution is correct, efficient, and well-organized. With a few minor improvements, it can be even more readable and maintainable.

## Optimized Solution
**Optimized Solution:**
The given original solution is already optimal for reversing a linked list. It uses an iterative approach, which is more efficient than a recursive approach for this problem, as it avoids the overhead of recursive function calls. The time complexity is O(n), where n is the number of nodes in the linked list, and the space complexity is O(1), as it only uses a constant amount of space to store the current, previous, and next nodes.

```python
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
            next_node = current.next  # Use a more descriptive variable name
            current.next = prev
            prev = current
            current = next_node

        return prev
```

**Explanation:**

1.  The `reverseList` function takes the head of a singly linked list as input and returns the head of the reversed linked list.
2.  It initializes three variables: `current`, `prev`, and `next_node`. The `current` variable is initialized to the head of the linked list, and the `prev` variable is initialized to `None`.
3.  The function then enters a while loop that continues as long as the `current` node is not `None`.
4.  Inside the loop, it first stores the next node of the `current` node in the `next_node` variable. This is necessary because the `current.next` pointer will be updated in the next step, and we need to keep track of the next node.
5.  Then, it updates the `next` pointer of the `current` node to point to the `prev` node. This effectively reverses the link between the `current` and `next` nodes.
6.  After that, it updates the `prev` variable to point to the `current` node and the `current` variable to point to the `next_node`. This moves the `current` and `prev` pointers one step forward in the list.
7.  Once the while loop completes, the `prev` variable will be pointing to the new head of the reversed linked list, which is then returned by the function.

**Time and Space Complexity:**

*   Time complexity: O(n), where n is the number of nodes in the linked list, because the function visits each node exactly once.
*   Space complexity: O(1), because the function uses a constant amount of space to store the `current`, `prev`, and `next_node` variables, regardless of the size of the input linked list.

**Step-by-Step Walkthrough:**

*   For example, if the input linked list is `[0, 1, 2, 3]`, the `reverseList` function will perform the following steps:
    *   Initially, `current` = `[0, 1, 2, 3]`, `prev` = `None`, and `next_node` is not defined.
    *   In the first iteration of the while loop:
        *   `next_node` = `[1, 2, 3]` (the next node of the current node)
        *   `current.next` = `None` (reversing the link between the current and next nodes)
        *   `prev` = `[0]` (moving the previous pointer one step forward)
        *   `current` = `[1, 2, 3]` (moving the current pointer one step forward)
    *   In the second iteration of the while loop:
        *   `next_node` = `[2, 3]`
        *   `current.next` = `[0]` (reversing the link)
        *   `prev` = `[1, 0]`
        *   `current` = `[2, 3]`
    *   In the third iteration of the while loop:
        *   `next_node` = `[3]`
        *   `current.next` = `[1, 0]` (reversing the link)
        *   `prev` = `[2, 1, 0]`
        *   `current` = `[3]`
    *   In the fourth iteration of the while loop:
        *   `next_node` = `None`
        *   `current.next` = `[2, 1, 0]` (reversing the link)
        *   `prev` = `[3, 2, 1, 0]`
        *   `current` = `None` (exiting the loop)
    *   Finally, the function returns the new head of the reversed linked list, which is `[3, 2, 1, 0]`.

## Lesson & Pattern
Let's break it down.

**The Core Algorithmic Pattern:**
The pattern used in this problem is **Two Pointers** or **Iterative Traversal**. Specifically, it's a variation of the two pointers technique where we use three pointers: `current`, `prev`, and `Next` (which is `current.next`).

**Why does this pattern fit this problem?**
This pattern fits this problem because we need to traverse the linked list and update the `next` pointers of each node. By using three pointers, we can keep track of the current node, its previous node, and the next node, which allows us to efficiently reverse the list.

**Similar LeetCode Problems that use the same pattern:**

1. **Middle of the Linked List** (LeetCode 876): This problem requires finding the middle node of a linked list. We can use two pointers, one moving twice as fast as the other, to find the middle node.
2. **Remove Duplicates from Sorted List** (LeetCode 83): In this problem, we need to remove duplicates from a sorted linked list. We can use two pointers to keep track of the current node and the next node, and update the `next` pointer accordingly.
3. **Delete Node in a Linked List** (LeetCode 237): This problem requires deleting a node from a linked list. We can use two pointers to keep track of the node to be deleted and its previous node, and update the `next` pointer accordingly.

**Mental Framework to recognize this pattern:**
To recognize the two pointers pattern, ask yourself:

* Do I need to traverse a data structure (e.g., linked list, array)?
* Do I need to keep track of multiple nodes or elements?
* Do I need to update pointers or references between nodes or elements?

If you answered "yes" to these questions, the two pointers pattern might be a good fit.

**One Key Takeaway:**
Remember that the two pointers pattern is all about using multiple pointers to keep track of different nodes or elements, and updating the relationships between them. Practice using this pattern to solve linked list problems, and you'll become more comfortable with it over time.
