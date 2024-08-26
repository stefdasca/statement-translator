## Scenario

Toffolo has a scenario with $N$ pages. This scenario needs to be divided into $K$ acts. For each act $i$, the number of scenes it must be divided into is known: $S_i$. Given $N$, $K$, and the array $S$, determine how many ways Toffolo can divide the scenario into $K$ acts, and each act $i$ into $S_i$ scenes. A division of the scenario into acts/scenes consists of delimiting each page within an act/scene.

## Input data

The input file `scenariu.in` will contain on the first line 2 natural numbers $N$ and $K$. The next line will contain $K$ values representing the array $S$.

## Output data

The output file `scenariu.out` will contain a line representing the answer modulo $666013$.

## Constraints

$1 \leq N \leq 10000$

$1 \leq K \leq 10000$

The total number of scenes will be less than or equal to $N$

## Example

`scenariu.in`
```
5 2
1 2
```

`scenariu.out`
```
6
```