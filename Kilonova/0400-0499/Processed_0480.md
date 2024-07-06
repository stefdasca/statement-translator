# Pattern Matching

We define a **pattern** as a **non-empty string** consisting only of the characters `0`, `1`, and `?`. We say that two patterns `A` and `B` of the same length **match** if and only if the characters `?` can be conveniently replaced with `0` and `1`, making the two strings identical. For example, given `A = 110?1`, `B = 1?001`, and `C = ??1?1`, the strings `A` and `B` match (the string `11001` can be formed by replacing the question marks), but the strings `A` and `C` do not match.

We are given a **tree** (an undirected connected acyclic graph) with `N` nodes. We need to assign each node a string consisting of the characters `0`, `1`, and `?` (a pattern) such that the following properties are satisfied:
* All patterns have the same length, which should be as small as possible (see the **Scoring** section).
* For any two distinct nodes `u` and `v`, their associated patterns match **if and only if** there exists the edge `(u, v)` in the tree.

# Implementation Details
You will implement the function with the following signature:
```cpp
std::vector<std::string> patterns(std::vector<std::pair<int, int>> edges)
```
The `patterns` function will be called exactly once within a test. The vector `edges` will have a size of `N - 1` and will represent the undirected edges of the tree, given as pairs of adjacent nodes. Formally, $edges_i$ is equal to a pair $(u_i, v_i) (0 \le i < N - 1, 1 \le u_i, v_i \le N)$, indicating that there is an undirected edge between nodes $u_i$ and $v_i$. The nodes are indexed from `1`. It is guaranteed that the edges will form a connected acyclic graph.

The function must return a vector containing exactly `N` non-empty patterns of the same length, consisting only of the characters `0`, `1`, and `?` (not necessarily all three). The string at position `i` (`0 \leq i < N`) will represent the pattern associated with the node indexed at `i + 1`.

For the solution to be valid, the returned patterns must satisfy the conditions mentioned above. Otherwise, the grader will end the program and mark the test as incorrect.

# Scoring
**Attention! This problem is partially scored**. The tests within each subtask will have an associated maximum length $prag_{sup}$ which is acceptable. Any response returned by your function containing patterns longer than this length will be considered incorrect for that test.

There is also a minimum length $prag_{inf}$ which guarantees the maximum score for that test. If the function returns a solution better than the lower length threshold, it will receive the maximum score for the test. If the length of the returned patterns is between these limits, the score received will be calculated as:
$$ \displaystyle score = \left\lfloor \frac{1}{2} \cdot P_{subtask} \cdot \left(1 + \frac{prag_{sup} - ans + 1}{prag_{sup} - prag_{inf} + 1}\right) \right\rfloor $$
Here, `ans` represents the length of the patterns in the returned answer, $P_{subtask}$ represents the score allocated to the subtask to which the test belongs, and $\\lfloor x \\rfloor$ represents the floor function of the real number `x`. Note that, for $ans = prag_{inf}$, the entire test score is obtained, and for $ans = prag_{sup}$, half of the test score is obtained.

**The total score awarded to a subtask is equal to the minimum score awarded for each test within the subtask.**

## Subtask 1 (6 points)
* `2 \leq N \leq 10`
* $prag_{inf} = 100$
* $prag_{sup} = 100$
## Subtask 2 (9 points)
* `2 \leq N \leq 100`
* $prag_{inf} = 100$
* $prag_{sup} = 100$
## Subtask 3 (5 points)
* `2 \leq N \leq 10\ 000`
* $prag_{inf} = 34$
* $prag_{sup} = 34$
* The tree is a chain of $N$ nodes
## Subtask 4 (6 points)
* `2 \leq N \leq 10\ 000`
* $prag_{inf} = 34$
* $prag_{sup} = 34$
* The tree is a complete binary tree
## Subtask 5 (42 points)
* `2 \leq N \leq 10\ 000`
* $prag_{inf} = 101$
* $prag_{sup} = 200$
## Subtask 6 (32 points)
* `2 \leq N \leq 10\ 000`
* $prag_{inf} = 34`
* $prag_{sup} = 42$

# Grader Model
The grader will read the input data from the console in the following format:
* line `1`: `N`
* line `1 + i` `(1 \leq i \leq N - 1)`: $u_i \ v_i$ (separated by space), representing the edge $(u_i, v_i)$

The grader will display to the console your response, in the following format:
* line `i` (`1 \leq i \leq N`): $p_i$, representing the pattern associated with node `i`

# Examples
`stdin`
```
4
1 2
1 3
1 4
```
`stdout`
```
???
000
0?1
11?
```
`stdin`
```
3
1 2
2 3
```
`stdout`
```
0
?
1
```
`stdin`
```
5
1 2
1 3
3 4
3 5
```
`stdout`
```
?00
000
1??
110
101
```
`stdin`
```
2
2 1
```
`stdout`
```
?
?
```
Explanation
---
This is the figure for the first and the third example:
\
~[image.png]