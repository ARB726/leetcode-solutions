# 1248 Count Number Of Nice Subarrays — Medium

## Problem
1248. Count Number of Nice Subarrays
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
 

Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length

## Problem Analysis
### Problem Analysis

**Problem Type:** Array, Prefix Sum, Hash Table

**Constraints and Edge Cases:**

* `nums` length: 1 to 50,000
* `nums[i]` value: 1 to 10^5
* `k` value: 1 to `nums.length`
* Edge cases:
	+ Empty array (already ruled out by the constraints)
	+ `k` larger than the number of odd elements in the array
	+ `k` equal to the number of odd elements in the array

**Inputs and Outputs:**

* Input: `nums` array and integer `k`
* Output: Number of nice sub-arrays with `k` odd numbers

**Best Data Structures to Use:**

* Prefix sum array to keep track of the cumulative count of odd numbers
* Hash table (e.g., unordered map) to store the count of prefix sums modulo a certain value
* Array to store the input `nums` and prefix sums

This problem can be solved using a prefix sum array and a hash table, with a time complexity of O(n) and space complexity of O(n), where n is the length of the input array `nums`.

## Code Review
**Code Review**

### Bug and Logical Errors

The code provided is almost correct but it can be improved. However, there is a logical error in the given solution. 

The current code does not correctly calculate the number of sub-arrays with `k` odd numbers. It seems to calculate the number of sub-arrays with at most `k` odd numbers instead.

### Time Complexity (Big O)

The time complexity of the given solution is O(n), where n is the length of the input array `nums`. This is because the code iterates over the input array once.

### Space Complexity (Big O)

The space complexity of the given solution is O(1), as it only uses a constant amount of space to store the variables `left`, `right`, `count`, and `windowSum`.

### Edge Cases

The code does not handle the edge case when `k` is larger than the number of odd numbers in the array. However, this is already ruled out by the problem constraints.

### Code Readability and Style

The code is generally well-structured and easy to read. However, there are some improvements that can be made:

* The variable names `left`, `right`, `count`, and `windowSum` could be more descriptive.
* The code could benefit from more comments to explain the logic behind the solution.
* The function `helperFunction` could be renamed to something more descriptive.

### Improved Solution

Here is an improved solution that uses a prefix sum array and a hash table:
```python
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Create a prefix sum array to store the cumulative count of odd numbers
        prefix_sum = [0] * (len(nums) + 1)
        
        # Calculate the prefix sum array
        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + (nums[i] % 2)
        
        # Initialize a hash table to store the count of prefix sums
        count = {0: 1}
        
        # Initialize the result
        res = 0
        
        # Iterate over the prefix sum array
        for i in range(1, len(prefix_sum)):
            # Calculate the target prefix sum
            target = prefix_sum[i] - k
            
            # If the target prefix sum is in the hash table, add the count to the result
            if target in count:
                res += count[target]
            
            # Increment the count of the current prefix sum
            count[prefix_sum[i]] = count.get(prefix_sum[i], 0) + 1
        
        # Return the result
        return res
```
This solution has a time complexity of O(n) and a space complexity of O(n), where n is the length of the input array `nums`. It correctly calculates the number of sub-arrays with `k` odd numbers. 

### Explanation of Changed Solution
- The new solution first creates a prefix sum array of odd numbers, `prefix_sum`.
- It then iterates over `prefix_sum`, and for each prefix sum at index `i`, it calculates the target prefix sum by subtracting `k` from the current prefix sum.
- It checks if the target prefix sum exists in the `count` hash table. If it does, it adds the count to the result `res`, because it has found a sub-array with exactly `k` odd numbers ending at index `i`.
- Finally, it increments the count of the current prefix sum in the `count` hash table.
- The time complexity of this solution is O(n), where n is the length of `nums`. This is because it makes one pass through `nums` to calculate `prefix_sum`, and another pass through `prefix_sum` to calculate `res`.
- The space complexity of this solution is also O(n), because in the worst case, every prefix sum in `prefix_sum` could be unique, which would require O(n) space to store in the `count` hash table.

## Optimized Solution
### Optimized Solution
The original solution has a time complexity of O(n) for the `helperFunction` but is called twice, resulting in a time complexity of O(2n) which simplifies to O(n). This is already quite efficient. However, the code can be improved for clarity and conciseness.

