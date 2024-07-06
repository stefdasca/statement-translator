```markdown
In the info club, a new Pokemon, Meow2, has appeared. Being passionate about trees, Meow2 has a tree with a root of `N` nodes, numbered from `0` to `N - 1`. Node `0` is the root of the tree and, for any node different from `0`, its parent has an index **strictly smaller** than it. Each node `i` initially has an associated natural number `S[i]` between `1` and `L`.

Meow2 would like to know how many times the sequence `1, 2, ..., L` appears as a subsequence "down" the initial tree. Formally, he is interested in how many sequences $A_0, A_1, ..., A_{L-1}$ exist such that each node $A_i$ has an associated value `i + 1` and, for each `0 \leq i < L - 1`, node $A_i$ is an ancestor (not necessarily direct) of node $A_{i+1}$.

Being a continuously evolving Pokemon, Meow2 progressively changes the initial tree. More precisely, he has a magic sequence of changes, `P`, of length `Q`, and at step `0 \leq i < Q`, he changes the number associated with the node `i % N` to `P[i], 1 \leq P[i] \leq L`. **The change at step `i` will remain valid for the subsequent steps**.

Meow2 would like to know, after each change, how many times the sequence `1, 2, ..., L` appears "down" the initial tree. If we denote by `ans[i]` the answer after the `i`-th change, we need to print the sum: $O = (1 * ans[0] + 2 * ans[1] + \ldots + q * ans[q-1]) \text{ mod } 10^9 + 7$.

# Input data
The input file `meow.in` contains on the first line three natural numbers separated by a space, `N`, `L` and `Q`, with the meanings given in the statement.
The next line contains the sequence `F` of `N - 1` numbers, where the number `F[i]` represents the parent of node `i`.
The 3rd line contains the sequence `S` of length `N`, representing the initial values of the nodes in the tree.
Then follow `Q` lines forming the sequence `P`, representing the changes that Meow2 makes to the tree in the manner presented in the statement, in order.

# Output data
The output file `meow.out` will contain the sum `O` required modulo $10^9+7$.

# Constraints and clarifications
* `1 \leq N \leq 100 000`
* `1 \leq L \leq N`
* `0 \leq F[i] < i`, for any `i`
* `1 \leq P[i], S[i] \leq L`, for any `i`
* `1 \leq Q \leq 200 000`
* For `20` points: `N \leq 200, L \leq 30, Q \leq 400`
* For `50` points: `N \leq 5 000, L \leq 300, Q \leq 5 000`

# Examples
`meow.in`
```
6 2 6
0 1 0 3 0
1 2 1 2 1 2
2
1
2
1
2
1
```
`meow.out`
```
29
```
Explanation
---
In the initial tree, the sequence `S` appears `3` times, but after the first change, it will appear `0` times, after the second change still `0` times, after the third change once, after the fourth change once, after the fifth change `2` times, after the sixth change `2` times.
The answer is `1 * 0 + 2 * 0 + 3 * 1 + 4 * 1 + 5 * 2 + 6 * 2 = 29`
```