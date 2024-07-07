Certainly, here is the translated competitive programming problem statement in English:

---

Romeo Fefetastic lives in the neighborhood of good boys and has `N` friends in the neighborhood. This neighborhood is represented as a tree with `N` nodes, where each node has a friend. Each of his friends has a value, `v[i]`, `1 \leq i \leq N`.

Before Romeo goes for a ride on his motorcycle through the neighborhood, he makes a list of all the friends he wants to visit. He will successively visit all his friends, each time choosing the shortest path. Practically, Romeo will walk through all the nodes that belong to the connected subtree with the minimum number of nodes that includes all the friends from his list, denoted as `S`.

He knows what the neighborhood looks like and knows that in his pilgrimage he will pass by the houses of some friends who are not on the list, so he will not visit them. After he has visited all the friends he planned to visit, he decides to stop at the node of the least valuable friend among all the nodes he has passed through, to teach him how to score points. This least valuable friend lives in the node with the smallest value from the subtree `S`. If that friend is already on his list, he will visit him twice.

If Romeo visits his friends from the nodes $n_1, n_2, ..., n_k$, and finally stops at the least valuable friend who lives in the node $n_{least\_valuable}$, then we define the *value of the walk* as $v[n_1] \\text{ \\textasciicircum } v[n_2] \\text{ \\textasciicircum } \ldots \\text{ \\textasciicircum } v[n_k] \\text{ \\textasciicircum } v[n_{least\_valuable}],$ where `^` represents the XOR operation. If there are multiple equally least valuable friends, Romeo will visit only one of them.

Romeo Fefetastic enjoys thinking more than acting. Thus, he imagines wanting to visit all possible subsets of friends and wonders what the sum of all possible walks would be.

We are asked to find the sum of the *values of all possible walks* for **all non-empty subsets** of friends Romeo can visit and display this sum modulo $10^9 + 7$.

# Task
Find the sum of the *values of all possible walks* for **all non-empty subsets** of friends Romeo can visit and display this sum modulo $10^9 + 7$.

# Input data
The first line of the input file `countfefete.in` contains the number of friends in the neighborhood `N`.

The second line contains the array `v` consisting of `N` numbers, where `v[i]` represents the value of the friend that stays in node `i`.

Each of the following `N \- 1` lines will contain a pair of numbers `x` and `y`, signifying that there is a direct path from node `x` to node `y`.

# Output data
The output file `countfefete.out` will contain the required sum modulo $10^9 + 7$.

# Constraints and clarifications
* `1 \leq N \leq 200 000`
* `0 \leq v[x] \leq 1 000 000 000`, for any `1 \leq x \leq N`
* For tests worth `15` points, it is guaranteed that `N \leq 15`
* For other tests worth `25` points, it is guaranteed that `N \leq 5 000`
* For other tests worth `15` points, it is guaranteed that `N \leq 20 000`
* For other tests worth `15` points, it is guaranteed that `N \leq 70 000`

# Example

`countfefete.in`
```
3
7 3 2
1 2
2 3
```

`countfefete.out`
```
21
```

Explanation
---
We have `3` friends with values `v[1]=7, v[2]=3` and `v[3]=2`.
The friends in the neighborhood form a chain `1 \- 2 \- 3`.

We consider all non-empty subsets of friends and calculate the value of the walks:
For the subset `{1}` he will pass through `{1}`, so the value of the walk `= v[1] ^ v[1] = 0`.
For the subset `{2}` he will pass through `{2}`, so the value of the walk `= v[2] ^ v[2] = 0`.
For the subset `{3}` he will pass through `{3}`, so the value of the walk `= v[3] ^ v[3] = 0`.
For the subset `{1, 2}` he will pass through `{1, 2}`, and the minimum value is in `v[2] = 3`, so the value of the walk `= v[1] ^ v[2] ^ v[2] = 7`.
For the subset `{2, 3}` he will pass through `{2, 3}`, and the minimum value is in `v[3] = 2`, so the value of the walk `= v[2] ^ v[3] ^ v[3] = 3`.
For the subset `{1, 3}` he will pass through `{1, 2, 3}`, and the minimum value is in `v[3] = 2`, so the value of the walk `= v[1] ^ v[3] ^ v[3] = 7`.
For the subset `{1, 2, 3}` he will pass through `{1, 2, 3}`, and the minimum value is in `v[3] = 2`, so the value of the walk `= v[1] ^ v[2] ^ v[3] ^ v[3] = 4`.
The sum of the values of all possible walks will be thus `0 + 0 + 0 + 7 + 3 + 7 + 4 = 21`.

---

`countfefete.in`
```
3
1 1 1
1 3
2 3
```

`countfefete.out`
```
3
```

Explanation
---
The sum of the values of all walks is `3`.

---

`countfefete.in`
```
5
1 3 7 2 5
1 2
2 3
2 4
4 5
```

`countfefete.out`
```
98
```

Explanation
---
The sum of the values of all walks is `98`.

---

