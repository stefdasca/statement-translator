The UFO invasion of $N$ flying saucers (commonly called UFOs) is giving authorities headaches. Each such UFO contains aliens whose mission is to destroy our planet. The radar that detected the invasion has a screen similar to the XOY plane. Each UFO is represented on the screen by a line segment.

To annihilate the UFOs, the authorities have $K$ laser weapons. The weapons are positioned on the ground (illustrated on the radar screen by the OX axis). Each weapon emits a laser beam, illustrated on the screen by a line parallel to the OY axis. If a laser beam intersects the segment on the radar screen corresponding to a UFO, the beam will kill all the aliens in that UFO.

Unfortunately, there is only one military specialist in laser weapons nearby, so the authorities want to know exactly which weapon they must use to destroy as many aliens as possible.

# Task

Help the authorities determine the number of aliens that can be annihilated with each available weapon.

# Input data

The input file `ozn.in` contains on the first line two natural numbers separated by a space $N \\ K$ representing the number of UFOs and respectively the number of laser weapons. On the next $N$ lines are described the $N$ UFOs, one per line. A UFO is described by $5$ natural numbers separated by a space $x1 \\ y1 \\ x2 \\ y2 \\ nr$, representing in order the coordinates of the ends of the corresponding segment ($x1, y1$), ($x2, y2$), and $nr$ - the number of aliens in it. On the last line, there are $K$ natural numbers $a_1, a_2, a_3, \\dots , a_K$, separated by a space, representing the coordinates on the OX axis (abscissas) where the laser weapons are placed.

# Output data

The output file `ozn.out` will contain $K$ lines. The $i$-th line will contain the total number of aliens that can be destroyed with weapon $i$, considering the weapons numbered in the order in which they appear in the input file.

# Constraints and clarifications

* $1 \\leq N \\leq 20\\ 000$;
* $1 \\leq K \\leq 20\\ 000$;
* $1 \\leq$ any coordinate in the input file $\\leq 2 \\ 000\\ 000$;
* $1 \\leq nr \\leq 100$, for any UFO;
* $x1 < x2$, for any UFO;
* On the radar screen, the segments that describe the ships can intersect.
* If the laser beam passes through one of the ends of a UFO, then it is destroyed.
* For $50$ % of the input tests $1 \\leq N \\cdot K \\leq 10\\ 000\\ 000$;

# Example

`ozn.in`

```
5 3
1 1 3 2 2
2 3 4 1 3
6 5 8 5 8
5 1 7 1 6
6 2 7 4 1
3 7 5 
```

`ozn.out`

```
5
15
6
```

## Explanation

~[ozn.jpg]

The weapon that emits from the point ($3,0$) strikes the flying saucers represented by the segments ($1,1$) ($3,2$) and ($2,3$) ($4,1$) destroying a total of $5$ aliens.
The weapon that emits from the point ($7,0$) strikes the flying saucers represented by the segments ($5,1$) ($7,1$), ($6,2$) ($7,4$) and ($6,5$) ($8,5$) destroying a total of $15$ aliens.
The weapon that emits from the point ($5,0$) strikes the flying saucer represented by the segment ($5,1$) ($7,1$) and destroys $6$ aliens.