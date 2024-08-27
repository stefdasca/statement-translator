# Increasing

Consider an array of $N$ natural numbers. We define the notion of an increasing sequence as a subarray of the initial array in which the elements appear in increasing order. The task is to determine how many increasing sequences can be found in the array, as well as the maximum length of an increasing sequence.

## Task

## Input data

The input file `crescator.in` will contain:
- The first line will contain the number $N$ representing the number of elements in the array.
- The next line will contain $N$ numbers representing the elements of the array.

## Output data

The output file `crescator.out` will contain, on the first line, two numbers. The first number represents the number of increasing sequences, and the second number will represent the maximum length of such a sequence.

## Constraints

$1 \leq N \leq 100\ 000$

The elements of the array will be natural numbers less than $2\ 000\ 000\ 000$

## Example

`crescator.in` 
```
5
1 3 2 4 5
```

`crescator.out`
```
9 3
```

## Explanation

The nine sequences are: $1$, $3$, $2$, $4$, $5$, $1 3$, $2 4$, $4 5$, $2 4 5$. The longest increasing sequence is $2 4 5$.