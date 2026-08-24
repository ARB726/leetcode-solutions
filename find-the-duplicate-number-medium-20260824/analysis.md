# Find The Duplicate Number — Medium

## Problem
Find the Duplicate Number
Medium
Topics
Company Tags
Hints
You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.

There is exactly one repeated integer in nums, and every other integer appears at most once.

Return the repeated integer.

Example 1:

Input: nums = [1,2,3,2,2]

Output: 2
Example 2:

Input: nums = [1,2,3,4,4]

Output: 4
Follow-up: Can you solve the problem without modifying the array nums and using 
O
(
1
)
O(1) extra space?

Constraints:

1 <= n <= 10,000
nums.length == n + 1
1 <= nums[i] <= n


Topics

Recommended Time & Space Complexity

Hint 1

Hint 2

Hint 3

Hint 4

Company Tags
Seen this question in a real interview?
Yes
No
Acceptance Rate
66.2%
Solution 1
+

NeetBot
|

Hint
|
|
Ln 20, Col 1

Ask NeetBot

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = nums[0]
        right = nums[0]

        while True:
            left = nums[left] # to iterate through the linked list
            right = nums[nums[right]]

            if left == right: break

        left = nums[0]

        while left != right:
            left = nums[left]
            right = nums[right]

        return left


1234567891011121314151617
Accepted

Passed test cases: 79 / 79


Visualize code
You have successfully completed this problem!



## Problem Analysis
**1. Problem type**

- **Array** with a hidden *linked‑list cycle* interpretation.  
- Can also be solved with **binary search** on the value range or **Floyd’s Tortoise‑Hare** cycle detection (O(1) space).  
- No DP/graph/tree needed.

---

**2. Constraints & edge cases**

| Constraint | Reason it matters |
|------------|-------------------|
| `1 ≤ n ≤ 10 000` (so `len(nums) = n+1 ≤ 10 001`) | Small enough for O(n log n) or O(n) solutions; but we must meet the O(1) extra‑space requirement. |
| `1 ≤ nums[i] ≤ n` | Guarantees every element can be used as an index into the array (0‑based shift). |
| Exactly **one** value appears *more than once* (could appear 2‑times or more). | The cycle detection works because the duplicate creates a merging point in the “next‑pointer” graph. |
| Array is **read‑only** for the follow‑up. | No sorting or in‑place marking allowed. |
| All other numbers appear at most once. | Prevents multiple cycles; there is a single entry point to the cycle. |

**Edge cases to test**

| Input | Why interesting |
|-------|------------------|
| `[1,1]` (n=1) | Minimum size, duplicate is the first element. |
| `[2,2,2,2]` (n=3) | Duplicate appears many times, still a single cycle. |
| `[1,3,4,2,2]` | Duplicate not at the ends, typical case. |
| `[3,1,3,4,2]` | Duplicate is the smallest index after 0‑based conversion. |
| Large `n` (≈10 000) with duplicate at the far end – tests performance. |

---

**3. Input / Output**

```python
def findDuplicate(nums: List[int]) -> int:
    ...
```

- **Input**: `nums` – a list of `n+1` integers (`1 … n` inclusive).  
- **Output**: The integer that occurs more than once (the duplicate).

---

**4. Best data structures**

| Goal | Recommended structure |
|------|------------------------|
| Constant extra memory | **No extra container** – just a few integer variables (`slow`, `fast`, `ptr`). |
| Fast “next” operation | Use the **array itself** as an implicit linked list: `next = nums[current]`. |
| Optional binary‑search solution | Use the **array** plus integer counters (still O(1) extra). |

---

**5. Typical O(1)‑space solution (Floyd’s Tortoise‑Hare)**  

*Idea*: Treat each index as a node, `next = nums[node]`. Because there are `n+1` nodes but only `n` possible values, the directed graph must contain a cycle; the entry point of the cycle is the duplicate.

