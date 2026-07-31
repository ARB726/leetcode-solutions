# Subarray Sum Equals K — Medium

## Problem
Subarray Sum Equals K
Medium
Topics
Company Tags
You are given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [2,-1,1,2], k = 2

Output: 4
Explanation: [2], [2,-1,1], [-1,1,2], [2] are the subarrays whose sum is equals to k.

Example 2:

Input: nums = [4,4,4,4,4,4], k = 4

Output: 6
Constraints:

1 <= nums.length <= 20,000
-1,000 <= nums[i] <= 1,000
-10,000,000 <= k <= 10,000,000


Topics

Company Tags
Seen this question in a real interview?
Yes
No
Acceptance Rate
61.9%
Solution 1
+

NeetBot
|

Hint
|
|
Ln 23, Col 55

Ask NeetBot

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        def helperFunction(k):
            left , right , count , totalSum = 0 , 0 , 0 , 0
            if k < 0:
                return 0

            while right < len(nums):

                totalSum += nums[right]

                while totalSum > k:
                    totalSum -=nums[left]
                
                    left +=1
                count+=1
                right +=1

            return count

        
        return helperFunction(k) + helperFunction(k-1)
3456789101213141516171819201211212223
Wrong Answer


Suggest Fix
Passed test cases: 0 / 2


Input:


nums=[2,-1,1,2]
k=2
Your Output:


8
Expected output:


4


## Problem Analysis
### Problem Analysis

1. **Problem Type**: Array, Hash Table (for efficient solution)
2. **Constraints**:
   - Array length: 1 <= nums.length <= 20,000
   - Element range: -1,000 <= nums[i] <= 1,000
   - Target sum range: -10,000,000 <= k <= 10,000,000
3. **Edge Cases**:
   - Empty array (not applicable due to length constraint)
   - Array with single element
   - Array with all elements equal
   - Array with all elements less than k
   - Array with all elements greater than k
4. **Input and Output**:
   - Input: Array of integers `nums` and target sum `k`
   - Output: Total number of subarrays whose sum equals `k`
5. **Data Structures**:
   - Hash Table (e.g., dictionary in Python) for storing cumulative sum counts

### Issues with the Provided Solution

- The provided solution attempts to use a sliding window approach but does not correctly implement it for counting subarrays with sums equal to `k`.
- It incorrectly calls `helperFunction(k)` and `helperFunction(k-1)`, which suggests an attempt to account for a condition that is not relevant to the problem statement.
- The function does not utilize a hash table to store cumulative sums, which is a more efficient approach for this problem.

### Suggested Approach

- Initialize a hash table with a default value for cumulative sum 0 as 1 (since a sum of 0 can be achieved by an empty subarray, but we count it as valid because we start summing from the beginning).
- Iterate through the array, maintaining a cumulative sum.
- At each step, check if the difference between the current cumulative sum and `k` exists in the hash table. If it does, increment the count of subarrays by the value stored for that difference.
- Update the hash table with the current cumulative sum.
- Return the total count of subarrays whose sum equals `k`.

### Improved Solution

```python
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumulative_sum_count = {0: 1}  # Hash table to store cumulative sum counts
        cumulative_sum = 0  # Cumulative sum variable
        subarray_count = 0  # Count of subarrays whose sum equals k
        
        for num in nums:
            cumulative_sum += num  # Update cumulative sum
            
            # Check if the difference between current cumulative sum and k exists in the hash table
            if cumulative_sum - k in cumulative_sum_count:
                subarray_count += cumulative_sum_count[cumulative_sum - k]
            
            # Update the hash table with the current cumulative sum
            cumulative_sum_count[cumulative_sum] = cumulative_sum_count.get(cumulative_sum, 0) + 1
        
        return subarray_count
```

This approach ensures an efficient solution by utilizing a hash table to store cumulative sums and their counts, allowing for fast lookups and updates.

## Code Review
# Step-by-step analysis of the problem:
1. **Incorrect sliding window implementation**: The provided solution attempts to use a sliding window approach but does not correctly implement it for counting subarrays with sums equal to `k`. The inner while loop tries to adjust the window by moving the left pointer to the right, but it does not handle cases when the current sum is less than `k`.
2. **Unnecessary calls to `helperFunction`**: The solution incorrectly calls `helperFunction(k)` and `helperFunction(k-1)`, which suggests an attempt to account for a condition that is not relevant to the problem statement.
3. **No utilization of a hash table**: The function does not utilize a hash table to store cumulative sums, which is a more efficient approach for this problem.

# Fixed solution:
```python
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumulative_sum_count = {0: 1}  # Hash table to store cumulative sum counts
        cumulative_sum = 0  # Cumulative sum variable
        subarray_count = 0  # Count of subarrays whose sum equals k
        
        for num in nums:
            cumulative_sum += num  # Update cumulative sum
            
            # Check if the difference between current cumulative sum and k exists in the hash table
            if cumulative_sum - k in cumulative_sum_count:
                subarray_count += cumulative_sum_count[cumulative_sum - k]
            
            # Update the hash table with the current cumulative sum
            cumulative_sum_count[cumulative_sum] = cumulative_sum_count.get(cumulative_sum, 0) + 1
        
        return subarray_count
```

