# 189 Rotate Array — Medium

## Problem
189. Rotate Array
Medium
Topics
premium lock icon
Companies
Hint
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?

## Problem Analysis
**Problem Analysis**

1. **Problem type**: Array manipulation, specifically rotation.
2. **Constraints and edge cases**:
	* Array length: 1 <= len(nums) <= 10^5
	* Array elements: -2^31 <= nums[i] <= 2^31 - 1
	* Rotation steps: 0 <= k <= 10^5
	* Edge cases: empty array, array with one element, k = 0, k >= len(nums)
3. **Inputs and outputs**:
	* Input: integer array `nums` and integer `k`
	* Output: rotated array `nums`
4. **Data structures**:
	* Python list (array) for input and output
	* Optional: temporary list or array for storing rotated elements

**Example Code**

```python
def rotate(nums: list[int], k: int) -> None:
    k %= len(nums)  # handle k >= len(nums)
    nums[:] = nums[-k:] + nums[:-k]  # rotate array in-place
```

**Additional Solutions**

To solve this problem with O(1) extra space, we can use the following approaches:

1. **Reversal algorithm**: Reverse the entire array, then reverse the first `k` elements and the remaining elements.
2. **In-place rotation**: Use a temporary variable to store the rotated elements and rotate the array in-place.

These solutions will be explored in further code examples.

## Code Review
**Code Review**

The provided code appears to be an attempt to solve the "Rotate Array" problem. However, it contains several issues:

### 1. Bugs or Logical Errors

* The current implementation does not correctly rotate the array. The line `left , right = nums[right] , nums[left]` is attempting to swap the values of `nums[left]` and `nums[right]`, but it's using the values of `nums[left]` and `nums[right]` as the new values, rather than swapping the values in the array. 
* The variables `left` and `right` are used as indices, but then reassigned to store values from the array. This will cause issues when trying to access the array using these variables.
* The loop only runs `k` times, but it doesn't actually rotate the entire array by `k` steps.

### 2. Time Complexity (Big O)

* The current implementation has a time complexity of O(k), but this is not the correct approach to solve the problem. A correct solution would involve rotating the entire array by `k` steps, which can be done in O(n) time.

### 3. Space Complexity (Big O)

* The current implementation has a space complexity of O(1) since it's only using a constant amount of extra space to store the indices and the count variable.

### 4. Edge Cases

* The current implementation does not handle edge cases where `k` is greater than the length of the array. While it might seem like it's handled due to the while loop condition, the actual rotation logic is incorrect.
* The implementation does not handle the case where the array is empty or has only one element.

### 5. Code Readability and Style

* The variable names `left` and `right` are not descriptive. Consider using `left_index` and `right_index` instead.
* The code could benefit from additional comments to explain the logic and purpose of each section.
* The code does not follow the standard naming conventions for Python. For example, `count` should be `rotation_count`.

**Corrected Solution**

Here's a corrected version of the solution using the reversal algorithm approach:
```python
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Rotate the array to the right by k steps.

        Args:
        nums (list[int]): The input array.
        k (int): The number of steps to rotate the array.
        """
        k %= len(nums)  # handle k >= len(nums)
        
        def reverse(left: int, right: int) -> None:
            """
            Reverse the elements in the array from index left to right.

            Args:
            left (int): The starting index.
            right (int): The ending index.
            """
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        # Reverse the entire array
        reverse(0, len(nums) - 1)
        
        # Reverse the first k elements
        reverse(0, k - 1)
        
        # Reverse the remaining elements
        reverse(k, len(nums) - 1)
```
This solution has a time complexity of O(n) and a space complexity of O(1), making it efficient for rotating large arrays. The code is also more readable and maintainable due to the use of descriptive variable names and comments.

## Optimized Solution
## Optimized Solution

The optimized solution for the problem "Rotate Array" can be achieved using the "Reversal algorithm" approach. This method allows us to rotate the array with O(1) extra space complexity.

### Code

