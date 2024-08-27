And

Ojilă, obsessed with the approaching OJI, was walking upset because he didn't know how to apply the operator and very well. Suddenly, in front of his eyes appeared an array of length $N$ which contained only natural numbers. Immediately, his face lit up, and he asked himself the following simple question: what is the longest subsequence of the form $a_i,a_{i+1},\dots,a_j$ such that the value of the expression $a_i \text{ and } a_{i+1} \text{ and } \dots \text{ and } a_j$ is different from $0$.

## Input data

The input file `and.in` contains on the first line the number $N$. The following line contains $n$ natural numbers separated by a space, representing the elements of the array.

## Output data

The output file `and.out` will contain a single natural number representing the maximum length of a subsequence that gives a non-zero result.

## Constraints and clarifications

$2 \leq N \leq 100\ 000$ 

The elements of the array are natural numbers less than or equal to $10^9$

$\text{and}$ is the bitwise conjunction operation; the operator is denoted by $&$ in C/C++ and by $\text{and}$ in Pascal; for example, $2\&3=10_2 (2) \& 11_2 (3) = 10_2 (2) = 2$

## Example

`and.in`
```
6
1 64 7 2 3 32
```

`and.out`
```
3
```

## Explanation

The maximum length subsequence $3$ is $7, 2, 3$ because $7 \& 2 \& 3 = 2$