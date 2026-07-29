# Problem
"""
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
"""

# My Solution
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        def helperFunction(k):
            if k < 0:
                return 0

            left , right , count , windowSum = 0 , 0 , 0 , 0 

            while right < len(nums):

                windowSum += nums[right] % 2

                while windowSum > k:

                    windowSum -= nums[left]  % 2

                    left +=1
                


                count = count +( right - left + 1)

                right +=1

            
            return count

        
        return helperFunction(k) - helperFunction(k-1)