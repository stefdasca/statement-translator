
You want to level the land you have bought, which has a width of $1$ meter and a length of $N$ meters, consisting of $N$ successive zones, each zone having a length of $1$ meter. The land is represented as a sequence of $N$ natural numbers $h_1, h_2, h_3, \ldots, h_N$ representing the heights in meters of the zones from the initial land, seen from left to right.

To level the land, you have rented a bulldozer that works as follows. A height $H$ (a natural number) is chosen to raise the blade of the bulldozer to. Initially, the bulldozer has on its blade a quantity $C=0$ cubic meters of soil. The bulldozer starts moving from left to right and when it reaches zone $i$, depending on the height $h_i$ of that zone, it will be in one of the following situations:
- if $h_i \geq H$ then the additional amount $h_i - H$ is added to $C$ and the level of the zone reaches $H$.
- if $h_i < H$ then the difference $H - h_i$ is subtracted from $C$ to bring the level of the zone to the level $H$.

We note that $H$ must be initially chosen so that every time the bulldozer reaches the second situation, it has enough soil on the blade ($C \geq H - h_i$). After the bulldozer goes through the $N$ zones of length $1$, it's possible that some soil will remain on the blade, but this does not concern you because at the right end of the land there is a river, and the remaining soil will be dumped there.

# Task
Write a program that calculates the maximum height $H$ to which the blade can be raised so that the land can be leveled to that height.

# Input data
The input file `buldo.in` contains on the first line the natural number $N$, and on the second line, separated by a space, the $N$ natural numbers $h_1$, $h_2$, $h_3$, $ \dots $, $h_N$, with the meaning from the statement.

# Output data
The output file `buldo.out` will contain a single line, on which the required natural number $H$ will be written.

# Constraints and clarifications
- $1 \leq N \leq 100\ 000$
- The heights are natural numbers, $1 \leq h_i \leq 1\ 000\ 000\ 000$, for any $i$, $1 \leq i \leq N$.
- For tests worth 50 points, $N \leq 1\ 000$ and $h_i \leq 1\ 000$, for any $i$, $1 \leq i \leq N$.

# Example
`buldo.in`
```
4
5 2 1 6
```
`buldo.out`
```
2
```
## Explanation
If the blade is set to the height $H=2$, after passing zone $1$ (the first meter in length), this zone remains at the height $2$ and $C=3$ cubic meters of soil are carried by the blade to zone $2$. There, a total of $2+3=5$ cubic meters of soil will be obtained, but only $2$ are kept, and the remaining $C=3$ is transported to zone $3$. At zone $3$, a total of $1+3=4$ cubic meters of soil will be obtained, but only $2$ are kept, and the remaining $C=2$ is transported to zone $4$. At zone $4$, a total of $6+2=8$ cubic meters of soil will be obtained, but only $2$ are kept, and the remaining $C=6$ is dumped into the river.

If the blade were set to the height $H=3$, at zone $3$ it can only reach the height $2$ and the attempt fails (as it is a lower height than the proposed one).