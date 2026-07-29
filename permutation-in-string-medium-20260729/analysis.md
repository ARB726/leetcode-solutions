# Permutation In String — Medium

## Problem
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

## Problem Analysis
**Problem Analysis**

1. **Problem Type**: String, Sliding Window
2. **Constraints and Edge Cases**:
	* Both strings contain only lowercase letters.
	* 1 <= s1.length, s2.length <= 1000
	* s1.length can be greater than s2.length
	* Empty strings are not considered
3. **Inputs and Outputs**:
	* Inputs: Two strings s1 and s2
	* Output: Boolean value indicating whether s2 contains a permutation of s1
4. **Recommended Data Structures**:
	* Hash Map (or Dictionary) to store character frequencies
	* Sliding Window technique to iterate over s2

This problem can be solved using a sliding window approach with a hash map to keep track of character frequencies in s1 and the current window of s2.

## Code Review
**Code Review**

**Overview**

The solution attempts to solve the "Permutation in String" problem using a sliding window approach with a hash map to track character frequencies. However, there are several issues with the implementation that need to be addressed.

**Bugs and Logical Errors**

1. The `right` variable is initialized to `len(s1) - 1`, but it should be initialized to `0` to start scanning `s2` from the beginning.
2. The `while` loop condition `right < len(s2)` is not sufficient, as we need to ensure that the window size is at least as large as `s1`.
3. Inside the `while` loop, the `if` statement checks if `s2[left]` is in `hashMap`, but it should be checking `s1[char]`.
4. The `if len(hashMap) == 0:` statement is not correct. We need to compare the character frequencies in `s1` and the current window of `s2`, not just check if `hashMap` is empty.
5. The solution does not correctly implement the sliding window approach. It should be expanding the window to the right and then shrinking it from the left when the window size exceeds `len(s1)`.

**Time Complexity**

The time complexity of the solution is O(n), where n is the length of `s2`. However, due to the incorrect implementation, the solution does not achieve this time complexity.

**Space Complexity**

The space complexity of the solution is O(n), where n is the length of `s1`. This is because we are using a hash map to store the character frequencies of `s1`.

**Edge Cases**

1. The solution does not handle the case where `s1` is longer than `s2`. We need to add a check at the beginning of the function to return `False` if `s1` is longer than `s2`.

**Code Readability and Style**

1. The variable names could be more descriptive. For example, `left` and `right` could be renamed to `window_start` and `window_end`.
2. The solution could benefit from more comments to explain the logic and algorithms used.

**Refactored Solution**

Here is a refactored version of the solution that addresses the issues mentioned above:
```python
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)
        window_count = Counter()

        window_start = 0
        for window_end in range(len(s2)):
            window_count[s2[window_end]] += 1

            if window_end >= len(s1) - 1:
                if window_count == s1_count:
                    return True
                window_count[s2[window_start]] -= 1
                if window_count[s2[window_start]] == 0:
                    del window_count[s2[window_start]]
                window_start += 1

        return False
```
This solution uses a sliding window approach with a hash map to track character frequencies. It correctly expands the window to the right and shrinks it from the left when the window size exceeds `len(s1)`. It also checks for the case where `s1` is longer than `s2` and returns `False` in that case.

## Optimized Solution
### Optimized Solution
The original solution has some issues, such as not correctly implementing the sliding window approach and not handling the window expansion correctly. Here's an optimized solution:

```python
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)
        window_count = Counter(s2[:len(s1)])

        if s1_count == window_count:
            return True

        for i in range(len(s1), len(s2)):
            window_count[s2[i]] += 1
            window_count[s2[i - len(s1)]] -= 1
            if window_count[s2[i - len(s1)]] == 0:
                del window_count[s2[i - len(s1)]]
            if s1_count == window_count:
                return True

        return False
```

### Explanation

*   We use the `Counter` class from the `collections` module to create two hash maps: `s1_count` to store the character frequencies of `s1` and `window_count` to store the character frequencies of the current window in `s2`.
*   We initialize the `window_count` with the first `len(s1)` characters of `s2`.
*   We then slide the window to the right by incrementing the count of the new character and decrementing the count of the character that is going out of the window.
*   If the `window_count` is equal to `s1_count` at any point, we return `True`.
*   If the loop completes without finding a match, we return `False`.

### Time and Space Complexity

*   **Time Complexity:** O(n + m), where n is the length of `s1` and m is the length of `s2`. This is because we are iterating over `s2` once.
*   **Space Complexity:** O(n), where n is the length of `s1`. This is because we are storing the character frequencies of `s1` and the current window in two hash maps.

### Step-by-Step Walkthrough

1.  We create two hash maps: `s1_count` to store the character frequencies of `s1` and `window_count` to store the character frequencies of the current window in `s2`.
2.  We initialize the `window_count` with the first `len(s1)` characters of `s2`.
3.  We then slide the window to the right by incrementing the count of the new character and decrementing the count of the character that is going out of the window.
4.  At each step, we check if the `window_count` is equal to `s1_count`. If it is, we return `True`.
5.  If the loop completes without finding a match, we return `False`.

### Example Usage

```python
solution = Solution()
print(solution.checkInclusion("abc", "lecabee"))  # Output: True
print(solution.checkInclusion("abc", "lecaabee"))  # Output: False
```

This optimized solution correctly implements the sliding window approach and uses hash maps to efficiently track character frequencies. It has a time complexity of O(n + m) and a space complexity of O(n), making it suitable for large inputs.

## Lesson & Pattern
Let's break it down together.

**Core Algorithmic Pattern:**
The core pattern here is the **Sliding Window** technique, combined with a **Hash Map** to store character frequencies. This pattern is particularly useful for string problems that involve checking substrings or subarrays for certain conditions.

**Why does this pattern fit this problem?**
The sliding window technique fits this problem because we need to check all substrings of `s2` that have the same length as `s1`. By using a sliding window, we can efficiently iterate over `s2` and check each substring of the same length as `s2`. The hash map helps us keep track of the character frequencies in `s1` and the current window of `s2`, allowing us to quickly determine if the current window is a permutation of `s1`.

**Similar LeetCode Problems:**

1. **Longest Substring with K Distinct Characters**: This problem uses the sliding window technique with a hash map to find the longest substring with a maximum of `k` distinct characters.
2. **Minimum Window Substring**: This problem uses the sliding window technique with a hash map to find the minimum window that contains all characters of a given string.
3. **Subarray Sum Equals K**: This problem uses the sliding window technique with a hash map to find the number of subarrays that sum up to a given value `k`.

**Mental Framework:**
To recognize the sliding window pattern, ask yourself:

* Am I dealing with a string or array problem?
* Do I need to check substrings or subarrays for certain conditions?
* Can I use a hash map to store frequencies or keep track of certain elements?

If you answer "yes" to these questions, the sliding window technique with a hash map might be a good fit for the problem.

**Key Takeaway:**
Remember that the sliding window technique is all about efficiently iterating over a string or array and checking substrings or subarrays for certain conditions. By combining it with a hash map, you can solve a wide range of problems involving strings and arrays. Practice using this technique, and you'll become more comfortable recognizing when to apply it to solve problems.

Now, let's take a closer look at your solution. There are some improvements that can be made to make it more efficient and easier to understand. Would you like me to walk you through the optimized solution?
