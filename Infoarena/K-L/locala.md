# Local

Dosoftei, in preparation for the Local Informatics Olympiad, tried to solve a problem related to locals, but he couldn't manage it. Can you help him? Given a positive natural number $N$ and two sets $A$ and $B$, subsets of the set $\{1 \dots n\}$, of sizes $N_A$ and $N_B$ respectively. You need to create a permutation of the numbers $\{1 \dots n\}$ that has as local minima, respectively local maxima, exactly the elements of sets $A$, respectively $B$, or indicate that there is none that satisfies this condition.

## Task

## Input data

The input file `locala.in` contains on the first line $N$, $N_A$, and $N_B$. The second line contains $N_A$ distinct natural numbers which represent the elements of set $A$. The third line contains $N_B$ distinct natural numbers which represent the elements of set $B$.

## Output data

The output file `locala.out` will contain on the first line the found permutation (if it exists), or $-1$ if there is none.

## Constraints

$1 \leq N \leq 300\ 000$

A local minimum is an element of the permutation $a_i$ whose neighbors are larger than it.

A local maximum is an element of the permutation $a_i$ whose neighbors are smaller than it.

Two elements are neighbors if they are in consecutive positions.

## Example

`locala.in` `locala.out`
5 2 2
1 2
3 5 
1 3 2 4 5

5 1 1 
5
1 
-1 

## Explanation

In the first example, the permutation contains as local minima only $1$ and $2$, and as local maxima only $3$ and $5$.

In the second example, there is no permutation that has $5$ as a local minimum.