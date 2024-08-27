## Task

Given a natural number $N$. The DivisorGraph of number $N$ is defined as a directed graph with $NrDivizori(N)$ nodes obtained as follows:
1. Each divisor of $N$ is associated with exactly one node. Likewise, each node is associated with exactly one divisor of $N$. In other words, there is a bijection between the divisors of $N$ and the nodes of the graph.
2. For any pair $(A, B)$ of divisors of $N$ that satisfy $A > B$ and for which $B$ divides $A$, a directed arc is added from the node associated with $A$ to the node associated with $B$.

Given a directed graph $G$, which is guaranteed to be the DivisorGraph of a natural number, find the smallest number that produces a DivisorGraph isomorphic to $G$. Since this number can be very large, return its remainder when divided by $10^9 + 7$ (One billion seven).

## Input data

The input file `divisorgraph.in` will contain the first line that contains an integer $T$ representing the number of tests in the file. Each test follows the format:

The first line contains the numbers $V$ and $E$ representing the number of nodes and the number of arcs of $G$, respectively. The next $E$ lines contain two numbers $x$ and $y$, signifying that there is an arc $x \rightarrow y$.

## Output data

The output file `divisorgraph.out` will contain $T$ lines, each containing the answer for the corresponding test modulo $1000000007$.

## Constraints and clarifications

$1 \leq T \leq 3$

$1 \leq V \leq 5000$

$0 \leq E \leq 450000$

Two graphs $A$ and $B$ are isomorphic if and only if there exists a bijection between them, $f$, such that the arc $f(x) \rightarrow f(y)$ appears in $B$ if and only if the arc $x \rightarrow y$ appears in $A$.

There are 2 groups of tests.

The first is worth 30 points and additionally respects the restriction $E \leq 500$. You will have full feedback on this group.

The second is worth 70 points and respects only the above-stated constraints. You will receive feedback on a randomly chosen test from this group.

## Example

`divisorgraph.in`
```
1
3
3
1 2
1 3
2 3
```

`divisorgraph.out`
```
4
```