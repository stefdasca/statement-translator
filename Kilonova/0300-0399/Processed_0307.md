
Nika is a naturally curious girl. She found an undirected connected graph with `N` nodes and `N` edges in her grandmother's box, with one of the edges designated as the edge that closes a cycle. Knowing that each edge has a cost, Nika asks three types of questions:
* `0 a b` : "What is the minimum distance between nodes `a` and `b`, if an edge can be crossed at most once?"
* `1 m c` : "How does the graph look if the cost of edge `m` is changed to value `c`?". The graph is modified by this operation, and the change is persistent.
* `2 a b c` : "How does the graph look if the edge that closes a cycle is deleted, and an edge between `a` and `b` with cost `c` is added?". The graph is modified by this operation, and the new edge will become the edge that closes a cycle. The change is persistent.

From this moment, the main goal of your life has become solving this problem, in order to join the National Informatics Team.

# Task
Answer Nika's questions as quickly as possible (otherwise *shewillgetboredandyou’llbewithoutprize*).

# Input data
The input file `nikagraf.in` contains the following data:
- The first line contains two natural numbers `N` and `Q` representing the number of nodes of the graph and the number of questions from the girl;
- The next `N` lines contain three numbers `x y c` representing the edge from `x` to `y` with the cost `c`. The first `N – 1` edges define a tree, and the last edge will represent the edge that closes a cycle. This edge will be changed when applying an operation of type `2`.
- The next `Q` lines contain the questions in the format described in the statement.

# Output data
The output file `nikagraf.out` will contain the answers only to type `0` questions (for the others you will be trusted).

# Constraints and clarifications
* `1 \leq N \leq 100 000`;
* `1 \leq Q \leq 200 000`;
* $-2 \cdot 10^4 \leq cost \leq 2 \cdot 10^4$;
* Edges are indexed from `1`;
* There is no edge from a node to itself and there is no more than one edge between two nodes;
* For `20%` of the tests, `N` and `Q` will not exceed `3000`;
* For `30%` of the tests, there will be no operations of type `1`, and for another `30%` of the tests, there will be no operations of type `2`.
* The minimum distance between two nodes `a` and `b` is defined as the sum of the costs of the edges of the shortest path between the two nodes.

# Examples
`nikagraf.in`
```
4 5
1 2 2
1 3 1
2 4 1
2 3 1
0 4 1
1 1 1
0 4 1
2 4 3 0
0 4 1
```

`nikagraf.out`
```
3
2
1
```

Explanation
---

The initial graph is: 

~[nikagraf.png]

It can be observed that the distance from `4` to `1` is `3` for both the path `4 – 2 – 1` and the path `4 – 2 – 3 – 1`.
For the second question, the answer is `2`, by taking the path `4 – 2 – 1`.
For the third question, the answer is `1`, by taking the path `4 – 3 – 1`.
```

Double-checking for grammar and/or syntax errors:
- All sentences appear to be properly constructed and clear.
- The technical terms and instructions match the provided guidelines.