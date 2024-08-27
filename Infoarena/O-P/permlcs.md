## Permlcs

## Task

Given $M$ arrays, each representing a permutation of numbers from $1$ to $N$. Determine the maximum length of an array that is a subsequence of each of the given $M$ arrays. An array $A$ is a subsequence of another array $B$ if it can be obtained from $B$ by deleting $0$ or more characters (for example, the array $1 \ 4 \ 3$ is a subsequence of the array $7 \ 1 \ 2 \ 4 \ 6 \ 5 \ 3$).

## Input data

The input file `permlcs.in` contains the numbers $N$ and $M$ on the first line. Each of the following $M$ lines contains a permutation of the numbers from $1$ to $N$, representing one of the $M$ arrays. The elements within a permutation are separated by a space.

## Output data

In the output file `permlcs.out`, you will print the maximum length of an array that is a subsequence of each of the $M$ arrays given in the input file.

## Constraints

$1 \leq N \leq 1000$

$1 \leq M \leq 10$

This problem has tests divided into $2$ groups, worth $30$ and, respectively, $70$ points.

## Example

`permlcs.in`

```
6 3 
6 1 5 2 4 3 
1 2 3 4 5 6 
4 1 5 2 6 3 
```

`permlcs.out`

```
3 
```

## Explanation

A common subsequence of length $3$ of all three arrays is $1 \ 2 \ 3$.