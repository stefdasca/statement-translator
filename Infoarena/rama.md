# The Frame

Marian, while walking quietly down the street, found a 100 RON bill on which a binary matrix was written. To be able to buy something with this bill, Marian needs to find the maximum area rectangle contained entirely within the matrix, which has only elements equal to $1$ on its sides (regardless of what it strictly contains inside). Marian doesn't know how to do this, but he asks you to help him!

## Input data

The input file `rama.in` contains on the first line two natural numbers $N$ and $M$, separated by a space, representing the number of rows and the number of columns of the binary matrix, respectively. On the next $N$ lines, there are $M$ characters each, equal to $1$ or $0$, representing the binary matrix found by Marian.

## Output data

In the output file `rama.out` you must print on the first line a single natural number: the maximum area of a rectangle that has only elements equal to $1$ on its sides.

## Constraints and clarifications

$2 \leq N \leq 700$  
$2 \leq M \leq 700$  
A binary matrix is a matrix that contains only elements of $1$ and $0$.  
A rectangle formed from a single element of $1$ is considered valid.

## Example

`rama.in`

```
5 5  
10101  
10111  
10101  
10111  
01111  
```

`rama.out`

```
12  
```

## Explanation

The rectangle with the maximum area has its top-left corner at position $(2, 3)$, and the bottom-right corner at position $(5, 5)$. There were other possibilities, but with a smaller area: $(1, 1) \rightarrow (1, 4)$ or $(4, 3) \rightarrow (5, 4)$.