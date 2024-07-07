Istvan went on a trip to the island *Modnarcaskurr* and started watching the flower dance. The flower dance works as follows. There are `N` dancers (numbered from `0` to `N-1`) and `N` flowers. At the beginning, dancer number `i` takes flower number `p[i]`, where `p` is a permutation (this permutation is a secret of the island's culture). Then, the dancers group into `k` groups, $A_1, ..., A_k$. Each of the `N` dancers fits into exactly one group. During the dance, the dancers within a group shuffle, and so do the groups among themselves, but the groups **CANNOT** be changed. After the dance, the dancers in each group throw their flowers into the air, and we can see how the flowers are grouped: in the groups $B_1, ..., B_k$, where any $B_i$ represents the flowers associated with a group of dancers (not necessarily group $A_i$).

Istvan then goes to the island's oracle, which lets him ask multiple questions of the form $A_1, ..., A_k$, where the answer to a query is $B_1, ..., B_k$. The oracle now asks him: “Can you find the permutation `p`?�.

Formally, there is a hidden permutation `p` of the numbers from `0` to `N-1`, and queries can be made in the form $A_1, ..., A_k$, where $A_1, ..., A_k$ is a partition of `{0, ..., N-1}`. The answer to a query is a partition $B_1, ..., B_k$ of `{0, ... , N-1}`, where for each $A_i$ there is exactly one $B_j$ such that $k ∈ A_i$ if and only if $p[k] ∈ B_j$. The task is to find `p`.

## Interaction Protocol

The contestant needs to implement a function:

```cpp
std::vector<int> solve(int N);
```

The parameter `N` represents the length of the permutation. The function will return a vector of length `N`, representing the permutation found by the contestant. **The contestant should not implement the main function. The function will be called just once per run.**

The contestant can call the following function for a query:

```cpp
std::vector<std::vector<int>> ask(const std::vector<std::vector<int>> &partition);
```

The parameter partition represents the partition for which the query is made (`A` mentioned above in the statement). Each vector in this vector of vectors represents one of the sets that make up the partition. Obviously, both the order of elements in the vector of vectors partition and the order of the vectors that constitute it are irrelevant (as they represent sets). The answer is the partition `B` described in the statement, represented as a vector of vectors, similar to `A`.

# Constraints and clarifications
* `3 \leq N \leq 10000`
* `Q` represents the maximum number of queries to achieve the maximum score on a test.
* `optimal` represents the minimum number of queries to find the hidden permutation.
* The score for a subtask is the minimum score obtained on a test from the subtask.
* `maxC` represents the maximum cardinality of any partition to achieve a non-zero score on a test.
* The contestant is allowed a maximum of `20000` queries for a test.
* You must include "islands.h"

## Subtask 1 (11 points)
* `N = 15`
* `Q = 15`
* `maxC = N`
## Subtask 2 (15 points)
* `N = 4997`
* `Q = optimal + 15`
* `maxC = N`
## Subtask 3 (15 points)
* `N = 5000`
* `Q = optimal + 15`
* `maxC = N`
## Subtask 4 (17 points)
* `N = 5010`
* `Q = optimal + 5`
* `maxC = N`
## Subtask 5 (16 points)
* $3 \leq N \leq 10^4$
* `Q = optimal`
* `maxC = N`
## Subtask 6 (9 points)
* `N = 8778`
* `Q = optimal`
* `maxC = 500`
## Subtask 7 (8 points)
* `N = 9889`
* `Q = optimal`
* `maxC = 500`
## Subtask 8 (9 points)
* $3 \leq N \leq 10^4$
* `Q = optimal`
* `maxC = 500`

# Scoring
The score is calculated as follows, depending on the number of queries made by the contestant (`contestantQ`) and the maximum cardinality of a partition (`contestantC`):

$ score = \\left\\{  
 \\begin{array}{ll}
        0.6^{\\max(contestantQ−Q,0)} \\cdot maxScore & \\text{if contestantC \\leq maxC} \\\\
        0 & \\text{otherwise}
    \\end{array}
\\right.
$

# Example

`Committee`
`p = (0, 2, 1)`
`solve(3)` is called

`Contestant`
`ask({{0, 1, 2}}) = {{0, 1, 2}}`
`ask({{0}, {1, 2}}) = {{0}, {1, 2}}`
`ask({{1}, {0, 2}}) = {{2}, {0, 1}}`
`ask({{2}, {0, 1}}) = {{1}, {0, 2}}`
`ask({{0}, {1}, {2}}) = {{0}, {1}, {2}}`
`solve` returns `(0, 2, 1)`.

Explanation
---

Observe that for `ask({{0, 1, 2}})` any permutation is a valid answer. Also, for `ask({{1}, {0, 2}})`, any answer among `{{2}, {0, 1}}, {{2}, {1, 0}}, {{1, 0}, {2}}, {{0, 1}, {2}}` is correct.

