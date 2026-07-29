# Problem
"""
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

"""

# My Solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        maxCount = 0
        if len(nums) == 0:
            return 0
        for i in range(len(nums)-1):

            if nums[i] + 1 == nums[i+1]:
                count +=1

        return count