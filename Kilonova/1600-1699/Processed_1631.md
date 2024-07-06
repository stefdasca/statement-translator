```
It's spring and the storks are returning. In our village, the poles at the edge of the road have tips that are too sharp, and therefore, the storks cannot build their nests. So there is great sadness here... But we all gathered together and decided to install a horizontal flat support on top of some poles, so that it would be easy for a stork to arrange its nest. We have $n$ poles at the edge of the road, arranged linearly and numbered from $0$ to $n - 1$.

A number of $m$ villagers came with a restriction of the form $i \\ j$, meaning that on the poles in the interval $[i, j]$ at most two supports for stork nests can be installed. The reasons for these restrictions are diverse, such as the poles being too close to each other. We will take these into account because we want all the villagers to be satisfied.

# Task

Knowing $n$, $m$ and the $m$ restrictions, determine the number of possibilities for the storks to arrange nests on the $n$ poles, modulo $700 \\ 001$.

# Input data

The input file `berze.in` contains on the first line the numbers $n$ and $m$ having the meaning in the statement. On the next $m$ lines there are two natural numbers $i$, $j$, meaning that in the pole interval $[i, i+1, i+2, \\dots, j]$ at most two supports for stork nests can be arranged.

# Output data

The output file `berze.out` will contain on a single line a natural number representing the number of possibilities to place supports for stork nests on the $n$ poles.

# Constraints and clarifications

* $2 \\leq m, n \\leq 1 \\ 000$
* $0 \\leq i < j \\leq n - 1$
* the $m$ intervals of the form $i \\ j$ are not necessarily disjoint
* at most one support for a stork nest can be installed on a pole
* for $50\\%$ of the tests $N \\leq 100$

# Example

`berze.in`
```
4 1
0 2
```

`berze.out`
```
14
```

## Explanation

Let's denote a pole without a support for a stork nest by `I` and a pole with a support by `T`. Then the $14$ solutions are:

```
I I I I 
I I I T
T I I I 
T I I T
I T I I 
I T I T
I I T I 
I I T T
T T I I 
T T I T
T I T I 
T I T T
I T T I 
I T T T
```
```