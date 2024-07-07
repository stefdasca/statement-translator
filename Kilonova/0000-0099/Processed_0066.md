
GrandPa (abbreviated GP) was very passionate about algorithmic competitions. In his youth, he participated in `N` prestigious contests, and at each of them, he managed to rank first and win a trophy. To identify them more easily, he assigned each trophy a number between `1` and `N`, so that any two distinct trophies were assigned **distinct** numbers.

The `N` trophies are now arranged in GrandPa's house on shelf `A`. The `i`-th trophy (`1 \leq i \leq N`), from left to right, is the one with number `P[i]`. GrandPa will soon be visited by his grandchildren, whom he wants to impress with his trophies. Therefore, he will move the trophies from shelf `A` to shelf `B` (which is initially empty) by repeatedly applying the following operation:
* Either the leftmost trophy on shelf `A` or the rightmost trophy on shelf `A` is chosen.
* This trophy is moved to shelf `B`, either to the left of all trophies already on shelf `B`, or to the right of them. If shelf `B` is empty, the trophy can be placed anywhere.

This operation will be applied until shelf `A` becomes empty, and all trophies have been moved to shelf `B`.

After all moves are performed, let `Q[i]` (`1 \leq i \leq N`) be the `i`-th trophy on shelf `B`, from left to right. To impress his grandchildren, GrandPa wants to perform the moving operations so that the sequence `Q` is lexicographically larger than any other sequence `Q'` that could be obtained by the described method. Find this maximum lexicographic sequence `Q`.

# Input data
The first line of the input file will contain the value `N`. The second line will contain `P[1], ... , P[N]`.

# Output data
Print a single line containing `Q[1], ... , Q[N]`.

# Constraints and clarifications
* `1 \leq N \leq 100\ 000`
* `1 \leq P[i] \leq N`
* `P[i] \ne P[j]` for `i \ne j`
* A sequence `A` of length `K` is lexicographically larger than a sequence `B` of length `K` if there exists a position `p` (`1 \leq p \leq K`) such that `A[p] > B[p]` and `A[i] = B[i]` for all `1 \leq i < p`.

## Subtask 1 (6 points)
* `N \leq 10`
## Subtask 2 (7 points)
* `N \leq 18`
## Subtask 3 (25 points)
* `N \leq 100`
## Subtask 4 (13 points)
* `N \leq 1000`
## Subtask 5 (14 points)
* `P[1] = N - 1` and `P[N] = N`
## Subtask 6 (35 points)
* No additional constraints.

# Examples

`stdin`

```
4
3 2 4 1
```

`stdout`

```
4 3 2 1
```

`stdin`

```
6
1 4 2 6 5 3
```

`stdout`

```
6 5 4 3 1 2
```

`stdin`

```
10
9 7 8 5 1 4 2 3 6 10
```

`stdout`

```
10 9 7 8 6 5 3 2 4 1
```

Explanations
---

In the first example, the shelves have the following states:

| Shelf A  | Shelf B  |
|----------|----------|
| 3 2 4 1  |          |
| 2 4 1    | 3        |
| 4 1      | 3 2      |
| 4        | 3 2 1    |
|          | 4 3 2 1  |

In the second example, the shelves have the following states:

| Shelf A      | Shelf B      |
|--------------|--------------|
| 1 4 2 6 5 3  |              |
| 4 2 6 5 3    | 1            |
| 4 2 6 5      | 3 1          |
| 2 6 5        | 4 3 1        |
| 6 5          | 4 3 1 2      |
| 6            | 5 4 3 1 2    |
|              | 6 5 4 3 1 2  |
```
