~[0.jpg|align=right]
The city of TownsVille is a very crowded city. It consists of $N$ intersections numbered from $1$ to $N$, connected by $M$ streets. The mayor of the city knows for some of the $N$ intersections a positive coefficient $A[i]$ representing the crowding in intersection $i$. For the intersections where this coefficient is unknown, the mayor is obliged to personally set this coefficient (also positive).

Initially, the mayor did not care much about what coefficients he chose. If for an intersection the coefficient was too small, people would be happy, if not, he would impose taxes, so he would be happy. Unfortunately, the Gangrene Gang is up to all kinds of mischief: from throwing paper in the plastic bin to stealing ice cream from small children, anything is possible. Today, however, they decided to steal the tires from the cars within the intersections. Thus, the mayor imposed the following rule: for any two intersections connected by a street, the difference in crowding coefficient between the two intersections must not be too large. If this difference is too great, the Gangrene Gang would surely attack the more crowded intersection. Otherwise, they would be confused about which one to attack (as they don't know how to count the number of cars in an intersection), which would gain time for the Powerpuff Girls to come to the rescue.

Given the configuration of the city of TownsVille, as well as the known crowding coefficients of some intersections, your goal is to select a crowding coefficient for the rest of the intersections such that you minimize the maximum difference between any two intersections connected by a street.

# Input Data
The input file `cangrena.in` will contain on the first line two natural numbers $N$ and $M$, with the meaning from the statement. The next line will contain $N$ numbers, the $i$-th number representing the crowding coefficient of the intersection numbered with index $i$, if this coefficient is known, $-1$ otherwise. The next $M$ lines will contain two natural numbers $A$ and $B$, representing the fact that intersection $A$ is connected to intersection $B$ through a street.

# Output Data
The output file `cangrena.out` will contain a single line with $N$ positive natural numbers (separated by a space), the $i$-th number representing the crowding coefficient of the intersection with index $i$ (initially fixed coefficients will also be displayed).

# Constraints and clarifications
* $2 \leq N \leq 100\ 000$
* $1 \leq M \leq 200\ 000$
* from any intersection, it is possible to reach any other through existing roads
* there is at least one intersection with a known crowding coefficient
* at least one street reaches every intersection
* streets are bidirectional
* **known** crowding coefficients are non-zero natural numbers less than or equal to $1\ 000\ 000\ 000$

# Example
`cangrena.in`
```
4 3
10 -1 20 12
1 2
2 3
4 2
```
`cangrena.out`
```
10 15 20 12
```
`cangrena.in`
```
8 8
-1 33 -1 -1 -1 -1 -1 31
1 3
1 6
2 5
3 8
4 8
5 6
5 7
6 7
```
`cangrena.out`
```
33 33 32 32 34 34 35 31
```

Explanations
---
~[1.jpg]
~[2.jpg]