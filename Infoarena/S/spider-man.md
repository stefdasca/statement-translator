## Task

Spider-Man's incredible web is no longer functioning as well as it did in his youth, but evil remains just as powerful, and Spider-Man is the only one who can protect humanity. Today, he is in the city of Disconia, which, as the name suggests, is shaped like a disc with negligible thickness. Doctor Curt Connors, the deadly lizard, has been terrorizing the population of this city for a few weeks. Spider-Man is on the front side of the disc, while the Lizard is on the back of it. Being greatly affected by the crisis, Spider-Man wants to reach the Lizard using public transport but spending as little money as possible on this journey. He is not very good at informatics, so he asks for your help. In the city of Disconia, there are 2 types of public transport: from inside the disc to a point on the circumference or from a point on the circumference to a point inside. For both types of tickets, the cost is equal to the square of the distance traveled. Thus, the cost of a ticket between two points $A(x_1, y_1)$ and $B(x_2, y_2)$ (exactly one of the points $A$ and $B$ is on the circumference) is equal to $(x_1 - x_2)^2 + (y_1 - y_2)^2$. Knowing the coordinates of the center of the disc, $(x_c, y_c)$, its radius, $r$, the coordinates of the point on the front side of the disc where Spider-Man is located, $(x_1, y_1)$, and the coordinates of the point on the back side of the disc where the Lizard is located, $(x_2, y_2)$, find the minimum cost that Spider-Man needs to pay to reach the criminal.

## Input data

The input file `spider-man.in` will contain on the first line the coordinates of the center of the circle, $x_c$ and $y_c$, and its radius, $r$. The second line will contain 4 real numbers $x_1$, $y_1$, $x_2$, $y_2$, having the significance described in the statement.

## Output data

The output file `spider-man.out` will contain on the first line a real number representing the minimum cost that Spider-Man needs to pay to reach the criminal.

## Constraints

$-10000 \leq x_1, y_1, x_2, y_2, x_c, y_c \leq 10000$

$0 \leq r \leq 20000$

Both Spider-Man and the Lizard are considered to be point-like.

An answer is considered correct if the absolute difference between it and the committee's result is $< 0.0001$.

The interior does not include the circumference.

It is guaranteed that both Spider-Man and the Lizard are inside.

Spider-Man will use exactly 2 means of public transport: one from the initial position to a point on the circumference and one from the point on the circumference to the Lizard’s position.

## Example

`spider-man.in`
```
2.4234 3.12341 5.123124 
2.6894 3.59560 -1.0304 1.4928
```
`spider-man.out`
```
32.621373
```