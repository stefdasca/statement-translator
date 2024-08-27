## Task

A sequence of numbers $a_1, a_2, \dots, a_k$ is bitonic if there exists a position $1 \leq i \leq n$ such that $a_1 < a_2 < \dots < a_i > a_{i+1} > \dots > a_k$ or $a_1 > a_2 > \dots > a_i < a_{i+1} < \dots < a_k$. Given a sequence, find the length of the longest bitonic subsequence. 

## Input data

The input file `bitonic.in` contains the number $T$ of tests on the first line, and the following lines contain the tests. Each test consists of two lines: the first line contains the number $n$ of elements in the sequence, and the next line contains the sequence. 

## Output data

The output file `bitonic.out` must print for each test a line containing the maximum length of a bitonic subsequence of the input sequence. 

## Constraints and clarifications

$1 \leq T \leq 20$

$1 \leq n \leq 1000$

The elements of the initial sequence are natural numbers between $1$ and $100000$. 

## Example

`bitonic.in`

```
3
8
1 10 5 11 1 3 12 2 10
1
10
2
3 7 6 5 4 8 9
5
1 2 5 3 4 5 7 4
```

`bitonic.out`

```
5
7
4
```

## Explanation

For the first test, a bitonic subsequence of maximum length is $1 5 11 3 2$, for the second test $1 2 3 7 6 5 4$, and for the last test $1 2 3 4$.