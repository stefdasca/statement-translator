## Task

In the past, the city of Târgu Mureș had $N$ towers of various heights numbered from $1$ to $N$. Chronicles mention that the fortress hosted the largest competition among $N$ dwarfs in the art of jumping from tower to tower, and the rules of the competition were as follows: each dwarf $i$ will start from tower $i$; a dwarf on a tower $k$ can only jump to towers with indices strictly smaller than $k$; dwarfs can only jump to towers strictly taller than the tower they are on; if there are multiple towers they can jump to, a dwarf will jump to the tower with the largest index; when a dwarf can no longer find a tower to jump to, they will stop; the score obtained by each dwarf is equal to the number of towers they have traversed. After hundreds of years since the competition, the heights of the towers have been forgotten. However, the chroniclers recorded the scores for each dwarf. Given the scores obtained by each dwarf $i$ out of the $N$ dwarfs, determine the heights of the $N$ towers from ancient times. Any solution is considered correct as long as it respects the competition rules and the dwarfs achieve the given scores. If the scores are not valid for any configuration of tower heights, then $-1$ will be displayed. The goal is to find the answers for $T$ such problems.

## Input data

The input file `salturi.in` contains on the first line the natural number $T$ representing the number of tests in the input file. Then follow $T$ tests. Each test is described over two lines in the file as follows: the first line contains the natural number $N$ representing the number of dwarfs that participated in the competition; the next line contains $N$ natural numbers separated by spaces indicating that the $i$-th number represents the score obtained by dwarf $i$.

## Output data

The output file `salturi.out` must contain $T$ lines: on the $k$-th line is the answer for test $k$. If there is a solution for test $k$, then the $k$-th line must contain $N$ natural numbers separated by spaces indicating that the $i$-th number represents the height of tower $i$. If there is no solution for test $k$, then the $k$-th line must contain the value $-1$.

## Constraints and clarifications

$1 \leq T \leq 5$.  
$1 \leq N \leq 250\ 000$.  
The sum of $N$ in a file is at most $500\ 000$.  
The scores obtained by the dwarfs are natural numbers between $1$ and $N$.  
The heights of the ancient towers are natural numbers between $1$ and $10^9$.  
For tests worth $30$ points, $1 \leq N \leq 1\ 000$.  
The problem will be evaluated on tests worth $90$ points.

## Example

`salturi.in`
```
2
5
1 1 2 1 2
4
1 3 2 1
```

`salturi.out`
```
3 4 2 6 3
-1
```

## Explanation

There are $T=2$ tests in the file. For the first test, $N=5$. If the heights of the towers are $3$ $4$ $2$ $6$ $3$, the dwarfs will jump as follows: Dwarf $1$ (initially on tower $1$ of height $3$) has nowhere to jump. Their score will be $1$. Dwarf $2$ (initially on tower $2$ of height $4$) has nowhere to jump. Their score will be $1$. Dwarf $3$ (initially on tower $3$ of height $2$) will jump to tower $2$ (of height $4$), and then has nowhere to jump. Their score will be $2$. Dwarf $4$ (initially on tower $4$ of height $6$) has nowhere to jump. Their score will be $1$. Dwarf $5$ (initially on tower $5$ of height $3$) will jump to tower $4$ (of height $6$), and then has nowhere to jump. Their score will be $2$. The scores $1$ $1$ $2$ $1$ $2$ are obtained, so the solution is valid. Note that the tower heights are not unique, so other solutions can also be provided. For the second test, $N=4$. It is not possible to obtain any configuration of tower heights for which the given scores can be achieved, so $-1$ is displayed.