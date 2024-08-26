# Aiacuxor

Bulanel was not paying attention during the computer science class and as a result, he misunderstood the given assignment. Since he cannot solve it, he asks for your help. Bulanel has an array $V$ with $N$ elements. Let $f(i,j)$ be the xor sum of the elements of the subarray determined by the positions between $[i,j]$, $i \leq j$ ($V(i)$ xor $V(i+1)$ xor $\dots$ xor $V(j)$). Bulanel is curious to find out the xor sum of the values returned by the function $f$ for all the subarrays of $V$ with a length between $[X, Y]$ ($X \leq Y$). Because Bulanel is curious, he asks you $Q$ such questions. Given that Bulanel is not good at reading, you will construct the array $V$ based on an auxiliary array $S$ of length $M$, with elements numbered from $0$ to $M-1$. The element at each position $i$, $0 \leq i < N$, in the array $V$ will be computed with the following formula: $V[i] = (S[i / M] xor S[i \mod M]) + i$, where $x / y$ represents the quotient of dividing $x$ by $y$, $x \mod y$ represents the remainder of dividing $x$ by $y$, and $x$ xor $y$ represents the result of the xor operation (exclusive or on bits) between $x$ and $y$. The questions are also generated as follows: knowing the first question $X$ $Y$, the next pairs $X$ $Y$ are found according to the procedure: $X_{\text{new}} = (X * A + Y * B) \mod N + 1$ $Y_{\text{new}} = (Y * C + (Z \mod N) * D) \mod N + 1$, (where $Z$ represents the answer to the last question and $A$, $B$, $C$, $D$ are some constants given in the input file) if $X_{\text{new}} > Y_{\text{new}}$: swap $X_{\text{new}}$, $Y_{\text{new}}$ $X$ = $X_{\text{new}}$ $Y$ = $Y_{\text{new}}$

## Task

Knowing $N$, the number of elements in the array $V$, $Q$ the number of questions, and the array $S$ with which you will construct the array $V$, Bulanel asks you to correctly answer all the $Q$ questions.

## Input data

The input file `aiacuxor.in` contains on the first line a natural number $N$, which represents the length of the array $V$, followed by $Q$, which represents the number of questions, and $M$, the length of the auxiliary array $S$. The next line contains $M$ numbers, representing the array $S$ with elements numbered from $0$ to $M-1$. The third line contains $X$ and $Y$, which represent the minimum length and the maximum length of the subarrays taken into account for the first question, and then in order $A$, $B$, $C$, $D$, the constants with which you will construct the following questions, from the second to the $Q$-th.

## Output data

The output file `aiacuxor.out` contains $Q$ lines, each containing the answer to the $i$-th question.

## Constraints and clarifications

$1 \leq X \leq Y \leq N \leq 1000000$

$1 \leq Q \leq 1000000$

$1 \leq M \leq 1000$, $N \leq M * M$

For 20 points:
$1 \leq N, Q \leq 100$

For another 20 points:
$1 \leq N \leq 1000$ and $1 \leq Q \leq 100$

For another 15 points:
$1 \leq N \leq 10000$ and $1 \leq Q \leq 100$

Elements of the array $V$ fit in 32 bits

$1 \leq S[i] < 2^{29}$

$0 \leq A,B,C,D \leq 10^3$

A subarray is a subsequence of elements that appear in consecutive positions in the initial array.

The xor operation represents the exclusive or operation performed on the bits of the operands. In Pascal, the corresponding operator is `xor`, and in C/C++ this operator is `^`.

For example, $20$ xor $14 = 26$.

The way the array and questions are generated is only due to the fact that Bulanel reads very slowly.

The problem will be evaluated on tests worth 90 points

10 points will be awarded by default

## Example

`aiacuxor.in`
```
4 4 4
10 8 10 8
1 1 9 8 5 3 4 5 0
```

`aiacuxor.out`
```
1
1
1
1
```

Explanation:
The array $V$ of length $N = 4$: $0 3 2 5$

The 4 questions are:
`1 1`
`2 2`
`2 3`
`3 4`

We will explain in detail the answer to the last question:
The subarrays of the array $V$ with a length between $[3, 4]$ are:
$(0, 3, 2)$ (between positions $0$ and $2$);
$(3, 2, 5)$ (between positions $1$ and $3$);
$(0, 3, 2, 5)$ (between positions $0$ and $3$).

$f(0, 2) = 0$ xor $3$ xor $2 = 1$
$f(1, 3) = 3$ xor $2$ xor $5 = 4$
$f(0, 3) = 0$ xor $3$ xor $2$ xor $5 = 4$

The answer to the last question is:
$1$ xor $4$ xor $4 = 1$

`10 10 4`
`2 8 9 1 6 9`
`9 6 2 9 28 5 23 5 22 22`
We obtain the array $V$: $0$ $11$ $13$ $6$ $14$ $5$ $7$ $16$ $19$ $10$

We obtain the questions:
`6 9`
`1 9`
`4 4`
`1 6`
`6 8`
`3 5`
`8 9`
`6 7`
`4 7`
`5 9`