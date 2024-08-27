# Cat

A cat in a cage. Introduction: A convex polygon Cat and a convex polygon Cage are given. In the vertices of the Cage polygon, there is a fixed and tall iron bar at each one. As there are many iron bars, the Cat feels too constrained. After all, it's a Cat living in the $21$st century and values its freedom. So Marcel, a philanthropist who understands the mechanisms of his time, decided to give the Cat the sensation of being free without that being the actual case.

## Task

Remove a maximum number of bars from the Cage in such a way that the Cat cannot escape, no matter how much it rotates and translates successively, knowing that it is not allowed to touch the remaining iron bars.

## Input data

The input file `pisica.in` contains on the first line the number $M$ of points that form the Cat polygon. On the next $M$ lines, there are two real numbers with values between $-400000$ and $400000$, with up to $4$ decimal places, representing, in trigonometric order, the vertices of the Cat polygon. In the same format follows, on the next $N + 1$ lines, the description of the Cage polygon, which has $N$ vertices.

## Output data

The output file `pisica.out` contains the number of bars remaining in the Cage after as many as possible have been removed, without allowing the Cat to escape the Cage.

## Constraints and Clarifications

$4 \leq M \leq 100\,000$

$24 \leq N \leq 100\,000$

The vertices of each polygon are distinct points

It is guaranteed that the Cat cannot escape if all the bars are kept

It is guaranteed that if the Cat gains or loses a little weight, the answer would remain the same (the tests are constructed in such a way that there are no issues related to the precision of real numbers).

It is guaranteed that if all the bars are kept, the Cat can rotate/translate successively in such a way that it touches any bar with any of its vertices.

For $60$ points, it is guaranteed that $N \leq 1\,000$ - feedback test $10$ Meow!!!

The rest of the feedback tests are among the largest tests

## Example

`pisica.in`
```
4
1.5 1.5
2.5 1.5
2.5 2.5
1.5 2.5
24
0 0
0.667 0
1.333 0
2 0
2.667 0
3.333 0
4 0
4 0.667
4 1.333
4 2
4 2.667
4 3.333
4 4
3.333 4
2.667 4
2 4
1.333 4
0.667 4
0 4
0 3.333
0 2.667
0 2
0 1.333
0 0.667
```
`pisica.out`
```
20
```

## Explanation

The Cat is a square with a side of $1$ and the Cage is a square with a side of $4$ around it, with bars every $\sim\frac{2}{3}$ units. We can remove the bars from the corners of the squares, but no other bars can be removed, because otherwise, the Cat would find it too easy to escape.