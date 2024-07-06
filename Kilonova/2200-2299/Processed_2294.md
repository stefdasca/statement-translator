Dubota is now a full-fledged police officer and has received the mission to patrol $N$ strategic objectives. The $N$ objectives are connected by $M$ bidirectional roads. Dubota wants to find the longest possible route of objectives to patrol. A route is a succession of nodes $o_1, o_2, \dots o_K$ such that $o_i \neq o_j$, $\forall i \neq j$ and there is a road from $o_i$ to $o_{i+1}$ for $1 \leq i < K$ and a road between $o_1$ and $o_K$.

# Task

Find the longest possible route of objectives for Dubota to patrol.

# Input data

The first line of the file `x-hamilton.in` contains two numbers, $N$ and $M$. The following $M$ lines contain $2$ numbers each, $u$, $v$, representing a road from objective $u$ to objective $v$.

# Output data

The first line of the file `x-hamilton.out` will contain the length of the longest route found, followed by the second line containing the description of the cycle, by listing the indices of the nodes on the route.
You are provided with 10 input files used for evaluation, named `0-hamilton.in`, `1-hamilton.in` $\dots$ `9-hamilton.in`. For each input file `x-hamilton.in`, you are required to generate an output file `x-hamilton.out` where you write the requested route. The files should be submitted one by one.

# Constraints and clarifications

* The score for a test is calculated as follows, where $K$ is the length of the displayed route:
    * For $N \leq 5000$: $\max(0, 10 - N + K)$
    * For $N > 5000$: $\lfloor 10 \cdot \left( \frac{K}{N} \right)^6 \rfloor$.

# Example

`hamilton.in`
```
8 12
1 2
1 6
2 3
2 4
2 6
3 5
3 7
4 6
4 7
5 8
6 7
7 8
```

`hamilton.out`
```
8
1 2 3 5 8 7 4 6
```
