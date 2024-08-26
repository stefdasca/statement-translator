# Arugaktus

Arugak is very interested in graphs, so she defined a new type of graph: the arugaktus. An arugaktus is an undirected connected graph where any simple cycle has an odd length. Arugak has drawn an arugaktus with $N$ nodes and $M$ edges. She also wants to buy $K$ different colored pencils but is unsure how many $K$ should be. To decide, she has $Q$ possible values for $K$, and wants to know, for each value, in how many ways she can color the nodes of her arugaktus with $K$ colors such that any two nodes connected by an edge are colored differently, modulo $1.000.000.7$. Can you help her?

## Input data

The input file `arugaktus.in` will contain, on the first line, $T$, the number of test cases found in the file. The first line of any test case will contain the numbers $N$, $M$, $Q$, with the meanings described above. The next $M$ lines contain a pair $i$, $j$ of nodes, indicating that there is an edge between node $i$ and node $j$. The next $Q$ lines will contain a different value of $K$ that Arugak is interested in.

## Output data

The output file `arugaktus.out` will contain the answers for the $T$ test cases, in order. For each test case, print, on a separate line, the answer for each value of $K$ that Arugak is interested in, in order.

## Constraints and clarifications

$1 \leq T \leq 20$

$1 \leq N \leq 100\,000$

$1 \leq Q \leq 10$

$1 \leq K \leq 1\,000\,000\,000$

## Example

`arugaktus.in`

```
1
5 5 3
1 2
2 3
3 1
1 4
1 5
1
2
3
```

`arugaktus.out`

```
0
0
24
```