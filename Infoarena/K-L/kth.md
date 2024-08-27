## Task

Given an array $V$ with $N$ elements, we apply $M$ operations of 2 types on this array:

Operation of type $0$: We are given an interval $[A, B]$ and a number $K$. We sort the elements in the interval in ascending order by value, then replace them with the $K$-th value from this interval.

Operation of type $1$: We are given an interval $[A, B]$ and a number $K$. All elements in this interval are replaced with the value $K$.

Display the array of $N$ elements after all $M$ operations.

## Input data

The input file `kth.in` will contain on the first line 2 natural numbers $N$ and $M$. The second line will contain $N$ natural numbers, representing the initial array. The following $M$ lines describe the updates. An update consists of 4 numbers: $tip\_update$, $A$, $B$ and $K$.

## Output data

The output file `kth.out` will contain $N$ natural numbers on a single line, representing the array $V$ after all $M$ updates.

## Constraints and clarifications

$1 \leq N, M \leq 100\ 000$

$1 \leq K \leq B - A + 1$ for operations of type $0$

The initial values in the array, as well as the $K$ values of type $1$ operations, will be within the interval $[1, 100\ 000]$

## Example

`kth.in`

```
5 3
1 3 2 3 4
0 2 4 2
0 4 5 2
1 3 4 10
```

`kth.out`

```
10 4 10 10 4
```