Here is a refactored version of the solution:
```python
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def at_most(k):
            if k < 0:
                return 0
            
            left, count = 0, 0
            window_sum = 0
            
            for right in range(len(nums)):
                window_sum += nums[right] % 2
                
                while window_sum > k:
                    window_sum -= nums[left] % 2
                    left += 1
                
                count += right - left + 1
            
            return count
        
        return at_most(k) - at_most(k - 1)
```

### Explanation
This solution uses a modified version of the `helperFunction`, now called `at_most`, which calculates the number of subarrays that contain at most `k` odd numbers.

The `at_most` function uses a sliding window approach, maintaining a `window_sum` of the number of odd numbers within the current window. When `window_sum` exceeds `k`, it slides the window to the right by incrementing the `left` pointer.

The number of subarrays that contain exactly `k` odd numbers is then calculated by subtracting the number of subarrays that contain at most `k-1` odd numbers from the number of subarrays that contain at most `k` odd numbers.

### Time and Space Complexity
* Time complexity: O(n)
* Space complexity: O(1), excluding the input array `nums`

### Step-by-Step Walkthrough

1. Define the `at_most` function, which calculates the number of subarrays that contain at most `k` odd numbers.
2. Initialize the `left` pointer, `count` variable, and `window_sum` variable.
3. Iterate over the input array `nums` using the `right` pointer.
4. For each element, increment `window_sum` by the parity of the current element (1 if odd, 0 if even).
5. If `window_sum` exceeds `k`, slide the window to the right by incrementing the `left` pointer and decrementing `window_sum` by the parity of the element at the `left` index.
6. Increment `count` by the number of subarrays that end at the current `right` index and have at most `k` odd numbers.
7. Return the total count of subarrays that contain at most `k` odd numbers.
8. Calculate the number of subarrays that contain exactly `k` odd numbers by subtracting the result of `at_most(k-1)` from `at_most(k)`.

The original solution is already optimal in terms of time complexity. This refactored version improves code clarity and conciseness while maintaining the same time complexity.

## Lesson & Pattern
Let's break this down together.

### Core Algorithmic Pattern: Prefix Sum and Sliding Window
The core pattern here is the combination of **Prefix Sum** and **Sliding Window**. The Prefix Sum technique is used to calculate the cumulative count of odd numbers, and the Sliding Window technique is used to find the number of sub-arrays with a certain property (in this case, exactly `k` odd numbers).

### Why this pattern fits this problem
This pattern fits this problem because it allows us to efficiently calculate the number of sub-arrays with `k` odd numbers. The Prefix Sum technique gives us a way to keep track of the cumulative count of odd numbers, and the Sliding Window technique allows us to slide a window over the array and count the number of sub-arrays that satisfy the condition. This approach reduces the time complexity from O(n^2) to O(n), making it much more efficient for large inputs.

### Similar LeetCode Problems
Here are 3 similar LeetCode problems that use the same pattern:

1. **LeetCode 560: Subarray Sum Equals K** - This problem also uses the Prefix Sum and Sliding Window techniques to find the number of sub-arrays with a certain sum.
2. **LeetCode 974: Subarray Sums Divisible by K** - This problem uses a similar approach to find the number of sub-arrays with sums divisible by `k`.
3. **LeetCode 904: Fruit Into Baskets** - This problem uses a sliding window approach to find the maximum number of fruits that can be collected with at most two different types.

### Mental Framework to Recognize this Pattern
Here's a simple mental framework to recognize this pattern:

* **Look for problems that involve sub-arrays or sub-strings** - If a problem involves finding the number of sub-arrays or sub-strings with certain properties, it may be a good candidate for the Prefix Sum and Sliding Window techniques.
* **Identify the property that needs to be maintained** - In this case, the property is the count of odd numbers. Identify what property needs to be maintained or calculated, and think about how you can use a prefix sum or sliding window to achieve this.
* **Consider using a hash table or prefix sum array** - If the problem involves counting or keeping track of certain values, a hash table or prefix sum array may be a good data structure to use.

### Key Takeaway
One key takeaway from this problem is that **combining multiple techniques can lead to more efficient solutions**. In this case, combining the Prefix Sum and Sliding Window techniques led to a much more efficient solution than using either technique alone. This is a good thing to keep in mind when solving problems - don't be afraid to combine different techniques to achieve a better solution!
