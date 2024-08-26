## Pieces

Danut has not yet discovered computer science and is playing with pieces of different sizes. His pieces are square and have a side length that is a power of $2$. Thus, Danut has pieces of sizes $1×1$, $2×2$, $4×4$, $8×8$, etc. We can consider that Danut has an unlimited number of pieces of each type. His task now is to cover a board of dimensions $M \times N$ with these pieces. He knows that every small square on the board must be covered by exactly one piece. Because he wants to achieve the covering with minimal effort, Danut wants to use a minimum number of pieces.

## Input data

The input file `piese.in` contains on the first line the numbers $M$ and $N$, with the meaning specified above.

## Output data

The output file `piese.out` will contain on the first line $MIN$, the minimum number of pieces used. Each of the following $M$ lines contains $N$ numbers describing the covering of the board with pieces. Each piece will be associated with a unique natural number from $1$ to $MIN$. Thus, the $j$-th number on the $i+1$-th line ($i$ from $1$ to $M$, $j$ from $1$ to $N$) represents the number of the piece covering the small square at coordinates $(i j)$ on the board. If there are multiple solutions with the minimum number of pieces, any of them can be displayed.

## Constraints and clarifications

$1 \leq M$  
$1 \leq N \leq 500$

The score for a test is awarded only if the covering with pieces is correct (uses a minimum number of pieces of the described type, and the board is completely covered).

## Example

`piese.in` 
```
3 4
```

`piese.out` 
```
6
1 1 2 4
1 1 3 3
5 6 3 3
```

## Explanation

The covering in the example corresponds to the figure:

~[name.png]