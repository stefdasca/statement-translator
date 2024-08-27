# Catun

In a feudal kingdom, there are multiple human settlements, numbered from $1$ to $N$, connected by roads of various lengths. Among these settlements, some are fortresses while the rest are simple catuns. Each fortress needs to supply the troops stationed in it, hence it requires fiefs. As the grand advisor to the monarch, you are asked to designate the fiefs assigned to each fortress, specifically all those catuns that are closer to the respective fortress than to any other. If a catun is at an equal distance from two fortresses, it will be considered to belong to the fortress with the smaller identification number.

## Task

Determine for each catun to which fortress it belongs.

## Input data

The input file `catun.in` will contain the numbers $N$, $M$, $K$, indicating, in this order, the number of settlements, the number of roads, and the number of fortresses. The second line of the file will contain $K$ distinct natural numbers indicating the identification numbers of the fortresses. The next $M$ lines, until the end of the file, will contain triplets of the form $(x, y, z)$, signifying that there is a bidirectional road between settlements $x$ and $y$ of length $z$, expressed in the unit of measurement for lengths used in the Middle Ages.

## Output data

The output file `catun.out` will contain a single line with $N$ natural numbers, the $i$-th number being $0$ if settlement $i$ is a fortress or is a catun from which none of the $K$ fortresses can be reached, or the number of the fortress to which settlement $i$ is connected, otherwise.

## Constraints and clarifications

$1 \leq K \leq N \leq 36\,000$

$1 \leq M \leq 72\,000$

There is at most one road between any two settlements

## Example

`catun.in`
```
8 9 2
2 5
1 3 6
1 5 3
1 6 1
2 3 9
5 6 5
6 8 7
3 6 2
4 7 1000
2 8 5
```

`catun.out`
```
5 5 0 5 0 0 5 0 2
```