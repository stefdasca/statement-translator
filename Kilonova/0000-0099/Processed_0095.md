Knowing that you have learned quite well how to configure Neuralink servers (so well that you make a new server daily), you have decided to take full control of the network and create your own communication tower system (whose positions can be represented as points on the `Ox` axis). You are thinking of buying a network of towers, which you want to split into `K` sub-networks, so that each tower is in exactly one network. The only criterion you have is that two towers in sub-network `i` should be at least $R_i$ distance apart (otherwise, they would be redundant for your network). You find several offers for tower networks that you can buy and want to see for each if it can be split into sub-networks according to your criterion.

# Input data
The first line contains a number `T` representing the number of offers. The next `3T` lines contain the `T` scenarios.
Line `3i + 1` contains the values `N` and `K` for the `i`-th scenario.
Line `3i + 2` contains the values $R_i$ for the `i`-th scenario.
Line `3i + 3` contains `N` values $P_i$, the coordinates of the towers for the `i`-th scenario.

# Output data
`T` lines will be printed, for each test `1` if the towers can be split according to the given criterion, and `0` if not.

# Constraints and clarifications
* `4 \leq T \leq 1000`
* `1 \leq K \leq 3`
* $K < N < \frac{S}{4} \leq 5 \cdot 10^5$, where `S` is the sum of all `N` in a test.
* $1 \leq R_i \leq 10^8$ for `1 \leq i < K`
* $0 \leq P_i \leq 10^8$ for `1 \leq i < N`
* $P_i < P_{i+1}$ for `1 \leq i < N`

## Subtask 1 (4 points)
* $S \leq 2 \cdot 10^6$
* `K = 1`

## Subtask 2 (5 points)
* $S \leq 2 \cdot 10^6$
* `K = 3`
* $R_0 = R_1 = R_2$

## Subtask 3 (9 points)
* `S \leq 40`
* `K = 3`

## Subtask 4 (11 points)
* `S \leq 800`
* `K = 3`

## Subtask 5 (13 points)
* $S \leq 2 \cdot 10^6$
* `K = 2`

## Subtask 6 (14 points)
* `S \leq 6 000`
* `K = 3`

## Subtask 7 (22 points)
* $S \leq 5 \cdot 10^5$
* `K = 3`

## Subtask 8 (22 points)
* $S \leq 2 \cdot 10^6$
* `K = 3`

# Example

`stdin`

```
2
7 2
8 5
1 2 4 9 11 14 15
7 3
8 5 10
1 2 4 9 11 14 15
```

`stdout`

```
0
1
```

Explanations
---

For the first offer, there is no valid split into sub-networks.
For the second offer, you can form the first sub-network from towers at coordinates `1` and `11`, the second from towers at coordinates `2`, `9` and `14`, and the third from towers at coordinates `4` and `15`.