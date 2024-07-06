After a successful evening on Piezișă Street, our hero Alex should return home ... *he should*. However, he doesn't want the fun to end, so he decides to visit another specific tourist attraction in the town of Jluc: *Cetățuia*.

Cetățuia can be seen as an array of `N` hills, the $i$-th hill having a height of $V_{i-1}$. After buying (and drinking) a lot of milk from the shops on *Piezișă Street*, Alex noticed that he has supernatural powers. More precisely, he can increase the height of a hill by exactly `1` unit. However, the milk starts to lose its effect, so he can do this at most `K` times. Alex doesn't like to climb or descend more than necessary, so he wants to minimize the sum $|V_0 - V_1| + |V_1 - V_2| + ... + |V_{N-2} - V_{N-1}|$. Nevertheless, the milk from *Piezișă Street* has an adverse effect as well: it makes the drinker think more slowly. Therefore, Alex is asking you to find the minimum value of the sum described above, after applying at most `K` operations.

# Input data
The first line will contain `T`, the number of scenarios. The following `T` groups of `2` lines each describe a scenario to be solved. The first line of a scenario contains `N` and `K` with the significance described in the statement. The next line contains the `N` elements of the array `V` separated by spaces, where the $i$-th of them represents the height of the $i$-th hill.

# Output data
For each scenario, print on a new line the minimum degree of difficulty that can be obtained.

# Constraints
* The degree of difficulty of an array with a single element is considered `0`.
* $1 \leq N \leq 1\ 000\ 000$
* $0 \leq K \leq 10^{18}$
* $1 \leq V_i \leq 10^9$
* The sum of all `N` values for all scenarios is $\leq 1\ 000\ 000$

## Subtask 1 (5 points)
* $N \leq 15, 1 \leq V_i \leq 40, K \leq 10$, the sum of all `N` values $\leq 50$
## Subtask 2 (25 points)
* $N \leq 100, 1 \leq V_i \leq 40, K \leq 200$, the sum of all `N` values $\leq 500$
## Subtask 3 (10 points)
* $N \leq 1\ 000$, the sum of all `N` values $\leq 10\ 000$
## Subtask 4 (15 points)
* $V_0 = V_{N-1} = 10^9$
## Subtask 5 (20 points)
* $N \leq 100\ 000$, the sum of all `N` values $\leq 100\ 000$
## Subtask 6 (25 points)
* No additional constraints.

# Examples

`stdin`

```
2
6 2
6 3 3 3 4 3
6 3
6 3 3 3 4 3
```

`stdout`

```
4
3
```

Explanations
---

We have `2` scenarios. In both cases, the initial array of heights is `V = [6, 3, 3, 3, 4, 3]`.

In the first case, `K = 2`, Alex will increase the height of the last hill once, and thus the final array becomes `[6, 3, 3, 3, 4, 4]`.
The degree of difficulty on this array is: `|6 − 3| + |3 − 3| + |3 − 3| + |3 − 4| + |4 − 4| = |3| + |0| + |0| + |−1| + |0| = 3 + 1 = 4`

In the last case, `K = 3`, Alex will increase the height of each hill at positions `1, 2` and `3` once. Thus, the final array becomes `[6, 4, 4, 4, 4, 3]`.
The degree of difficulty on this array is: `|6 − 4| + |4 − 4| + |4 − 4| + |4 − 4| + |4 − 3| = |2| + |0| + |0| + |0| + |1| = 2 + 1 = 3`

