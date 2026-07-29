# LeetCode Analysis - 20260728_192227

## Problem

Code
Accepted
Accepted
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
### Analysis of LeetCode Problem: Count Number of Nice Subarrays

#### 1. Problem Type
The problem type is an **array problem** involving a sliding window technique and can be solved using **prefix sum** or **hashing**.

#### 2. Constraints and Edge Cases
- **Constraints**:
  - `1 <= nums.length <= 50000`
  - `1 <= nums[i] <= 10^5`
  - `1 <= k <= nums.length`
- **Edge Cases**:
  - An empty array or an array with all even numbers when `k` is greater than 0.
  - An array with less than `k` odd numbers.

#### 3. Inputs and Outputs
- **Inputs**:
  - `nums`: An array of integers.
  - `k`: The target number of odd integers in a subarray.
- **Outputs**:
  - The number of nice sub-arrays (continuous subarrays with `k` odd numbers).

#### 4. Suggested Data Structures
- **Array** or **list** to store the input array `nums`.
- **HashMap** or **dictionary** to store the prefix sum and its frequency for efficient look-up.
- **Variables** to store the current window's start and end indices, the number of odd numbers in the current window, and the count of nice sub-arrays.

## Code Review
### Code Review

#### 1. Check for bugs or logical errors

The given solution seems to be mostly correct but has a few issues. 

*   The current implementation counts all subarrays that have `k` or more odd numbers, and then subtracts the number of subarrays that have `k-1` or more odd numbers to get the number of subarrays with exactly `k` odd numbers. However, this approach is incorrect. 
*   Instead, we should count the number of subarrays that have exactly `k` odd numbers by directly checking the prefix sum of odd numbers in the array.

#### 2. Evaluate time complexity (Big O)

The time complexity of the given solution is O(n), where n is the length of the input array `nums`. This is because we are using a single loop to traverse the array.

#### 3. Evaluate space complexity (Big O)

The space complexity of the given solution is O(1), which means the space required does not change with the size of the input array, making it very space-efficient.

#### 4. Check for edge cases that are not handled

The given solution does not handle edge cases properly. For example, it does not check for an empty input array or handle the case where `k` is greater than the number of odd numbers in the array.

#### 5. Comment on code readability and style

The code is not well-structured and lacks clear comments, making it difficult to understand. The variable names are not descriptive, and the logic is not separated into clear functions.

### Improved Solution

```python
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Initialize variables
        count = 0
        prefix_sum = {0: 1}  # Initialize prefix sum dictionary
        current_sum = 0
        
        # Iterate over the array
        for num in nums:
            # Update the current sum by adding the parity of the current number
            current_sum += num % 2
            
            # If the difference between the current sum and k exists in the prefix sum dictionary,
            # it means we have found a subarray with k odd numbers
            if current_sum - k in prefix_sum:
                count += prefix_sum[current_sum - k]
            
            # Update the prefix sum dictionary
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
        
        return count
```

### Explanation of Changes

*   We use a prefix sum dictionary to store the prefix sum of odd numbers and its frequency.
*   We iterate over the array, updating the current sum by adding the parity of the current number.
*   If the difference between the current sum and `k` exists in the prefix sum dictionary, it means we have found a subarray with `k` odd numbers, so we increment the count.
*   We update the prefix sum dictionary by incrementing the count of the current sum.
*   The time complexity of this solution is O(n), where n is the length of the input array.
*   The space complexity of this solution is O(n), where n is the length of the input array. This is because in the worst case, we might need to store all prefix sums in the dictionary.

## Optimized Solution
### Optimized Solution

The optimized solution is already provided in the code review. However, I will further optimize and explain it.

