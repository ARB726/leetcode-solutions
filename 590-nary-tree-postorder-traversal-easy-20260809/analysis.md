# 590 Nary Tree Postorder Traversal — Easy

## Problem
590. N-ary Tree Postorder Traversal
Solved
Easy
Topics
premium lock icon
Companies
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

 

Example 1:


Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]
Example 2:


Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The height of the n-ary tree is less than or equal to 1000.
 

Follow up: Recursive solution is trivial, could you do it iteratively?

 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
440,304/542.4K
Acceptance Rate
81.2%
Topics
icon
Companies
Similar Questions
Discussion (89)


Choose a type
















Copyright © 2026 LeetCode. All rights reserved.



## Problem Analysis
### Problem Analysis

1. **Problem Type**: Tree (N-ary Tree) Traversal
2. **Constraints and Edge Cases**:
   * The number of nodes in the tree is in the range [0, 10^4].
   * Each node's value is in the range [0, 10^4].
   * The height of the n-ary tree is less than or equal to 1000.
   * The tree may be empty (root is None).
3. **Inputs and Outputs**:
   * Input: The root of the n-ary tree.
   * Output: A list of node values in postorder traversal order.
4. **Recommended Data Structures**:
   * A Node class to represent each node in the n-ary tree.
   * A list or array to store the node values in postorder traversal order.
   * A stack can be used for iterative solution.

Example of a Node class in Python:
```python
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
```
This problem can be solved using either recursive or iterative approaches. The recursive approach is more straightforward, but the iterative approach using a stack can also be implemented.

## Code Review
**Code Review**

### Bug Checking and Logical Errors
The provided recursive solution appears to be correct and does not contain any obvious bugs. It correctly performs a postorder traversal of the n-ary tree by recursively visiting each child node before appending the current node's value to the result list.

### Time Complexity (Big O)
The time complexity of the solution is **O(N)**, where N is the number of nodes in the tree. This is because each node is visited exactly once by the helper function.

### Space Complexity (Big O)
The space complexity of the solution is **O(N)** as well. This is due to the space required for the recursive call stack in the worst case (when the tree is highly unbalanced) and the space required to store the result.

### Edge Cases
The solution correctly handles the following edge cases:

* An empty tree (root is None): The helper function will not be called, and an empty list will be returned.
* A tree with a single node: The node's value will be appended to the result list.

However, it's worth noting that the solution does not explicitly check for a None root node in the main function. While this is not strictly necessary (since the helper function handles this case), it might be considered better practice to include a simple check at the beginning of the main function to make the code more readable and explicit.

### Code Readability and Style
The code is generally well-structured and easy to follow. However, a few suggestions for improvement can be made:

* The `helperFunction` could be given a more descriptive name, such as `postorder_helper`.
* The `self.Result` instance variable could be replaced with a local variable in the main `postorder` method, which would then be returned directly. This would make the code slightly more concise and easier to understand.

Here is the revised version of the code:
```python
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []

        def postorder_helper(node):
            if not node:
                return

            for child in node.children:
                postorder_helper(child)
            result.append(node.val)

        postorder_helper(root)
        return result
```
Alternatively, an iterative solution using a stack could also be implemented:
```python
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        result = []
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    result.append(node.val)
                else:
                    stack.append((node, True))
                    stack.extend((child, False) for child in reversed(node.children))

        return result
```
This iterative solution has the same time and space complexity as the recursive solution but avoids the use of recursive function calls.

## Optimized Solution
### Optimized Solution

The original solution is already quite efficient with a recursive approach. However, we can optimize it further by avoiding the use of a helper function and a class variable to store the result. Here's an optimized recursive solution:

```python
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def traverse(node):
            if node is None:
                return []
            result = []
            for child in node.children:
                result += traverse(child)
            result += [node.val]
            return result

        return traverse(root)
```

For an iterative solution using a stack, we can use the following approach:

```python
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)
            stack.extend(reversed(node.children))

        return result[::-1]
```

### Explanation

The recursive solution works by traversing each child node and appending their values to the result list before appending the current node's value. This ensures that the values are added in postorder traversal order.

The iterative solution uses a stack to store the nodes to be visited. It pops a node from the stack, adds its value to the result list, and then pushes its children onto the stack in reverse order. This ensures that the children are visited before the parent node. Finally, it returns the result list in reverse order to get the correct postorder traversal order.

### Time and Space Complexity

* Recursive Solution:
	+ Time Complexity: O(N), where N is the number of nodes in the tree, since we visit each node once.
	+ Space Complexity: O(N), since we use a recursive call stack of maximum depth N.
* Iterative Solution:
	+ Time Complexity: O(N), where N is the number of nodes in the tree, since we visit each node once.
	+ Space Complexity: O(N), since we use a stack of maximum size N.

### Walkthrough

1. Start with the root node.
2. For each child node, recursively traverse its children and add their values to the result list.
3. Add the current node's value to the result list.
4. Return the result list.

For the iterative solution:

1. Push the root node onto the stack.
2. While the stack is not empty:
	* Pop a node from the stack and add its value to the result list.
	* Push its children onto the stack in reverse order.
3. Return the result list in reverse order.

### Example Usage

```python
# Create a sample n-ary tree
root = Node(1, [
    Node(3, [
        Node(5),
        Node(6),
    ]),
    Node(2),
    Node(4),
])

# Create a solution instance
solution = Solution()

# Perform postorder traversal
result = solution.postorder(root)
print(result)  # Output: [5, 6, 3, 2, 4, 1]
```

## Lesson & Pattern
Let's break down this problem and identify the key takeaways.

### Core Algorithmic Pattern
The core algorithmic pattern in this problem is **Depth-First Search (DFS)**, specifically **Postorder Traversal**. 

### Why This Pattern Fits This Problem
This pattern fits this problem because postorder traversal visits the children of a node before the node itself, which matches the definition of postorder traversal in an n-ary tree. The DFS approach allows us to recursively traverse the tree, visiting each node's children before the node itself, and then backtracking to visit the node.

### Similar LeetCode Problems
Here are three similar LeetCode problems that use the same pattern:

1. **589. N-ary Tree Preorder Traversal**: This problem requires you to perform a preorder traversal of an n-ary tree, visiting the node before its children.
2. **257. Binary Tree Path Sum II**: This problem requires you to find all paths in a binary tree that sum up to a given target value. While it's not a direct traversal problem, it uses a similar DFS approach.
3. **404. Sum of Left Leaves**: This problem requires you to find the sum of all left leaves in a binary tree. It also uses a DFS approach to traverse the tree.

### Mental Framework to Recognize This Pattern
To recognize this pattern in future problems, ask yourself these questions:

* Is the problem related to tree or graph traversal?
* Does the problem require visiting nodes in a specific order (e.g., preorder, inorder, postorder)?
* Can the problem be solved using a recursive or iterative approach?

If you answer "yes" to these questions, it's likely that the problem involves a DFS pattern.

### Key Takeaway
The key takeaway from this problem is that **DFS is a versatile technique for solving tree and graph traversal problems**. By recognizing the pattern and applying the correct traversal order, you can solve a wide range of problems efficiently.

Here's an example of how you can implement an iterative solution using a stack:
```python
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        result = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            stack.extend(node.children[::-1])
        
        return result[::-1]
```
Note that this iterative solution uses a stack to store nodes and their children, and then reverses the result to obtain the postorder traversal order.
