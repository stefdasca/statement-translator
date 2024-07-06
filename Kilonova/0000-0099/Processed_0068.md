In the country there are `N` ski resorts, numbered from `1` to `N`, connected by `N - 1` bidirectional roads, with the property that between any two resorts there exists a direct or indirect road (note: the country does not invest in tourism more than is minimally necessary). The ski season consists of `M` weeks, numbered from `1` to `M`. Every week Marcel the Skier visits a ski resort, noting in his diary the last time he skied there. Because the travel costs on the country's roads are quite high, in consecutive weeks Marcel will ski in resorts between which there is a direct road (one of the aforementioned `N - 1`). Note that Marcel will never ski in the same resort in two consecutive weeks — that would be boring.

At the end of the season, Marcel extracts from his diary `N` numbers: $v_1, ... v_N$, where $v_i$ signifies the number of the week when he last skied in resort `i \in \{1, ... , N\}`. You, seeing the numbers in the sequence `v`, do not trust him and want to check if he has made a mistake.

Given `N`, the `N - 1` roads in the country, and the numbers $v_1, ... v_N$, determine if Marcel surely made a mistake transcribing the numbers `v` or if what he says could be true. Moreover, you must solve the problem for `T` independent scenarios.

# Task
On the first line will be found `T`, the number of scenarios. Then follow `T` groups of lines, each describing a scenario to solve. On the first line of a scenario is `N`, the number of resorts in the country. On the second line are `N` numbers separated by spaces: $v_1 v_2 ... v_N$. On the next `N - 1` lines are pairs of numbers `a b`, indicating the existence of a bidirectional road between resorts `a` and `b`.

# Input data
The first line contains `T`, the number of scenarios. Then follow `T` groups of lines, each describing a scenario to solve. The first line of a scenario contains `N`, the number of resorts in the country. The second line contains `N` numbers separated by spaces: $v_1 v_2 ... v_N$. The next `N - 1` lines contain pairs of numbers `a b`, indicating the existence of a bidirectional road between resorts `a` and `b`.

# Output data
A single line will be printed, consisting of `T` binary digits. The `i`-th digit, for `1 \leq i \leq T`, will be `1` if in the `i`-th scenario what Marcel says could be true, and `0` otherwise.

# Constraints and clarifications
* `1 \leq T \leq 15\ 000`
* `2 \leq N \leq 100\ 000`
* `2 \leq M \leq 100\ 000\ 000\ 000`
* Marcel visits each resort at least once: $1 \leq v_i \leq M$ for `i \in \{1, ... , N\}`.
* The sum of the values of `N` for the `T` scenarios is at most `400\ 000`.

## Subtask 1 (7 points)
* `N \leq 3`

## Subtask 2 (19 points)
* Exactly `2` resorts are "isolated" — there is only one bidirectional road extending from each of these `2` resorts.

## Subtask 3 (18 points)
* `N \leq 2\ 000`
* The sum of the values of `N` for the `T` scenarios is at most `8\ 000`.

## Subtask 4 (19 points)
* For any two resorts `a, b \in {1, ... , N}` it is possible to reach `b` from `a` using at most `200` direct roads.

## Subtask 5 (37 points)
* Without additional restrictions.

# Examples

`stdin`

```
1
6
11 6 5 3 10 9
1 2
2 3
2 4
1 5
5 6
```

`stdout`

```
1
```

`stdin`

```
2
9
10 9 8 13 1 7 12 14 6
1 2
1 4
2 3
3 5
3 6
6 9
4 7
4 8
4
5 4 5 3
1 2
1 3
2 4
```

`stdout`

```
10
```

Explanation
---

For the first scenario in the first example, Marcel could pass, in order, through the resorts:
`4, 2, 4, 2, 3, 2, 1, 5, 6, 5, 1`

For the first scenario in the second example, Marcel could pass, in order, through the resorts:
`5, 3, 6, 9, 6, 9, 6, 3, 2, 1, 4, 7, 4, 8`

For the second scenario in the second example, it is impossible for Marcel to be both in resort `1` and in resort `3` at the same time.
