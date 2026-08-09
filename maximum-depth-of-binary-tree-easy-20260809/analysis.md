# Maximum Depth Of Binary Tree — Easy

## Problem
Maximum Depth of Binary Tree
Easy
Topics
Company Tags
Hints
Given the root of a binary tree, return its depth.

The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:



Input: root = [1,2,3,null,null,4]

Output: 3
Example 2:

Input: root = []

Output: 0
Constraints:

0 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100


Topics

Recommended Time & Space Complexity

Hint 1

Hint 2

Hint 3

Company Tags
Seen this question in a real interview?
Yes
No


## Problem Analysis
### Problem Analysis

* **Problem Type:** Tree (Binary Tree)
* **Constraints and Edge Cases:**
	+ The number of nodes in the tree is between 0 and 100 (inclusive).
	+ Node values are between -100 and 100 (inclusive).
	+ The tree can be empty (i.e., `root` is `None`).
	+ The tree can be unbalanced.
* **Inputs and Outputs:**
	+ Input: The root of a binary tree.
	+ Output: The maximum depth of the binary tree.
* **Recommended Data Structures:**
	+ A binary tree node class to represent each node in the tree.
	+ A recursive or iterative approach using a stack or queue to traverse the tree.

### Example Code (Recursive Approach)
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:
    """
    Returns the maximum depth of a binary tree.
    
    Args:
    root: The root of the binary tree.
    
    Returns:
    An integer representing the maximum depth of the tree.
    """
    if root is None:
        return 0
    else:
        left_depth = maxDepth(root.left)
        right_depth = maxDepth(root.right)
        return max(left_depth, right_depth) + 1
```
### Example Code (Iterative Approach)
```python
from collections import deque

def maxDepth(root: TreeNode) -> int:
    if root is None:
        return 0
    
    queue = deque([(root, 1)])
    max_depth = 0
    
    while queue:
        node, depth = queue.popleft()
        max_depth = max(max_depth, depth)
        
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    
    return max_depth
