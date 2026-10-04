# 219 Contains Duplicate Ii — Easy

## Problem
219. Contains Duplicate II
Solved
Easy
Topics
conpanies icon
Companies
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105

## Problem Analysis
**1. Problem type**  
- **Category:** Array + Hashing (sliding‑window)  
- **Core technique:** Keep track of the last *k* elements (or the most recent index of each value) and check for a repeat within that distance.  

---

**2. Constraints & important edge cases**

| Constraint | Why it matters |
|------------|----------------|
| `1 ≤ nums.length ≤ 10⁵` | Linear‑time (`O(n)`) is required; anything worse will TLE. |
| `-10⁹ ≤ nums[i] ≤ 10⁹` | Values can be negative; use a hash‑based container, not a direct‑address array. |
| `0 ≤ k ≤ 10⁵` | `k = 0` means “no two distinct indices can be within distance 0”, so answer is always `False`. |
| `k` may be larger than `len(nums)` | Effectively the whole array is the window; still `O(n)` works. |

**Edge‑case checklist**

1. **Single element** → always `False`.
2. **`k == 0`** → immediate `False`.
3. **All elements equal** → `True` if `k >= 1`.
4. **Duplicates exist but farther than `k`** → must return `False`.
5. **Negative numbers / large magnitude** → hash structures handle them automatically.
6. **Maximum size (`10⁵`) with large `k`** → keep memory to `O(k)` (or `O(distinct values)`).

---

**3. Input / Output**

```python
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    ...
```

- **Input**  
  - `nums`: `List[int]` – the integer array.  
  - `k`: `int` – maximum allowed index distance.

- **Output**  
  - `bool` – `True` if any two distinct indices `i, j` satisfy `nums[i] == nums[j]` **and** `abs(i - j) <= k`; otherwise `False`.

---

**4. Best data structures**

| Goal | Recommended structure | Reason |
|------|-----------------------|--------|
| **O(1) membership test for recent values** | `set` (hash set) | `x in s` is amortized `O(1)`. |
| **Remember the index of the last occurrence** | `dict[int, int]` (value → last index) | Allows direct distance check without sliding‑window eviction. |
| **Sliding window of size `k`** | `set` + simple `pop` of the element that leaves the window (`nums[i‑k]`) | Guarantees the set never holds more than `k` items → `O(k)` space. |

Both approaches are `O(n)` time, `O(min(k, n))` space. The dictionary version is slightly simpler to code, while the sliding‑window set version uses exactly `k` memory.

---

### Quick Python illustration (dictionary version)

```python
from typing import List

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    last_index = {}                     # value -> most recent index
    for i, v in enumerate(nums):
        if v in last_index and i - last_index[v] <= k:
            return True
        last_index[v] = i               # update last seen position
    return False
```

**Complexities**  
- **Time:** `O(n)` – one pass through `nums`.  
- **Space:** `O(min(n, distinct values))` (≤ `O(n)`, often ≤ `O(k)` if using the sliding‑window set).

---

**Summary**  
- Treat the problem as “detect a duplicate within a moving window of size `k`”.  
- Use a hash‑based container (`set` or `dict`) to achieve constant‑time checks.  
- Guard against `k == 0` and very small arrays early for a tiny constant‑time win.

## Code Review
**Code under review**

```python
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        left = 0
        seen = set()

        for right in range(len(nums)):

            if right - left > k:
                seen.remove(nums[left])
                left += 1

            if nums[right] in seen:
                return True

            seen.add(nums[right])

        return False
```

---

## 1. Correctness / Logical bugs  

| Situation | What the code does | Expected result | Verdict |
|-----------|-------------------|----------------|---------|
| Normal case (`k > 0`) | Maintains a sliding window of at most `k` indices (`left … right‑1`) in `seen`. When the window would become larger than `k`, the left‑most element is evicted before the new element is examined. | Detects a duplicate **inside** the window → `True`. | ✅ Correct |
| `k == 0` | The condition `right - left > k` is true as soon as `right` moves to the next index, so the element that just entered the set is immediately removed. No two distinct indices can ever be in the set together, therefore the method never returns `True`. | Should always be `False`. | ✅ Correct |
| `k` larger than `len(nums)` | The eviction branch never executes, so `seen` may grow to `len(nums)`. The algorithm still checks every new element against all previously‑seen ones, which is exactly what the problem asks for when the window is “the whole array”. | Correct result, but uses `O(n)` space (which is unavoidable when `k ≥ n`). | ✅ Correct |
| Duplicate values that are farther apart than `k` | When the distance exceeds `k`, the older occurrence is removed from the set before the newer one is examined, so the later duplicate will not see the earlier one. | Should return `False`. | ✅ Correct |
| Empty `nums` (not allowed by constraints) | The loop never runs, returns `False`. | Not required, but harmless. | ✅ Correct |

