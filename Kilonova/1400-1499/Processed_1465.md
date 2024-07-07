
The game that Robo plays when he gets bored is a smart game for little robots. On the screen of his little robot's tablet, there are $N$ square-shaped boxes, each with a side length of $1$. The boxes are arranged in a row, one next to the other, being labeled, in this order, with numbers from $1$ to $N$. Each box contains a natural number, the identifier of one of his friends, little robots like him. The identifiers can repeat.
~[sort2dist.png|align=right]

Robo can swap the contents of two boxes, only if the horizontal distance between them is equal to the distance between his arms; the horizontal distance between the centers of two boxes labeled $i$ and $j$ is $j-i$ ($1 \le i < j \le N$). He can set the distance between his arms at any moment to $1$ or he can double the current distance between his arms, as many times as needed, without exceeding the value $N-1$. Thus, the distance between his arms can be $1$, then $2$ by doubling, then $4$ by doubling, then $8$ by doubling, and so on.

At the beginning of the game, the distance between Robo's arms is $1$. Each time he considers the distance between his arms convenient, he performs a swap.

# Task
Robo is required to arrange the identifiers in the boxes in increasing order, through a maximum of $12500$ swaps of the type specified above.

# Input data
The file `sort2dist.in` contains:
- the first line contains the natural number $N$, with the meaning from the statement;
- the next $N$ lines contain $N$ numbers, representing, in this order, the identifiers contained in the boxes of the tablet (the identifier on line $i$ is contained in box $i-1$).

# Output data
The file `sort2dist.out` contains:
- the first line contains a natural number $M$, representing the number of swaps performed by Robo (not necessarily the minimum number of swaps needed);
- on each of the next $M$ lines (only if $M$ is non-zero), two natural numbers, separated by a space, representing the labels of the boxes whose contents were swapped, in the order these swaps were performed.

# Constraints and clarifications
- $1 \le N \le 1 \ 000$;
- the identifiers are natural numbers of up to $30$ digits;
- for $25\%$ of the score, test files contain numbers with up to $18$ digits;
- for $25\%$ of the score, $N \le 100$.

# Example
`sort2dist.in`
```
4
5
7
6
2
```
`sort2dist.out`
```
2
2 4
2 1
```

## Explanation
The tablet has $4$ boxes, containing, in this order, the identifiers $(5, 7, 6, 2)$. To arrange in increasing order, $2$ swaps were performed:
- the contents of boxes $2$ and $4$ were swapped (the distance between their centers being $2$), the identifiers in the boxes now being $(5, \underline{2}, 6, \underline{7})$;
- the contents of boxes $1$ and $2$ were swapped (the distance between their centers being $1$), the identifiers in the boxes now being $(\underline{2}, \underline{5}, 6, 7)$, ordered increasingly.
