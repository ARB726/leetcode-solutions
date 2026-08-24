# Problem
"""
Find the Duplicate Number
Medium
Topics
Company Tags
Hints
You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.

There is exactly one repeated integer in nums, and every other integer appears at most once.

Return the repeated integer.

Example 1:

Input: nums = [1,2,3,2,2]

Output: 2
Example 2:

Input: nums = [1,2,3,4,4]

Output: 4
Follow-up: Can you solve the problem without modifying the array nums and using 
O
(
1
)
O(1) extra space?

Constraints:

1 <= n <= 10,000
nums.length == n + 1
1 <= nums[i] <= n


Topics

Recommended Time & Space Complexity

Hint 1

Hint 2

Hint 3

Hint 4

Company Tags
Seen this question in a real interview?
Yes
No
Acceptance Rate
66.2%
Solution 1
+

NeetBot
|

Hint
|
|
Ln 20, Col 1

Ask NeetBot

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = nums[0]
        right = nums[0]

        while True:
            left = nums[left] # to iterate through the linked list
            right = nums[nums[right]]

            if left == right: break

        left = nums[0]

        while left != right:
            left = nums[left]
            right = nums[right]

        return left


1234567891011121314151617
Accepted

Passed test cases: 79 / 79


Visualize code
You have successfully completed this problem!


"""

# My Solution
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = nums[0]
        right = nums[0]

        while True:
            left = nums[left] # to iterate through the linked list
            right = nums[nums[right]]

            if left == right: break

        left = nums[0]

        while left != right:
            left = nums[left]
            right = nums[right]

        return left

