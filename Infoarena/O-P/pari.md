# Even

Consider an array $S$ of $n$ integers and another array of length $n$ consisting of the words **even** and **odd**. The numbers in the array must be transformed according to the rules below so that each number becomes of the indicated parity: a pair of indices $(i, j)$ is chosen such that $i$ and $j$ have different parities and their greatest common divisor is greater than or equal to a given natural number $d$. An arbitrary integer is added to the numbers $S_i$ and $S_j$.

## Task

Determine the transformation path of the given array according to the operations described above.

## Input data

The first line of the input file `pari.in` contains two natural numbers $n$ and $d$, representing the number of elements in the array $S$ and the minimum value of the greatest common divisor. The next $n$ lines contain an integer, a space, and a word, which can be **par** (even) or **impar** (odd), representing the parity that the number must have.

## Output data

The output file `pari.out` will contain, on each line, the operations applied to the array. An operation is represented by three numbers $i$, $j$, $k$, where $i$ and $j$ indicate the pair of indices, and $k$ is the value added to the numbers in the array at positions $i$ and $j$. The three numbers will be separated by a space. If there is no solution, the output file will contain three numbers $0$, separated by a space.

## Constraints and clarifications

$2 \leq n \leq 1\ 000$

$1 \leq d \leq 1\ 000$

$1 \leq S_i \leq 30\ 000, i = 1, 2, \dots, n$

It is guaranteed that the total number of pairs that can be formed does not exceed $10\ 000$.

If there are multiple solutions, only one is required.

## Example

`pari.in` `pari.out`
```
5 1
8 par
10 par
7 par
6 impar
7 impar
```
`3 4 -3`