# Explanation of changes:
*   Replaced the original solution with a new approach that utilizes a hash table to store cumulative sums and their counts.
*   Removed unnecessary calls to `helperFunction` and instead used a single loop to iterate through the array.
*   Added a hash table `cumulative_sum_count` to store cumulative sums and their counts.
*   Updated the solution to correctly count subarrays whose sum equals `k` by checking if the difference between the current cumulative sum and `k` exists in the hash table.

# Tests and example uses:
```python
solution = Solution()
print(solution.subarraySum([1, 1, 1], 2))  # Output: 2
print(solution.subarraySum([1, 2, 3], 3))  # Output: 2
print(solution.subarraySum([2, -1, 1, 2], 2))  # Output: 4
```

# Time complexity:
The time complexity of the improved solution is **O(n)**, where n is the length of the input array, since it involves a single pass through the array.

# Space complexity:
The space complexity of the improved solution is **O(n)**, where n is the length of the input array, since in the worst case, the hash table can store cumulative sums for each prefix of the array.

## Optimized Solution
**Optimized Solution:**
The provided improved solution is already optimized for this problem.

```python
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumulative_sum_count = {0: 1}  # Hash table to store cumulative sum counts
        cumulative_sum = 0  # Cumulative sum variable
        subarray_count = 0  # Count of subarrays whose sum equals k
        
        for num in nums:
            cumulative_sum += num  # Update cumulative sum
            
            # Check if the difference between current cumulative sum and k exists in the hash table
            if cumulative_sum - k in cumulative_sum_count:
                subarray_count += cumulative_sum_count[cumulative_sum - k]
            
            # Update the hash table with the current cumulative sum
            cumulative_sum_count[cumulative_sum] = cumulative_sum_count.get(cumulative_sum, 0) + 1
        
        return subarray_count
```

**Why it is faster or more efficient:**

1. **Hash Table Usage**: The solution uses a hash table to store cumulative sums, allowing for efficient lookups and updates. This reduces the time complexity compared to other approaches without hash tables.
2. **Single Pass Through Array**: The algorithm only requires a single pass through the input array, processing each element once. This minimizes the number of operations and makes the solution more efficient.

**Improved Time and Space Complexity:**

* **Time Complexity**: O(n), where n is the length of the input array `nums`. This is because the algorithm processes each element in the array once.
* **Space Complexity**: O(n), as in the worst-case scenario, the hash table may store cumulative sums for each prefix of the input array.

**Step-by-Step Walkthrough:**

1. Initialize a hash table `cumulative_sum_count` with a default value for cumulative sum 0 as 1.
2. Initialize variables `cumulative_sum` to 0 and `subarray_count` to 0.
3. Iterate through each element `num` in the input array `nums`.
4. Update the `cumulative_sum` by adding the current element `num`.
5. Check if the difference between the current `cumulative_sum` and `k` exists in the hash table. If it does, increment `subarray_count` by the value stored for that difference.
6. Update the hash table with the current `cumulative_sum`.
7. After iterating through all elements, return the `subarray_count`, which represents the total number of subarrays whose sum equals `k`.

This optimized solution efficiently solves the problem by utilizing a hash table to store cumulative sums and their counts, allowing for fast lookups and updates.

## Lesson & Pattern
Let's break down the problem and its solution to identify the underlying pattern.

**1. Core Algorithmic Pattern:**
The problem can be solved using a technique that involves maintaining a **Prefix Sum** or **Cumulative Sum**, in combination with a **Hash Table**. This approach allows for efficient counting of subarrays with sums equal to `k`.

**2. Why this pattern fits this problem:**
The pattern fits this problem because it enables us to:
	* Calculate the cumulative sum of elements up to each index.
	* Store the cumulative sums in a hash table and their counts.
	* When calculating the cumulative sum at each step, we can quickly check if the difference between the current cumulative sum and `k` exists in the hash table.
	* If it does, we increment the count of subarrays whose sum equals `k` by the value stored for that difference in the hash table.

**3. Similar LeetCode problems that use the same pattern:**
Here are three similar LeetCode problems that use the same pattern:
	* **Continuous Subarray Sum** (523): This problem asks you to find the length of the longest subarray where the sum of any subarray is a multiple of `k`.
	* **Subarray Product Less Than K** (713): This problem requires finding the number of contiguous subarrays whose product is less than `k`.
	* **Binary Subarrays With Sum** (1124): This problem asks you to find the number of subarrays whose sum is equal to a given target value, with the constraint that each subarray can only contain binary digits (0s and 1s).

**4. Mental framework to recognize this pattern:**
When encountering problems that involve:
	+ Arrays or sequences.
	+ Sums or products of subarrays.
	+ Constraints on the sum or product (e.g., equal to `k`, less than `k`, or a multiple of `k`).
	+ The need to count or find subarrays that satisfy certain conditions.
Consider using a prefix sum or cumulative sum approach, combined with a hash table to store intermediate results.

**5. Key takeaway:**
Remember that when dealing with array problems involving sums or products of subarrays, a prefix sum or cumulative sum approach can often be useful. Additionally, using a hash table to store intermediate results can significantly improve the efficiency of your solution. This pattern can be applied to a wide range of problems, so it's essential to recognize when it can be used and to practice implementing it efficiently.
