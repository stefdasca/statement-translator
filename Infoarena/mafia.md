## Task

You are given an array of $N$ numbers $v_1 \dots v_n$ which represent the frequencies of numbers from 1 to $N$, and a number $X \leq N$. Calculate the probability that when choosing $M$ numbers from $v_1 + v_2 + \dots + v_n$, the number $X$ will appear at least once.

## Input data

The input file `mafia.in` contains on the first line the number $T$ representing the number of tests. For each test, the first line contains the numbers $N$, $M$ and $X$ separated by a space. On the second line, the elements of the array are contained, separated by a space.

## Output data

In the output file `mafia.out`, print $T$ lines, on the $i^{th}$ line the answer for the $i^{th}$ test, with at least 7 decimal places.

## Constraints and clarifications

$1 \leq T \leq 10$

$1 \leq X \leq N \leq 100\ 000$

$1 \leq V_i \leq 1\ 000\ 000$

$1 \leq M \leq V_1 + V_2 + \dots + V_n$

## Example

`mafia.in`

```
2
2 2 1
1 3
2 2 1
1 2
```

`mafia.out`

```
0.5000000000
0.6666666667
```