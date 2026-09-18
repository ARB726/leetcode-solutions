# 219 Contains Duplicate Ii — Easy

## Problem
219. Contains Duplicate II
Solved
Easy
Topics
premium lock icon
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
- Sliding‑window / hash‑table problem (array traversal).  
- Related to “duplicate detection with distance constraint”.

**2. Constraints & important edge cases**  

| Constraint | Reason it matters |
|------------|-------------------|
| `1 ≤ nums.length ≤ 10⁵` | Linear‑time required; O(n²) will TLE. |
| `-10⁹ ≤ nums[i] ≤ 10⁹` | Values can be large/negative, but they are hash‑able. |
| `0 ≤ k ≤ 10⁵` | `k` can be zero (only adjacent duplicates count) or larger than the array length. |
| `k ≥ nums.length` | Effectively “any duplicate anywhere” – just need to know if any value appears twice. |

**Edge‑case checklist**

| Situation | Expected result |
|-----------|-----------------|
| `k == 0` | Must return `False` unless the same index is counted (which is disallowed). |
| `k >= len(nums)` | Same as “contains any duplicate”. |
| All elements distinct | `False`. |
| All elements equal | `True` if `k >= 1`. |
| Small arrays (`len == 1`) | Always `False`. |
| Negative numbers / large magnitude | No impact; hash works. |
| Repeated pattern with distance exactly `k` | `True`. |
| Repeated pattern with distance `k+1` | `False`. |

**3. Input / Output**  

```python
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    ...
```

- **Input**  
  - `nums`: list of integers (size up to 10⁵).  
  - `k`: non‑negative integer.  

- **Output**  
  - `True` if ∃ i ≠ j such that `nums[i] == nums[j]` **and** `abs(i‑j) <= k`; otherwise `False`.

**4. Best data structures**  

| Operation | Desired complexity | Data structure |
|-----------|--------------------|----------------|
| “Have I seen this value within the last k positions?” | O(1) amortized lookup/insertion/removal | `set` (or `dict` storing last index) |
| “Update sliding window when moving past index i‑k” | O(1) removal | `set` (remove the element that leaves the window) |

**Typical solution** – maintain a sliding window of at most `k` recent values in a `set`. While scanning `nums`:

1. If `nums[i]` already in the set → duplicate within distance ≤ k → return `True`.
2. Add `nums[i]` to the set.
3. If window size exceeds `k`, remove `nums[i‑k]` (the element that is now > k away).

Overall **O(n)** time, **O(k)** extra space (≤ O(n) in worst case).

```python
from typing import List

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    recent = set()                     # holds at most k elements
    for i, x in enumerate(nums):
        if x in recent:                # duplicate within window
            return True
        recent.add(x)
        if i >= k:                     # slide the window
            recent.remove(nums[i - k])
    return False
```

*Alternative*: store the **last index** of each value in a dictionary and check `i - last_idx <= k`. This also runs in O(n) time but uses O(n) space in the worst case (still acceptable for 10⁵).  

```python
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    last_seen = {}
    for i, x in enumerate(nums):
        if x in last_seen and i - last_seen[x] <= k:
            return True
        last_seen[x] = i
    return False
```

Both implementations satisfy the constraints and run comfortably within LeetCode limits.

## Code Review
## ✅ Quick summary  

| Aspect | Verdict |
|--------|---------|
| **Correctness** | ✅ The algorithm is logically sound and passes the classic “sliding‑window‑set” approach. |
| **Time complexity** | **O(n)** – one pass, O(1) work per element. |
| **Space complexity** | **O(min(k, n))** – the set never holds more than *k* + 1 distinct values (worst‑case O(n) when *k* ≥ n). |
| **Edge‑case handling** | ✅ Handles `k == 0`, `k >= len(nums)`, negative numbers, single‑element arrays, etc. |
| **Readability / style** | ⚠️ Variable names and formatting can be improved; a small bug‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑⚠️ Minor style issues (see below). |

Below is a detailed code review.

---

## 1️⃣ Correctness & Logical Errors  

The core idea – keep a sliding window of the last `k` elements in a `set` – is correct.  
The loop works as follows:

1. **Check** whether the current value already exists in the window (`hashSet`).  
   *If yes → a duplicate within distance ≤ k exists → return `True`.*  
