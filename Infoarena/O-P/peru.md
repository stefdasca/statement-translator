## Task

This morning, Roxy found $N$ cockroaches on her desk. They are numbered from $0$ to $N - 1$ and each cockroach $i$ has power $S_i$. Roxy wants to smash the cockroaches to do her math homework. For this, she bought a special glove that she can use to hit a continuous subarray of $K$ cockroaches. If Roxy makes an effort $E$, then those cockroaches whose power $S_i$ is less than or equal to $E$ will be smashed, while all others will remain unharmed. The smashed cockroaches remain in their positions on the desk. Roxy can use the glove as many times as she wants. Roxy wants to know if you can calculate the minimum effort required to smash the first $i$ cockroaches for each $1 \leq i \leq N$. Because there are too many numbers, Roxy wants you to give her the result of the following expression: $X_0 * 23^{N-1} + X_1 * 23^{N-2} + \dots + X_{N-1}$ modulo $10^9 + 7$, where $X_i$ represents the total minimum effort to smash the first $i+1$ cockroaches.

## Input data

The input file `peru.in` contains the numbers $N$ and $K$ on the first line, and on the second line contains a sequence of $N$ numbers.

## Output data

The output file `peru.out` contains a single number representing the obtained result.

## Constraints

$1 \leq N \leq 2500000$

$1 \leq K \leq N$

$1 \leq S_i \leq 2 * 10^9$

For 20 points, $1 \leq N \leq 2000$

For other 30 points, $1 \leq N \leq 400000$

It is recommended to parse the input file 

## Example

`peru.in`

```
8 3
3 2 9 8 7 11 3 4
```

`peru.out`

```
720026253
```