## Task

Depending on the end of the story, display the state of $Snake$ and the forest map at that second. The map should mark the plots occupied by the body of $Snake$, including the head.

## Input data

The first line of the file $culegere.in$ contains the values: $N$ - the number of rows, $M$ - the number of columns into which the forest is divided, $K$ - the length of the snake, and $E$ - the number of events in the forest, separated by a space. The following $E$ lines follow one of the formats:
- 1 $x$ $y$ $st$ $en$ - An apple appears at second $st$, on row $x$, column $y$ and disappears at second $en$
- 2 $x$ $y$ $st$ $en$ $v$ - A switch appears at second $st$, on row $x$, column $y$, disappears at second $en$ and has the value $v$.

The events are sorted in ascending order based on $st$.

## Output data

The first line of the file $culegere.out$ will contain the word $BLOCAT$ or $LIBER$, depending on the state of $Snake$ at the end of the story. On each of the following $N$ lines, there will be $M$ characters from the set {'$\cdot$', '$O$', '$#$'}, with the following meaning:
- $\cdot$ - free plot 
- uppercase $O$ - plot in which a portion of the snake's body is located
- $#$ - the plot in which the head of $Snake$ is located

The character $#$ will appear only once in the matrix.

## Constraints and clarifications

$2 \leq N$ \
$2 \leq M$ \
$2 \leq K < M$ \
$1 \leq E \leq 500\ 000$ \
$1 \leq x \leq N$ \
$1 \leq y \leq M$ \
$1 \leq st < en \leq 500\ 000$ \
$v \in \{1,2,3,4\}$ \
Objects only appear on free plots. The story begins at second 0.

## Example

`culegere.in`\
`culegere.out`

## Explanation

```
4 5 3 4
1 1 5 1 5
2 1 1 2 6 3
2 1 2 5 2
2 4 5 3 5 4
```
```
LIBER
O....
OO#..
.....
.....
```

```
Second 0: OO#..
.....
.....
.....
Second 1: an apple appears, move to the East
.OO#M
.....
.....
.....
Second 2: 2 switches appear, move to the East, swallow the apple, tail grows
3OOO#
2....
.....
.....
Second 3: a switch appears at (4, 4), move to the East and the head appears on the first column over switch 3 from position (1, 1)
#.OOO
2....
.....
....4
Second 4: No objects appear or disappear, move to the South, the body follows the same path as the head which was influenced at second 3 by switch with value 3; the head reaches over switch 2 from position (2,1)
O..OO
#....
.....
....4
Second 5: the switch at (4, 4) disappears, move to the East because the head was influenced by switch with value 2 at second 4; if the apple had not been eaten, it would disappear now
O...O
O#...
.....
.....
Second 6: the first switch disappears even if it was covered by the body of $Snake$, move to the East
O....
OO#..
.....
.....
This is the final configuration because now also the last object disappeared. $Snake$ did not get stuck in its own body, so it is FREE.
```

```
2 6 5 3
2 1 6 1 20 3
2 2 6 1 20 4
2 2 5 1 20 1
```
```
BLOCAT
...OOO
....#O
```

$Snake$ got stuck in its own body before the last object disappeared.