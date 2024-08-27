# Zota & Chidil

Zota and Chidil had a quarrel. This time, Zota plans to set a series of traps in the forest through which Chidil usually walks. Using a magic formula, he places a trap in multiple cells of the forest. All cells that are at a Manhattan distance less than or equal to $2$ from the trap are also affected. In the image below, the trap is represented by $O$ and the other affected cells are marked with $X$.
```
.......
...X...
..XXX..
.XXOXX.
..XXX..
...X...
....... 
```
Chidil always plans his route. He always starts from the cell with coordinates $(0,0)$. His path is described by a pair $(D, x)$ where $D$ belongs to the set $\{N, E, S, W\}$, and $x$ is a non-zero natural number. This means that from the position he is in, he will take $x$ steps in direction $D$. Although he learns of Zota's evil plan, Chidil does not want to change his route at all. He prefers to know how many cells on his path contain traps or are affected by traps, so he knows exactly how much magic dust to bring with him to neutralize the cells.

## Task

Help Chidil find the answer!

## Input data

The first line of the input file `zc.in` contains two natural numbers $N$ and $M$, representing the number of traps set by Zota and the number of pairs $(D, x)$ according to which Chidil will move.
Lines $2 \dots N+1$ contain a pair of numbers $(x, y)$, representing the coordinates of the traps.
Lines $N+2 \dots N+M+1$ contain a pair in the form $D, x$, indicating that Chidil takes $x$ steps in direction $D$.

## Output data

The output file `zc.out` will contain on the first line the number of dangerous cells that need to be neutralized by Chidil on his path.

## Constraints and clarifications

$1 \leq N, M \leq 100\,000$

Chidil's coordinates will never leave the interval $[-2\,000\,000\,000, 2\,000\,000\,000]$

Even if Chidil's starting cell contains or is affected by a trap, no magic dust is needed to neutralize it

Even if a cell is affected by multiple traps, only a single unit of magic dust is needed to neutralize it

The effect of the magic dust is temporary; each time Chidil passes through an affected cell, he needs magic dust to neutralize it

## Example

`zc.in`

```
2 8
5 6
12 10
N 3
E 6
N 7
E 2
S 3
E 6
N 6
W 3
```

`zc.out`

```
4
```

## Explanation

```
...........####............
............X.#............
...........XXX#............
......###.XXOX#............
............XXX#............
.....X#.#...X.#............
....XX # .#######............
...XXO # X...................
....XX # ....................
.....X#....................
#######....................
#..........................
#..........................
#..........................
```