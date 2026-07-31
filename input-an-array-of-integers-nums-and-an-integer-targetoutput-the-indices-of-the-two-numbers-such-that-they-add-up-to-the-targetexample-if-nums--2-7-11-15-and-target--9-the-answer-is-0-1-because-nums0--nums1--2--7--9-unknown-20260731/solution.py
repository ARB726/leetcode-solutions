# Problem
"""
Input: An array of integers nums and an integer target.Output: The indices of the two numbers such that they add up to the target.Example: If nums = [2, 7, 11, 15] and target = 9, the answer is [0, 1] because nums[0] + nums[1] == 2 + 7 == 9.
"""

# My Solution
def twoSum(nums, target):
2
seen = {}
3
 
4
for i, num in enumerate(nums):
5
complement = target - num
6
 
7
if complement in seen:
8
return [seen[complement], i]
9
 
10
seen[num] = i