```python
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1 – find intersection inside the cycle
        slow = nums[0]          # move one step
        fast = nums[nums[0]]    # move two steps
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # Phase 2 – find the entrance to the cycle
        slow = 0                # restart one pointer at start
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
```

*Complexities*  
- **Time**: `O(n)` – each pointer traverses at most `2n` steps.  
- **Space**: `O(1)` – only a handful of integer variables.

---

**Alternative O(n log n) with O(1) extra space (binary search on value range)**  

```python
def findDuplicate(nums: List[int]) -> int:
    low, high = 1, len(nums) - 1   # possible values
    while low < high:
        mid = (low + high) // 2
        # count how many numbers ≤ mid
        cnt = sum(x <= mid for x in nums)
        if cnt > mid:          # duplicate is in [low, mid]
            high = mid
        else:                  # duplicate is in (mid, high]
            low = mid + 1
    return low
```

*Complexities*  
- **Time**: `O(n log n)` (log n passes, each O(n) counting).  
- **Space**: `O(1)`.

Both meet the “no modification & O(1) extra space” requirement; Floyd’s method is linear‑time and usually preferred.

## Code Review
**Review of the submitted solution**

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = nums[0]
        right = nums[0]

        while True:
            left = nums[left]            # move one step
            right = nums[nums[right]]    # move two steps

            if left == right:
                break

        left = nums[0]                   # ← reset one pointer

        while left != right:
            left = nums[left]
            right = nums[right]

        return left