```python
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Initialize variables
        count = 0
        prefix_sum = {0: 1}  # Initialize prefix sum dictionary
        current_sum = 0
        
        # Iterate over the array
        for num in nums:
            # Update the current sum by adding the parity of the current number
            current_sum += num % 2
            
            # If the difference between the current sum and k exists in the prefix sum dictionary,
            # it means we have found a subarray with k odd numbers
            if current_sum - k in prefix_sum:
                count += prefix_sum[current_sum - k]
            
            # Update the prefix sum dictionary
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
        
        return count
```

### Explanation of Optimizations

*   **Time Complexity:** The time complexity of this solution is **O(n)**, where n is the length of the input array. This is because we are iterating over the array once.
*   **Space Complexity:** The space complexity of this solution is **O(n)**, where n is the length of the input array. This is because in the worst case, we might need to store all prefix sums in the dictionary.
*   **Improved Code Structure:** The code structure has been improved by using descriptive variable names and separating the logic into clear sections.
*   **Prefix Sum Dictionary:** The prefix sum dictionary is used to store the prefix sum of odd numbers and its frequency. This allows us to efficiently check for subarrays with k odd numbers.
*   **Efficient Counting:** We are counting the number of subarrays with k odd numbers by checking the difference between the current sum and k in the prefix sum dictionary.

### Step-by-Step Walkthrough

1.  Initialize variables: We initialize the count to 0 and the prefix sum dictionary with a key of 0 and a value of 1.
2.  Iterate over the array: We iterate over the input array, updating the current sum by adding the parity of the current number.
3.  Check for subarrays with k odd numbers: We check if the difference between the current sum and k exists in the prefix sum dictionary. If it does, it means we have found a subarray with k odd numbers, so we increment the count.
4.  Update the prefix sum dictionary: We update the prefix sum dictionary by incrementing the count of the current sum.
5.  Return the count: Finally, we return the count of subarrays with k odd numbers.

### Example Use Case

*   Input: `nums = [1, 1, 2, 1, 1], k = 3`
*   Output: `2`
*   Explanation: The only sub-arrays with 3 odd numbers are `[1, 1, 2, 1]` and `[1, 2, 1, 1]`.

## Lesson & Pattern
Let's break down the problem and identify the core algorithmic pattern.

**1. Core Algorithmic Pattern:**
The core algorithmic pattern in this problem is the **Prefix Sum** technique, which is often combined with a **Hashmap** (in this case, a dictionary) to efficiently count the number of subarrays that meet a certain condition. This pattern is also closely related to the **Sliding Window** technique, as we're essentially maintaining a window of elements and adjusting its boundaries based on the condition.

**2. Why this pattern fits this problem:**
The Prefix Sum technique fits this problem because we need to count the number of subarrays with exactly `k` odd numbers. By maintaining a prefix sum of odd numbers, we can efficiently check for subarrays that meet this condition. The Hashmap allows us to store the frequency of each prefix sum, which enables us to count the number of subarrays with `k` odd numbers.

**3. Similar LeetCode problems that use the same pattern:**
Here are three similar LeetCode problems that use the same pattern:

* **523. Continuous Subarray Sum**: This problem asks you to find the number of continuous subarrays whose sum is a multiple of `k`.
* **974. Subarray Sums Divisible by K**: This problem asks you to find the number of continuous subarrays whose sum is divisible by `k`.
* **930. Binary Subarrays With Sum**: This problem asks you to find the number of binary subarrays with a given sum.

**4. Simple mental framework to recognize this pattern:**
To recognize this pattern, ask yourself:

* Do I need to count the number of subarrays or substrings that meet a certain condition?
* Can I use a prefix sum or a cumulative sum to simplify the problem?
* Is there a way to use a Hashmap or a dictionary to store the frequency of each prefix sum?

If you answer "yes" to these questions, the Prefix Sum technique might be a good fit for the problem.

**5. One key takeaway:**
One key takeaway from this problem is that the Prefix Sum technique can be combined with a Hashmap to efficiently count the number of subarrays that meet a certain condition. This technique is particularly useful when dealing with problems that involve cumulative sums or frequencies.
