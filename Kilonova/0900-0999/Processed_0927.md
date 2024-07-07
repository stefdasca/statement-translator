
The model of a solar system consisting of $N$ planets revolving around a star $S$ in a counterclockwise direction is considered. The trajectories of the planets are considered circular and with different radii, and the rotational speeds of the planets around the star are natural numbers and are expressed in degrees per day ($\\degree$/day).

# Task
Given the number of planets $N$ and their rotational speeds $V_i$, $1 \\leq i \\leq N$, as well as two natural numbers $P$ and $Z$, determine the number $A$ of alignments of at least $P$ planets in a line passing through the center of star $S$, after $Z$ days have passed. The evolution of the solar system begins with all the planets positioned horizontally, to the right of star $S$.
\
For example, for $N=4$, $P=3$, $Z=365$ and $V = [20, 11, 8, 6]$, the alignment of at least $3$ out of the $4$ planets will occur at the end of days $60$, $90$, $120$, $180$, $240$, $270$, $300$, $360$. After $365$ days, there will be $A=8$ alignments. The image to the right shows the position of the planets at the first alignment.
~[1.jpg|align=center|width=55em]

# Input data
The input file `alinieri.in` contains on the first line, in this order, the natural numbers $N$, $P$, and $Z$, and on the second line, $N$ natural numbers $V_i$, $1 \\leq i \\leq N$ with the above significance. The numbers on the same line of the file are separated by a space.

# Output data
The output file `alinieri.out` will contain on the first line the number $A$, with the above significance.

# Constraints and clarifications
- $2 \\leq P \\leq N \\leq 10^5$
- $1 \\leq Z \\leq 10^6$
- $1 \\leq V_i \\leq 10^3$, $1 \\leq i \\leq N$
- For tests worth $30$ points, $1 \\leq Z \\leq 1\\ 000$.
- For tests worth $30$ points, $1 \\leq N \\leq 100$.
- For tests worth $30$ points, $2 \\leq P \\leq 9$.
- Only alignments at the end of each day (midnight) when the planets have completed their daily course will be considered.

# Example 1
`alinieri.in`
```
4 3 365
20 11 8 6
```
`alinieri.out`
```
8
```
## Explanation
$N=4$, $P=3$, $Z=365$ and $V = [20, 11, 8, 6]$.

The first alignment of at least $3$ planets out of the $4$ planets occurs after $60$ days (as shown in the figure above).

The evolution of the $4$ planets is as follows:
- planet $1$ makes 3 complete rotations and an additional $120\\degree$;
- planet $2$ makes one complete rotation and an additional $300\\degree$;
- planet $3$ makes one complete rotation and an additional $120\\degree$;
- planet $4$ makes exactly one rotation.

The next alignments of at least $3$ out of the $4$ planets occur after $90$, $120$, $180$, $240$, $270$, $300$, $360$ days. Thus, in $365$ days, there will be $8$ alignments.

# Example 2
`alinieri.in`
```
7 3 2020
10 20 10 15 20 10 20
```
`alinieri.out`
```
3928
```
## Explanation
$N=7$, $P=3$, $Z=2020$ and $V = [10, 20, 10, 15, 20, 10, 20]$.

In the $2020$ days there were $3928$ alignments of at least $3$ planets out of the $7$ planets that form the solar system.

# Example 3
`alinieri.in`
```
6 3 658903
17 24 12 150 200 12
```
`alinieri.out`
```
58568
```
## Explanation
$N=6$, $P=3$, $Z=658903$ and $V = [17, 24, 12, 150, 200, 12]$.

In the $658903$ days there were $58568$ alignments of at least $3$ planets out of the $6$ planets that form the solar system.
