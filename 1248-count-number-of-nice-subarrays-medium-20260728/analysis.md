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

* **Problem Type:** Array
* **Constraints and Edge Cases:**
	+ Array length: 1 <= nums.length <= 50000
	+ Element value: 1 <= nums[i] <= 10^5
	+ k value: 1 <= k <= nums.length
	+ Edge cases: empty array, single-element array, k equals the number of odd elements
* **Inputs and Outputs:**
	+ Input: array of integers `nums`, integer `k`
	+ Output: integer representing the number of nice sub-arrays
* **Best Data Structures to Use:**
	+ Prefix sum array or hashmap to store the cumulative sum of odd numbers
	+ Sliding window technique to efficiently traverse the array
	+ Possible use of a counter or a variable to store the count of nice sub-arrays

This problem can be solved using a prefix sum array and the sliding window technique, with a time complexity of O(n) and a space complexity of O(n). The prefix sum array will help to efficiently calculate the number of odd elements in each sub-array.

## Code Review
### Code Review

I'd be happy to help you review your solution. However, you didn't provide the solution code. Please provide the code, and I'll be able to review it based on the following criteria:

1. **Bugs or Logical Errors**: I will check if the code is free from bugs and logical errors.
2. **Time Complexity (Big O)**: I will evaluate the time complexity of the code.
3. **Space Complexity (Big O)**: I will evaluate the space complexity of the code.
4. **Edge Cases**: I will check if the code handles edge cases correctly.
5. **Code Readability and Style**: I will comment on the readability and style of the code.

Please provide the solution code, and I'll proceed with the review.

If you'd like, I can also provide a sample solution to the problem. Here's a sample solution in Python:

```python
def numberOfSubarrays(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # Initialize the count of odd numbers and the result
    odd_count = 0
    result = 0
    
    # Initialize the hashmap to store the prefix sums
    prefix_sum = {0: 1}
    
    # Iterate over the array
    for num in nums:
        # Check if the number is odd
        if num % 2 != 0:
            odd_count += 1
        
        # Update the result using the hashmap
        result += prefix_sum.get(odd_count - k, 0)
        
        # Update the hashmap
        prefix_sum[odd_count] = prefix_sum.get(odd_count, 0) + 1
    
    return result
```

This solution uses a hashmap to store the prefix sums of odd numbers and updates the result by looking up the hashmap. The time complexity is O(n), and the space complexity is O(n).

Please provide your solution code for a more accurate review.

## Optimized Solution
**Optimized Solution**

We can use a hashmap to store the cumulative sum of odd numbers. The cumulative sum is calculated as we traverse the array. We initialize a variable `count` to store the number of nice sub-arrays.

```python
from collections import defaultdict

def numberOfSubarrays(nums, k):
    prefix_sum = 0
    count = 0
    hashmap = defaultdict(int)
    hashmap[0] = 1

    for num in nums:
        if num % 2 != 0:
            prefix_sum += 1
        if prefix_sum - k in hashmap:
            count += hashmap[prefix_sum - k]
        hashmap[prefix_sum] += 1

    return count
```

**Explanation of Optimizations**

1.  **Use of Hashmap:** We use a hashmap to store the cumulative sum of odd numbers. This allows us to efficiently look up the number of sub-arrays with a specific number of odd elements.
2.  **Prefix Sum Calculation:** We calculate the prefix sum as we traverse the array, which avoids the need to recalculate the sum for each sub-array.
3.  **Sliding Window Technique:** We use a sliding window technique to efficiently traverse the array. This is achieved by only considering the current element when updating the prefix sum and the hashmap.

**Time and Space Complexity**

*   **Time Complexity:** The optimized solution has a time complexity of **O(n)**, where n is the length of the input array. This is because we traverse the array once and perform constant-time operations for each element.
*   **Space Complexity:** The optimized solution has a space complexity of **O(n)**, where n is the length of the input array. This is because we use a hashmap to store the cumulative sum of odd numbers, which can have up to n entries in the worst case.

**Walkthrough of Optimized Code**

1.  Initialize a variable `prefix_sum` to store the cumulative sum of odd numbers.
2.  Initialize a variable `count` to store the number of nice sub-arrays.
3.  Create a hashmap to store the cumulative sum of odd numbers.
4.  Initialize the hashmap with a key-value pair `(0, 1)`, which represents the base case where the prefix sum is 0.
5.  Traverse the input array `nums`. For each element:
    *   If the element is odd (i.e., `num % 2 != 0`), increment the `prefix_sum`.
    *   If the difference between the current `prefix_sum` and `k` exists in the hashmap, increment the `count` by the value associated with that key in the hashmap.
    *   Increment the value associated with the current `prefix_sum` in the hashmap.
6.  Return the `count`, which represents the number of nice sub-arrays.

**Example Usage**

```python
nums = [1, 1, 2, 1, 1]
k = 3
result = numberOfSubarrays(nums, k)
print(result)  # Output: 2

nums = [2, 4, 6]
k = 1
result = numberOfSubarrays(nums, k)
print(result)  # Output: 0

nums = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
k = 2
result = numberOfSubarrays(nums, k)
print(result)  # Output: 16
```

## Lesson & Pattern
I'm glad you're interested in learning from this problem. Let's break it down together.

**1. Core algorithmic pattern:** 
The core pattern here is the **AtMost/AtLeast K** problem, which is a variation of the **Sliding Window** technique. In this case, we're using a **Prefix Sum Array** (or a HashMap) to store the cumulative sum of odd numbers, and then applying the sliding window approach to count the number of sub-arrays with exactly `k` odd numbers.

**2. Why this pattern fits this problem:**
This pattern fits because we need to efficiently count the number of sub-arrays with a specific property (having `k` odd numbers). By using a prefix sum array, we can quickly calculate the number of odd numbers in each sub-array, and then use the sliding window technique to iterate over all possible sub-arrays. This approach allows us to avoid redundant calculations and reduce the time complexity to O(n).

**3. Similar LeetCode problems:**
Here are three similar problems that use the same pattern:
* **904. Fruit Into Baskets**: In this problem, we need to find the maximum number of fruits we can collect in a basket, given that we can only collect at most two types of fruits at a time.
* **1004. Max Consecutive Ones III**: In this problem, we need to find the maximum length of a sub-array that can be obtained by flipping at most `k` zeros to ones.
* **1151. Minimum Swaps to Group All 1s Together**: In this problem, we need to find the minimum number of swaps required to group all ones together in a binary array.

**4. Mental framework:**
To recognize this pattern in future problems, ask yourself:
* Is the problem asking me to count or find the maximum/minimum of something?
* Is there a specific property or constraint that I need to satisfy (e.g., having `k` odd numbers)?
* Can I use a prefix sum array or a HashMap to efficiently calculate the property I'm interested in?
* Can I apply a sliding window technique to iterate over all possible sub-arrays?

**5. Key takeaway:**
Remember that the AtMost/AtLeast K pattern is a powerful tool for solving problems that involve counting or finding the maximum/minimum of something with a specific property. By recognizing this pattern, you can apply a systematic approach to solve problems efficiently. 

So, how do you feel about this problem now? Do you have any questions or would you like me to elaborate on any of the points I mentioned?