2. **Insert** the current value into the window.  
3. **If the window grew larger than `k`**, evict the element that fell out of range (`nums[i‑k]`).  

Because we return **immediately** on finding a duplicate, we never mistakenly remove a value that would be needed later.

**Edge‑case `k == 0`**  
When `k == 0` the set never holds more than one element: after we add `nums[i]` we instantly remove it (`len(hashSet) > 0`). Consequently the `if nums[i] in hashSet` test never succeeds, which is exactly the required behavior (`False` for any input).  

**Edge‑case `k >= len(nums)`**  
The removal condition never triggers, so the set may grow to `n` elements. That is fine – we simply end up checking “any duplicate anywhere”, which matches the specification.

**No hidden bugs** were found; the algorithm returns the correct answer for all inputs respecting the constraints.

---

## 2️⃣ Complexity Analysis  

| Step | Cost per element | Total |
|------|------------------|-------|
| `in` lookup on a `set` | O(1) average | O(n) |
| `add` to a `set` | O(1) average | O(n) |
| `remove` from a `set` (executed at most once per iteration) | O(1) average | O(n) |
| **Overall time** | – | **O(n)** |

The set never stores more than `k+1` distinct numbers, so the extra memory is **O(min(k, n))**. In the worst case (`k ≥ n`) this becomes **O(n)**, which is still acceptable for `n ≤ 10⁵`.

---

## 3️⃣ Edge‑Case Coverage  

| Edge case | How the code behaves | Correct? |
|-----------|----------------------|----------|
| `len(nums) == 1` | Loop runs once, never finds a duplicate, returns `False`. | ✅ |
| `k == 0` | Set size never exceeds 0 after removal; always returns `False`. | ✅ |
| `k >= len(nums)` | No removal, set may contain all distinct values; returns `True` if any value repeats. | ✅ |
| All elements equal (`[x, x, …]`) | Returns `True` as soon as the second element is processed (if `k >= 1`). | ✅ |
| Large negative/positive numbers | Hashable, no special handling required. | ✅ |
| Duplicate exactly `k` positions apart | Detected because the older element is still in the set when the later one is examined. | ✅ |
| Duplicate `k+1` positions apart | The older element is removed before the later one is examined → `False`. | ✅ |

All relevant corner cases are naturally handled.

---

## 4️⃣ Readability & Style  

| Issue | Explanation | Suggested fix |
|-------|-------------|---------------|
| **Variable name `num` is misleading** – it actually holds an *index* (`i`). | Makes the code harder to follow, especially for readers who expect `num` to be the array element. | Rename to `i` or use `enumerate` (`for i, val in enumerate(nums):`). |
| **Extra spaces** (`set ()`, `hashSet = set ()`). | PEP‑8 recommends `set()` without a space. | `hashSet = set()` |
| **Missing type imports** (`List` is used but not imported). | In a real‑world module this would raise a `NameError`. | Add `from typing import List` at the top (or use `list[int]` in Python 3.9+). |
| **Repeated indexing (`nums[num]`)** – every time we access the list by index. | Using `enumerate` removes the need for `nums[num]` and clarifies intent. | `for i, val in enumerate(nums):` and then work with `val`. |
| **Commenting** – none. | A couple of short comments would make the algorithm self‑explanatory. | Add inline comments describing the three steps (check, add, evict). |
| **Naming of the set (`hashSet`)** – not a big issue but `window` or `recent` is more expressive. | Improves readability. | `window = set()` |

### Refactored version (PEP‑8 compliant, a bit clearer)

```python
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Return True iff there exist i != j such that nums[i] == nums[j]
        and |i - j| <= k.
        """
        window: set[int] = set()          # stores at most k recent values

        for i, val in enumerate(nums):
            # 1️⃣ duplicate inside the current window?
            if val in window:
                return True

            # 2️⃣ add current element to the window
            window.add(val)

            # 3️⃣ evict element that is now farther than k positions away
            if i >= k:                     # window size would become k+1
                window.remove(nums[i - k])

        return False
```

The logic is unchanged; only readability, naming, and compliance with PEP‑8 have been improved.

---

## 5️⃣ Final Recommendations  

