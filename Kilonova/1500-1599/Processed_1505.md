Sure, here's the translated text as requested:

---

Now that winter has ended and with the summer season approaching, the townspeople living by the riverside want to prepare the promenade to properly welcome tourists. The promenade is rectangular in shape with a length of $n$ meters and a width of $2$ meters. In the fall, it was paved with $2 \cdot n$ square tiles with a side of one meter, glued to each other, and completely covering the promenade area. After the harsh winter, some tiles have deteriorated, and now they wish to replace them.

As people often do things "halfway", the townspeople decided to spend as little as possible on restructuring the promenade, so they decided that it is not necessary to replace all the deteriorated tiles but only a minimum number of them so that it is possible to walk the promenade from one end to the other by stepping only on good (undamaged) tiles. One can step from one tile to another only if they share a common side.

# Task

Write a program to determine the minimum number of deteriorated tiles that need to be replaced so that the promenade can be traversed from one end to the other.

# Input data

The input file `faleza.in` contains on the first line a natural number $n$ representing the length of the promenade. The second and third lines contain $n$ numbers that can be $0$ or $1$. On the same line, the numbers are separated by a single space. A value of $1$ signifies the presence of a good tile at that place, while a value of $0$ signifies a deteriorated tile. The second line of the file contains the encoding of one part of the promenade (let's say the one facing the water), and the third line contains the encoding of the other part of the promenade. The tiles are glued to each other within the same line, and two by two on columns.

# Output data

The output file `faleza.out` contains a single natural number representing the minimum number of deteriorated tiles that need to be replaced to make it possible to traverse the promenade from one end to the other.

# Constraints and clarifications

* $3 \leq n \leq 100 \ 000$;
* for tests worth $20$ points, one side of the promenade has all deteriorated tiles.

# Example

`faleza.in`
```
8
0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 1
```

`faleza.out`
```
5
```

## Explanation

We denote with `D` a replaced tile.
`D D 1 1 1 0 0 0`
`0 0 0 0 D D D 1`

In this solution, the promenade can be traversed from left to right by stepping on $5$ tiles from the top, then going down to the bottom part and stepping on the $4$ tiles until reaching the right side.

**or**

`D D 1 1 1 D D D`
`0 0 0 0 0 0 0 1`

In this solution, the promenade can be traversed from left to right by stepping only on the tiles from the top.

---