## Expected Xor

Note: This is not the statement used in the contest, but technically the described problem is the same. A positive integer $M$ and a sequence of $N$ positive integers $A_i$ are given, with the property that $(A_i, M) = 1$ (i.e., the greatest common divisor of the numbers $A_i$ and $M$ is 1). Find the expected value of $B_1 \text{ xor } B_2 \text{ xor } \dots \text{ xor } B_N$, where each $B_i$ is a random integer with the property that $0 \leq B_i < A_i$. It can be proven that the answer is rational. The answer is requested modulo $M$, as described below.

## Input data

The input file `expected2.in` contains, on the first line, the numbers $M$ and $N$ separated by a space. On the next line, there are $N$ numbers separated by a space, representing the sequence $A$.

## Output data

The output file `expected2.out` contains on the first line a natural number $X < M$. If the answer is a rational number $U / V$, then $X$ has the property $X \times V \equiv U \pmod{M}$.

## Constraints and clarifications

$1 \leq N \leq 50000$

$2 \leq M \leq 10^9 + 7$

$1 \leq A_i \leq 2^{62}$

For 20 points,

$N \leq 5$, $M = 11$, $A_i < 2^3$

For other 20 points,

$N \leq 100$, $M = 997$, $A_i \leq 2^5$

For other 20 points,

$M = 10^9 + 7$

For other 20 points,

$N \leq 1000$, $M \leq 1000$, $A_i < 2^{30}$

## Example

`expected2.in`:
```
11 1
10
```

`expected2.out`:
```
10
```

`expected2.in`:
```
10 3
7 9 3
```

`expected2.out`:
```
8
```

## Explanation

In the first example, the answer is $9 / 2$ and $10 \times 2 = 20 \equiv 9 \pmod{11}$

In the second example, the answer is $274 / 63$ and $8 \times 63 = 504 \equiv 4 \pmod{10} \equiv 274$