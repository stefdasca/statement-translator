## Task

You are given $N$ arrays of $M$ binary elements, the $i$-th array being denoted as $S_i$. Let $P$ be the set of permutations that have the property that, when applied to any of the given arrays, the resulting array follows the next array in the set. More specifically, the permutation $P$ is valid if:

You are required to display:
a) Any valid permutation $P$
b) The median permutation $P$ (sorting all correct permutations lexicographically, the one in the middle is considered, and if there are two in the middle, the smallest lexicographically is chosen)
c) The number of valid permutations $P$ modulo $10^9 + 7$.

It is guaranteed that there is at least one permutation that satisfies the above property.

## Input data

The input file `permbit.in` contains on the first line the number $C$, representing the task for that test case: 1 for task a), 2 for task b), and 3 for task c).

The next line contains the numbers $N$ and $M$, and the following $N$ lines each contain an array of $M$ bits.

## Output data

The output file `permbit.out` contains, if $C = 3$, the number of valid permutations modulo $1.000.000.007$, otherwise, a permutation, either any or median as required.

## Constraints and clarifications

$2 \leq N$

$M \leq 10^6$

$N * M \leq 10^6$

10 points: $N, M \leq 8$, $1 \leq C \leq 3$

10 points: $N, M \leq 300$, $C = 1$

10 points: $N, M \leq 300$, $C = 2$

10 points: $N, M \leq 300$, $C = 3$

30 points: $N * M \leq 10^6$, $C = 2$

10 points: $N * M \leq 10^6$, $C = 1$

20 points: $N * M \leq 10^6$, $C = 3$

## Example

`permbit.in`

1

3 8 

10111010

11000111

01111100

`permbit.out`

2 5 8 7 1 4 6 3

`permbit.in`

2

3 10

0000011010

0001100001

1010000100

`permbit.out`

6 9 7 8 3 10 5 2 4 1

`permbit.in`

3

3 6

001100

000011

100100

`permbit.out`

8