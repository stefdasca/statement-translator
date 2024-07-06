Here is the translated text:

Given a permutation $P$ of length $N$. We consider the operation of swapping values located at two consecutive positions.

We define a permutation of length $N$ as a sequence that contains all numbers from $0$ to $N-1$ exactly once. Given a permutation $P = (p_0, p_1, p_i, p_{i+1}, p_{N-1})$ and an index $0 \leq i < N - 1$. After swapping the values at positions $i$ and $i + 1$ in $P$, the permutation $P$ becomes $P = (p_0, p_1, p_{i+1}, p_i, p_{N-1})$.

The contestant (that is, you) can purchase such swaps. Once purchased, a swap can be used any number of times. We define the cost of $P$ as the minimum number of such swaps that need to be purchased so that the permutation can be sorted using only the purchased swaps, each used any number of times.

The committee (that is, us) changes the permutation $P$ $Q$ times by swapping values at two arbitrary positions, **not necessarily adjacent**. Once a change has been made to the permutation, it remains valid thereafter.

Both for the initial permutation and for the permutations obtained after each of the committee's changes, the cost of $P$ is required.

# Interaction Protocol
The contestant will implement two functions `init` and `query`, with the following signatures:
```cpp
int init (std::vector<int> p);
int query (int x, int y);
```

The function `init`:
* Will be called only once, at the beginning of each test.
* Receives the initial permutation $P$, of length $N$.
* Must return a single value, representing the cost of the permutation $P$.
The function `query`:
* Will be called multiple times ($Q$ times) during a test.
* Receives the swap made by the committee $(0 \leq x < y < N)$. **It is possible that** $y \neq x + 1$.
* Must return a single value, representing the cost of the permutation $P$ after applying the change.

**The contestant MUST NOT implement a `main` function.**

## Subtask 1 (6 points)
* $1 \leq N \leq 1\ 000$
* $1 \leq Q \leq 10$
## Subtask 2 (13 points)
* $2 \leq N \leq 100\ 000$
* $1 \leq Q \leq 100$
## Subtask 3 (46 points)
* $2 \leq N \leq 50\ 000$
* $1 \leq Q \leq 50\ 000$
## Subtask 4 (22 points)
* $2 \leq N \leq 100\ 000$
* $1 \leq Q \leq 200\ 000$
* The changes made by the committee swap only values at adjacent positions. Specifically, $y = x + 1$ for all committee changes.
## Subtask 5 (13 points)
* $2 \leq N \leq 100\ 000$
* $1 \leq Q \leq 200\ 000$

# Examples
`Input`
```
3 4
0 1 2
0 1
0 1
0 2
1 2
```
`Output`
```
0
1
0
2
2
```

`Input`
```
4 6
0 3 2 1
1 2
1 3
0 2
0 1
1 2
0 2
```
`Output`
```
2
2
1
3
3
2
3
```

Explanations
---
For the first example:
In the initial permutation $(0, 1, 2)$, no swap is needed to sort the permutation.

In the permutation after the first change, $(1, 0, 2)$, it is necessary to purchase the swap $(0, 1)$.

The permutation after the second change is identical to the initial one.

The penultimate permutation is $(2, 0, 1)$ and it is necessary to purchase the swaps $(0, 1)$ and $(1, 2)$.

The last permutation is $(2, 1, 0)$, and the swaps $(0, 1)$ and $(1, 2)$ remain both necessary **(even if they are used multiple times, each is purchased only once)**.