The given text has been translated from Romanian to English while preserving the structure, mathematical values, variable names, and format as requested. Grammar and syntax errors have been fixed according to the rules of English language.

---

Given a tree with $N$ nodes numbered from $1$ to $N$, with the root being the node numbered $1$.  
Each node $i (1 \leq i \leq N)$ has an associated value $C_i$.  
We need to answer queries of the type: "What is the sum of the values associated with the nodes in the subtree rooted at node $i$ at a distance not exceeding $j$ from node $i$?"  
The distance from node $x$ to node $y$ is equal to the number of edges on the path from $x$ to $y$.

# Task

Write a program that answers $M$ queries of the specified type.

# Input data

The input file `arb.in` contains on the first line the natural number $N$. The second line contains $N$ numbers representing the costs associated with the $N$ nodes. The third line contains $N-1$ numbers, the $i$-th number representing the parent of the node numbered $i+1$. The fourth line contains the natural number $M$. The following $M$ lines each contain two natural numbers $i \\ j$ representing a query of the type specified in the prompt ($i$ is the root of the subtree, and $j$ is the maximum distance). The values on the same line are separated by a space.

# Output data

The output file `arb.out` will contain $M$ lines. Line $i$ contains a single natural number representing the answer to the $i$-th query in the input file.

# Constraints and clarifications

* $1 \leq N \leq 250\ 000$
* $1 \leq M \leq 500\ 000$
* $0 \leq C_i \leq 5\ 000$, $1 \leq i \leq N$

# Example

`arb.in`
```
7
1 2 2 1 3 4 5
1 1 1 3 3 6
3
3 1
3 2
1 0
```

`arb.out`
```
9
14
1
```

