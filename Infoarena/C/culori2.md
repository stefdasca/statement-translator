# Colors2

The workers from the cooperative "Pointless Work" have a pipe of length $N$ meters at their disposal. Initially, this pipe is colored with color $C$. The workers can cut a piece of the pipe into two smaller pieces of integer lengths and recolor the two pieces. The workers can also change their mind and weld back two pieces into the larger piece from which they were separated and recolor it with the color it had before the cut. Through cutting or welding, the pipe pieces do not move from their initial position, so a piece of the pipe can be identified by its position. The position of a piece of pipe is specified by the distance between the start of the initial pipe and the start of the piece of the pipe, expressed in meters.

## Task

You work at this cooperative and need to write a program that implements the following commands:
- SPLIT ($P$ $L$ $CL$ $CR$): the piece of the pipe that starts at position $P$ will be split into two smaller pieces, the left one having the length $L$. Then the left piece will be colored with color $CL$ and the right piece with color $CR$. It is guaranteed that $0 < L < \text{length of the piece of pipe to be split}$
- UNDO ($P$): the piece that starts at position $P$ will be rewelded with the piece immediately to its right. It is guaranteed that at the moment of calling this command, the piece immediately to its right is the one obtained through the same splitting operation that resulted in the piece at position $P$ (even if either of the two pieces could have been cut and rewelded). The resulting piece will be recolored with the color it had before the cut.
- GETCOLOR ($P$): displays the color of the piece that starts at position $P$.

For all commands, there will be a piece of the pipe that starts at position $P$.

## Input data

The file `culori2.in` contains on the first line the numbers $N$, $C$, and $M$, separated by a space. Each of the following $M$ lines contains a command. The commands are encoded as follows:
- SPLIT ($P$ $L$ $CL$ $CR$) $\rightarrow$ `2 P L CL CR`
- UNDO ($P$) $\rightarrow$ `1 P`
- GETCOLOR ($P$) $\rightarrow$ `0 P`

## Output data

The file `culori2.out` will contain as many lines as there are GETCOLOR commands, representing the respective colors, in the order of the corresponding GETCOLOR commands.

## Constraints

$1 \leq N \leq 524288 \ (2^{19})$

$1 \leq M \leq 2\ 000\ 000$

All colors have values between $0$ and $255$ (inclusive)

Positions will be integers between $0$ and $N-1$ (inclusive)

## Example

`culori2.in`
```
11 3 13 
2 0 8 1 3 
1 0 
2 0 10 3 0 
0 0 
2 0 9 1 1 
2 0 8 2 3 
1 0 
2 0 5 2 3 
1 0 
2 0 5 3 2 
0 9 
1 0 
0 0
```

`culori2.out`
```
3 
3 
1 
3 
2 
3 
1
```