```

---

## 1. Correctness / Logical errors  

*The algorithm is a variant of Floyd’s Tortoise‑Hare cycle‑detection, which is the canonical O(1)‑space solution for this problem.*  

- **Phase 1** (finding an intersection) is implemented correctly: `left` moves one step, `right` moves two steps until they meet.  
- **Phase 2** (finding the entrance of the cycle) also works, but the reset is done with `left = nums[0]` instead of the more common `left = 0`.  
  *Why it still works:* the “graph” we walk on has nodes that are **values** (`1 … n`) rather than indices. Starting the second pointer at `nums[0]` is equivalent to starting it one step ahead of index 0, and because the first pointer is also one step ahead of the start, the two pointers meet exactly at the duplicate value.  
  Nevertheless, this choice is **non‑standard** and can be confusing; resetting to `0` is clearer and matches the textbook proof.

- **Edge‑case handling** – The solution correctly returns the duplicate for:
  - Minimum size `[1,1]`
  - Duplicate appearing many times (`[2,2,2,2]`)
  - Duplicate equal to the first element, the last element, or any middle element.

There are **no logical bugs** that would produce a wrong answer for any input that satisfies the problem constraints.

---

## 2. Time Complexity  

Both pointers traverse at most `2·n` steps in phase 1 and at most `n` steps in phase 2.

```
T(n) = O(n)
```

This meets the required linear time bound.

---

## 3. Space Complexity  

Only a few integer variables (`left`, `right`) are used, irrespective of `n`.

```
S(n) = O(1)
```

The solution satisfies the “O(1) extra space” requirement.

---

## 4. Edge‑case coverage  

| Input                           | Reason it is interesting                                 | Result produced |
|--------------------------------|----------------------------------------------------------|-----------------|
| `[1,1]`                         | Smallest possible array (n = 1)                         | `1` (correct)   |
| `[2,2,2,2]`                     | Duplicate appears > 2 times                             | `2` (correct)   |
| `[1,3,4,2,2]`                   | Duplicate not at ends                                    | `2` (correct)   |
| `[3,1,3,4,2]`                   | Duplicate is the smallest possible value after `0`      | `3` (correct)   |
| Large random array (n ≈ 10 000) | Stress test for performance                               | Returns the correct duplicate in ≤ O(n) time |

All of these are handled correctly by the current code.

---

## 5. Readability & Style  

| Issue | Why it matters | Suggested improvement |
|-------|----------------|-----------------------|
| Variable names `left` / `right` | In Floyd’s algorithm they are traditionally called `slow` and `fast`. The current names suggest a two‑pointer “left‑right” approach rather than a “tortoise‑hare”. | Rename to `slow` and `fast` (or `tortoise` / `hare`). |
| Resetting pointer with `left = nums[0]` | This deviates from the textbook version (`slow = 0`). Future readers may wonder whether the extra step is intentional or a bug. | Use `slow = 0` (or `left = 0`) for the second phase; it’s clearer and still O(1). |
| No import for `List` | LeetCode supplies it, but in a standalone module the code would raise a `NameError`. | Add `from typing import List` at the top. |
| Missing doc‑string / comments | The algorithm is non‑trivial; a short explanation helps reviewers and interviewers. | Add a doc‑string describing the “linked‑list cycle” interpretation and brief inline comments. |
| `while True:` with internal `break` | Works, but some style guides prefer a condition directly in the while statement. | `while left != right:` (after an initial move) or keep as‑is with a comment “loop until intersection”. |

**Re‑written version (more idiomatic):**

```python
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """Return the element that appears more than once using
        Floyd's Tortoise‑Hare cycle detection (O(n) time, O(1) space)."""

        # Phase 1 – find a meeting point inside the cycle.
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # Phase 2 – locate the entry point of the cycle (the duplicate).
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
```

The logic is unchanged; only variable names, the reset step, and documentation are improved.

---

## 6. Summary  

- **Correctness:** ✅ The algorithm always returns the duplicate for any valid input.  
- **Time:** `O(n)` – optimal.  
- **Space:** `O(1)` – meets the follow‑up requirement.  
- **Edge cases:** All relevant scenarios are handled.  
- **Readability:** Minor naming and resetting‑pointer choices make the code harder to read than necessary, but they do not affect correctness.

**Recommendation:** Keep the algorithm as‑is (it works), but refactor the variable names and the second‑phase reset to the conventional `slow = 0`. Add a brief comment or doc‑string to clarify the cycle‑detection idea. This will make the solution instantly recognizable to anyone familiar with Floyd’s algorithm and improve maintainability.

## Optimized Solution
**Answer – Floyd’s Tortoise‑Hare (cycle detection) is already optimal**  

For the “no‑modification & O(1) extra‑space” version the best‑possible time
complexity is **Θ(n)**, because we have to look at the array at least once to
see the duplicate.  
The classic Floyd cycle‑detection algorithm achieves this bound with only a
few integer variables → **O(1) extra space**.  

The solution you posted is a correct implementation of this idea; it can be
written a little more idiomatically, but the asymptotic complexity cannot be
improved further. Below is a clean, fully‑commented version that is
functionally identical and therefore optimal.

---

## Optimized (but still Θ(n) time, O(1) space) code

```python
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Floyd's Tortoise and Hare (cycle detection).

        1. Treat each index as a node in a linked list.
           The "next" pointer of node i is nums[i].
        2. Because there are n+1 nodes but only n distinct values,
           a cycle must exist – the entry point of the cycle is the duplicate.
        3. Phase‑1: find a meeting point inside the cycle.
        4. Phase‑2: start one pointer from the list head (index 0) and move
           both pointers one step at a time; they meet at the cycle entry,
           i.e. the duplicated number.
        """
        # ---------- Phase 1: find intersection ----------
        slow = nums[0]            # moves 1 step each iteration
        fast = nums[nums[0]]      # moves 2 steps each iteration
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # ---------- Phase 2: locate entry of the cycle ----------
        slow = 0                  # restart one pointer at the start
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow               # or `fast`, they are equal here
```

### Why this is optimal
| Metric | Value | Reason |
|--------|-------|--------|
| **Time** | `O(n)` | Each pointer traverses at most `2·n` steps; any algorithm must read the array Ω(n) times to guarantee the duplicate. |
| **Space** | `O(1)` | Only a constant number of integer variables (`slow`, `fast`). No auxiliary containers. |
| **Array mutation** | None | The algorithm only reads `nums`, satisfying the “read‑only” follow‑up. |

### Step‑by‑step walkthrough

1. **Interpret the array as a linked list**  
   - Node = array index (0 … n).  
   - Edge = `next = nums[current]`.  
   - Because values are in `[1, n]`, every node points to a **valid index**.  
   - With `n+1` nodes but only `n` possible values, the graph must contain a
     cycle; the duplicate value is exactly the node where the cycle begins.

2. **Phase 1 – find an interior intersection**  
   ```python
   slow = nums[0]          # one hop from the head
   fast = nums[nums[0]]    # two hops from the head
   while slow != fast:
       slow = nums[slow]          # 1 step
       fast = nums[nums[fast]]    # 2 steps
   ```
   - `slow` moves 1 edge per loop, `fast` moves 2 edges.
   - By the pigeonhole principle they will inevitably meet inside the cycle.
   - The loop finishes after at most `2·n` moves.

3. **Phase 2 – locate the cycle entrance (the duplicate)**  
   ```python
   slow = 0                # restart from the head
   while slow != fast:
       slow = nums[slow]   # 1 step
       fast = nums[fast]   # 1 step
   ```
   - When the two pointers are the same distance from the start of the cycle,
     moving them together makes them meet exactly at the entry node.
   - The entry node’s value equals the duplicated number.

4. **Return the duplicate**  
   - At this point `slow == fast == duplicate`, so we return either.

---

## Alternative (still O(1) space) – binary search on value range  

If you prefer a non‑pointer solution, you can binary‑search the answer
between `1` and `n`. It runs in `O(n log n)` time, which is slower than the
linear Floyd method but uses the same constant extra memory.

```python
def findDuplicate(nums: List[int]) -> int:
    lo, hi = 1, len(nums) - 1          # possible values
    while lo < hi:
        mid = (lo + hi) // 2
        cnt = sum(x <= mid for x in nums)   # O(n) count
        if cnt > mid:
            hi = mid          # duplicate is ≤ mid
        else:
            lo = mid + 1      # duplicate is > mid
    return lo
```

*Time*: `O(n log n)` (log n passes, each O(n) counting)  
*Space*: `O(1)`

---

### Bottom line
- The Floyd‑Tortoise‑Hare implementation shown above is **already optimal** for the given constraints.
- It runs in linear time, uses constant extra memory, does not modify the input, and is easy to understand once the “array‑as‑linked‑list” view is adopted.

## Lesson & Pattern
### 🎯 The pattern you should lock into  
**Floyd’s Tortoise‑&‑Hare (cycle‑detection) on a *functional graph***  

In this problem we don’t have an explicit linked list, but every element of `nums`
can be seen as a “next‑pointer”:

```
node i  ──►  nums[i]          (1 ≤ nums[i] ≤ n)
```

Because we have **n + 1** nodes but only **n** possible values, at least two
different nodes must point to the same successor – that’s the duplicate.
The structure is therefore a *directed graph where every node has out‑degree 1*,
so it must contain exactly one cycle.  
Finding the entry point of that cycle is precisely what Floyd’s algorithm does,
and it uses only two pointers and **O(1)** extra memory.

---

## 1️⃣ Why the cycle‑detection pattern fits perfectly  

| Property of the problem | What it gives us | How Floyd exploits it |
|--------------------------|------------------|-----------------------|
| `nums[i]` is a valid index (1 … n) | We can “jump” from one index to another using the array itself. | Treat the array as an implicit linked list (`next = nums[cur]`). |
| Length = n + 1, values range = 1 … n | By the pigeonhole principle a value repeats → two different indices lead to the same next node. | Guarantees a **single cycle** in the functional graph. |
| We cannot modify the array & must use O(1) extra space | No extra hash set, no sorting. | Floyd needs only two integer variables (`slow`, `fast`). |
| Exactly **one** number appears more than once | Only one cycle, so the algorithm’s “meeting point” is well‑defined. | The first node where the two pointers meet is somewhere inside that unique cycle. |

Because all these conditions line up, the classic “tortoise‑and‑hare” approach
gives us an *O(n) time / O(1) space* solution without ever touching the array
contents except for reading them.

---

## 2️⃣ Three other LeetCode problems that use the same pattern  

| # | Problem (LeetCode link) | What the pattern solves there |
|---|--------------------------|--------------------------------|
| 1️⃣ | **Linked List Cycle II** – 142. <br>*(Find the node where the cycle begins.)* | The list is already a pointer structure; Floyd finds the entry point of the cycle. |
| 2️⃣ | **Find the Duplicate Number** – 287. <br>*(Exactly the same problem; many solutions use Floyd.)* | Same functional‑graph idea – duplicate creates a cycle. |
| 3️⃣ | **Find the Start of the Loop in a Linked List** – 142 (same as 1) but also appears as a “hidden” version in interview questions like “Given an array where `arr[i]` points to the next index, find the repeated index.” | Any situation where you have a *function* `f(i)` that maps a finite set onto itself and you know a collision must exist. |

*(If you prefer a “binary‑search‑on‑answer” flavor, problems like **Capacity To Ship Packages Within D Days** (1011) or **Koko Eating Bananas** (875) also share the “search the answer space” pattern, but the core idea here is cycle detection.)*

---

## 3️⃣ A mental checklist to spot “use Floyd’s cycle detection”

When you read a new problem, run the following quick questions in your head:

| Question | If **YES**, think “cycle detection” |
|----------|--------------------------------------|
| **Can I treat each element/value as a pointer to another index/value?** (i.e., `next = f(i)` where `f` is given by the input) | ✔ |
| **Is the domain size one larger than the codomain?** (e.g., `n+1` items, each in range `1..n`) | ✔ |
| **The statement guarantees *exactly one* repetition / collision.** | ✔ |
| **I’m not allowed to modify the data and must keep extra memory O(1).** | ✔ |
| **The structure is a *functional graph* (every node has out‑degree 1).** | ✔ |

If you answered “yes” to most of these, you’ve got a functional‑graph → **Floyd** is your go‑to.

---

## 4️⃣ One key takeaway to remember  

> **When an array (or any collection) can be interpreted as a “next‑pointer” and the size mismatch guarantees a collision, you can find the duplicate **in linear time and constant space** by simply running two pointers at different speeds.**

In practice, write the two‑pointer skeleton once and reuse it:

```python
def find_duplicate(nums):
    # Phase 1 – find a meeting point inside the cycle
    slow = fast = nums[0]
    while True:
        slow = nums[slow]          # 1 step
        fast = nums[nums[fast]]    # 2 steps
        if slow == fast:
            break

    # Phase 2 – locate the entrance of the cycle
    slow = 0                       # restart one pointer at the start
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow
```

Just plug it in, and you’ve solved the classic “find the duplicate” problem
(and any other functional‑graph duplicate) with the elegance of a two‑pointer
dance.

---

### 🎓 Wrap‑up

- **Pattern:** Floyd’s Tortoise‑&‑Hare (cycle detection) on a functional graph.  
- **Why it fits:** The array’s values act as pointers, the size mismatch forces a cycle, and we need O(1) extra space.  
- **Similar problems:** 142 (Linked List Cycle II), 287 (Find Duplicate Number), any “next‑pointer array” collision problem.  
- **Recognition framework:** “pointer‑like array + size mismatch + one collision + read‑only → Floyd”.  
- **Takeaway:** When you see a read‑only array where each value can be an index, think “maybe it hides a linked list”. If the count of elements exceeds the range of values, the hidden list must loop, and two pointers will find the loop’s entry for free.

Give it a try on a few practice problems, and you’ll start spotting those hidden cycles automatically! 🚀 Happy coding!
