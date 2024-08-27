## Task

Determine a permutation of the numbers $1, \dots, N$ with the following property: the arithmetic mean of any $2$ elements of the permutation must not be placed between those $2$ elements (this property only makes sense if the arithmetic mean of the $2$ elements is an integer). Specifically, let $2$ distinct elements $i$ and $j$, situated at positions $p_i$ and $p_j$ in the permutation. Also, let $x$ be the arithmetic mean of $i$ and $j$ ($x=(i+j)/2$). If $x$ is an integer, then let $p_x$ be the position of $x$ in the permutation. The condition that the permutation must satisfy is that $p_x$ must not be between positions $p_i$ and $p_j$.

## Input data

The first line of the input file `permavg.in` contains the integer $N$, representing the number of elements in the permutation.

## Output data

In the output file `permavg.out` you will print the $N$ elements of the permutation, in order, separated by a space. If there are multiple solutions, you can print any of them.

## Constraints and clarifications

$1 \leq N \leq 16000$

## Example

`permavg.in`
```
4
```

`permavg.out`
```
1 3 2 4
```