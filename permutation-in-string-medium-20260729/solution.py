# Problem
"""
Permutation in String
Medium
Topics
Company Tags
Hints
You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

Example 1:

Input: s1 = "abc", s2 = "lecabee"

Output: true
Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

Example 2:

Input: s1 = "abc", s2 = "lecaabee"

Output: false
Constraints:

1 <= s1.length, s2.length <= 1000


Topics

Recommended Time & Space Complexity

Hint 1
"""

# My Solution
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1) -1
        hashMap = {}

        for char in range(len(s1)):

            hashMap[s1[char]] = hashMap.get(s1[char] , 0) + 1

        
        while right < len(s2):

            while right - left + 1 > len(s1):
                if s2[left] in hashMap:
                    hashMap[s2[left]] -= 1

                    if hashMap[s2[left]] == 0:
                        del hashMap[s2[left]]

                    left +=1
                
                else:
                    left = right + 1

            
            right +=1

        
        if len(hashMap) == 0:
            return True

        else:
            return False