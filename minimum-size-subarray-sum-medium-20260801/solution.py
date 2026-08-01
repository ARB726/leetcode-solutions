# Problem
"""
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


"""

# My Solution
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left , right , totalSums , minSize = 0 , 0 , 0 , float('inf')

        while right < len(nums):

            totalSums += nums[right]

            while totalSums >= target:

                totalSums -=nums[left]

                minSize = min(minSize , right - left +1)
                left +=1

            


            right +=1
        return 0 if isinstance(minSize , float) else minSize