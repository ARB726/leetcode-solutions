# Contains Duplicate — Easy

## Problem
Contains Duplicate
Easy
Topics
Company Tags
Hints
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
Constraints:

0 <= nums.length <= 10^5
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
72.6%
Solution 1
+

NeetBot
|

Hint
|
|
Ln 9, Col 21

Ask NeetBot

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False
123456789


























1

1






## Problem Analysis
**1. Problem Type**  
- **Category:** Array / Hash‑based lookup  
- **Difficulty:** Easy (requires O(n) detection of a repeated element)

**2. Constraints & Edge Cases**  

| Constraint | Reason it matters |
|------------|-------------------|
| `0 ≤ nums.length ≤ 10⁵` | Linear‑time algorithm is required; O(n²) will time‑out at the upper bound. |
| `-10⁹ ≤ nums[i] ≤ 10⁹` | Values can be negative; we cannot use counting‑array tricks that rely on non‑negative small ranges. |
| Empty array (`len == 0`) | Should return `False` – no duplicates exist. |
| Single‑element array | Also `False`. |
| All elements identical | Should return `True` as soon as the second element is seen. |
| Large input with many distinct values | Must still run in O(n) time and O(n) extra space (worst‑case). |

**3. Input / Output**  

```python
def hasDuplicate(nums: List[int]) -> bool:
    ...
```

- **Input:** `nums` – list of integers (may be empty).  
- **Output:** `True` if any integer appears at least twice, otherwise `False`.

**4. Recommended Data Structure**  

- **`set` (hash set)** – O(1) average‑case membership test and insertion.  
  - Keeps track of values seen so far.  
  - When a value is already in the set, we have found a duplicate.

**5. Typical Solution (Python)**  

```python
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """Return True iff any value occurs more than once."""
        seen = set()
        for x in nums:
            if x in seen:          # duplicate found
                return True
            seen.add(x)            # record first occurrence
        return False               # loop finished without repeats
```

**Complexity Analysis**

| Aspect      | Complexity |
|-------------|------------|
| **Time**    | `O(n)` – each element is inspected once, set operations are O(1) amortized. |
| **Space**   | `O(n)` in the worst case (all elements are distinct, the set stores `n` items). |

**6. Alternative One‑Liner (if allowed)**  

```python
def containsDuplicate(nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)
```

- Still `O(n)` time & space, but creates an intermediate set of the whole list; the explicit loop version can return early on the first duplicate, which is preferable for large inputs with early repeats.

**7. Quick Checklist for Implementation**  

- ✅ Handle empty list → return `False`.  
- ✅ Use a `set` for O(1) look‑ups.  
- ✅ Return immediately when a duplicate is detected (early exit).  
- ✅ Ensure function signature matches LeetCode (`containsDuplicate`).  

That’s all you need to solve “Contains Duplicate” efficiently.

## Code Review
## ✅ Quick Verdict  
The algorithm is **correct** and runs in the optimal `O(n)` time / `O(n)` extra space.  
The only functional problem is the **method name / signature** – LeetCode expects `containsDuplicate(self, nums: List[int]) -> bool`. With the current name (`hasDuplicate`) the solution will not be recognized and will raise a runtime error.

Below is a detailed review covering bugs, complexity, edge‑cases, and style.

---

## 1. Correctness & Logical Errors  

| Issue | Explanation | Fix |
|-------|-------------|-----|
| **Method name mismatch** | LeetCode calls `Solution().containsDuplicate(nums)`. Your method is called `hasDuplicate`. | Rename to `containsDuplicate`. |
| **Missing import for `List`** | `List` is used only as a type hint; without `from typing import List` the code will raise a `NameError` in a plain Python environment. | Add `from typing import List` (or remove the hint). |
| **Logic** | The loop adds unseen numbers to a set and returns `True` on the first repeat – exactly what the problem asks. | No change needed. |

No other logical bugs were found.

---

## 2. Complexity Analysis  

| Metric | Reasoning |
|--------|-----------|
| **Time** | Each element is inspected once; `x in set` / `set.add` are *amortized* `O(1)`. → **`O(n)`** where `n = len(nums)`. |
| **Space** | In the worst case (all elements distinct) we store every element in `seen`. → **`O(n)`** extra space. |

Both match the “Recommended Time & Space Complexity” for this problem.

---

## 3. Edge‑Case Coverage  

| Edge case | Behaviour of current code | Correct? |
|-----------|--------------------------|----------|
| `[]` (empty list) | Loop never runs, returns `False`. | ✅ |
| Single element `[5]` | No duplicate found, returns `False`. | ✅ |
| All identical `[7,7,7,…]` | Returns `True` after the second element. | ✅ |
| Large input with early duplicate | Early exit stops processing early, saving time. | ✅ |
| Very large input with all distinct values | Traverses whole list, uses `O(n)` memory – expected. | ✅ |

