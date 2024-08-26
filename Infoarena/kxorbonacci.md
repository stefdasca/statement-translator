# Kxorbonacci

Tyrant's eye has found, while exploring some magical ruins, the definition of a new type of sequence, called the mystic sequence! The values of the sequence are $a[1],\dots$, and the sequence is considered to be infinite. The mystic sequence is determined by the first $K$ elements $a[1], \dots, a[K]$. The next numbers are equal to the xor of the last $K$ numbers in the sequence. Thus, $a[K+1] = a[1] \text{ xor } \dots \text{ xor } a[K]$, and $a[K+2] = a[2] \text{ xor } \dots \text{ xor } a[K+1]$, and so on. Tyrant's eye ultimately managed to find, deep in the ruins, a sequence of $N$ numbers $v[1], \dots, v[N]$. She guesses that this sequence is a subarray of the mystic sequence; that is, for a position $P$, $v[1] = a[P], v[2] = a[P+1], \dots, v[N] = a[P+N-1]$. She now wants to find $K$ and $P$. If there are multiple possible solutions, the one with the smallest $K$ should be found; if there are still multiple solutions, the one with the smallest $P$ should be found. 

## Task

The input file kxorbonacci.in contains, on the first line, the number $T$ of tests in the file. The $T$ pairs of lines follow, each describing a test scenario. The first line contains the number $N$, the second line contains the values $v[1], \dots, v[N]$. 

## Input data

The output file kxorbonacci.out will contain $T$ lines. Each line will contain the answer for a test, namely the values of $K$ and $P$ required. 

## Output data

In the output file kxorbonacci.out $T$ lines will be printed. Each line will contain the answer for a test, specifically the values $K$ and $P$ required.

## Constraints and clarifications

$1 \leq N \leq 300\ 000$

$0 \leq v[i] \leq 10^9$

$1 \leq T \leq 10$

The sum of the values of $N$ in a file is at most $300\ 000$

For 10 points, $K = 1$

For another 10 points, $K \leq 2$

For another 10 points, $K \leq 15, v[i] \leq 1$

For another 50 points, $N \leq 1\ 000$

## Example

`kxorbonacci.in`

```
3
5
1 0 1 1 0
5
1 2 3 1 2
5
0 0 0 0 0
2
1 2
1
1
1
```

`kxorbonacci.out`

```
2 1
1 1
1 1
```

## Explanation

For the first test, $K = 2$ and $a[1] = 1, a[2] = 0$. If we apply the rule from the statement to calculate the next values in $a$, we deduce that $a[3] = a[1] \text{ xor } a[2] = 1 \text{ xor } 0 = 1$, $a[4] = a[2] \text{ xor } a[3] = 0 \text{ xor } 1 = 1$, $a[5] = a[3] \text{ xor } a[4] = 1 \text{ xor } 1 = 0$. Thus we see that $v$ is found in $a$ starting at position $P = 1$.