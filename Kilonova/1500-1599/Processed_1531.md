b'\xef\xbb\xbfA game board with $n$ rows, numbered from $1$ to $n$ and $m$ columns, numbered from $1$ to $m$ contains $n * m$ identical cells. The cell in the top left corner is in row $1$ and column $1$. A cell can be: a free cell, a cell containing a stone, or a hole cell.

Stones are numbered starting from $1$. **The stones on the board are numbered in the order they are provided in the input file.**

A cell on the board has at most four neighboring cells, located in the directions: north, west, south, east, and a stone can jump only over one neighboring cell that contains a stone. As a result of such a jump, the stone that was jumped over disappears from the board. Thus, a stone located in the cell in row $i$ and column $j$ can jump:
- in the **north** direction over the stone located in the cell in row $i-1$ and column $j$ and reach the cell in row $i-2$ and column $j$; the stone in row $i-1$ and column $j$ disappears; such a jump is denoted by the letter `N`;
- in the **east** direction over the stone located in the cell in row $i$ and column $j+1$ and reach the cell in row $i$ and column $j+2$; the stone in row $i$ and column $j+2$ disappears; such a jump is denoted by the letter `E`;
- in the **south** direction over the stone located in the cell in row $i+1$ and column $j$ and reach the cell in row $i+2$ and column $j$; the stone in row $i+1$ and column $j$ disappears; such a jump is denoted by the letter `S`;
- in the **west** direction over the stone located in the cell in row $i$ and column $j-1$ and reach the cell in row $i$ and column $j-2$; the stone in row $i$ and column $j-1$ disappears; such a jump is denoted by the letter `V`.

A jump of a stone is allowed only if the cell where it is supposed to land is on the game board, is free, and in the cell over which it jumps, there is a stone.

A known sequence of jumps consists of up to $255$ characters `S`, `N`, `E`, or `V`, after which a stone executes the specified jumps in order, from left to right. If the stone should execute a jump that is not allowed, its position does not change and it proceeds to the next jump in the sequence.

# Task

Determine the number of the stone that, by making jumps according to the given sequence, leads to a final configuration with the minimum number of stones on the board. If there are multiple stones that result in the same minimum number of stones in the final configuration, the smallest value among the identification numbers of those stones will be displayed.

# Input data

The input file `pietre.in` will contain:
- the first line of the file will contain the natural number $n$ representing the number of rows, the natural number $m$ representing the number of columns, the natural number of stones $k$, and the natural number of holes $g$; the values are separated by a space;
- the next $k$ lines will contain two values each, separated by a space, representing the row and column of a stone;
- the next $g$ lines will contain two values each, separated by a space, representing the row and column of a hole;
- the last line contains the jump sequence.

# Output data

The output file `pietre.out` will contain:
- the first line will contain the number of the stone that when applying the jump sequence leads to the configuration containing the smallest number of stones;
- the second line will contain the number of stones in the final configuration (let this be $t$);
- the next $t$ lines will contain two values each, separated by a space, representing the row and column of each stone left on the board, starting with the topmost row (smallest row) and leftmost column (smallest column) to the bottommost row (largest row) and rightmost column (largest column).

# Constraints and clarifications

* $2 \leq n, m \leq 100$
* $2 \leq k \leq n \cdot m - 1$
* $0 \leq g \leq n \cdot m - 1$
* It is guaranteed that in each test there is at least one stone that executes at least one jump.

# Example 1

`pietre.in`
```
5 4 6 2
1 1
1 2
2 2
3 2
3 3
4 1
3 4
5 3
VSE
```

`pietre.out`
```
5
4
1 1
1 2
2 2
5 1
```

## Explanation

~[imagine pietre.png|align=right]

The initial configuration is in the adjacent figure.

Stone $1$: cannot make the jump **V** (because it would leave the game board), nor the jump **S** (because there is no stone in the neighboring cell in the south direction); it makes the jump **E**, so the final configuration of the board will contain $5$ stones.

For stone $2$, the final configuration is identical to the initial one, as it cannot make any jumps.

~[imagine pietre2.png|align=right]

Stone $3$ can only make the jump **S**. The final configuration contains $5$ stones.

Stone $4$ cannot make any jumps. The final configuration contains $6$ stones.

Stone $5$ can make the jumps: **V** and stone $4$ disappears, **S** and a stone disappears, and it cannot make the jump **E**. The final configuration has $4$ stones and is in the adjacent figure.

Stone $6$ cannot make any jumps. The final configuration contains $6$ stones.