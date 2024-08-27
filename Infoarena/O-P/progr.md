# Progr

After Petrică's success, it is now Georgică's turn to play with arithmetic progressions. He has an array with $N$ natural numbers and wonders how many maximal arithmetic progressions with a positive ratio (greater than zero), which have at least two terms, can be formed with these numbers. An arithmetic progression $X_1, X_2, \dots, X_k$, with $X_1, X_2, \dots, X_k$ belonging to the array, is maximal if:
- For any $Y$ belonging to the array, $Y, X_1, X_2, \dots, X_k$ is not an arithmetic progression.
- For any $Y$ belonging to the array, $X_1, X_2, \dots, X_k, Y$ is not an arithmetic progression.

## Input data

The input file `progr.in` contains the first line that will contain $T$, the number of tests. Next, for each test, the first line will contain a natural number $N$, and on the next line, $N$ natural numbers, as described in the statement.

## Output data

The output file `progr.out` will contain $T$ lines, and each line $i$ will contain a single natural number, representing the number of arithmetic progressions that can be formed with the numbers from test $i$.

## Constraints and clarifications

$T = 10$

$1 \leq N \leq 2\ 000$

$1 \leq v[i] \leq 10^9$, where $v[i]$ is an element among Georgică's $N$ numbers.

It is guaranteed that the elements of the array are distinct.

## Example

`progr.in` `progr.out`

`1` `2`

`3` `2`

`2 3 1`

## Explanation

The two progressions are: $1\ 3$, $1\ 2\ 3$. $1\ 2$ and $2\ 3$ are progressions but are not maximal.