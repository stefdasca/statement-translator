Por Costel and the Betrayal

Por Costel sold his soul and authorship, agreeing to become a character in a final round problem of the ONIS competition. For this, he received as a Bribe a rectangular land with $N$ rows and $M$ columns, each of the $N \times M$ plots being available for corn cultivation. Hearing about this new opportunity, Por Costel's friends started to occupy some plots, already preparing for the harvest. Each of Por Costel's $K$ friends occupies exactly one plot of land. Por Costel is worried because his friends, being real pigs, did not consider that they might interfere with the corn harvesting. Specifically, he wants to find out if, after his $K$ friends have occupied the plots, the remaining free plots are still connected. We say that plots are connected if for any two free plots, $A$ and $B$, we can reach from $A$ to $B$, always moving to an adjacent free plot without leaving the land.

## Input Data

The input file `tradare.in` will contain on its first line the number of tests $T$. Then follow $T$ tests, the structure of a test being the following: the first line contains the numbers $N$ $M$ $K$, representing the dimensions of the land and the number of Por Costel's friends. The next $K$ lines each contain a pair of numbers $X$ $Y$, representing the coordinates of the plot occupied by the respective friend ($X$ being the row and $Y$ the column). The rows of the land are numbered from 1 to $N$, and the columns from 1 to $M$.

## Output Data

The output file `tradare.out` will contain $T$ lines, each containing the answer for the corresponding test: the message "DA" if the free plots are still connected, and "NU" otherwise.

## Constraints and clarifications

$1 \leq T \leq 10\ 000$

$1 \leq N, M \leq 100\ 000$

$0 \leq K \leq \min(100\ 000, N \times M)$

A plot can appear multiple times.

If there are no free plots, the answer is DA.

The sum of the values of $K$ in the same input file will not exceed 1\ 000\ 000.

## Example

`tradare.in`

```
2
3 3 3
1 2
2 2
3 2
3 4 1
3 4
```

`tradare.out`

```
NU
DA
```