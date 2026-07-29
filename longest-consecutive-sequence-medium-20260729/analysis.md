# Longest Consecutive Sequence — Medium

## Problem
Longest Consecutive Sequence
Medium
Topics
Company Tags
Hints
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
Constraints:

0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9


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
51.4%

Solution 1
+

NeetBot
|

Hint
|
|
Ln 13, Col 21

Ask NeetBot

12384591011126713
Wrong Answer


Suggest Fix
Passed test cases: 15 / 24

Last executed test case

Input:


nums=[9,1,4,7,3,-1,0,5,8,-1,6]
Your Output:


9
Expected output:


7


## Problem Analysis
**Problem Analysis: Longest Consecutive Sequence**

1. **Problem Type:** Array, Hashing
2. **Constraints and Edge Cases:**
	* `0 <= nums.length <= 1000`
	* `-10^9 <= nums[i] <= 10^9`
	* Duplicate elements are allowed
	* The input array can be empty
	* The input array can contain negative numbers
3. **Expected Inputs and Outputs:**
	* Input: An array of integers `nums`
	* Output: The length of the longest consecutive sequence
4. **Recommended Data Structures:**
	* Hash Set (e.g., Python's `set`) to store unique elements and enable O(1) lookups

**Key Insights:**

* To achieve O(n) time complexity, we need to avoid iterating over the array multiple times.
* Using a hash set can help us quickly check if an element is part of a consecutive sequence.
* We should focus on finding the starting point of the longest consecutive sequence, as we can then easily extend it by checking for the presence of subsequent numbers in the hash set.

## Code Review
**Code Review**

### Bugs or Logical Errors

1. The solution sorts the input array `nums`, which has a time complexity of O(n log n). This does not meet the required time complexity of O(n).
2. The solution does not handle duplicate elements correctly. When `nums[i]` is equal to `nums[i+1]`, the solution still increments the count, which is incorrect.
3. The solution does not handle the case where `nums[i]` is not equal to `nums[i+1]`, but `nums[i+1]` could be the start of a new consecutive sequence.

### Time Complexity (Big O)

* The current solution has a time complexity of O(n log n) due to the sorting operation.
* To achieve O(n) time complexity, we should use a different approach that does not require sorting.

### Space Complexity (Big O)

* The current solution has a space complexity of O(1) since it only uses a few variables to store the count and max count.
* However, if we use a different approach that involves storing all elements in a set, the space complexity would be O(n).

### Edge Cases

1. Empty input array: The solution handles this case correctly by returning 0.
2. Duplicate elements: The solution does not handle this case correctly, as mentioned earlier.
3. Negative numbers: The solution can handle negative numbers, but the current implementation does not account for the fact that the input array can contain negative numbers.

### Code Readability and Style

1. The variable names `count` and `maxCount` are not very descriptive. Consider using more descriptive names like `current_sequence_length` and `longest_sequence_length`.
2. The solution can be improved by using a more concise and efficient way to handle the iteration and counting.

**Improved Solution**

Here is a revised solution that meets the O(n) time complexity requirement and handles edge cases correctly:
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_sequence_length = 0

        for num in num_set:
            # Check if num is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_sequence_length = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_sequence_length += 1

                longest_sequence_length = max(longest_sequence_length, current_sequence_length)

        return longest_sequence_length
```
This solution works by iterating over the set of unique numbers in the input array. For each number, it checks if it is the start of a sequence by verifying that `num - 1` is not in the set. If it is the start of a sequence, it then checks for the presence of subsequent numbers in the set, keeping track of the current sequence length. Finally, it updates the longest sequence length if the current sequence is longer.

**Time Complexity:** O(n)

**Space Complexity:** O(n)

This solution meets the required time complexity of O(n) and handles edge cases correctly, including duplicate elements and negative numbers. The code is also more concise and readable than the original solution.

## Optimized Solution
**Optimized Solution**

The original solution has a time complexity of O(n log n) due to the sorting operation. To achieve O(n) time complexity, we can use a hash set to store the elements and then iterate over the set to find the longest consecutive sequence.

```python
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create a hash set from the input array
        num_set = set(nums)
        
        # Initialize the maximum length of the consecutive sequence
        max_length = 0
        
        # Iterate over the hash set
        for num in num_set:
            # Check if the current number is the start of a sequence
            if num - 1 not in num_set:
                # Initialize the current number and the length of the current sequence
                current_num = num
                current_length = 1
                
                # Check for the presence of subsequent numbers in the hash set
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                # Update the maximum length
                max_length = max(max_length, current_length)
        
        # Return the maximum length
        return max_length
```

**Explanation**

1.  We create a hash set `num_set` from the input array `nums`. This allows us to perform O(1) lookups and avoids duplicates.
2.  We iterate over the hash set `num_set`. For each number `num`, we check if it is the start of a sequence by verifying if `num - 1` is not in the hash set. This ensures that we only consider the starting point of each sequence.
3.  If `num` is the start of a sequence, we initialize the current number `current_num` to `num` and the length of the current sequence `current_length` to 1.
4.  We then check for the presence of subsequent numbers in the hash set by iterating from `current_num + 1` onwards. If the next number is in the hash set, we increment `current_num` and `current_length`.
5.  After finding the length of the current sequence, we update the maximum length `max_length` if the current sequence is longer.
6.  Finally, we return the maximum length `max_length`, which represents the length of the longest consecutive sequence.

**Time and Space Complexity**

*   **Time complexity:** O(n)
    *   Creating the hash set takes O(n) time.
    *   Iterating over the hash set and checking for subsequent numbers takes O(n) time in total, as each number is visited at most twice (once as the starting point and once as part of a sequence).
*   **Space complexity:** O(n)
    *   Storing the input array in a hash set takes O(n) space.

**Example Walkthrough**

Input: `nums = [100, 4, 200, 1, 3, 2]`

1.  Create a hash set: `num_set = {100, 4, 200, 1, 3, 2}`
2.  Iterate over the hash set:
    *   `num = 100`: Not the start of a sequence (`99` is not in the hash set, but `100 - 1 = 99` is not in the hash set, however `100 + 1 = 101` is not in the set, and `100 - 1 = 99` is not either, so we can skip this)
    *   `num = 4`: Start of a sequence
        *   `current_num = 4`, `current_length = 1`
        *   `5` is not in the hash set, so we stop here
        *   `max_length` remains 0 (because we didn't update it in the previous steps)
    *   `num = 200`: Not the start of a sequence (we skip this because `200 + 1` is not in the set, and `200 - 1 = 199` is not either)
    *   `num = 1`: Start of a sequence
        *   `current_num = 1`, `current_length = 1`
        *   `2` is in the hash set, so `current_num = 2`, `current_length = 2`
        *   `3` is in the hash set, so `current_num = 3`, `current_length = 3`
        *   `4` is in the hash set, so `current_num = 4`, `current_length = 4`
        *   `max_length = 4`
3.  Return `max_length = 4`, which is the length of the longest consecutive sequence `[1, 2, 3, 4]`.

## Lesson & Pattern
Let's break it down together.

The core algorithmic pattern in this problem is **Hashing**, specifically using a `set` to store unique elements and enable O(1) lookups. This pattern fits this problem because it allows us to:

1. **Efficiently store and look up elements**: By storing all elements in a `set`, we can quickly check if an element is present in O(1) time.
2. **Avoid duplicate elements**: Using a `set` automatically eliminates duplicates, which is important in this problem since we're interested in the length of the longest consecutive sequence, not the actual sequence itself.
3. **Achieve O(n) time complexity**: By iterating over the array once and using O(1) lookups, we can find the longest consecutive sequence in linear time.

There are several other LeetCode problems that use the same Hashing pattern, including:

1. **Contains Duplicate** (Easy): Given an array of integers, return `True` if there are any duplicates, and `False` otherwise.
2. **Single Number** (Easy): Given an array of integers, find the single number that appears only once.
3. **Two Sum** (Easy): Given an array of integers and a target sum, find two numbers that add up to the target sum.

To recognize this pattern in future problems, here's a simple mental framework:

* **Look for problems that involve**: Sets, dictionaries, or other data structures that allow for O(1) lookups.
* **Check if the problem requires**: Efficient storage and lookup of elements, elimination of duplicates, or finding unique elements.
* **Consider using Hashing if**: The problem has a large input size, and you need to optimize for time complexity.

One key takeaway to remember is that **Hashing can be used to optimize problems that require efficient lookup and storage of elements**, especially when dealing with large input sizes or performance-critical applications.

Now, let's take a look at your original solution. The main issue is that it doesn't handle duplicates correctly and it only checks for consecutive sequences in the sorted array, which isn't the correct approach. The optimized solution uses a `set` to store unique elements and then iterates over the array to find the longest consecutive sequence. Do you want me to explain the optimized solution in more detail?
