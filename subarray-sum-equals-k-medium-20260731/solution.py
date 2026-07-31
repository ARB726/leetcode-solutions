# Problem
"""
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

"""

# My Solution
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