Researchers

Researchers on the planet Terminus have discovered a solar system with at least peculiar behavior. The planets orbit around a star, some planets have satellites that orbit around them. What is curious is the fact that satellites in turn have other satellites, which also have satellites, and so on. The researchers were greatly astonished when they realized that:
- any celestial body needs $360$ time units to make a full orbit around the body it orbits.
- all orbits relative to the body they revolve around have the shape of a perfect circle.
- all bodies rotate counterclockwise
  
Given the positions of the planets at a zero moment in time, researchers can accurately predict where any celestial body will be positioned at any moment in time. Can you?

## Input data

The input file `cercetatori.in` contains on the first line two numbers $N$ and $Q$ representing the number of bodies in the solar system and the number of questions, respectively. The next $N$ lines contain $4$ integers each: $I$ $P$ $X$ $Y$. $I$ represents the number of the current body, $P$ represents the number of the parent body it orbits around, and the pair $\(X, Y\)$ represents the position of the body at the zero moment in time. If it is a star that does not orbit around any body, $P$ will have the value $0$. The following $Q$ lines contain $2$ integers each: $A$ $B$ representing the question: where will body number $A$ be after $B$ time units.

## Output data

In the output file `cercetatori.out` you will write $Q$ lines. Line number $i$ will contain two numbers $X$ $Y$ representing the answer to the $i$-th question.

## Constraints and clarifications

$1 \leq N \leq 10000$

$1 \leq Q \leq 500000$

$1 \leq I, A \leq N$

$0 \leq P \leq N$

$0 \leq X, Y \leq 10000$

$1 \leq B \leq 1000000$

Numbers in the output file will be written with exactly $6$ decimal places.

## Example

`cercetatori.in` 

`3 4`

`1 0 1 1`

`2 1 2 1`

`3 2 3 1`

`1 10`

`2 90`

`3 90`

`3 12`

`cercetatori.out` 

`1.000000 1.000000`

`1.000000 2.000000`

`0.000000 2.000000`

`2.891693 1.614648