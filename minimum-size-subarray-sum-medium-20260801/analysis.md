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
**Problem Type:** Array, Two-Pointer Technique
**Constraints and Edge Cases:**
* Array length: 1 <= nums.length <= 100,000
* Array elements: 1 <= nums[i] <= 10,000
* Target value: 1 <= target <= 1,000,000,000
* Edge cases: 
  + Empty array (not applicable due to constraint)
  + Target value larger than the sum of all array elements
  + Array elements larger than the target value

**Inputs and Outputs:**
* Input: target (integer), nums (array of integers)
* Output: Minimal length of a subarray with sum greater than or equal to the target (integer)

**Suggested Data Structures:**
* Array (for input and processing)
* Two pointers (left and right pointers for the sliding window)

**Example Code (Two-Pointer Technique, O(n)):**
```python
def minSubArrayLen(target: int, nums: list[int]) -> int:
    left = 0
    min_length = float('inf')
    current_sum = 0

    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return 0 if min_length == float('inf') else min_length
```

## Code Review
**Code Review**

### Bug and Logical Errors

The provided solution code has a logical error. When the `totalSums` is greater than or equal to the `target`, the code correctly updates `minSize` and moves the `left` pointer to the right. However, when the `totalSums` becomes less than `target` again (after subtracting `nums[left]`), the code does not add `nums[right]` to `totalSums`. To fix this, the inner while loop should only move the `left` pointer, not update `right` until the second while loop finishes.

Here's the corrected code:
```python
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left, right, total_sums, min_size = 0, 0, 0, float('inf')

        while right < len(nums):
            total_sums += nums[right]
            while total_sums >= target:
                min_size = min(min_size, right - left + 1)
                total_sums -= nums[left]
                left += 1
            right += 1
        return 0 if min_size == float('inf') else min_size
```

### Time Complexity (Big O)

The time complexity of the given solution is **O(n)**. The solution uses a two-pointer technique, where the `right` pointer moves through the array once, and the `left` pointer moves through the array at most once. This results in a linear time complexity.

### Space Complexity (Big O)

The space complexity of the given solution is **O(1)**. The solution uses a constant amount of space to store the `left`, `right`, `total_sums`, and `min_size` variables, regardless of the input size.

### Edge Cases

The provided solution code handles most edge cases correctly. However, here are a few additional edge cases to consider:

*   If the input array is empty, the function will return 0, which is correct based on the problem constraints.
*   If the target value is larger than the sum of all array elements, the function will return 0, which is correct.
*   If the array elements are larger than the target value, the function will still work correctly and return the minimal length of the subarray.

### Code Readability and Style

The code readability and style can be improved in a few ways:

*   Variable names should be descriptive and follow the conventional naming style (lowercase with underscores).
*   Comments can be added to explain the purpose of each section of code, especially for complex logic.
*   The code can be formatted consistently, following standard Python coding conventions.

Here's the refactored code with improved readability and style:
```python
class Solution:
    def min_subarray_len(self, target: int, nums: list[int]) -> int:
        # Initialize two pointers and the minimum length
        left, right, total_sum, min_length = 0, 0, 0, float('inf')

        # Move the right pointer through the array
        while right < len(nums):
            # Add the current element to the total sum
            total_sum += nums[right]

            # Move the left pointer to the right if the total sum is greater than or equal to the target
            while total_sum >= target:
                # Update the minimum length
                min_length = min(min_length, right - left + 1)
                # Subtract the leftmost element from the total sum and move the left pointer to the right
                total_sum -= nums[left]
                left += 1

            # Move the right pointer to the right
            right += 1

        # Return 0 if no subarray is found, otherwise return the minimum length
        return 0 if min_length == float('inf') else min_length
```

## Optimized Solution
## Optimized Solution

The provided original solution and code review are already optimized with a time complexity of O(n). However, we can make some minor improvements for better readability and maintainability.

```python
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """Returns the minimal length of a subarray whose sum is greater than or equal to target."""
        
        # Initialize two pointers and the minimum length
        left = 0
        min_length = float('inf')
        current_sum = 0
        
        # Iterate over the array with the right pointer
        for right in range(len(nums)):
            # Add the current element to the sum
            current_sum += nums[right]
            
            # Shrink the window if the sum is greater than or equal to the target
            while current_sum >= target:
                # Update the minimum length
                min_length = min(min_length, right - left + 1)
                # Subtract the leftmost element from the sum and move the left pointer
                current_sum -= nums[left]
                left += 1
        
        # Return 0 if no such subarray exists, otherwise return the minimum length
        return 0 if min_length == float('inf') else min_length
```

## Explanation

The optimized solution uses the two-pointer technique with a sliding window approach.

