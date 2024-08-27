## Task

Flubby Doo has to solve a mystery. At the moment, he is in front of a secret door. To open it and enter the monster's hideout, he must quickly answer the following question: given an array of $N$ non-zero real numbers, what is the subarray with the maximum product, whose length is between $X$ and $Y$. Flubby Doo can easily answer this question, but he is interested if you, his friends, can do it as well.

## Input data

The file `secv4.in` contains on the first line 3 numbers: $N$, $X$, and $Y$. The next line contains $N$ numbers.

## Output data

The file `secv4.out` contains on the first line two numbers: $L$ and $P$, where $L$ represents the length of the subarray and $P$ the starting position of this subarray. 

## Constraints and clarifications:

$1 \leq N \leq 100\ \\ 000$

The elements of the array are non-zero real numbers in the interval [$-10^9$; $10^9$]

In all tests, the subarray with the maximum product will be positive

A subarray of length $L$ is understood as a subarray of $L$ consecutive numbers of the initial array 

If there are multiple solutions, the one with the smallest ending position will be displayed; if there are still multiple solutions, the one with the smallest starting position will be displayed

For $40\%$ of the tests, the elements of the array will be only positive numbers

For $10\%$ of the tests, the elements of the array will be positive numbers and $N \leq 2000$

The elements of the array will have at most 3 decimal places

## Example:

`secv4.in`

$5$ $1$ $4$

$2$ $2$ $0.1$ $2$ $2$

`secv4.out`

$1$ $2$

`6$ $1$ $4$

$-2$ $-3$ $-4$ $-2$ $-3$

`1$ $4$

`2$