## Task

Given a non-zero natural number $X$ with $N$ digits. When performing the addition of $X$ with another number $Y$ digit by digit, sometimes a carry is obtained. For example, if $X = 156$ and $Y = 247$, then first $6$ and $7$ are added which give a carry of $1$, at step $2$ $5$ is added to $4$ and to the carry $1$ resulting in another carry of $1$. In total, the addition $156 + 247$ results in a carry $1$ twice. Given the number $X$ with $N$ digits and a value $K$, determine how many numbers with $N$ digits result in exactly $K$ carries of $1$ when added to $X$. Because this number is very large, the result will be displayed modulo $30211$.

## Input data

The input file `carry.in` contains on the first line the numbers $N$ and $K$ separated by a space. The second line contains, without spaces, the $N$ digits of $X$.

## Output data

The output file `carry.out` will contain on the first line the number of $N$ digit numbers that result in exactly $K$ carries of $1$ when added to $X$, modulo $30211$.

## Constraints and clarifications

$1 \leq N \leq 100000$

$1 \leq K \leq \min\{100, N\}$

## Example

`carry.in`

```
2 1
98
```

`carry.out`

```
18
```

## Explanation

The number $X$ is $98$, which has $N = 2$ digits. The two-digit numbers which, when added to $98$, result in a single carry of $1$ are: $10, 11, 20, 21, 30, 31, 40, 41, 50, 51, 60, 61, 70, 71, 80, 81, 90, 91$.