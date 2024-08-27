## Task

We say that a sequence of natural numbers is interesting if for any two distinct numbers in this sequence, the smallest one divides the largest one. Given a sequence $A$ of $N$ elements, we ask how many of its subarrays are interesting. 

## Input data

The input file `divseq.in` will contain on its first line the value $N$. The second line will contain $N$ natural numbers, the elements of the array $A$. 

## Output data

The output file `divseq.out` will contain a single value, equal to the number of subarrays of $A$ that are interesting, according to the definition in the statement. 

## Constraints and clarifications

$1 \leq N \leq 250\ 000$

$1 \leq A[i] \leq 10^{12}$

Tests worth 30 points have $N = 100$

Tests worth 20 points have $N = 1000$

An array $B$ is a subarray of an array $A$ if it contains elements on consecutive positions from the array $A$.

Two subarrays $B_1$ and $B_2$ are considered different if they start or end on different positions. 

## Example

`divseq.in`  
```
4
1 6 2 10
```

`divseq.out`
```
8
```