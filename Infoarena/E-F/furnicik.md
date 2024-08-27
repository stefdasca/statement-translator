# Ants

There are $N$ ants on a bar of length $L$ millimeters. For each ant, we know its initial position (its position at time $0$) and the direction in which it is moving. All ants move at a speed of $1$ millimeter/second. Because it is good in life to avoid bad outcomes, Igah placed $2$ poles at the ends of the bar (one pole at position $0$ and one at position $L$). Knowing that when an ant collides with a pole or another ant, it changes its direction (but maintains its speed), determine the position of each ant $i$ after $T$ seconds.

## Input data

The input file `furnicik.in` will contain on the first line $3$ natural numbers $N$, $L$, and $T$. On the next $N$ lines, there will be $2$ natural numbers each, $poz_i$ and $sens_i$, representing the initial position and the direction of movement of ant $i$. (if the direction is $0$, the ant starts moving to the left; if the direction is $1$, the ant starts moving to the right). The ants are sorted in ascending order by position.

## Output data

The output file `furnicik.out` will contain $N$ natural numbers representing the positions of the $N$ ants after $T$ seconds of movement.

## Constraints

$1 \leq N \leq 100\,000$ 

$0 \leq poz_i \leq L \leq 1\,000\,000\,000$

$1 \leq T \leq 2\,000\,000\,000$ 

## Example

`furnicik.in`

```
2 10 3
1 0
5 1
```

`furnicik.out`

```
2 8
```