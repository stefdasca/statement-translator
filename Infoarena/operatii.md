## Task

Consider a zero array with $N$ elements (each element is equal to $0$). The array undergoes a number of operations as follows: select two indices $i$ and $j$, $i \leq j$, and increment by one all elements in the array between positions $i$ and $j$ inclusive. Given an array $v$ with $N$ elements, determine the minimum number of the above operations required to transform the zero array into the array $v$.

## Input data

The input file `operatii.in` contains:

- The first line contains the number $N$.
- The second line contains $N$ natural numbers, representing the elements of the array $v$.

## Output data

The output file `operatii.out` will contain the minimal number of operations that need to be performed on the zero array to obtain the array $v$.

## Constraints and clarifications

$1 \leq N \leq 1\ 000\ 000$

Each number in $v$ is less than or equal to $100\ 000$

It is considered that the first element of any array is located at position $1$

For $10\%$ of the tests, $N \leq 10$

For $30\%$ of the tests, $N \leq 1\ 000$

For $40\%$ of the tests, it is guaranteed that the result will not exceed $3\ 000$

## Example

`operatii.in`

```
7
0 2 2 1 0 1 2
```

`operatii.out`

```
4
```

## Explanation

array operation performed

$0 \ 0 \ 0 \ 0 \ 0 \ 0 \ 0 \ \ i = 2, \ j = 4$

$0 \ 1 \ 1 \ 1 \ 0 \ 0 \ 0 \ \ i = 2, \ j = 3$

$0 \ 2 \ 2 \ 1 \ 0 \ 0 \ 0 \ \ i = 6, \ j = 7$

$0 \ 2 \ 2 \ 1 \ 0 \ 1 \ 1 \ \ i = 7, \ j = 7$

$0 \ 2 \ 2 \ 1 \ 0 \ 1 \ 2$