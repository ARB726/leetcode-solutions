# Problem
"""
Contains Duplicate
Easy
Topics
Company Tags
Hints
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9


Topics

Recommended Time & Space Complexity

Hint 1

Hint 2
"""

# My Solution
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False