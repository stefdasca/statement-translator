# War of the Worlds

Country A has $N$ cities numbered from $1$ to $N$. These cities are connected by bidirectional roads in such a way that there is exactly one single path between any pair of cities. Since country A was attacked by country B, country A wants to position the army headquarters in one of its cities. For defensive reasons, the headquarters must be placed in the city with the property that the maximum distance between the chosen city and any other city is minimized (in case any city is attacked, the headquarters must reach there as quickly as possible; using the above property, it is attempted to minimize the damage in the worst-case scenario).

## Task

Find all the cities where the headquarters can be placed.

## Input data

The input file `razboi.in` contains on the first line the number $T$ of tests. The following lines describe these $T$ tests. The first line of each test contains the number $N$, representing the number of cities in country A. The next $N-1$ lines contain the description of a road - three integers separated by spaces: $A$, $B$, $D$. $A$ and $B$ represent the numbers of the cities connected by that road and $D$ represents the length of the road.

## Output data

For each test, print in the output file `razboi.out` the following line: "Test no # $XXX$ ", where $XXX$ represents the respective test number. Then print on the following lines the number of cities where the headquarters could be placed. These numbers must be printed in ascending order.

## Constraints and clarifications

$1 \leq N \leq 16000$

$1 \leq D \leq 10000$

$1 \leq T \leq 20$

## Example

`razboi.in`

```
3 
5 
1 2 1 
1 3 2 
1 4 3 
4 5 4 
2 
1 2 19 
3 
1 2 1 
2 3 1 
```

`razboi.out`

```
Test no #1 
4 

Test no #2 
1 2 

Test no #3 
2 
```