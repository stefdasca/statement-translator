Rebellion

The Great Galactic Empire includes several inhabited solar systems. Naturally, the distances between systems are enormous, so to travel between them, wormholes have been generated between various pairs of planets. Wormholes are bidirectional, but they require an enormous amount of energy to keep open. Within the empire, it is possible to travel between any two systems, but the Emperor has decided that there should not be more than one way to reach between any two systems, to keep costs to a minimum. The inhabitants of the far corners of the galaxy have revolted because they have to make too many jumps to reach certain systems. To calm the population, the Emperor decided to generate another wormhole while deactivating an existing one. To please everyone, the constructed wormhole and the destroyed one will be chosen to minimize the maximum number of jumps between any two systems in the galaxy.

## Input data

The input file `revolta.in` will contain on the first line a single number, $t$, representing the number of tests. Each test will begin with the number of systems in the galaxy, $n$, followed by $n-1$ lines of the form $a$ $b$, representing a wormhole between systems $a$ and $b$.

## Output data

The output file `revolta.out` will contain, for each test, a line containing the minimum number of jumps that can be obtained after replacement. If the initial number of jumps was already optimal, this will be printed.

## Constraints

$1 \leq t \leq 10$  
$2 \leq n \leq 100000$  
$0 \leq a, b < n$  

## Example

`revolta.in`
```
2
4
0 1
1 2
2 3
4
0 1
1 2
1 3
```

`revolta.out`
```
2
2
```