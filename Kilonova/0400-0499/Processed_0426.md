Fresh out of college, Bujorel decided that the best career he could pursue is that of a hacker. Thus, he came across a network of `N` computers, labeled from `1` to `N`, arranged in the form of a weighted graph which is a tree. Each edge has a weight, which represents the distance between the two computers located at the nodes of the edge. The distance between any two computers is defined as the sum of the distances on the path between them.

Before starting his attack, Bujorel will have `M` tasks. A task is in the form of a pair `(x, p)`, where `x` represents the index of a computer in the tree, and `p` a distance. He wants to determine the position on an edge where a new computer can be placed so that the distance between the new computer and the computer with index `x` is exactly `p`.

# Task
To become Bujorel's apprentice, you must correctly answer all `M` tasks.

# Input data
The input file `hacker.in` contains on the first line `N` and `M`, the number of computers in the network, and the number of queries, respectively. The next `N - 1` lines contain triplets of the form `(x, y, d)` representing a direct link between computer `x` and computer `y` with distance `d`. The last `M` lines contain pairs of the form `(x, p)` representing the task: "Find two computers `a` and `b` in the tree between which there is an edge, and a position `k` on the edge, such that the sum of `k` and the distance from `x` to `a` is exactly `p`."

# Output data
The output file `hacker.out` will contain `M` lines representing the answers to the `M` tasks. An answer will be in the form `(a, b, k)` indicating that on the edge between computers `a` and `b` a new computer will be placed at distance `k` from `a`.

# Constraints and clarifications
* `1 \leq N, M \leq 100 000`
* `1 \leq x, y \leq N`
* `1 \leq d \leq 64`
* For an answer of the form `(a, b, k)`, `k` must be in the interval `[0, D(a, b)]`, where `D(a, b)` is the distance from computer `a` to computer `b`.
* All numbers in the input and output files will be natural numbers.
* It is guaranteed that for each query there is an answer.
* Any correct solution is accepted.

# Example
`hacker.in`
```
8 4
1 2 1
1 7 1
7 8 1
2 3 1 
2 4 1
4 5 1
4 6 1
4 3
2 1
2 3
1 3	
```
`hacker.out`
```
7 1 0
1 7 0
8 7 0
6 4 0
