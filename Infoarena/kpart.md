## Task

Virgil has just decided to study the properties of sequences. Thus, he defines a $K$-sequence as any sequence of non-zero natural numbers that has the property that any of its subarrays of length $K$ can be partitioned into two disjoint subsequences, not necessarily subarrays, having the same sum. For example, $1, 2, 1, 3$ is a $3$-sequence because $1, 2, 1$ can be partitioned into $1, 1$ and $2$, and $2, 1, 3$ can be partitioned into $2, 1$ and $3$. It is not a $2$-sequence because $1, 2$ cannot be partitioned into two subsequences with equal sums. It is also not a $4$-sequence. For $T$ non-zero natural number sequences $A$, Virgil wants to determine all the values of $K$ for which sequence $A$ can be called a $K$-sequence.

## Input data

The input file `kpart.in` contains on the first line the number $T$. Then follows $T$ sequences. Each sequence is given through two lines. The first line contains the value of $N$. The second line contains the elements of the sequence separated by a space.

## Output data

The output file `kpart.out` should display the answers for each sequence in order. For each sequence print a line that first contains the number of values $K$ for which the sequence is a $K$-sequence and then, in ascending order, those values $K$ for which the sequence is a $K$-sequence.

## Constraints

$1 \leq T \leq 20$

Let $S$ be the sum of the values in a sequence (not the sum of the values in all sequences). Then 
$1 \leq S \leq 100\ 000$

Additionally:

### Constraints

1 

$10$

$1 \leq N \leq 30$

2 

$20$

$31 \leq N \leq 120$

3 

$70$

$121 \leq N \leq 1\ 000$

## Example

`kpart.in` 
```
2
7
7 3 5 1 3 3 5
6
1 2 3 5 8 3
```
`kpart.out` 
```
2 4 6
2 3 6
```

## Explanation

The first sequence, of length $7$, is a $4$-sequence and a $6$-sequence because each subarray of length $4$, respectively $6$, contains two disjoint subsequences with equal sums which partition the subarray. The second sequence, of length $6$, is a $3$-sequence and a $6$-sequence because each subarray of length $3$ and each subarray of length $6$, contains two disjoint subsequences with equal sums which partition the subarray.