```python
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Rotate the input array to the right by k steps.

        Args:
        - nums (list[int]): The input array.
        - k (int): The number of steps to rotate to the right.

        Returns:
        None
        """

        k %= len(nums)  # handle k >= len(nums)

        # Reverse the entire array
        self.reverse(nums, 0, len(nums) - 1)

        # Reverse the first k elements
        self.reverse(nums, 0, k - 1)

        # Reverse the remaining elements
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums: list[int], start: int, end: int) -> None:
        """
        Reverse the elements in the input array from start to end.

        Args:
        - nums (list[int]): The input array.
        - start (int): The starting index.
        - end (int): The ending index.

        Returns:
        None
        """

        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print("Original array:", nums)
    solution.rotate(nums, k)
    print("Rotated array:", nums)

    # Example 2
    nums = [-1, -100, 3, 99]
    k = 2
    print("Original array:", nums)
    solution.rotate(nums, k)
    print("Rotated array:", nums)
```

### Explanation

*   The `rotate` method takes an input array `nums` and an integer `k` as arguments. It first calculates the effective number of steps `k` by taking the modulus of `k` with the length of the array. This handles cases where `k` is greater than or equal to the length of the array.
*   The `reverse` method is a helper function that reverses the elements in the input array from a given start index to a given end index. It uses a simple swap technique to reverse the elements in-place.
*   The `rotate` method uses the `reverse` method to reverse the entire array, then to reverse the first `k` elements, and finally to reverse the remaining elements. This approach effectively rotates the array to the right by `k` steps.
*   The optimized solution has a time complexity of O(n), where n is the length of the input array, because each element is visited and reversed once. The space complexity is O(1), which means the solution uses a constant amount of extra space.

### Time and Space Complexity

*   Time complexity: O(n), where n is the length of the input array.
*   Space complexity: O(1), which means the solution uses a constant amount of extra space.

### Step-by-Step Walkthrough

1.  Calculate the effective number of steps `k` by taking the modulus of `k` with the length of the array.
2.  Reverse the entire array using the `reverse` method.
3.  Reverse the first `k` elements using the `reverse` method.
4.  Reverse the remaining elements using the `reverse` method.

By following these steps, the optimized solution effectively rotates the input array to the right by `k` steps while maintaining a time complexity of O(n) and a space complexity of O(1).

## Lesson & Pattern
This problem is a classic example of the **array manipulation** pattern, but more specifically, it can be solved using the **two pointers technique** or **in-place rotation**.

Let's break down why the two pointers technique or in-place rotation fit this problem:

* The problem requires rotating the array to the right by `k` steps. We can use two pointers to achieve this, one at the start of the array and one at the end. We can rotate the array by swapping elements from the end of the array with elements from the start of the array.
* Alternatively, we can use in-place rotation by shifting the elements to the right and wrapping around to the start of the array when necessary.

However, your original solution doesn't quite fit this pattern, and the optimized solution I provided earlier uses array slicing to solve the problem in a more concise and efficient way.

Here are three similar LeetCode problems that use the same pattern:

1. **LeetCode 31: Next Permutation** - This problem requires generating the next lexicographically larger permutation of a given array of integers.
2. **LeetCode 41: First Missing Positive** - This problem requires finding the first missing positive integer in a given unsorted array of integers.
3. **LeetCode 238: Product of Array Except Self** - This problem requires calculating the product of all numbers in an array except for each number at its corresponding index.

To recognize the two pointers or in-place rotation pattern in future problems, you can use the following mental framework:

* **Identify the array or sequence**: Is the problem dealing with an array or sequence of elements?
* **Look for rotation or shifting**: Is the problem requiring a rotation or shifting of elements in the array?
* **Check for constraints**: Are there any constraints on the size of the array or the number of rotations?

One key takeaway from this problem is that when dealing with array rotation or manipulation problems, it's essential to consider the **modulus of the rotation steps** (`k %= len(nums)`) to handle cases where `k` is greater than the length of the array. This ensures that we only perform the necessary rotations to achieve the desired result. 

Here is a more in-depth code example that uses the reversal algorithm to solve this problem with O(1) extra space:
```python
def rotate(nums: list[int], k: int) -> None:
    k %= len(nums)
    def reverse(left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    reverse(0, len(nums) - 1)
    reverse(0, k - 1)
    reverse(k, len(nums) - 1)
```
