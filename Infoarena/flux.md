# Flow

In the city there are $N$ reservoirs connected by $M$ pipes. The reservoir numbered $1$ is the source, and the reservoir numbered $N$ is the destination. For each pipe, the volume of water that can pass through it is known. For each reservoir, it is known that the volume of water entering that reservoir is equal to the volume of water exiting that reservoir (which is not valid for the source and the destination). In addition, the following restriction is imposed: for any two reservoirs $i$ and $j$, the sum of the volumes of water that pass through the pipes on an arbitrary path from $i$ to $j$ is constant (it is the same regardless of the path). Note: When calculating the sum, if water flows through a pipe in the direction opposite to its usage in the solution, then it is considered with a negative sign.

## Task

Calculate the maximum volume of water that can reach the destination in such a network.

## Input data

In the input file `flux.in`, the first line contains $N$ , the number of reservoirs. The second line contains $M$ , the number of pipes. Then follow $M$ lines containing triplets $a$ $b$ $c$ meaning there is a bidirectional pipe with capacity $c$ between $a$ and $b$.

## Output data

The output file `flux.out` will contain a single line that contains the maximum volume of water that can reach the destination.

## Constraints and clarifications

$2 \leq N \leq 100$

$1 \leq M \leq 5000$

$0 \leq c \leq 10000$

An error margin of $10^{-3}$ is accepted for the result.

## Example

`flux.in`

```
4
6
1 3 3
2 1 3
4 3 6
2 3 3
2 4 6
1 2 2
```

`flux.out`

```
6.500
```

## Explanation

Through pipe $1$, $2.5$ is sent from $1$ to $3$. Through pipe $2$, $2$ is sent from $1$ to $2$. Through pipe $3$, $3$ is sent from $3$ to $4$. Through pipe $4$, $0.5$ is sent from $2$ to $3$. Through pipe $5$, $3.5$ is sent from $2$ to $4$. Through pipe $6$, $2$ is sent from $1$ to $2$.

For reservoir $2$, the sum of incoming quantities is $2 + 2 = 4$ and is equal to the sum of outgoing quantities $3.5 + 0.5 = 4$.

For reservoir $3$, the sum of incoming quantities is $0.5 + 2.5 = 3$ and is equal to the sum of outgoing quantities $3$.

We will illustrate the additional condition for several paths from $1$ to $3$.

Pipes

Sum

$1$

$2.5$

$2\ 4$

$2 + 0.5 = 2.5$

$6\ 5\ 3$

$2 + 3.5 - 3 = 2.5$

In the last example, pipe $3$ is traversed from $4$ to $3$ while water flows from $3$ to $4$, hence it has a negative sign.