All relevant edge cases are handled.

---

## 4. Readability & Style  

| Observation | Recommendation |
|-------------|----------------|
| **Method name** | Use the exact LeetCode name (`containsDuplicate`). |
| **Type hint import** | Add `from typing import List` at the top, or drop the hint if you prefer plain Python. |
| **Docstring** | Include a short docstring describing the contract – helpful for future readers. |
| **`if num not in seen:`** vs `if num in seen:` | The more natural “detect‑duplicate first” pattern reads clearer: `if num in seen: return True`. |
| **Spacing** | A blank line after the import and before the class definition follows PEP 8. |
| **One‑liner alternative** | `return len(set(nums)) != len(nums)` is concise but does **not** early‑exit, so the explicit loop is preferable for large inputs with early repeats. |
| **Naming of the set** | `seen` is a good name; keep it. |

### Suggested polished version

```python
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Return True iff any value appears more than once in `nums`.
        Uses a hash set for O(1) average look‑ups and exits as soon
        as a duplicate is found.
        """
        seen = set()
        for x in nums:
            if x in seen:          # duplicate detected
                return True
            seen.add(x)            # first occurrence
        return False               # no duplicates
```

---

## 5. Summary of Action Items  

1. **Rename** the method to `containsDuplicate`.  
2. **Import** `List` (or drop the hint).  
3. Optionally add a docstring and switch the conditional to `if x in seen:` for readability.  
4. Keep the rest of the algorithm unchanged – it is already optimal and handles all edge cases.

After these small adjustments the solution will pass LeetCode and be clean, idiomatic Python. Good job on getting the core logic right!

## Optimized Solution
**Answer – the given solution is already optimal**

For the *“Contains Duplicate”* problem the best‑possible asymptotic bounds are  

* **Time:** **O(n)** – we have to look at each element at least once.  
* **Extra Space:** **O(n)** – in the worst case (all numbers distinct) we must remember every value we have seen.

The posted implementation:

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False
```

* uses a hash set (`set`) → O(1) average‑case lookup/insertion,  
* returns **as soon as** a duplicate is found → early exit,  
* scans the array exactly once → O(n) time,  
* stores at most `n` elements → O(n) extra space.

Hence the algorithm meets the optimal bounds; no further asymptotic improvement is possible.

---

## A tiny‑style‑focused rewrite (still O(n) / O(n))

If you prefer a more idiomatic‑Python one‑liner that does **not** gain speed but is concise, you can write:

```python
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """Return True iff any value occurs more than once."""
        # Early‑exit version – identical complexity to the original.
        seen = set()
        for x in nums:
            if x in seen:          # duplicate found
                return True
            seen.add(x)
        return False
```

Or, if early exit is not required (e.g., the list is short or you value brevity):

```python
def containsDuplicate(nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)
```

Both variants have the same **O(n)** time and **O(n)** space characteristics; the explicit loop version is usually faster on large inputs with an early duplicate because it can stop before processing the whole array.

---

## Complexity Summary

| Metric          | Value                                 |
|-----------------|---------------------------------------|
| **Time**        | `O(n)` – one pass, constant‑time set ops |
| **Space**       | `O(n)` – worst‑case set stores all `n` elements |
| **Best‑case time** | `O(1)` when a duplicate is at index 1 |
| **Worst‑case time** | `O(n)` when all elements are distinct |

---

## Step‑by‑step walk‑through of the optimal code

```python
def containsDuplicate(nums: List[int]) -> bool:
    seen = set()               # 1️⃣  create an empty hash set
    for x in nums:             # 2️⃣  iterate once over the input list
        if x in seen:          # 3️⃣  O(1) average‑case check:
            return True        #      duplicate found → stop immediately
        seen.add(x)            # 4️⃣  otherwise remember this value
    return False               # 5️⃣  loop finished → no duplicates
