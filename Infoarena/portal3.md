# Portal3

Derpina is in a matrix with $N+1$ rows and $M+1$ columns starting at element $(0, 0)$. She wants to reach her friend Derp who is in the matrix at element $(N, M)$. At each step, Derpina can move to an adjacent cell. To reach her friend faster, Derpina has called upon a portal company. This company built $3$ pairs of portals in the matrix: $P_1$ with $P_2$, $P_3$ with $P_4$, and $P_5$ with $P_6$. Each portal $P_i$ is located in the matrix at position $(X_i, Y_i)$. To use a pair of portals $i$, Derpina must be in a cell where one of the portals from the pair $i$ is located and activate the portal. She will instantly arrive at the other portal, but the activation time for a portal from pair $i$ is $C_i$. Derpina likes to spend her time in the kitchen and wants to stay outside of it as little as possible. Derpina will ask for your help and you need to calculate the minimum time in which she reaches Derp.

## Input data

The input file `portal3.in` will contain on the first line a natural number $T$ representing the number of tests. For each test, the first line contains $N$ and $M$, the second line contains $X_1, Y_1, X_2, Y_2, C_1$, the third line contains $X_3, Y_3, X_4, Y_4, C_2$, and the fourth line contains $X_5, Y_5, X_6, Y_6, C_3$.

## Output data

The output file `portal3.out` will contain $T$ lines. On line $i$ will be the answer for test $i$.

## Constraints and clarifications

$1 \leq T \leq 10\ 000$ 

$1 \leq N, M \leq 1\ 000\ 000\ 000$ 

$0 \leq X_1, X_2, X_3, X_4, X_5, X_6 \leq N$

$0 \leq Y_1, Y_2, Y_3, Y_4, Y_5, Y_6 \leq M$

$0 \leq C_1, C_2, C_3 \leq 1\ 000\ 000\ 000$

## Example

### portal3.in
```
1
50 50
10 5 20 4 3
27 19 35 16 5
19 23 42 40 11
```

### portal3.out
```
67
```