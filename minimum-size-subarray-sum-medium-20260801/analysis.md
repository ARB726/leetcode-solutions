# Minimum Size Subarray Sum — Medium

## Problem
Minimum Size Subarray Sum
Medium
Topics
Company Tags
You are given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: target = 10, nums = [2,1,5,1,5,3]

Output: 3
Explanation: The subarray [5,1,5] has the minimal length under the problem constraint.

Example 2:

Input: target = 5, nums = [1,2,1]

Output: 0
Constraints:

1 <= nums.length <= 100,000
1 <= nums[i] <= 10,000
1 <= target <= 1,000,000,000
Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

## Problem Analysis
**Problem Analysis**

1. **Problem Type**: Array, Sliding Window
2. **Constraints and Edge Cases**:
   - Array length: 1 <= nums.length <= 100,000
   - Array elements: 1 <= nums[i] <= 10,000
   - Target: 1 <= target <= 1,000,000,000
   - Edge case: If there is no such subarray, return 0
3. **Inputs and Outputs**:
   - Input: Array `nums` and integer `target`
   - Output: Minimal length of a subarray whose sum is greater than or equal to `target`
4. **Recommended Data Structures**:
   - Array or List for storing the input `nums`
   - Two pointers (left and right) for implementing the sliding window technique
   - Variables to store the current window sum, minimum length, and the result

**Solution Approach**:
To solve this problem efficiently, we can use the sliding window technique. The idea is to maintain a window of elements whose sum is greater than or equal to the target. We can achieve this by moving the right pointer to the right and adding elements to the window sum. When the window sum becomes greater than or equal to the target, we try to minimize the window by moving the left pointer to the right and subtracting elements from the window sum. We keep track of the minimum length of such a window.

**Time Complexity**:
- O(n) using the sliding window technique
- O(n log(n)) using a prefix sum array and binary search (for the follow-up question)

## Code Review
**Code Review**

### Bugs or Logical Errors

The code seems to be logically correct and does not contain any apparent bugs. It correctly implements the sliding window technique to find the minimum length subarray whose sum is greater than or equal to the target.

### Time Complexity

The time complexity of the given solution is **O(n)**, where n is the length of the input array `nums`. This is because the solution uses a single pass through the array to find the minimum length subarray.

### Space Complexity

The space complexity of the given solution is **O(1)**, as it only uses a constant amount of space to store the variables `left`, `right`, `maxLength`, and `sum`.

### Edge Cases

The code correctly handles the edge case where there is no subarray whose sum is greater than or equal to the target. In this case, it returns 0.

### Code Readability and Style

The code is well-organized and follows the standard Python style guide (PEP 8). However, there are a few minor suggestions for improvement:

* The variable `sum` is a built-in Python function. It would be better to use a different variable name, such as `window_sum`, to avoid potential conflicts.
* The variable `maxLength` could be initialized to a more descriptive value, such as `float('inf')`, to indicate that it represents infinity.
* The use of whitespace is mostly consistent, but there are a few places where it could be improved. For example, there is no space between the `while` keyword and the following condition.
* The code could benefit from additional comments to explain the purpose of each section and the logic behind the algorithm.

Here is the refactored code with these suggestions incorporated:

```python
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Initialize the sliding window boundaries
        left = 0
        right = 0
        
        # Initialize the minimum length to infinity
        min_length = float('inf')
        
        # Initialize the window sum to 0
        window_sum = 0

        # Iterate through the array with the right pointer
        while right < len(nums):
            # Add the current element to the window sum
            window_sum += nums[right]

            # Try to minimize the window when the sum is greater than or equal to the target
            while window_sum >= target:
                # Update the minimum length if the current window is smaller
                min_length = min(min_length, right - left + 1)
                
                # Subtract the leftmost element from the window sum and move the left pointer to the right
                window_sum -= nums[left]
                left += 1

            # Move the right pointer to the right
            right += 1

        # Return 0 if no subarray is found, otherwise return the minimum length
        return 0 if min_length == float('inf') else min_length
```

