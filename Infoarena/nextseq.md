## Task

Given a set of distinct numbers, $X$, and two sequences, $A$ and $B$, with elements from set $X$ such that $B$ is larger than $A$. Determine how many sequences are larger than $A$ but smaller than $B$.

## Input data

The input file contains on the first line three numbers $N$, $M$, and $P$ representing the number of elements in the set $X$, the number of elements of the sequence $A$, and respectively, the number of elements of the sequence $B$.  
The second line contains $N$ natural numbers representing the set $X$.  
The third line contains $M$ natural numbers separated by spaces from the set $X$ representing the elements of the sequence $A$.  
The fourth line contains $P$ natural numbers separated by spaces from the set $X$ representing the elements of the sequence $B$.

## Output data

The first line of the output file will contain the searched number. This number will not be greater than $100$.

## Constraints and clarifications

$1 \leq N, M, P \leq 10\,000$

A sequence $A$ is larger than a sequence $B$ if it has more elements than $B$ or if the sequences have the same number of elements and there exists a position $i$ such that $A[i] \geq B[i]$ and $A[k] = B[k]$ for any $k \geq i$ (see example).

The number of sequences between $A$ and $B$ inclusive will not exceed $100$.

The numbers in the set $X$ are integers in the interval $[0 \dots 10\,000]$.

For $70\%$ of the tests $N, M, P \leq 100$.

## Example

`nextseq.in`
```
4 2 3 
8 3 9 1 
9 3 
1 3 8 
```

`nextseq.out`
```
8
```

## Explanations

The sequences that meet the conditions from the statement (lexicographically ordered) are: $\{9, 8\}$, $\{9 9\}$, $\{1 1 1\}$, $\{1 1 3\}$, $\{1 1 8\}$, $\{1 1 9\}$, $\{1 3 1\}$, $\{1, 3, 3\}$