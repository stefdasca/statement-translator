Permutations

A permutation of length $N$ is a sequence of distinct elements from the set $\{1, 2, 3 \dots N\}$. We say that a permutation has $K$ maxima if there are exactly $K$ distinct positions in the permutation where the current element is greater than all the elements to its left.

##  Task

Write a program that determines how many permutations of length $N$ with $K$ maxima exist.

##  Input data

The first line of the file `perm.in` will contain the numbers $N$ and $K$, separated by a space.

##  Output data

The first line of the file `perm.out` will contain the number of permutations of length $N$ with $K$ maxima.

##  Constraints and clarifications

$1 \leq K$  
$K \leq N$  
$N \leq 200$

##  Examples

`perm.in`  
`perm.out`  
`3 2`  
`3`

`5 3`  
`35`

