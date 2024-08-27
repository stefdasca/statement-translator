## Task

Given a permutation $P$ of length $N$, you are asked to sort the permutation in ascending order using a minimum number of operations of the type $move(i, j)$ which places the element of value $i$ immediately after the element of value $j$. If you want to move the element of value $i$ to the beginning of the permutation, the parameter $j$ will be equal to $0$.

## Input data

The input file `move.in` contains on its first line the number $N$, and on the second line the permutation of length $N$.

## Output data

The output file `move.out` will contain on its first line the value $min$, signifying the minimum number of operations needed to sort the permutation. The next $min$ lines will be of the form $a\ b$, with the interpretation that the operation $move(a, b)$ is performed. If you want the element $a$ to reach the beginning of the permutation, then $b$ will be equal to $0$.

## Constraints and clarifications

$1 \leq N \leq 10^5$

For an operation $move(a, b)$ to be considered valid, it must be that $a \ne b$.

## Example

`move.in`
```
3
3 1 2
```

`move.out`
```
1
3 0
```

## Explanation

A single move is sufficient to bring the permutation to the sorted permutation.