**No logical bugs were found.** The sliding‑window invariant (`seen` contains exactly the values whose indices lie in `[right‑k, right‑1]`) is maintained correctly.

---

## 2. Time Complexity  

* The loop iterates once per element → **`O(n)`** where `n = len(nums)`.  
* Each iteration performs at most one `set.__contains__`, one `set.add`, and (occasionally) one `set.remove`. All are *amortised* `O(1)`.  

Overall: **`O(n)` time**.

---

## 3. Space Complexity  

* The set never holds more than `k + 1` elements (the current window plus the element about to be added).  
* In the worst case `k ≥ n`, the set can hold all distinct values → `O(n)`.

Hence **`O(min(k, n))`** auxiliary space, which matches the optimal solution.

---

## 4. Edge‑case handling  

| Edge case | Handled? | Comments |
|-----------|----------|----------|
| `k == 0` | Yes (implicit). Could be made explicit for readability. |
| `k` larger than array length | Yes (window never shrinks). |
| All numbers identical | Returns `True` as soon as the second element is processed (provided `k ≥ 1`). |
| Single‑element array | Returns `False` (no pair exists). |
| Negative numbers / large magnitude | No problem – they are hashable. |
| Invalid `k` (<0) | Not required by problem constraints; the code would raise a `KeyError` when trying to `remove` an element that was never added. Adding a guard (`if k < 0: return False`) could make the function more robust for misuse. |

---

## 5. Readability & Style  

| Aspect | Observations | Suggestions |
|--------|--------------|-------------|
| **Naming** | `left` / `right` are clear for a sliding window. `seen` accurately describes the container. | Good. |
| **Type hints** | Only the `nums` parameter is typed (`list[int]`). The method itself could be annotated (`-> bool`). | Add `from typing import List` and use `List[int]` for consistency with typical LeetCode signatures. |
| **Docstring** | None. | A short docstring explaining the algorithm would aid future readers. |
| **Blank lines** | There is an empty line after the `for` line that isn’t needed. | Remove the extra blank line for tighter formatting. |
| **Guard for `k == 0`** | Not required for correctness but makes intent explicit. | ```python\nif k == 0:\n    return False\n``` |
| **Error handling** | `seen.remove` will raise a `KeyError` if, for any reason, the element isn’t in the set. With the current invariant that never happens, but using `discard` is safer. | Replace `seen.remove(nums[left])` with `seen.discard(nums[left])`. |
| **Overall style** | Conforms to PEP‑8 (indentation, spacing). | Minor cosmetic tweaks only. |

---

## 6. Revised version (optional)

```python
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Return True if there exist i != j such that nums[i] == nums[j] and
        |i - j| <= k.  Uses a sliding window of size k+1 stored in a hash set.
        """
        if k == 0:                 # early‑exit for the degenerate case
            return False

        left = 0
        window: set[int] = set()   # values whose indices are in [left, right-1]

        for right, val in enumerate(nums):
            # Keep window size <= k
            if right - left > k:
                window.discard(nums[left])
                left += 1

            if val in window:      # duplicate found inside the window
                return True

            window.add(val)

        return False
```

The revised code is functionally identical, but:

* adds a docstring,
* uses `List[int]` for the public signature,
* guards the trivial `k == 0` case,
* uses `discard` (safer than `remove`),
* iterates with `enumerate` for clarity.

---

### Bottom line
Your original implementation is **correct**, runs in optimal `O(n)` time and `O(min(k, n))` space, and gracefully handles all required edge cases. Minor readability and defensive‑coding improvements (docstring, early‑exit for `k == 0`, `discard` instead of `remove`) would make the solution even cleaner, but they are not required for correctness. Great job!

## Optimized Solution
**Solution Overview**

The task is to decide whether the same value appears twice **close enough** – i.e. the distance between the two indices is at most `k`.

The optimal strategy is a single linear scan while remembering, for every value we have seen, the **most recent index** where it occurred.  
When we encounter a value again we can instantly compute the distance to its previous occurrence and answer `True` if the distance ≤ `k`.

This needs only constant‑time hash‑look‑ups, so the overall complexity is `O(n)` time and `O(min(k, n))` extra space (the hash table never stores more than the last `k` positions, because older positions are useless for the distance test).

---

## 1️⃣  Optimized Code (Python)

