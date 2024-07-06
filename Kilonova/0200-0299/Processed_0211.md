Zhuge Liang, also known by the name Kongming, wants to restore the Han dynasty to power. After unifying the Shu Han region, he plans a military campaign against the Cao Wei region.

China is composed of `N` territories numbered from `0` to `N - 1` and `M` bidirectional roads. Being a vast country, the travel duration on any road is one day. Formally, it is an undirected multigraph without costs, which can include loops.

The army is initially positioned in the Shu Han region, represented by the node `S`, and needs to reach the Cao Wei region, represented by the node `T`, traveling only on roads. Once during the journey, when the army is in a region (i.e., not traveling on a road), the enemy army can block exactly one road, making its use further impossible. The army will immediately find out which road was blocked and can adjust its route as desired.

Zhuge Liang has predicted this possibility and wants to choose a route from `S` to `T` that minimizes the total travel time in the worst-case scenario. Write a program that finds the optimal time in the worst-case and finds an optimal route.

# Input data
The first line contains the numbers `N`, `M`, `S`, and `T` with the meaning given in the statement. The following `M` lines describe the edges of the graph in the form `U V`.

# Output data
The first line will contain `opt` - the optimal time in the worst case and `len` - the length of the optimal route. The next line will contain the optimal route consisting of `len + 1` regions. If there is no solution, only `-1` will be printed.

# Constraints and clarifications
* `1 \ \leq N \ \leq 100 000`
* `0 \ \leq M \ \leq 1 000 000`
* $0 \ \leq S, T, U_i, V_i < N$

## Subtask 1 (17 points)
* `1 \ \leq N \ \leq 1 000`
## Subtask 2 (19 points)
* `1 \ \leq N \ \leq 4 000`
## Subtask 3 (43 points)
* `1 \ \leq N \ \leq 30 000`
## Subtask 4 (21 points)
* `1 \ \leq N \ \leq 100 000`

# Examples

`stdin`

```
7 10 0 6
0 1
0 2
1 1
1 3
2 3
3 4
3 4
4 5
4 6
5 6
```

`stdout`

```
6 4
0 1 3 4 6
```

`stdin`

```
2 1 0 1
0 1
```

`stdout`

```
-1
```

Explanations
---

Following the planned route, when the army is at node `1`, the enemy army can block the road from `1` to `3`. The army will need to continue on the path formed by nodes `1, 0, 2, 3, 4, 6`. The length of this path is `6`.

In all possible variations where an edge is removed, the worst road will be at most `6`. Among all possible plans, the road in the output is the optimal one.