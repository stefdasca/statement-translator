
In the city of Etsivograt, there are `n` intersections numbered from `1` to `n`. Between some pairs of intersections, there are streets. In total, there are `m` streets, and the street network formed by these has been designed such that there is at least one connection between any two intersections, which may be direct or may pass through other intersections.

After the cold season, the state of the streets has become deplorable, so it is decided to repave them. The cost of repaving each street is known.

With limited resources, the mayor decides to repave a few streets that will ensure at least one connection (direct or indirect, passing through other intersections) between any two intersections, and the sum of the repaving costs of these few streets should be minimal. His advisors present him with a list of all possible repaving possibilities that ensure connections (direct or indirect) between all intersections and for which the sum of the costs is minimal. The mayor observes that there are streets that appear in all these repaving possibilities. He considers these streets as "vital."

# Task
Write a program that determines the number of vital streets in the street network of the city of Etsivograt, as well as which these vital streets are.

# Input data 
The input file `vitale.in` contains on the first line two natural numbers `n m` separated by a space representing the number of intersections and the number of streets in the city, respectively. On the next `m` lines, there are three natural numbers `a b c` separated by a space; `a` and `b` represent the ordinal numbers of two distinct intersections in the city between which there is a street, and `c` represents the repaving cost of the street that connects intersections `a` and `b`.

# Output data
The output file `vitale.out` will contain on the first line a natural number `x`, representing the number of vital streets in the city. On each of the next `x` lines, two natural numbers will be written, representing the ordinal numbers of the intersections that delimit a vital street, and the first number will be strictly smaller than the second. These `x` lines will be sorted in lexicographical order, in other words, denoting with $a_i$ and $b_i$ the two numbers on line `i+1` and with $a_j$ and $b_j$ the two numbers on line `j+1`, if `i<j` then $a_i < a_j$ or $a_i=a_j$ and $b_i < b_j$.

# Constraints

* `1 \ \leq \ n \ \leq \ 50 \ 000`
* `1 \ \leq \ m \ \leq \ 100 \ 000`
* `1 \ \leq \ c \ \leq \ 1 \ 000 \ 000 \ 000`
* Between any two intersections, there can be at most one street. The streets are bidirectional.

# Example

`vitale.in`
```
4 5
1 2 1
2 3 2
4 3 1
1 4 2
1 3 6
```

`vitale.out`
```
2
1 2
3 4
```

Explanations
---

The intersections and streets in the example correspond to the adjacent configuration.
The repaving possibilities that meet the requirements are composed of the streets: 
`1-2, 1-4, 3-4`   and   `1-2, 2-3, 3-4`
There are two vital edges (that appear in both possibilities), namely `1-2` and `3-4`
~[vitale.png]
```
