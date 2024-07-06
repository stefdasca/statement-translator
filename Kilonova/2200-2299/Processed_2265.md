# Task

Following the international success of Miruna's shgraphs, Laura decided to launch her own type of graph, called _ubergraf_. An _ubergraf_ is a directed, acyclic, unlabeled graph, with the property that the sets of neighbors of any two distinct vertices are distinct.
Consider the following examples of graphs:

~[ubergraf0.png]

We observe that the first example is not an _ubergraf_, because there exist two vertices whose set of neighbors is the empty set (the two vertices with out-degree $0$). The second example is also not an _ubergraf_, because the two vertices with in-degree $0$ have the same set of neighbors. The third example is an _ubergraf_. The last example is not an _ubergraf_, because it is not an acyclic graph.
Laura now faces a new problem: given a natural number $N$, she would like to know how many distinct _ubergraf_-s with $N$ vertices exist. Since the number of _ubergraf_-s can be very large, she would be satisfied if you provide the result modulo $P$, where $P$ is a given prime number.

# Task

Determine the number of _ubergraf_-s with $N$ nodes modulo $P$.

# Input data

The input file `ubergraf.in` contains two integers $N$ and $P$ with the meaning described in the statement.

# Output data

The output file `ubergraf.out` contains a single integer representing the required number.

# Constraints and clarifications

* $1 \leq N \leq 300$
* $N < P \leq 30 \ 000$, $P$ prime
* For $65\%$ of the tests $N \leq 150$.
* Two _ubergraf_-s are considered distinct if there does not exist a bijection from the set of vertices to the set of vertices such that there is an arc between two vertices if and only if there is an arc between the corresponding vertices.

# Example 1

`ubergraf.in`
```
4 37
```

`ubergraf.out`
```
9
```

## Explanation

The $9$ ubergraf-s corresponding to the first example are:

~[ubergraf.png]

# Example 2

`ubergraf.in`
```
60 9221
```

`ubergraf.out`
```
2385
```