1.  **Initialization**: We initialize two pointers, `left` and `right`, to represent the sliding window. We also initialize `min_length` to store the minimum length of the subarray and `current_sum` to store the sum of the elements within the current window.
2.  **Iteration**: We iterate over the array with the `right` pointer.
3.  **Expansion**: Inside the loop, we add the current element to `current_sum`.
4.  **Contraction**: If `current_sum` is greater than or equal to the target, we update `min_length` and subtract the leftmost element from `current_sum`. We then move the `left` pointer to the right to contract the window.
5.  **Result**: Finally, we return 0 if no such subarray exists (i.e., `min_length` is still `float('inf')`). Otherwise, we return the minimum length.

## Time and Space Complexity

*   **Time Complexity**: O(n), where n is the length of the input array. This is because we make a single pass through the array with the `right` pointer, and the `while` loop inside the `for` loop runs in total O(n) time.
*   **Space Complexity**: O(1), which means the space required does not change with the size of the input array. We only use a constant amount of space to store the two pointers, the minimum length, and the current sum.

## Step-by-Step Walkthrough

Let's use the example input `target = 10` and `nums = [2, 1, 5, 1, 5, 3]`.

1.  Initialize `left = 0`, `min_length = float('inf')`, and `current_sum = 0`.
2.  Iterate over the array:

    *   `right = 0`, `current_sum = 0 + 2 = 2`. Since `current_sum < target`, we do not update `min_length`.
    *   `right = 1`, `current_sum = 2 + 1 = 3`. Still, `current_sum < target`.
    *   `right = 2`, `current_sum = 3 + 5 = 8`. `current_sum < target`.
    *   `right = 3`, `current_sum = 8 + 1 = 9`. `current_sum < target`.
    *   `right = 4`, `current_sum = 9 + 5 = 14`. Now, `current_sum >= target`, so we update `min_length = 5` and subtract the leftmost element from `current_sum`: `current_sum = 14 - 2 = 12`. Move the `left` pointer: `left = 1`.
    *   `current_sum = 12 >= target`, so we update `min_length = min(5, 4) = 4` and subtract the leftmost element: `current_sum = 12 - 1 = 11`. Move the `left` pointer: `left = 2`.
    *   `current_sum = 11 >= target`, so we update `min_length = min(4, 3) = 3` and subtract the leftmost element: `current_sum = 11 - 5 = 6`. Move the `left` pointer: `left = 3`.
    *   `right = 5`, `current_sum = 6 + 3 = 9`. Since `current_sum < target`, we do not update `min_length`.
3.  After iterating over the entire array, `min_length = 3`, which is the minimum length of a subarray whose sum is greater than or equal to the target. Therefore, we return `3`.

## Lesson & Pattern
Let's break down the problem and the solution to identify the core algorithmic pattern.

**Core Algorithmic Pattern:**
The pattern used in this solution is called the **Two-Pointer Technique**, specifically a variation known as the **Sliding Window** approach. This technique involves using two pointers (in this case, `left` and `right`) to represent a window or a subarray within the larger array.

**Why this pattern fits this problem:**
The Two-Pointer Technique is a great fit for this problem because we need to find a subarray with a sum greater than or equal to the target. By using two pointers, we can efficiently expand and contract the window to find the smallest subarray that meets the condition. The `right` pointer moves to the right to expand the window, and the `left` pointer moves to the right to contract the window when the sum exceeds the target.

**Similar LeetCode problems that use the same pattern:**

1. **Maximum Subarray** (LeetCode 53): Find the maximum sum of a subarray within a given array.
2. **Subarray Sum Equals K** (LeetCode 560): Find the number of subarrays with a sum equal to a given target.
3. **Longest Substring Without Repeating Characters** (LeetCode 3): Find the length of the longest substring without repeating characters.

**Simple mental framework to recognize this pattern:**
To recognize the Two-Pointer Technique, ask yourself:

* Do I need to find a subarray or a subset within a larger array?
* Do I need to maintain a window or a range of elements?
* Can I use two pointers to efficiently expand and contract the window?

If you answer "yes" to these questions, the Two-Pointer Technique might be a good fit for the problem.

**One key takeaway:**
Remember that the Two-Pointer Technique is all about efficiently managing a window or a subarray within a larger array. By using two pointers, you can reduce the time complexity of the solution and make it more scalable. Keep practicing, and you'll become proficient in recognizing and applying this pattern to a wide range of problems! 

Here is a python code snippet to further demonstrate the Two-Pointer Technique:
```python
def example_two_pointer_technique(arr):
    left = 0
    right = 0
    max_sum = float('-inf')

    while right < len(arr):
        # Expand the window
        current_sum = sum(arr[left:right+1])
        max_sum = max(max_sum, current_sum)

        # Contract the window
        if current_sum > target:
            left += 1

        right += 1

    return max_sum

# Example usage:
arr = [1, 2, 3, 4, 5]
target = 5
result = example_two_pointer_technique(arr)
print(result)
```
In this example, we use two pointers (`left` and `right`) to manage a window within the array. We expand the window by moving the `right` pointer and contract the window by moving the `left` pointer. This allows us to efficiently find the maximum sum of a subarray within the array.
