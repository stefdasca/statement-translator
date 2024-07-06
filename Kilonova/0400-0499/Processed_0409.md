# Task

The island CLand consists of `N` communal settlements, numbered from `1` to `N`, connected by `N-1` bidirectional paths. It is known that there is only one way to travel from any settlement to any other by using the existing paths (in other words, the island is shaped like a tree). Each settlement has a coefficient of intelligence for the people living there (an integer, **which may be negative**).

The censorship commission wants to divide the island into `K` counties such that between any two settlements in the same county, it is possible to travel from one to the other using the existing paths and **without ever leaving the county**.

We define the *anarchy* of a county as the difference between the maximum intelligence coefficient and the minimum intelligence coefficient of the settlements in the county. We define the *total anarchy* as the sum of the anarchies of the `K` counties.

# Task

Given the value of `N`, the `N-1` paths in CLand, and the intelligence coefficients of the `N` settlements, determine for each value of `K` from `1` to `N` the maximum possible anarchy of a division into exactly `K` counties of the island.

# Input data

The first line of the input file `anarhie.in` contains the value `N`, representing the number of settlements in CLand. The second line contains `N` integers separated by spaces, representing the intelligence coefficients associated with the `N` settlements. The next `N-1` lines each contain two numbers `a` and `b`, separated by a space, indicating that there is a path between settlements `a` and `b`.

# Output data

The first line of the output file `anarhie.out` contains `N` numbers, separated by spaces, the `K`-th of which represents the maximum possible anarchy of a division into `K` counties of the island.

# Constraints and clarifications

* `1 \leq N \leq 2000`
* `-1000000 \leq intelligence coefficients \leq 1000000`
* For tests worth `12` points `N \leq 20`
* For other tests worth `63` points `N \leq 300`

# Examples

`anarhie.in`
```
5
5 6 7 -7 3
3 5
1 5
2 1
4 1
```
`anarhie.out`
```
14 17 16 12 0
```

`anarhie.in`
```
17
1 3 -2 9 4 -2 5 -9 3 -8 -3 6 9 5 -2 -7 -5
14 1
13 14
14 6
6 8
12 2
3 1
11 4
3 10
1 5
6 7
2 9
16 5
12 10
17 15
4 10
17 7
```
`anarhie.out`
```
18 35 47 56 65 68 68 68 68 65 61 54 47 38 28 17 0
```