```python
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Edge case: k == 0 → no two *distinct* indices can satisfy the condition
        if k == 0:
            return False

        last_pos: dict[int, int] = {}          # value -> most recent index

        for i, v in enumerate(nums):
            # If we have seen `v` before, check the distance to the latest occurrence
            if v in last_pos and i - last_pos[v] <= k:
                return True

            # Record (or update) the latest index of `v`
            last_pos[v] = i

            # Optional micro‑optimisation: keep the dictionary size bounded by k
            # (only needed when `k` << number of distinct values)
            if len(last_pos) > k:
                # Find the element whose index is `i - k` and delete it.
                # Because we only store the *most recent* index for each value,
                # the element that left the window is exactly nums[i - k].
                # This deletion is O(1) on average.
                old_val = nums[i - k]
                # Delete only if the stored index really points to the element that is sliding out.
                if last_pos.get(old_val) == i - k:
                    del last_pos[old_val]

        return False
```

### Why this version is *better* (or equally good)

| Aspect | Original (sliding‑window set) | Optimised (dictionary) |
|--------|------------------------------|------------------------|
| **Readability** | Uses two pointers (`left`, `right`) and a `set`. The eviction logic is a little indirect (`seen.remove(nums[left])`). | Directly records the *last* index of each value; the check is a one‑liner. |
| **Constant‑factor speed** | For each step we may do `set.__contains__`, `set.add`, and occasionally `set.remove`. | One dictionary lookup + one assignment per element; the optional eviction is also a dictionary operation. In practice the dict version is a tiny bit faster. |
| **Space usage** | Stores at most `k` elements in the set → `O(k)`. | Stores at most `k` *key → index* pairs (same order of magnitude). |
| **Correctness on all inputs** | Handles everything, but needs the `left` pointer dance. | Handles everything, plus an early‑return for `k == 0`. |

Both algorithms are already **optimal** (linear time, linear‑in‑`k` space). The dictionary version simply expresses the same idea more compactly and can be marginally faster because it avoids the extra `left` pointer and the `remove` call when the window slides.

---

## 2️⃣  Complexity Analysis  

| Metric | Explanation |
|--------|-------------|
| **Time** | The loop runs once per element (`n = len(nums)`). All operations inside the loop (`in`, assignment, optional deletion) are *amortized* `O(1)`. → **`O(n)`**. |
| **Space** | The hash table holds at most one entry per distinct value that appears in the last `k` positions. → **`O(min(k, n))`** (worst‑case `O(k)`). |

---

## 3️⃣  Step‑by‑Step Walk‑through  

Consider `nums = [1, 2, 3, 1]`, `k = 3`.

| i | v | `last_pos` before processing | Condition `v in last_pos and i - last_pos[v] <= k`? | Action |
|---|---|-----------------------------|---------------------------------------------------|--------|
| 0 | 1 | `{}` | `False` (1 not seen) | `last_pos[1] = 0` → `{1:0}` |
| 1 | 2 | `{1:0}` | `False` | `last_pos[2] = 1` → `{1:0, 2:1}` |
| 2 | 3 | `{1:0,2:1}` | `False` | `last_pos[3] = 2` → `{1:0,2:1,3:2}` |
| 3 | 1 | `{1:0,2:1,3:2}` | `True` because `3 - 0 = 3 ≤ k` | **return `True`** |

The algorithm stops as soon as a qualifying duplicate is found.

---

### When `k` is much smaller than the number of distinct values  

Suppose `k = 2` and the stream is `[5,6,5,7,6]`.

| i | v | `last_pos` after update | Eviction check (`len(last_pos) > k`) |
|---|---|------------------------|--------------------------------------|
|0|5|`{5:0}`|skip|
|1|6|`{5:0,6:1}`|skip|
|2|5|`{5:2,6:1}`|size = 2 ≤ k → no eviction|
|3|7|`{5:2,6:1,7:3}`|size = 3 > k → evict `nums[3‑2] = nums[1] = 6`. Since `last_pos[6]==1`, delete it → `{5:2,7:3}`|
|4|6|`{5:2,7:3,6:4}`|size = 3 > k → evict `nums[4‑2] = nums[2] = 5`. `last_pos[5]==2`, delete → `{7:3,6:4}`|

At any moment the dictionary contains only elements that are still within distance `k` of the current index, guaranteeing the space bound.

---

## 4️⃣  Final Remarks  

* The problem **cannot be solved faster than linear time** because every element must be examined at least once (otherwise a duplicate could be missed).  
* The presented dictionary approach achieves this lower bound with the smallest possible auxiliary memory (`O(k)`).  
* The early `k == 0` guard handles the degenerate case instantly.  

Thus the solution is both **optimal** and **clean**. Feel free to drop the optional eviction block – the algorithm remains correct (just uses up to `O(n)` extra space) – but keeping it preserves the `O(k)` guarantee for very large inputs.

