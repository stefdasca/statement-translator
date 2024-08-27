Robots

In every cell of an $N$x$N$ grid, there is a placed robot. The top-left corner of the grid has the coordinates ( $0$ , $0$ ), and the bottom-right corner ( $N-1$ , $N-1$ ). The robots are programmed to move, every second, according to the following rule: $newX_i = (oldX_i^2 + offsetX) \mod modX$ and $newY_i = (oldY_i^2 + offsetY) \mod modY$, where ( $oldX_i$ , $oldY_i$ ) represents the old position of robot $i$ (the mode of numbering the robots is not important) and ( $newX_i$ , $newY_i$ ) its new position. $offsetX$, $offsetY$, $modX$, and $modY$ are common to the movement rules of the robots.

## Task

Knowing that each robot will make $M$ moves, find how many robots pass through position ( $X$ , $Y$ ) exactly $n$ times, for each $n$ between $0$ and $M$.

## Input data

The first line of the input file will contain $8$ integers separated by spaces: $N$, $M$, $X$, $Y$, $modX$, $modY$, $offsetX$, and $offsetY$ with the meanings from the statement.

## Output data

The output file will contain one line for each $n$ with two integers, $n$ and $C_n$ meaning: "$C_n$ robots pass through position ( $X$ , $Y$ ) exactly $n$ times". The number pairs will be displayed in ascending order of $n$ and only those for which $C_n$ is different from $0$ will be displayed.

## Constraints and clarifications

All numbers in the input file are integers in the range $[0, 1\ 000\ 000]$
This problem will be tested with $10$ tests, each worth $10$ points.
The values used in tests for $N$, $M$, $modX$, and $modY$ are found in the table below.

Over time, a cell can contain multiple robots.

Test \
$1$ $2$ $3$ $4$ $5$ $6$ $7$ $8$ $9$ $10$ \
$N$ $20$ $33$ $61$ $43139$ $83$ $504$ $32668$ $906$ $1523$ $44339$ \
$M$ $1000$ $2100$ $400745$ $337654$ $237891$ $367398$ $500000$ $325000$ $476388$ $666732$ \
$modX$ $13$ $31$ $40$ $54$ $72$ $270$ $561$ $877$ $997$ $997$ \
$modY$ $19$ $29$ $50$ $65$ $69$ $256$ $437$ $809$ $991$ $1000$ 

## Example

`robotei.in` `robotei.out` \
$3$ $4$ $1$ $2$ $2$ $3$ $1$ $1$ \
$1$ $2$ \
$2$ $6$ \
$3$ $1$ 

## Explanations

There are $3 \times 3 = 9$ robots. The robot located in the cell ($3$ $2$) will have the following route: ($3$ $2$) → ($0$ $2$) → ($1$ $2$) → ($0$ $2$) → ($1$ $2$). 
As a result, it passes $2$ times through position ( $1$ $2$ ).