1. **Rename the loop variable** (or use `enumerate`) to make it clear you are iterating over indices.  
2. **Remove the stray spaces** in `set ()`.  
3. **Add the missing import** for `List` (or switch to native `list[int]`).  
4. **Consider adding a brief comment** above the loop explaining the three‑step sliding‑window process.  
5. (Optional) **Replace the set‑based approach with the dictionary‑based version** if you want to keep the last index of each number; it uses `O(n)` space in the worst case but avoids the `len(window) > k` check. Both are acceptable.

With those small stylistic tweaks, the solution is production‑ready: it is correct, optimal in time, linear‑space (bounded by `k`), and handles all edge cases. Great job!

## Optimized Solution
**Answer – an even‑leaner O(n) solution**

The sliding‑window‑set approach you posted is already linear‑time and uses at most `k` extra cells, which is optimal for the given constraints.  
If we want to shave a few constant‑factor operations we can avoid the *remove* step completely by remembering **the last index where each value was seen**.  
For every element `x` at position `i` we only need to know the most recent index `last[x]`.  
If `i – last[x] ≤ k` we have found a valid duplicate; otherwise we update `last[x] = i` and keep scanning.

```python
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Returns True iff there exist i != j with nums[i] == nums[j] and |i-j| <= k.
        Runs in O(n) time and O(min(n, k)) ≈ O(n) extra space.
        """
        last_index = {}                     # value -> most recent position
        for i, x in enumerate(nums):
            # If we have seen x before, check the distance to the previous occurrence
            if x in last_index and i - last_index[x] <= k:
                return True
            # Record the current position as the newest occurrence of x
            last_index[x] = i
        return False
```

---

### Why this version is “faster” / more efficient  

| Aspect | Original set‑window solution | Dictionary‑last‑index solution |
|--------|------------------------------|--------------------------------|
| **Lookup** | `x in recent` (hash‑set) – O(1) | `x in last_index` (hash‑dict) – O(1) |
| **Insert** | `recent.add(x)` – O(1) | `last_index[x] = i` – O(1) |
| **Delete** | `recent.remove(nums[i‑k])` – O(1) *only when `i ≥ k`* | **No deletion** – we just overwrite the old index |
| **Constant factor** | One extra `remove` per iteration after the first `k` elements | Only a single dictionary write per iteration |
| **Space used** | At most `k` elements in the set (≤ O(k)) | At most one entry per distinct value (≤ O(n)) |

Both algorithms are Θ(n) time, but the dictionary version does **one** hash operation per loop (lookup + assignment) instead of **two** (lookup + add + optional remove). For large inputs this small difference can be noticeable in practice.

---

### Complexity analysis  

| Metric | Explanation |
|--------|-------------|
| **Time** | Each element is processed once; dictionary look‑up, arithmetic, and assignment are amortized O(1). Hence **O(n)** where `n = len(nums)`. |
| **Space** | In the worst case every number is distinct, so we store `n` keys → **O(n)**. If `k` is much smaller than `n`, the original set‑window uses only **O(k)**, but the asymptotic bound of the problem allows O(n). |
| **Best‑case** | As soon as a qualifying duplicate is found we return, giving O(1) average‑case when duplicates are early. |
| **Worst‑case** | No qualifying pair → we scan the whole array → Θ(n). |

---

### Step‑by‑step walkthrough  

1. **Initialize** an empty dictionary `last_index`.  
   It will map each value we have seen to the index of its *most recent* appearance.

2. **Iterate** over `nums` with `enumerate`, obtaining the current index `i` and value `x`.

3. **Check for a recent duplicate**  
   - If `x` already exists in `last_index`, compute the distance `i - last_index[x]`.  
   - If this distance ≤ `k`, we have satisfied the problem condition → return `True`.

4. **Update** the record for `x`  
   - Whether or not we found a duplicate, we store `i` as the latest position: `last_index[x] = i`.  
   - This overwrites any older position, which is exactly what we need because only the *nearest* previous occurrence can possibly be within distance `k`.

5. **Finish the loop** – if we never returned `True`, there is no pair meeting the criteria → return `False`.

---

### When the original solution is already optimal  

