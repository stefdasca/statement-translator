# Por Costel and the Alien Invasion

Aliens are invading Earth! Fortunately, we have someone to call upon: humanity's squeaky hero, Por Costel! He has a brilliant plan involving aluminum foil and many staplers, but he also needs your help. The alien invasion occurs in multiple phases. It is concentrated on an area of kilometers (we imagine the kilometers numbered from left to right starting from 1). The invasion consists of the following types of events: An alien spaceship enters the atmosphere and hovers at a distance from the ground, stretching between kilometers $x$ and $y$. The last alien spaceship that entered the atmosphere leaves the atmosphere. All Por Costel needs from you is to implement a radar. He needs the radar to communicate at certain moments the altitude at which the closest alien spaceship to the ground is located at kilometer $z$.

## Input data

The input file `invazia.in` will contain on the first line $N$ and $M$ (the number of events). The following $N$ lines describe each event:
- the character 'I' followed by 3 integers $x$ $y$ $z$ - a new alien spaceship appears
- the character 'E' - an alien spaceship disappears
- the character 'R' followed by an integer $x$ - radar query

## Output data

The output file `invazia.out` will contain $M$ lines that contain the answers for each radar query. In case there is no spaceship at kilometer $x$, the message "GUITZZZ!" (without quotes) will be printed.

## Constraints and clarifications

$1 \leq N \leq 100,000$

$1 \leq M \leq 10,000$

$1 \leq x \leq 1\,000\,000$ for any operation I

$1 \leq y \leq 1\,000\,000$ for any operation I

$1 \leq z \leq 1\,000\,000$ for any operation R

It is guaranteed that for any operation of type E, there is at least one alien spaceship in the atmosphere.

## Example

`invazia.in`

```
12
6
I 1 7 10
R 3
I 1 12 1
E
I 5 12 2
R 7
```

`invazia.out`

```
10
2
```