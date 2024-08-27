## Task

Given $N$ types of numbers. Consider an array of elements with the property that for each type $i$ numbered from $0$ to $N - 1$, it appears $(FR_i)$ times. The numbers of type $i$ are equal to $2^{PW_i}$. Partition the elements of the array into $2$ multisets such that the sums of the two are as close as possible (the absolute difference is minimized). Find this minimum difference modulo $1,000,000,007$.

## Input data

The input file `greutati.in` will contain on the first line $2$ integers $N$ and $P$, where $N$ represents the number of powers of $2$ for which the frequency is different from $0$, and $P$ represents the maximum power at which $2$ can appear. On the next $N$ lines, there will be $2$ integers $PW_i$ and $FR_i$ representing a power and a corresponding frequency for that power.

## Output data

The output file `greutati.out` will contain a single natural number representing the minimum difference you can achieve modulo $1,000,000,007$.

## Constraints

$1 \leq N \leq 100,000$

$1 \leq P \leq 1,000,000,000$

$0 \leq PW_i \leq P$

$1 \leq FR_i \leq 1,000,000,000$

There will not be pairs $i$ and $j$ in the input such that $PW_i = PW_j$

For $15$ points: $P \leq 20$, sum of frequencies $\leq 20$

For $25$ points: $P \leq 50$, sum of frequencies $\leq 2000$

For $35$ points: $P \leq 2000$, sum of frequencies $\leq 2000$

For $50$ points: $P \leq 100,000$, sum of frequencies $\leq 100,000$

For $70$ points: $P \leq 100,000$ and sum of frequencies $\leq 1,000,000,000$

## Example

`greutati.in`
```
6 10
4 4
3 3
5 2
8 4
6 1
7 3
```

`greutati.out`
```
0
```

`greutati.in`
```
7 10
4 4
3 3
5 2
8 4
6 1
7 3
0 3
```

`greutati.out`
```
5
```