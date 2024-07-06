Here is the translated and processed problem statement:

---

For a permutation $p_1, p_2, \ldots , p_N$ of the numbers from `1` to `N` and a position `K`, (`1 \leq K \leq N`), let us denote by `BestK` the minimum number of swaps (of values located on consecutive positions) needed to obtain a permutation that is decreasing from position `1` to position `K` and increasing from position `K` to position `N`. A permutation is given.

You are asked to solve one of the following two tasks:
1. For a given position `K`, calculate `BestK`.
2. For all positions `K` from `1` to `N`, calculate `BestK`.

# Input data
The first line contains three integers separated by space `C, N` and `K`. `C` represents the task and can take the value `1` or the value `2`. `N` represents the order (length) of the permutation. If `C = 1` then `1 \leq K \leq N` represents the position for which we need to calculate `BestK`. If `C = 2` then `K = 0` and `BestK` needs to be calculated for all positions from `1` to `N`. The second line contains `N` integers separated by space $p_1, p_2, \ldots , p_N$ representing the elements of the permutation.

# Output data
If `C = 1` solve task `1`. In this case, the first line will contain a single number: `BestK`. If `C = 2` solve task `2`. In this case, the first line will contain `N` numbers separated by space: $Best_1, Best_2, \ldots , Best_N$.

# Constraints and clarifications
* `1 \leq C \leq 2`
* `1 \leq N \leq 100\ 000`
* If `C = 1`, then `1 \leq K \leq N`.
* If `C = 2`, then `K = 0`.
* $1 \leq p_i \leq N$ for any `i` with `1 \leq i \leq N` and they are distinct.

## Subtask 1 (2 points)
* `C = 1, N \leq 3000, K = 1`

## Subtask 2 (4 points)
* `C = 1, N \leq 100\ 000, K = 1`

## Subtask 3 (2 points)
* `C = 1, N \leq 3000, K = N`

## Subtask 4 (4 points)
* `C = 1, N \leq 100\ 000, K = N`

## Subtask 5 (9 points)
* `C = 2, N \leq 8`

## Subtask 6 (11 points)
* `C = 2, N \leq 18`

## Subtask 7 (13 points)
* `C = 2, N \leq 60`

## Subtask 8 (14 points)
* `C = 2, N \leq 200`

## Subtask 9 (15 points)
* `C = 2, N \leq 3000`

## Subtask 10 (26 points)
* `C = 2, N \leq 100\ 000`

# Examples

`stdin`

```
1 7 1
1 2 5 6 7 4 3
```

`stdout`

```
7
```

`stdin`

```
2 7 0
2 5 1 6 7 4 3
```

`stdout`

```
9 7 6 7 8 10 12
```

