After playing with Neuralink's IP addresses, you developed a passion for permutations. You managed to get a permutation `p` of length `N` and set a simple goal: sort it by performing a minimum number of *swaps* between adjacent elements. Your friend Radu Slav noticed your new interest, and to help you save time sorting the permutation, he offered you a special *swap* operation that you can use at any moment or ignore, but which can be performed between any `2` elements from `p` (not necessarily adjacent). Now, you want to calculate the total minimum number of operations, considering that you can use the operation $swap(i, i + 1)$, `1 \leq i < N` as many times as needed and at most once Radu's operation $swap(i, j)$, `1 \leq i < j \leq N`, where the result of the operation $swap(x, y)$ applied to the permutation $p = p_1, p_2, ... , p_x, ... , p_y, ..., p_N$ is $p' = p_1, p_2, ... , p_y, ... , p_x, ..., p_N$ .

# Input data
The first line contains an integer `N`, representing the length of the permutation.
The second line contains `N` integers $p_1 ... p_N$, representing the permutation that needs to be sorted.

# Output data
Print a single line containing a single integer, representing the minimum number of operations needed to sort the permutation.

# Constraints and clarifications

* `1 \leq N \leq 1 000 000`
* `p` is a valid permutation of numbers from `1` to `N`
## Subtask 1 (7 points)
* `1 \leq N \leq 10`
## Subtask 2 (8 points)
* `1 \leq N \leq 100`
## Subtask 3 (9 points)
* `1 \leq N \leq 500`
## Subtask 4 (10 points)
* `1 \leq N \leq 2 500`
## Subtask 5 (11 points)
* `1 \leq N \leq 10 000`
## Subtask 6 (16 points)
* `1 \leq N \leq 100 000`
* The permutation is generated uniformly at random from the set of permutations of length `N`
## Subtask 7 (27 points)
* `1 \leq N \leq 250 000`
## Subtask 8 (12 points)
* No additional constraints.

# Example

`stdin`

```
5
4 2 1 5 3
```

`stdout`

```
3
```

`stdin`

```
10
1 9 6 10 4 2 8 5 7 3
```

`stdout`

```
14
```

Explanations
---

In the first example, the swaps needed to sort the permutation are (by position): `(4, 5)`, `(1, 3)`, `(3, 4)`, where the special swap operation (which is not between `2` adjacent positions) is `(1, 3)`.