If memory usage is a strict concern (e.g., the interview environment limits auxiliary space to `O(k)`), the sliding‑window `set` is the best choice because it never stores more than `k+1` elements.  
In that scenario the original code is optimal and needs no change.

---

**Bottom line** – both approaches are linear‑time, but the dictionary‑based version eliminates the extra removal operation, giving a cleaner and slightly faster implementation while remaining within the required `O(n)` time bound.

## Lesson & Pattern
## Hey there! 👋  
Let’s unpack **“Contains Duplicate II”** together and see the pattern that makes this problem click.

---

### 1️⃣ Core algorithmic pattern  
**Sliding‑window + hash‑table (set or dict)**  

You keep a *window* of the last `k` elements you have seen and you ask, “Did I already see this value inside the window?”  
The hash‑table gives you O(1) look‑ups, inserts, and deletions, so the whole scan stays linear.

---

### 2️⃣ Why the sliding‑window fits  

| What the problem asks | How the window helps |
|-----------------------|----------------------|
| Two equal numbers **and** their indices are at most `k` apart. | If we only remember numbers that are **≤ k positions behind** the current index, any match we find is automatically within distance `k`. |
| We must scan the whole array (size ≤ 10⁵). | A single left‑to‑right pass with O(1) work per element gives O(n) time, which is the only realistic option. |
| Values can be huge or negative, but they are hashable. | A Python `set` (or a `dict` that stores the last index) works for any integer. |

So the window guarantees the distance constraint, and the hash‑table guarantees fast “have I seen it?” checks.

---

### 3️⃣ Three “cousin” LeetCode problems that use the same pattern  

| # | Problem | Why it’s the same pattern |
|---|---------|---------------------------|
| 1 | **219. Contains Duplicate II** (this one) | Sliding window of size `k` with a set. |
| 2 | **3. Longest Substring Without Repeating Characters** | Window expands until a duplicate appears, then contracts while removing leftmost chars from a set. |
| 3 | **567. Permutation in String** | Window of length `len(s1)` slides over `s2`, checking character counts with a hash map. |
| 4 | **1695. Maximum Erasure Value** (a bit more subtle) | Keep a window whose sum ≤ `k`, using a set to avoid duplicate numbers. |

(You only asked for three, but I tossed in a fourth because it’s a neat variant!)

---

### 4️⃣ Simple mental framework to spot “sliding‑window + hash”  

1. **“Window” clue in the statement** – words like *“within k distance”, “subarray of length L”, “contiguous”, “at most … apart”.**  
2. **“Duplicate / frequency / count” clue** – you need to know *whether* something appears, not *how many* times overall. → a hash set/dict is perfect.  
3. **Ask yourself:**  
   *If I only remembered the last **X** elements, would any future decision be safe?*  
   *If yes, X is the window size (often given directly, e.g., `k`).*  

When both answers line up → you have a sliding‑window‑with‑hash problem.

---

### 5️⃣ One key takeaway  

> **Keep only what you actually need.**  
> In this problem you don’t need the whole history of the array—just the last `k` values. By discarding everything older than `k`, you turn a potentially O(n²) duplicate check into a clean O(n) solution.

---

## Quick Python refresher

### Set‑based window (the most common way)

```python
from typing import List

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    recent = set()                 # holds at most k elements
    for i, val in enumerate(nums):
        if val in recent:          # duplicate inside the window
            return True
        recent.add(val)           # expand window
        if i >= k:                 # shrink window when it gets too big
            recent.remove(nums[i - k])
    return False
```

### Dict‑based version (stores last index)

```python
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    last_idx = {}                  # value → most recent index
    for i, val in enumerate(nums):
        if val in last_idx and i - last_idx[val] <= k:
            return True
        last_idx[val] = i
    return False
```

Both run in **O(n)** time and **O(k)** (or O(n) worst‑case) extra space, easily satisfying the constraints.

---

### TL;DR  
- **Pattern:** sliding window + hash set/dict.  
- **Why:** the window enforces the distance `k`; the hash gives O(1) duplicate checks.  
- **Spot it:** look for “within X distance” + “do I already have this value?”.  
- **Takeaway:** keep only the last `k` items—nothing more, nothing less.

Give it a try on the cousin problems above; you’ll start recognizing the pattern automatically. Happy coding! 🚀
