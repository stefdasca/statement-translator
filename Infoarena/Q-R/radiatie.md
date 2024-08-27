## Radiation

Zaharel is a nuclear physics researcher working at a secret research complex consisting of $N$ laboratories, conveniently numbered from $1$ to $N$. These laboratories are also connected by $M$ bidirectional tunnels of various lengths. Although the laboratories are designed to protect researchers from radiation, the tunnels do not offer complete protection. As a result, if a researcher uses a particular tunnel, they will be exposed to a level of radiation directly proportional to the tunnel's length. Zaharel has to perform $K$ trips between various pairs of laboratories. Knowing that prolonged exposure to radiation has harmful effects, he will always choose a route where the maximum length of any tunnel used is minimized. Determine which routes Zaharel will choose.

## Input data

The first line of the input file `radiatie.in` will contain the natural numbers $N$, $M$, and $K$ separated by spaces. The next $M$ lines will contain three natural numbers $a$ $b$ $c$ with the meaning that there is a tunnel between laboratory number $a$ and laboratory number $b$, with length $c$. Subsequently, the next $K$ lines will contain pairs of natural numbers $x$ $y$ indicating that Zaharel will make a trip between laboratories $x$ and $y$.

## Output data

The output file `radiatie.out` will contain $K$ lines, each containing the minimum maximum length considering the tunnels traversed by Zaharel for each trip. The results will be printed in the order in which the $K$ trips are given in the input file.

## Constraints and clarifications

$1 \leq N, K \leq 15000$

$1 \leq M \leq 30000$

The length of a tunnel is a natural number in the interval $[1, 10^9]$

A route represents a sequence of laboratories $a_1, a_2 \dots a_x$ with the property that there is a tunnel between $a_i$ and $a_{i+1}$ for any $i < x$

It is guaranteed that there is at least one route between each of the $K$ pairs of laboratories in the input file

## Example

`radiatie.in`

```
6 6 8
1 2 5
2 3 4
3 4 3
1 4 8
2 5 7
4 6 2
1 2
1 3
1 4
2 3
2 4
5 1
6 2
6 1
```

`radiatie.out`

```
5
5
4
4
4
7
4
5
```