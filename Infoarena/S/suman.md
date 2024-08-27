# Suman

Given a natural number $N$ and $K$ natural numbers $v_1, \dots, v_K$. Calculate the sum of all natural numbers in the interval $[1, N]$ that are divisible by at least one of the numbers $v_1, \dots, v_K$.

## Input data

The input file `suman.in` contains on the first line the integer $N$. The second line contains the integer $K$. On the $i$-th of the following $K$ lines, the number $v_i$ is contained.

## Output data

In the output file `suman.out`, you will print the sum of all natural numbers in the interval $[1, N]$ that are divisible by at least one of the numbers $v_1, \dots, v_K$.

## Constraints and clarifications

$1 \leq N \leq 1\ 000\ 000\ 000$

$1 \leq K \leq 20$

$1 \leq v_i \leq N$

This problem has tests divided into 2 groups, worth 30 and 70 points respectively.

## Example

`suman.in`

```
10
2
2
3
```

`suman.out`

```
42
```

## Explanation

$N=10$, $K=2$, $v_1=2$ and $v_2=3$. The natural numbers in the interval $[1, 10]$ which are divisible by at least one of the numbers 2 or 3 are: 2, 3, 4, 6, 8, 9, 10. Their sum is $2+3+4+6+8+9+10=42$.