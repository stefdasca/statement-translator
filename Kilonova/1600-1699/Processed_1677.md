~[cerc1.png|align=right]

$N$ points numbered from $1$ to $N$ are placed on a circle, clockwise, in a strictly increasing order. There are $M$ different line segments connecting $M$ pairs of points among the given $N$ points. The two points that form any pair are distinct. The distances between two successive points are chosen so that there are not $3$ or more segments passing through the same interior point of the circle.

# Task

Knowing the number of points, the number of pairs and the pairs of points that will be connected, determine the number $P$ of intersection points formed by these inside the circle (the intersection points located right on the circle are not considered).

# Input data

The input file `cerc.in` contains:

- The first line contains two numbers $N$ and $M$ separated by a space, representing the number of points and respectively the number of line segments;
- The next $M$ lines contain a pair of distinct numbers $p_{i_1}$, $p_{i_2}$ separated by a space, representing the endpoints of each segment.

# Output data

The output file `cerc.out` will contain a single number $P$ representing the total number of intersection points formed inside the circle. If this number exceeds $999\ 999$, then the number will be written containing only its last $6$ digits.

# Constraints and clarifications

* $1 \leq N \leq 500$, natural number
* $0 \leq M < 125\ 000$, natural number
* $1 \leq p_{i_1} < p_{i_2} \leq N$, natural numbers, for any $i \in \{1, \dots, M \}$
* There are no two identical pairs $p_{i_1}$, $p_{i_2}$

# Example

`cerc.in`
```
5 6
1 2
1 3
1 4
2 4
3 5
4 5
```

`cerc.out`
```
3
```

## Explanation

There are $3$ intersection points formed inside the circle (marked by small circles in the figure below).

~[cerc2.png]