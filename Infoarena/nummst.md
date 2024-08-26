# NumMst

After recent events, the Elders of the City got angry and decided to change their strategy, turning to their magical quiver from which they can draw all sorts of things. Among other things, it contains $N$ gold coins, which the Elders of the City wish to divide into multiple heaps. The goal is for the greatest common divisor (gcd) of the numbers representing how many coins are in each heap to be maximized. In case there are multiple ways to achieve the maximum gcd, the Elders of the City want the one where the least common multiple (lcm) of the numbers is maximized. To appease the Elders of the City, you need to solve this problem.

## Input data

The input file `nummst.in` contains on the first (and only) line $N$, the number of gold coins.

## Output data

The output file `nummst.out` will contain a single line containing $n_1$, $n_2$, $\dots$ $n_k$, $(2 \leq k \leq N)$ where $n_i$ is the number of coins in heap $i$.

## Constraints

$10 \leq N \leq 10^{7}$

For a solution that meets only the first condition, 20% of the points will be awarded.

Attention: $N$ will be composite (there exist two natural numbers $A$ and $B$ different from 1 such that $N = A \times B$)

## Example

`nummst.in`
```
200
```
`nummst.out`
```
100 100
```