## Task

A certain street in the Ephemeral City can be viewed as the $Ox$ axis of natural numbers. Along this street, there are $N$ public lighting pillars. The $i$-th pillar is located at coordinate $X_i$ and for an amount of $C_i$ lei, a bulb can be installed inside the pillar, which will illuminate $S_i$ meters to the left of the pillar and $D_i$ meters to the right of the pillar. The mayor of the city wants all pillars to be visible. A pillar is visible if a bulb is installed inside it or if it is within the illumination range of another pillar with a bulb installed. He has decided to select a set of pillars and install a bulb in each of them. The problem is that he will have to pay for each chosen pillar the cost required to install a bulb in that pillar, and he wants the sum of these costs to be minimal. Help the mayor find the minimum cost required for all the pillars in the Ephemeral City to be visible.

## Input data

The input file `stalpi.in` contains in the first line the number $N$ having the significance mentioned in the statement. On the next $N$ lines, there follows a quadruple $X \ C \ S \ D$ with the significance that the $i$-th pillar (on line $i+1$ there is information about pillar $i$) is located at coordinate $X$, the cost to install a bulb inside it is $C$, and if this is done, it will illuminate $S$ meters to the left and $D$ meters to the right.

## Output data

The first line of the output file `stalpi.out` contains a natural number $MIN$ representing the minimum cost required for all pillars in the city to be visible.

## Constraints and clarifications

$1 \leq N \leq 100 \ 000$

$1 \leq X_i , S_i , D_i \leq 10^9$

$1 \leq C_i \leq 100 \ 000$

If a bulb is installed in pillar $i$, it will illuminate any pillar $j$ with the property $X_i - S_i \leq X_j \leq X_i + D_i$

There are no two different pillars that have the same coordinate $X$

All numbers in the input file are natural

In at least 40% of the tests $1 \leq N \leq 1000$

Due to the strange infrastructure of the pillars, a bulb can be installed inside them

## Example

`stalpi.in`
```
4
3 1 3 5
1 10 10 9
7 2 5 3
10 18 4 4
```

`stalpi.out`
```
3
```

## Explanation

Bulbs will be installed inside pillars 1 and 3. Pillar 2 will be illuminated by pillar 1, and pillar 4 will be illuminated by pillar 3.