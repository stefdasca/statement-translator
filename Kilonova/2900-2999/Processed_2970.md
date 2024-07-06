> "... Alexandru Lăpușneanul, after being defeated twice by Despot's armies, fled to
Constantinople, managed to gather Turkish troops and is now returning to oust the usurper Tomșa and reclaim his throne, which he would not have lost if he had not been betrayed by the boyars."

Upon returning to Moldova, Alexandru Lăpușneanul wants to take revenge on the boyars in a draconic manner, and the only way they can escape the ruler's wrath is by solving the following problem:
# Task

Given a tree with $N$ nodes and root at node $1$, each node $i$ having an associated value $v_i$. There are $Q$ queries of the form: $x, l, r$ ($l \\le r$), which ask to find out how many nodes in the subtree of node $x$ have values between $l$ and $r$ (inclusive).

# Input data
The first line will contain the natural number $N$. The second line will contain $N$ natural numbers $v_1, v_2, ...,v_N$ - the values associated with the $N$ nodes. The next $N-1$ lines will contain 2 natural numbers $u$ and $v$, indicating that there is an edge in the tree between nodes $u$ and $v$. The following line will contain the natural number $Q$, representing the number of queries. The next $Q$ lines contain 3 natural numbers $x, l, r$ with the meaning given in the statement.

# Output data
$Q$ lines will be displayed, on the $i$-th line containing the answer to the $i$-th query.

# Constraints and clarifications
- $1 \\leq N \\leq 150\\ 000$
- $1 \\leq Q \\leq 150\\ 000$
- $1 \\leq v_i \\leq 10^9$ for $1 \\leq i \\leq N$
- For tests worth $20$ points, $1 \\leq N \\leq 1000$ and $1 \\leq Q \\leq 1000$
- Additional tests were added following the competition stage.

# Example

`stdin`
```
5
10 17 10 19 4
2 1
1 3
2 4
2 5
3
2 6 19
1 11 17
1 4 19
```

`stdout`
```
2
1
5
```