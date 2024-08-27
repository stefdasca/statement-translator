# Nrbanda

Given a permutation of the numbers $1, \dots, N$, the task is to sort this permutation in ascending order by performing only the operation described below:
The permutation is split between two consecutive positions, $i$ and $i+1$. All numbers from the beginning of the permutation up to position $i$ (inclusive) are rotated one position to the left, and all numbers from position $i+1$ to position $N$ are rotated one position to the right. The permutation can also be split between the fictitious position $0$ and position $1$ (in which case the entire permutation is rotated one position to the right) as well as between position $N$ and the fictitious position $N+1$ (in which case the entire permutation is rotated to the left).

## Input data

The first line of the `nrbanda.in` file contains the number $N$ of elements in the permutation, and the second line contains the $N$ numbers, separated by spaces.

## Output data

In the `nrbanda.out` file, you will print multiple lines (possibly $0$, one or more). On each line, you will print a number $p$, signifying that an operation was performed according to the aforementioned rule, splitting between positions $p$ and $p+1$. The operations in the output file are considered to be executed in the order they are printed.

## Constraints

$1 \leq N \leq 256$

## Example

`nrbanda.in`

```
5
2 1 4 5 3
```

`nrbanda.out`

```
2
```

## Explanation

The permutation was split between positions $2$ and $3$. The first $2$ elements are rotated to the left (becoming $1 \ 2$), and the last elements are rotated to the right (becoming $3 \ 4 \ 5$). This way, the permutation becomes $\mathbf{1 \ 2 \ 3 \ 4 \ 5}$ and is sorted.