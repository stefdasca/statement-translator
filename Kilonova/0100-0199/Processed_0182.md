
King Gefghev thought of visiting a country where many wonders happen, the Wonderland. This country is made up of `N` cities, numbered from `1` to `N`. Between cities `i` and `i + 1` `(1 \leq i < N)` there is a modern road that can be used only from city `i` to city `i + 1`. Being a clever guy, Gefghev realized that he can get from any city `i` to a city `j` `(j > i)` by traveling in total on `j-i` roads. Tronomir, an employee of the road maintenance department, devised a plan to construct `M` new roads to make it easier for Gefghev to travel. The roads will be built one by one, over `M` consecutive days, with the `i`-th road being built on day `i`. A road will be built from city `a` to city `b` `(1 \leq a < b - 1 < N)` and on this road, it will only be possible to travel from city `a` to city `b`. Being a travel-minded person, Gefghev is now thinking of finding out, after each road is built, between which cities he can now travel faster than he could before the road was built. In other words, he wants to know how many pairs of cities `(x, y)` `(1 \leq x < y \leq N)` have changed their minimum distance. The minimum distance between two cities `x` and `y` is the minimum number of roads that need to be traveled to get from city `x` to city `y`.

# Task
Write a program that determines for King Gefghev, after each road is built, the number of pairs of cities `(x, y)` `(1 \leq x < y \leq N)` for which the minimum distance from `x` to `y` has changed after the construction of the respective road.

# Input data
The input file `minuni.in` contains two integers `N` and `M` separated by a single space, with the significance given in the statement. On the next `M` lines, there are two natural numbers separated by a single space, `a` and `b`, indicating that a road has been built from city `a` to city `b`. The roads are built in the order given in the input file.

# Output data
The output file `minuni.out` will contain `M` natural numbers, one number per line. On line `i`, it will contain the number of pairs of cities `(x, y)` `(1 \leq x < y \leq N)` for which the minimum distance from `x` to `y` has changed, after the construction of the `i`-th road from the input file.

# Constraints and clarifications
* `1 \leq N \leq 1\ 000\ 000\ 000`
* `1 \leq M \leq 100\ 000`
* All cities between which new roads have been built are distinct.
* There are no two newly built roads, one `(a, b)` and the other `(c, d)` such that `a \leq c \leq b \leq d`.
* For `30%` of the tests `M \leq 1000`.

# Example

`minuni.in`	
```
8 3
2 4
1 5
6 8
```

`minuni.out`
```
10
4
6	
```

Explanation
---

There are `8` cities. `3` new roads will be built. After the construction of the road `2 4`, the distances between the following pairs of cities will change: 
`(1 4), (1 5), (1 6), (1 7), (1 8), (2 4), (2 5), (2 6), (2 7), (2 8)`. 