## Lesson & Pattern
### Hey there! 👋  
Let’s unpack what’s really going on in **“Contains Duplicate II”** and turn it into a reusable pattern you can spot on many other problems.

---

## 1️⃣ Core algorithmic pattern  
**Sliding‑window + hash‑set (or hash‑map) for “recent‑elements” membership**  

- We keep a *window* that contains the last `k` elements we have seen.  
- Inside that window we need **O(1)** checks: “Have I already seen this value?” → a hash‑based container (`set` or `dict`).  
- When the window grows past size `k` we *evict* the oldest element so the structure never stores more than `k` items.

That combination of a *fixed‑size moving window* + *constant‑time look‑ups* is the pattern.

---

## 2️⃣ Why this pattern fits the problem  

| Requirement | How the pattern satisfies it |
|-------------|------------------------------|
| **“Two indices i, j with |i‑j| ≤ k”** | The window guarantees we only compare a value to indices that are at most `k` steps behind the current one. |
| **“Same value”** | A hash‑set/dict tells us instantly whether that value already exists in the current window. |
| **Linear‑time needed (n ≤ 10⁵)** | We scan the array once; each step does only O(1) work (membership test + possible removal). |
| **Space bounded by k** | By evicting the leftmost element when the window exceeds `k`, we never store more than `k` items (O(k) space). |

If you tried a naïve double‑loop you’d get O(n²) → far too slow. The sliding window shrinks the search space to “the last k positions”, and the hash set makes the “is there a duplicate?” test constant‑time.

---

## 3️⃣ Three sibling LeetCode problems that use the same pattern  

| # | Problem | What the pattern does there |
|---|---------|-----------------------------|
| 1 | **219. Contains Duplicate II** (this one) | Detect a duplicate within a distance *k*. |
| 2 | **3. Longest Substring Without Repeating Characters** | Keep a sliding window of unique characters; `set` tells you when a repeat appears, then shrink from the left. |
| 3 | **239. Sliding Window Maximum** (variant) | Maintain a deque (still a “window”) that holds candidates for the max; you add new element, evict old ones beyond size `k`. |
| 4 | **567. Permutation in String** | Window of size `len(p)` over `s`; a hash‑map of character counts lets you check “is this an anagram?” in O(1) per step. |

(You only asked for three, but the fourth is a nice bonus!)

---

## 4️⃣ Simple mental framework to spot this pattern  

> **When you see “within X distance / of size X / at most X apart”, think “sliding window of size X”.**  
> Then ask:
> 1. **Do I need fast “have I seen this before?”** → bring in a hash‑set / hash‑map.  
> 2. **Do old elements become irrelevant after they move out of the X‑range?** → evict them when the window slides.  

If the answer to both is **yes**, you’re almost certainly looking at the *sliding‑window + hash‑container* pattern.

**Quick checklist while reading a problem:**

| Question | If “Yes”, you probably need the pattern |
|----------|------------------------------------------|
| Is there a constraint on the distance between two indices? | ✅ |
| Do I only care about the *presence* of something, not the exact count? | ✅ (set) |
| Do I need the *most recent* index of each value? | ✅ (dict value → index) |
| Is the input size up to 10⁵‑10⁶, demanding O(n) time? | ✅ (linear scan) |

---

## 5️⃣ One key takeaway to remember  

> **“Window = recent history, Hash = instant memory”**  
> Keep only the last *k* things you’ve seen, and use a hash structure so you can ask “Did I see it?” in constant time. This gives you linear time overall and O(k) extra space—exactly what most “within‑k‑distance” problems require.

---

## Quick, clean Python implementation (dictionary version)

```python
from typing import List

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    # value -> most recent index where we saw it
    last_pos = {}
    for i, v in enumerate(nums):
        if v in last_pos and i - last_pos[v] <= k:
            return True
        last_pos[v] = i          # update the latest position
    return False
```

And the classic *set‑window* version, which shows the eviction step more explicitly:

```python
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    window = set()               # holds at most k elements
    left = 0
    for right, val in enumerate(nums):
        # shrink window if it grew larger than k
        if right - left > k:
            window.remove(nums[left])
            left += 1
        if val in window:        # duplicate inside the window!
            return True
        window.add(val)
    return False
```

Both run in **O(n)** time, **O(min(k, n))** space, and embody the sliding‑window + hash pattern.

---

### 🎯 TL;DR  
Whenever a problem talks about “distance ≤ k” (or any fixed‑size constraint), picture a moving window of the last *k* items and ask yourself, “Can I test membership instantly?” If yes → grab a `set` or `dict` and you’ve got a solution that’s fast, simple, and reusable. Happy coding! 🚀
