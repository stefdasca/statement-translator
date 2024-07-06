```markdown
With the Easter holiday, Alex decided to go to the sea by car. The map of Romania is modeled as a tree (a connected acyclic undirected graph) that has `N` nodes representing the cities of the country. It is well-known that Alex is a speedster, so he wants to avoid any potential speed radars, which are placed on the edges of the tree (each edge can have at most one radar). If there is a radar on an edge, Alex will not risk and **will not** travel on that edge.

Each city has a given visit time, and we all know that Alex is very busy, so he doesn't want to waste too much time visiting. Alex starts from Gheorgheni (node `1`, considered the root) and wants to know in how many ways the radars can be placed on the map so that the total visit time of the cities accessible from node `1` equals `P`, knowing that Alex will not travel on any edge containing a radar.

This problem is quite simple for Alex, so he thought to give it to you.

# Task
Write a program to solve Alex's problem, that is, to determine in how many ways the radars can be placed on the edges so that the total visit time of the cities accessible from node `1` equals `P`.

# Input data
The file `radare.in` contains on the first line `N` and `P`, with the meanings from the statement. The next `N-1` lines will each contain two integers `x` and `y`, indicating that there is an edge between cities `x` and `y`.
The last line will contain `N` natural numbers between `1` and `P` inclusive, the `i`-th of these representing the visit time of city `i`.

# Output data
The file `radare.out` will contain a single number representing the answer to Alex's problem `modulo 31333`.

# Constraints and clarifications
* `1 \leq N \leq 3\ 000`
* `1 \leq P \leq 3\ 500`
* `1 \leq x, y \leq N`
* `1 \leq visit\ time\ of\ a\ city \leq P`
* if a radar is placed on an edge, Alex **WILL NOT** travel on that edge
* two radar configurations differ if there is at least one edge `(a, b)` which contains a radar in one configuration and doesn't in the other.
* for `30%` of the tests `N \leq 15`
* for `50%` of the tests, the visit times for each city will be `1`
* for `60%` of the tests, `N \leq 300`

# Example

`radare.in`
```
6 3
1 2
1 3
2 4
4 5
4 6
1 1 1 1 1 1
```

`radare.out`
```
5
```

Explanation
---

The `5` possible ways are:
1. there is a radar on the edge `(2,4)`
2. there are radars on the edges `(2,4), (4,5)`
3. there are radars on the edges `(2,4), (4,6)`
4. there are radars on the edges `(2, 4), (4,5), (4,6)`
5. there are radars on the edges `(1,3), (4,5), (4,6)`

~[radare.png]
```