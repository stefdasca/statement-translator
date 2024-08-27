# Coins

The farmer Victor has $N$ types of banknotes, each in an unlimited amount. He is curious about the minimum sum $S_{min}$ such that any sum greater than $S_{min}$ can be paid using the banknotes he has at his disposal.

## Task

Knowing the values of the $N$ types of banknotes, find $S_{min}$.

## Input data

The first line of the file `banuti.in` contains the number $N$. The next line contains $N$ numbers $V_i$ which represent the value of each type of banknote.

## Output data

The first line of the file `banuti.out` contains the number $S_{min}$ or $-1$ if no solution exists.

## Constraints and clarifications

$2 \leq N \leq 50\ 000$

$1 \leq V_i \leq 10\ 000\ 000$

It is guaranteed that there is at least one banknote with a value $\leq 5000$.

$S_{min} < 1\ 000\ 000\ 000$

For $20\%$ of the tests $N \leq 50$, $S_{min} \leq 100\ 000$ and the minimum value of at least one banknote $\leq 200$.

For $50\%$ of the tests $N \leq 1000$.

## Example

`banuti.in`
```
2
3 5
```

`banuti.out`
```
7
```

`banuti.in`
```
2
3 6
```

`banuti.out`
```
-1
```