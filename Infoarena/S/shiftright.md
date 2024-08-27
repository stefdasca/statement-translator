## Task

Two strings $A$ and $B$ of equal length, $|A| = |B|$, composed of lowercase English alphabet characters, are given. Starting from string $A$, we perform the following operation a number of times: we choose a (possibly non-contiguous) subsequence which we circularly permute to the right by one position. For example, starting with the string $abcabbda$, we can obtain $adbacbba$ by circularly permuting the bold subsequence. What is the minimum number of operations required to transform string $A$ into string $B$?

## Input data

The input file `shiftright.in` contains the string $A$ on the first line and the string $B$ on the second line.

## Output data

The output file `shiftright.out` will contain on the first line $ans$, the minimum number of operations required to transform string $A$ into string $B$, and each of the following $ans$ lines a natural number $k$, followed by $k$ values between $0$ and $|A| - 1$, in ascending order, representing the operations in the order they are performed. After performing all $ans$ operations, the strings must become identical. Only solutions that display at most $1\ 000\ 000$ (one million) positions in total will be scored. It is guaranteed that if there is a solution, there is at least one solution with a total number of positions less than or equal to $1\ 000\ 000$.

## Constraints and clarifications

$1 \leq |A| = |B| \leq 100\ 000$

Any correct solution is accepted, as long as the number of operations is optimal and the strings become identical at the end.

For tests worth 30 points, it is guaranteed that the only characters appearing in the two strings are $a$ and $b$.

The strings $A$ and $B$ are indexed from $0$.

For each test, 30% of its score represents the correctly displayed answer, while 70% represents a valid solution.

## Examples

`shiftright.in`
```
abcabbda
adbca bba
```

`shiftright.out`
```
1
4 1 2 4 6
```

`shiftright.in`
```
abcde
caebd
```

`shiftright.out`
```
2
3 0 1 2
3 2 3 4
```

`shiftright.in`
```
aba
bab
```

`shiftright.out`
```
-1
```