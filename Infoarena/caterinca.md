## Task

Note: This problem statement is translated from English. This problem is about "caterinca," a Romanian word that approximately translates to "mischief" -- though an exact translation is not easy to find. Tanaka is visiting his friend, George Mirihcihc. His house can be modeled as a tree with $N$ nodes, where the nodes are rooms, and the edges are corridors. In each room, there is a party, each party having an index of "caterinca." The $i$-th party has a "caterinca" index equal to $c_i$. Tanaka loves the prime number $M$. Thus, when he arrives, DJ PyroSava will multiply the "caterinca" indices of all parties by a random prime number $X$, which satisfies $X < M$. Now, Tanaka is tired from the journey, so he cannot visit parties in all rooms. Thus, he will randomly choose to visit a connected subset of nodes of exact size $K$. The total "caterinca" Tanaka will experience is equal to the product of the "caterinca" indices (after DJ PyroSava's multiplication) of all visited rooms. Now consider the expected value of this total "caterinca." Let's say it is $p / q$. What is the value of $pq^{-1}$ mod $M$ (where $q^{-1}$ represents the modular inverse of $q$ with respect to $M$)?

## Input data

The input file `caterinca.in` will start with a number $T$, the number of test cases in the file.  
Each test starts with a line containing the numbers $N$, $M$, $K$. The second line of a test will contain $N$ integers, the values of $c_i$, in order. The next $N-1$ lines will each contain a pair $i, j$, representing an edge between node $i$ and node $j$.

## Output data

The output file `caterinca.out` will print $T$ lines, each containing the answer for one test.

## Constraints and clarifications

$T \leq 3$

$1 \leq N \leq 1\ 000\ 000$

$0 \leq c_i \leq 1\ 000\ 000\ 000$

$1 \leq M \leq 20\ 000$

$1 \leq K \leq N$

$1 \leq N \cdot K \leq 10\ 000\ 000$

## Example

`caterinca.in`
```
3
3 23 3
2 3 2
3 1
3 2
4 23 4
2 2 4 3
1 4
2 4
3 2
4 23 4
3 3 3 2
4 1
3 2
1 3
```
`caterinca.out`
```
15
21
```