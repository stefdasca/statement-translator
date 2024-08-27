## Task

You are given a string $S$ of length $N$. A non-empty subsequence $A$ of $S$ and a non-empty subarray $B$ of $S$ are randomly selected. What is the probability that $A$ and $B$ are equal?

## Input data

The input file `eqprob.in` will contain on the first line an integer $T$ representing the number of tests. Each test has the following format: the first line contains an integer $N$, the length of the string; the second line contains the string $S$.

## Output data

The output file `eqprob.out` will contain the answers for the $T$ tests. The answer for each test has the following format: a real number representing the probability that $A$ and $B$ are equal, printed with a precision of 12 decimals.

## Constraints

$1 \leq T \leq 10$

$1 \leq N \leq 50$

$S$ contains only lowercase English letters. 

A subsequence of length $K$ of the string $S$ is a string $T = S_{i1} S_{i2} \dots S_{iK}$, such that $1 \leq i1 < i2 < \dots < iK \leq N$. 
A subarray of the string $S$ is a string $T = S_i S_{i+1} \dots S_{j-1} S_j$, $1 \leq i \leq j \leq N$. 
Two subsequences are considered distinct if the two sequences of indices corresponding to the two subsequences differ by at least one element. The same applies to subarrays.

The result will be considered correct if it differs from the correct result by at most $10^{-9}$.

## Example

`eqprob.in`
```
3
1 x
2 aa
3 aca
```

`eqprob.out`
```
1.000000000000
0.555555555556
0.190476190476
```

## Explanation

In test $2$, $S = aa$. There are $3$ non-empty subsequences: $a, a, aa$. There are $3$ non-empty subarrays: $a, a, aa$. 
If we choose $A = aa$, the probability that $A = B$ is $\frac{1}{3}$. 
If we choose $A = a$, the probability that $A = B$ is $\frac{2}{3}$. 
Thus, the total probability is $\frac{1}{3} * \frac{2}{3} + \frac{1}{3} * \frac{2}{3} + \frac{1}{3} * \frac{1}{3} = \frac{5}{9}$.