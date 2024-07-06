# Archipelago RGB

The RGB Archipelago consists of islands belonging to the countries $R$, $G$, and $B$. We can represent the map of the archipelago as a matrix with $n$ rows and $m$ columns, with elements from the set $\{0, 1, 2, 3\}$. An element equal to $0$ represents a water-covered area; an element equal to $1$ represents a land area belonging to an island from country $R$, an element equal to $2$ represents a land area belonging to an island from country $G$, and an element equal to $3$ represents a land area belonging to an island from country $B$.

Two matrix elements are considered neighbors if they have the same value and are either consecutive on a row or consecutive on a column. Two elements belong to the same island if they are neighbors or if a path can be reached from one element to the other along which any two consecutive elements are neighbors.

To encourage collaborative relationships between the countries $R$ and $G$, it is desired to build a bridge connecting an island belonging to country $R$ with an island belonging to country $G$. The bridge must meet the following conditions:

* It must start in a water area that is consecutive on the row or column with an area belonging to country $R$;
* It must end in a water area that is consecutive on the row or column with an area belonging to country $G$;
* It must traverse only water-covered areas;
* Any two consecutive elements of the bridge must be neighbors;
* The length of the bridge must be minimal (the length of the bridge is equal to the number of elements traversed by the bridge).

# Task

Given the map of the archipelago, determine how many islands belong to each country, as well as the minimal length of a bridge that satisfies the conditions from the statement.

# Input data

The input file `insule.in` contains on the first line the natural numbers $n$ and $m$, separated by a space. On the next $n$ lines, the map of the archipelago is described. On each of these $n$ lines, there are $m$ values from the set $\{0, 1, 2, 3\}$; the values are not separated by spaces.

# Output data

The output file `insule.out` will contain a single line where four natural numbers separated by spaces are written `NR` `NG` `NB` `Lg`, where `NR` represents the number of islands belonging to country $R$, `NG` the number of islands belonging to country $G$, `NB` the number of islands belonging to country $B$, and `Lg` the minimal length of the bridge.

# Constraints and clarifications

* $1 < n, m \leq 100$;
* It is guaranteed that on the map there is at least one element $1$, one element $2$ and one element $0$;
* 40% of the score is awarded for correctly determining the number of islands in each country; full score is awarded for correctly solving all requirements;
* The start and end of the bridge can coincide;
* There is always a solution for the test data.

# Example

`insule.in`
```
6 7
1000320
0110313
3333000
2033000
2203011
2000010
```

`insule.out`
```
4 2 3 4
```

## Explanation

Country $R$ has $4$ islands, country $G$ has $2$ islands, and country $B$ has $3$ islands.

The minimal length of a bridge that can be constructed is $4$; for example, the bridge crosses the cells $(6,5)$, $(6,4)$, $(6,3)$, $(6,2)$.