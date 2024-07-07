
*This problem is dedicated to those who wait for the metro with the greatest ardor: the inhabitants of Drumul Taberei.*  

Given the plan of a metro network with `N` stations and `M` bidirectional tunnels between stations. Two metro stations are called *neighbors* if there is a tunnel between them in this plan. Each station `i` has an associated profit $p_i$ given.  

Henry has recently been promoted from a position in the cleaning department to the project manager of the company. Since there are no funds for building the entire metro network, Henry must choose a subset of stations to be built, such that any two chosen stations are not neighbors in the original plan. To maintain his position in the company, the sum of the profits of the chosen stations in this subset must be maximum.

# Task
Given `N`, `M`, the profits provided by each of the `N` stations, and the initial plan of the network, determine the maximum sum of the profits of the stations that Henry can choose so that any two chosen stations are not neighbors in the initial plan.

# Input data
The first line of the input file `metrou.in` will contain two natural numbers `N` and `M` separated by a space, representing the number of stations and the number of tunnels in the initial plan, respectively. The second line will contain `N` natural numbers separated by a space, the `i`-th of these representing the profit $p_i$ provided if station `i` were to be built. The following `M` lines will contain two natural numbers `x` and `y` separated by a space, indicating that a tunnel connects stations `x` and `y` in the initial plan.

# Output data
The output file `metrou.out` will contain a single line containing a single natural number, representing the maximum sum of the profits of the stations that Henry can choose such that any two chosen stations are not neighbors in the initial plan.

# Constraints and clarifications
* `1 \leq N \leq 100 000`
* `1 \leq M \leq 150 000`
* `1 \leq x, y \leq N`
* $1 \leq p_i \leq 10\ 000$, for any `i`, `1 \leq i \leq N`.
* There are at most `15` stations that are neighbors with `3` or more stations in the given plan.
* There are at most `20` stations that are neighbors with exactly one station in the given plan.
* For `20%` of tests, `N \leq 20`.
* For another `10%` of tests, the network plan is a simple chain within an undirected graph.
* For another `10%` of tests, the network plan is a simple cycle within an undirected graph.
* We can reach any station from any other station following the existing tunnels in the initial plan.

# Example

`metrou.in`
```
8 10
1 3 2 5 4 1 2 1
1 2
2 3
3 4
4 5
5 3
3 6
2 6
2 7
7 8
8 3
```

`metrou.out`
```
9
```

Explanations
---
We have `N = 8` metro stations and `M = 10` tunnels in the plan.  
The subset of stations `{2, 4, 8}` ensures the maximum profit of `3 + 5 + 1 = 9`.  
We observe that the subset respects the rule described, as there is no tunnel connecting stations `2-4`, `2-8`, or `4-8`.