```

## Code Review
### Code Review

#### Bugs or Logical Errors
The provided code seems to be logically correct. However, there is a minor issue with variable naming convention. In Python, it's conventional to use lowercase letters for variable names. Therefore, `Right` should be `right`.

#### Time Complexity (Big O)
The time complexity of the provided solution is O(n), where n is the number of nodes in the binary tree. This is because each node is visited exactly once during the recursive traversal.

#### Space Complexity (Big O)
The space complexity of the provided solution is O(h), where h is the height of the binary tree. This is because the maximum depth of the recursive call stack is determined by the height of the tree. In the worst-case scenario (i.e., an unbalanced tree), the space complexity becomes O(n).

#### Edge Cases
The provided code handles the following edge cases correctly:

* An empty tree (`root` is `None`): returns 0
* A tree with a single node: returns 1
* An unbalanced tree: returns the correct maximum depth

However, it's worth noting that the provided code does not explicitly handle the case where the tree is `None`. While the code will still work correctly in this case (thanks to the `if not root` condition), it's a good practice to include a docstring or a comment to explicitly mention this edge case.

#### Code Readability and Style
The provided code follows the conventional Python naming conventions and style guidelines. However, here are a few suggestions for improvement:

* Consider adding a docstring to the `maxDepth` method to describe its purpose and behavior.
* Use consistent naming conventions throughout the code (e.g., `right` instead of `Right`).
* Consider adding a check for `None` values in the recursive calls to handle potential errors.

Here's the refactored code with these suggestions applied:
```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Returns the maximum depth of a binary tree.

        Args:
        root: The root of the binary tree.

        Returns:
        An integer representing the maximum depth of the tree.
        """
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)
```
Overall, the provided code is clear, concise, and well-structured. With these minor suggestions, the code becomes even more readable and maintainable.

## Optimized Solution
**Optimized Solution**

The provided original solution and code review already contain optimized solutions for the Maximum Depth of Binary Tree problem. However, I will provide a slight modification to improve readability and follow best practices.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """Returns the maximum depth of a binary tree."""
        if not root:
            return 0
        
        # Recursively calculate the depth of the left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # Return the maximum depth plus 1 (for the current node)
        return max(left_depth, right_depth) + 1
```

Alternatively, an iterative approach using a queue can also be used:

```python
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """Returns the maximum depth of a binary tree."""
        if not root:
            return 0
        
        max_depth = 0
        queue = deque([(root, 1)])
        
        while queue:
            node, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        
        return max_depth
```

**Time and Space Complexity**

* **Time Complexity:** O(N), where N is the number of nodes in the tree, since we visit each node once.
* **Space Complexity:**
	+ Recursive approach: O(H), where H is the height of the tree, due to the recursive call stack.
	+ Iterative approach: O(N), where N is the number of nodes in the tree, in the worst-case scenario when the tree is unbalanced and the queue stores all nodes at the last level.

**Step-by-Step Explanation**

1. **Base Case:** If the tree is empty (i.e., `root` is `None`), return 0.
2. **Recursive Approach:**
	* Recursively calculate the depth of the left and right subtrees.
	* Return the maximum depth plus 1 (for the current node).
3. **Iterative Approach:**
	* Initialize a queue with the root node and its depth (1).
	* While the queue is not empty:
		+ Dequeue a node and its depth.
		+ Update the maximum depth if the current depth is greater.
		+ Enqueue the left and right children of the node with their respective depths (if they exist).
	* Return the maximum depth.

**Why this Solution is Optimal**

The provided solutions have a time complexity of O(N) and space complexity of O(H) or O(N), which is optimal for this problem. The recursive approach is more concise and easier to understand, while the iterative approach can be more efficient in terms of memory usage for very large trees. However, the difference in performance is negligible for this problem, and the choice of approach depends on personal preference and specific requirements.

## Lesson & Pattern
In this problem, the core algorithmic pattern is **Depth-First Search (DFS)**, which is used to traverse the binary tree and calculate its maximum depth.

This pattern fits this problem for several reasons:

1. **Tree structure**: The problem involves a tree data structure, which is typically traversed using DFS or **Breadth-First Search (BFS)**. In this case, DFS is more suitable because we need to explore the tree depth-first to calculate the maximum depth.
2. **Recursive nature**: The problem has a recursive nature, where we need to calculate the maximum depth of the left and right subtrees and then combine the results. DFS is a natural fit for recursive problems like this.
3. **Efficient exploration**: DFS allows us to efficiently explore the tree by traversing the nodes in a depth-first manner, which reduces the number of nodes we need to visit to calculate the maximum depth.

Here are 3 similar LeetCode problems that use the same pattern:

1. **Binary Tree Level Order Traversal** (102): This problem involves traversing a binary tree level by level, which can be solved using BFS or DFS.
2. **Path Sum** (112): This problem involves finding a path in a binary tree that sums up to a given target value, which can be solved using DFS.
3. **Lowest Common Ancestor of a Binary Tree** (236): This problem involves finding the lowest common ancestor of two nodes in a binary tree, which can be solved using DFS.

To recognize this pattern in future problems, you can use the following mental framework:

* **Is the problem tree-related?**: If the problem involves a tree data structure, DFS or BFS might be a good fit.
* **Is the problem recursive?**: If the problem has a recursive nature, where you need to break it down into smaller sub-problems and combine the results, DFS might be a good choice.
* **Do you need to explore the tree depth-first?**: If you need to traverse the tree in a depth-first manner, such as to calculate the maximum depth or find a path, DFS is likely the way to go.

One key takeaway from this problem is that **DFS is a powerful technique for traversing tree data structures and solving recursive problems**. By recognizing the recursive nature of the problem and the need to explore the tree depth-first, you can apply DFS to solve a wide range of tree-related problems.

Here is a code example that demonstrates the mental framework:
```python
def is_tree_related(problem):
    # Check if the problem involves a tree data structure
    return "tree" in problem

def is_recursive(problem):
    # Check if the problem has a recursive nature
    return "recursive" in problem

def use_dfs(problem):
    # Use DFS if the problem is tree-related and recursive
    if is_tree_related(problem) and is_recursive(problem):
        return True
    return False

problem = "Maximum Depth of Binary Tree"
if use_dfs(problem):
    print("Use DFS to solve the problem")
else:
    print("Use a different approach to solve the problem")
```
This code example is a simplified demonstration of the mental framework, and you can modify it to fit your specific needs and problem-solving approach.
