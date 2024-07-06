When he was visiting his grandparents, Cătălin discovered a Nintendo console from 1970 in the garage. Fortunately, that console also had a game. This game was called "TreeGCD". Cătălin is given a tree with `N` nodes and a number `M`. He must determine in how many ways he can assign each node a number from `1` to `M`, such that any two adjacent nodes do not have coprime numbers assigned to them (i.e., the greatest common divisor is strictly greater than `1`).

# Task
Determine the number of ways in which we can assign each node a number from `1` to `M`, such that any two nodes connected by an edge do not have coprime numbers assigned to them. The number must be displayed modulo `1.000.000.007`.

# Input data
In the file `treegcd.in`, the first line contains two nonzero natural numbers `N` and `M`, separated by a space. On each of the next `N-1` lines, there are two nonzero natural numbers `x` and `y`, separated by a space, indicating that nodes `x` and `y` are adjacent.

# Output data
In the file `treegcd.out`, there must be a single number. This number represents the number of ways to assign each node a value from `1` to `M`, such that for any two adjacent nodes, the associated values are not coprime. Since the result can be very large, the remainder modulo ($10^9+7$) of the requested number will be displayed.

# Constraints and clarifications
* `2 \leq N \leq 100`;
* `2 \leq M \leq 10000`;
* for tests worth `4` points, we have `N = 2` and `M \leq 1000`;
* for other tests worth `13` points, we have `N \leq 6` and `M \leq 10`;
* for tests worth `40` points, we have `N \leq 100` and `M \leq 100`;
* for other tests worth `43` points, we have `N \leq 100` and `M \leq 10000`

# Example

`treegcd.in`

```
2 6
1 2
```

`treegcd.out`

```
13
```

Explanations
---

The pairs of values associated with nodes `1`, `2` are: `(2,2), (2,4), (2,6), (3,3), (3,6), (4,2), (4,4), (4,6), (5,5), (6,2), (6,3), (6,4), (6,6)`.

`treegcd.in`

```
5 6
5 3
3 1
5 4
3 2
```

`treegcd.out`

```
397
```

Explanations
---

The result is `397`.

`treegcd.in`

```
10 67
1 2
1 3
2 4
2 5
2 6
2 7
5 8
5 9
7 10
```

`treegcd.out`

```
534323877
```

Explanations
---

The result is `6315455578532062`, and `6315455578532062 % 1000000007 = 534323877`.