Overall, the code is well-structured and easy to follow. With a few minor adjustments, it can be even more readable and maintainable.

## Optimized Solution
**Optimized Solution**
The original solution is already optimized to have a time complexity of O(n). However, we can improve the code readability and handle edge cases more elegantly. Here's the optimized solution:

```python
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_length = float('inf')
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        
        return 0 if min_length == float('inf') else min_length
```

**Explanation**
The optimized solution uses the same sliding window technique as the original solution. The main improvements are:

*   Renaming `sum` to `current_sum` to avoid shadowing the built-in `sum` function.
*   Using a more Pythonic way of iterating over the `nums` array using a `for` loop.
*   Using `float('inf')` to represent infinity, which is more readable and consistent with the rest of the code.
*   Simplifying the condition to return 0 when no such subarray is found.

**Time Complexity**
The time complexity of the optimized solution remains O(n), where n is the length of the `nums` array. This is because we only iterate over the array once and use a constant amount of extra memory to store the `left` and `right` pointers, as well as the `current_sum` and `min_length` variables.

**Space Complexity**
The space complexity of the optimized solution remains O(1), which means it uses a constant amount of extra memory that does not grow with the size of the input array.

**Step-by-Step Walkthrough**

1.  Initialize the `left` pointer to 0, `current_sum` to 0, and `min_length` to infinity.
2.  Iterate over the `nums` array from left to right using a `for` loop.
3.  At each iteration, add the current element to `current_sum`.
4.  If `current_sum` becomes greater than or equal to `target`, enter a nested loop where we try to minimize the window by moving the `left` pointer to the right and subtracting elements from `current_sum`.
5.  Inside the nested loop, update `min_length` with the minimum length of the window that meets the condition.
6.  After the nested loop, continue iterating over the `nums` array.
7.  Once the iteration is complete, return 0 if `min_length` remains infinity (indicating no such subarray was found) or the minimum length otherwise.

Overall, the optimized solution is more readable and maintainable while retaining the same time complexity as the original solution.

## Lesson & Pattern
I love this problem. Let's break it down together.

The core algorithmic pattern here is the **Sliding Window** technique. This pattern fits this problem because we need to find a contiguous subarray (a "window" of elements) whose sum meets a certain condition (being greater than or equal to the target). By moving the window's boundaries (the left and right pointers), we can efficiently explore all possible subarrays and find the one with the minimum length that satisfies the condition.

The Sliding Window technique is particularly useful when dealing with arrays or strings and we need to find a subset that meets certain criteria. It's often used to solve problems that involve finding a maximum or minimum value within a certain range or window.

Here are 3 similar LeetCode problems that use the same pattern:

1. **Longest Substring Without Repeating Characters**: This problem asks you to find the length of the longest substring without repeating characters in a given string. You can use a sliding window to keep track of the unique characters in the current substring.
2. **Maximum Sum Subarray**: This problem asks you to find the maximum sum of a subarray within a given array. You can use a sliding window to keep track of the maximum sum of a subarray ending at each position.
3. **Subarray Product Less Than K**: This problem asks you to find the number of contiguous subarrays whose product is less than a given value K. You can use a sliding window to keep track of the product of the current subarray and adjust the window boundaries accordingly.

To recognize the Sliding Window pattern in future problems, here's a simple mental framework:

* **Is the problem asking me to find a subset or a range that meets certain criteria?** (e.g., a subarray, a substring, a range of numbers)
* **Can I use a "window" of elements to solve the problem?** (e.g., a pair of pointers, a range of indices)
* **Can I move the window's boundaries to explore all possible solutions?** (e.g., incrementing a pointer, adjusting a range)

One key takeaway from this problem is to **always consider the trade-offs between using a brute-force approach and using a more efficient technique like Sliding Window**. In this case, using a Sliding Window reduced the time complexity from O(n^2) to O(n), making the solution much more efficient for large inputs. Remember to always look for opportunities to apply this pattern in your problem-solving endeavors!
