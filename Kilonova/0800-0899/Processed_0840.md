```markdown
A sequence $A$ consisting of $N$ non-zero natural elements is considered. We call the subarray of length $K$ of sequence $A$ any succession of consecutive elements in the form $A_i, A_{i+1}, \dots, A_{i+K-1}$.

A subarray is called a *cool subarray* if the elements it contains are distinct and can be rearranged to form a continuous sequence of consecutive numbers.

For example, considering the sequence $A = (3,1,6,8,4,5,6,7,4,3,4)$, then the subarray $(8,4,5,6,7)$ is a *cool subarray* because it contains distinct elements that can be rearranged to form the consecutive number sequence $4,5,6,7,8$, whereas the subarrays $(4,3,4)$, $(6,7,4,3)$ **are not** considered *cool subarrays*.

# Task
Given a sequence of $N$ non-zero natural numbers, the following are required:
1. For a given value $K$, verify if the subarray $A_1, A_2, \dots, A_K$ is a *cool subarray*. If the subarray is *cool*, then display the largest value in the subarray. If the subarray is not *cool*, then display the number of distinct elements in the subarray $A_1, A_2, \dots, A_K$, meaning the number of elements that appear only once.
2. The maximum length of a *cool subarray* and the number of *cool subarrays* of maximum length.

# Input data
The input file `cool.in` contains on the first line a natural number $p$. For all input tests, the number $p$ can only have the value $1$ or the value $2$. The second line contains, separated by a space, two natural numbers $N$ and $K$. On the next line are $N$ integers, separated by a space, representing the elements of the sequence.

# Output data
If the value of $p$ is $1$, then **only point 1** from the task will be solved. In this case, the output file `cool.out` will contain on the first line a natural number representing according to task $1$, the maximum value of the subarray $A_1, A_2, \dots, A_K$, if the subarray is a *cool subarray*, or the number of distinct elements in the subarray, if it is **not** a *cool subarray*.
\
If the value of $p$ is $2$, **only point 2** from the task will be solved. In this case, the output file `cool.out` will have two lines. The first line will contain a non-zero natural number representing the maximum length of a *cool subarray*, and the next line a non-zero natural number representing the number of *cool subarrays* that have the maximum length.

# Constraints and clarifications
- $1 \leq N \leq 5\ 000$
- $2 \leq K \leq 1\ 000$
- $1 \leq A_i \leq 1\ 000$, $1 \leq i \leq N$
- For $30\\%$ of the tests, $N \leq 1\ 000$.
- For solving the first task, $20\\%$ of the score is awarded, and for the second task, $80\\%$ of the score is awarded.

# Example 1
`cool.in`
```
1
7 4
6 4 5 7 8 3 5
```
`cool.out`
```
7
```

## Explanation
**Attention! For this test, only task 1 is solved.**
The subarray $(6, 4, 5, 7)$ is *cool*.
The maximum value in the subarray is $7$.

# Example 2

`cool.in`
```
1
7 6
6 4 5 7 5 4 3
```
`cool.out`
```
2
```

## Explanation
**Attention! For this test, only task 1 is solved.**
The subarray $(6, 4, 5, 7, 5, 4)$ is not a *cool subarray*. The number of distinct values in the subarray is $2$. The distinct values are $6$ and $7$.

# Example 3
`cool.in`
```
2
11 4
7 4 5 6 8 4 5 7 4 3 2
```
`cool.out`
```
5
2
```
## Explanation
**Attention! For this test, only task 2 is solved.**
The two *cool subarrays* of maximum length $5$ are:
$(7, 4, 5, 6, 8)$
$(6, 8, 4, 5, 7)$
```