# Kangaroo

A garden is composed of a line with $N$ cells numbered from $1$ to $N$. Initially, all cells contain plants. A kangaroo starts in cell numbered $cs$. Then he jumps from cell to cell, eating the plants he encounters. He always stops in cell numbered $cf$ after visiting each of the $N$ cells exactly once, including $cs$ and $cf$. Evidently, the kangaroo will make $N-1$ jumps. The kangaroo does not want to be caught and therefore after each jump he changes the direction he will jump next: if he is in cell numbered $current$, immediately after he jumped here from cell numbered $prev$ and will jump from the cell numbered $current$ to the cell numbered $next$, then: if $prev < current$, then $next < current$; otherwise, if $current < prev$, then $current < next$. Knowing the number $N$ of cells in the garden, the initial cell $cs$ from where the kangaroo starts eating plants and the final cell $cf$ where the kangaroo stops, you must calculate the number of distinct routes the kangaroo can take while jumping through the garden.

## Input data

The input file `kangaroo.in` will contain three positive integers $N$, $cs$, $cf$, separated by a space. 

## Output data

The output file `kangaroo.out` must contain a single integer representing the number of distinct routes the kangaroo can take modulo $1000000007$ $(10^9 + 7)$. 

## Constraints

$2 \leq N \leq 2000$

$1 \leq cs \leq N$

$1 \leq cf \leq N$

$cf \neq cs$

For tests worth 6 points, $N \leq 8$.

For tests worth 36 points, $N \leq 40$.

For tests worth 51 points, $N \leq 200$.

Any route is uniquely determined by the order in which cells are visited.

It is guaranteed for each test that there exists at least one route that respects the rules.

The kangaroo can jump in any direction from $cs$. 

## Example

`kangaroo.in`
```
4 2 3
```

`kangaroo.out`
```
2
```

## Explanation

The kangaroo starts in cell $2$ and stops in cell $3$. The two correct routes are $2 \rightarrow 1 \rightarrow 4 \rightarrow 3$ and $2 \rightarrow 4 \rightarrow 1 \rightarrow 3$.