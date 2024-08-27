# Zapezi2

The Great Leaders of Another City are facing a prolonged winter. In Another City, there are $N$ intersections, numbered from $1$ to $N$, any two of which are directly connected by a bidirectional street. Under dire weather conditions, the Great Leaders need to be prepared for emergencies. We call an emergency network a minimum cardinal subset of streets uncovered by snow, ensuring the existence of a direct or indirect path between any two intersections. As of now, there exist $K$ snow-covered streets. The Great Leaders of Another City would like to know how many different emergency networks can be formed at the moment, modulo $10^9$.

## Input data

The input file `zapezi2.in` will contain on its first line the number of tests $T$. The first line of a test contains the numbers $N$ and $K$ signifying the number of intersections and the number of snow-covered streets, respectively. The following $K$ lines each contain a pair $A$ $B$ signifying that the street connecting intersections $A$ and $B$ is snow-covered.

## Output data

The output file `zapezi2.out` will contain $T$ lines, each containing the answer for the corresponding test modulo $10^9$.

## Constraints

$1 \leq T \leq 20$

$1 \leq N \leq 10\ 000$

$1 \leq K \leq 16$

## Example

`zapezi2.in`

`2`

`3 0`

`4`

`3 1`

`2 1`

`3 1`

`4`

`3 0`

`3`