```

1. **Initialize** an empty `set` called `seen`.  
2. **Iterate** through every integer `x` in `nums`.  
3. **Membership test** `x in seen` is O(1) on average because a Python `set` is a hash table.  
   * If the test succeeds, we have already encountered `x` → a duplicate exists, so we `return True` right away.  
4. If `x` is not yet in the set, we **add** it (`seen.add(x)`). This stores the value for future checks.  
5. After processing the whole list without hitting the `return True` branch, we **return False** – every element was unique.

Because each element triggers at most one hash‑lookup and one hash‑insert, the overall work scales linearly with `n`. The set may grow to size `n` in the worst case, giving the linear extra‑space usage.

---

### Bottom line
The original implementation is already the optimal solution for this problem in terms of both time and space. The only possible “optimisation” is stylistic (e.g., a one‑liner) or a micro‑benchmark tweak, but the asymptotic complexity cannot be improved beyond **O(n) time / O(n) space**.

## Lesson & Pattern
### Hey there! 👋  
Let’s take a step back from the line‑by‑line code and think **“what’s the big idea that makes this problem fast?”**  

---

## 1️⃣ Core algorithmic pattern  
**🔑 Pattern:** **Hash‑based lookup (using a `set` or a `dict`)** – often described as the **“use a hash table to record what you’ve seen”** pattern.  

You keep a collection that lets you answer “*have I seen this value before?*” in *O(1)* average time.  
When the answer is “yes” you can stop immediately.

---

## 2️⃣ Why this pattern fits *Contains Duplicate*  

| What the problem asks for | How the hash‑set helps |
|---------------------------|------------------------|
| “Is there any element that appears twice?” | As you scan the array, you insert each element into a set. The set can tell you in constant time whether the element is already present. |
| Need **early exit** (as soon as you spot a repeat) | The moment `x in seen` is true you return `True`. No need to finish the whole scan. |
| Input size up to 10⁵ → we need **linear time** | Inserting and checking in a hash set is amortized *O(1)*, so the whole loop is *O(n)*. A naïve double‑loop would be *O(n²)* and would time out. |
| Values can be negative and huge (‑10⁹ … 10⁹) | A hash table works for *any* hashable value; we don’t need a counting array limited to a small range. |

---

## 3️⃣ Three “cousin” LeetCode problems that use the same pattern  

| Problem (LeetCode #) | How the set/dict is used |
|----------------------|--------------------------|
| **219. Contains Duplicate II** – *Check if two equal numbers are ≤ k apart* | Keep a sliding window set of the last *k* elements; test membership before inserting. |
| **242. Valid Anagram** – *Are two strings anagrams?* | Build a frequency `dict` (or a `Counter`) for one string and decrement while scanning the other. |
| **349. Intersection of Two Arrays** – *Return the common elements* | Convert one array to a set, then iterate the other and collect items that are already in the set. |
| *(Bonus)* **128. Longest Consecutive Sequence** – *Find longest run of consecutive integers* | Put every number in a set, then for each number that is the start of a run (i.e., `num‑1` not in set) expand forward using set look‑ups. |

All of these boil down to “**store what you’ve seen, ask “have I seen this before?” in O(1)**”.

---

## 4️⃣ A simple mental checklist – “Is this a *hash‑lookup* problem?”  

1️⃣ **What’s the question?**  
   *“Does something exist / how many times does it appear / is there a pair that satisfies a condition?”*  

2️⃣ **Can I answer “have I seen X before?” quickly?**  
   *If yes → a set or dict is your friend.*  

3️⃣ **Do I need early termination?**  
   *If the moment the answer is “yes” you can stop, the hash‑lookup approach shines.*  

4️⃣ **Do the values have a huge range or can be negative?**  
   *If yes, a hash table works where a counting array would not.*  

If you answered “yes” to most of those, reach for the **hash‑set / hash‑map** pattern.

---

## 5️⃣ One key takeaway to remember  

> **“When a problem is about *whether* something appears (once, twice, or with a certain relation), think “record‑and‑check” with a hash set. It gives you linear time and constant‑average‑time look‑ups, and you can quit the moment you find the answer.”**

That’s the golden rule for a whole family of “duplicate / frequency / membership” questions.

---

### Quick, clean implementation (just for reference)

```python
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()               # O(1) average look‑up & insert
        for x in nums:
            if x in seen:          # duplicate found → we can stop
                return True
            seen.add(x)            # remember this value
        return False               # scanned all, no repeats
```

Or the one‑liner (nice for readability, but no early exit):

```python
def containsDuplicate(nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)
```

---

### TL;DR  

- **Pattern:** hash‑based “have I seen this before?” (set / dict).  
- **Why it works:** O(1) membership → O(n) total, early exit, works for any integer range.  
- **Similar problems:** 219 Contains Duplicate II, 242 Valid Anagram, 349 Intersection of Two Arrays (plus many more).  
- **Spot‑the‑pattern tip:** look for “does X exist / how many times does X occur?” → reach for a set/dict.  
- **Takeaway:** Master the set/dict trick and you’ll instantly turn many O(n²) ideas into O(n) solutions.

Happy coding, and keep an eye out for that “have I seen this?” moment in future questions! 🚀
