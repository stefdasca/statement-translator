Here is the translated text with the given instructions:

~[autostrada1.png|align=right]

Gimi has just won a bid for paving a new highway. His company is responsible for processing areas in a two-dimensional surface of size $N \cdot N$. We know that if a road passes through the $i$-th row and the $j$-th column, then the area at position ($i, j$) will need to be paved. The rows and columns of the two-dimensional surface are numbered from $1$ to $N$. Unfortunately for him, he found out only after signing the contract that the project is not as simple as he thought. The road will be determined by the route followed by a drone. Moreover, Gimi does not even know this route, but he received from the highway designer the initial position of the drone ($ls, cs$), representing the row and column of the area where the drone initially is, and a list of $K$ instructions that were applied to the drone. Each instruction is a pair of the form ($dir, p$), meaning that the drone moved in the direction $dir$ for $p$ units, where $dir$ can have the following values:

~[autostrada2.png|align=right]

* $0$ - North direction
* $1$ - East direction
* $2$ - South direction
* $3$ - West direction

For example, if the drone is at position ($1, 3$) and received the instruction ($2, 3$), then the drone will move south (direction $2$) for $3$ units and will traverse areas ($2, 3$), ($3, 3$) and ($4, 3$) where it will stop. All these areas will need to be paved by Gimi's company.

The cost of paving an area through which a simple road passes is $C_z$. Fortunately for Gimi, an area traversed multiple times by the drone only needs to be paved once. However, he noticed that there are some special cases:

If in an area a $\cup$-type intersection occurs, it means that acceleration/deceleration lanes are needed at the intersection. Then the paving cost of the area becomes $C_t$.
If in an area a +-type intersection occurs, it means that a bridge needs to be built, in which case the paving cost of the area becomes $C_p$.

~[autostrada3.png]

# Task

Having this information, Gimi wants to check if the drone's route is valid, meaning the drone will never leave the surface for which Gimi's company is responsible. If the route is invalid, Gimi wants to know which of the $K$ instructions caused the drone to move outside the surface. If the route is valid, he wants to determine the total paving cost of the highway.

# Input data

The first line of the input file `autostrada.in` will contain four natural numbers $N$, $K$, $ls$ and $cs$, where $N$ is the size of the surface, $K$ is the number of instructions applied to the drone, and ($ls, cs$) represents the row and column of the area where the drone initially is. The second line will contain three natural numbers $C_z$, $C_t$ and $C_p$, representing the paving costs of a simple area, a $\cup$-type intersection, and a +-type intersection, respectively.

The next $K$ lines will contain two natural numbers $dir_i$ and $p_i$, representing the specific values of the $i$-th instruction received by the drone. The numbers on the same line are separated by a single space.

# Output data

If the drone's route is invalid, the first line of the output file `autostrada.out` will print the text INVALID ROUTE, and then, the second line will contain a single natural number representing which of the $K$ instructions caused the drone to move outside the surface. Otherwise, the first line of the output file will print the text VALID ROUTE, and then, the second line will contain a single natural number representing the total cost required to pave the highway.

# Constraints and clarifications

* $2 \leq N \leq 2\ 000$
* $1 \leq K \leq 1\ 000\ 000$
* $1 \leq l_s, c_s \leq N$
* $1 \leq C_z, C_t, C_p \leq 100$
* $dir_i \in$ {$0$, $1$, $2$, $3$} for any $1 \leq i \leq K$
* $1 \leq p_i \leq N$ for any $1 \leq i \leq K$
* The initial and final position of the drone must be paved

|#|Points|Constraints|
|-|-|--------|
|1|14|The route is invalid|
|2|6|$1 \leq K \leq 2\ 000$ the route is valid and does not contain any type of intersection|
|3|8|$1 \leq K \leq 2\ 000$ the route is valid and does not contain +-type intersections|
|4|9|$1 \leq K \leq 2\ 000$ the route is valid and does not contain T-type intersections|
|5|24|$1 \leq K \leq 2\ 000$ the route is valid|
|6|39|The route is valid|

# Example 1

`autostrada.in`
```
3 3 1 1
1 2 3
1 2
2 3
3 1
```

`autostrada.out`
```
INVALID ROUTE
2
```

## Explanation

The second instruction is invalid, the drone leaves the surface as it would reach coordinates ($4, 3$).
~[autostrada4.png|width=12em]

# Example 2


`autostrada.in`
```
5 7 2 1
1 2 3
1 4
2 2
3 3
0 3
1 2
2 1
3 3
```

`autostrada.out`
```
VALID ROUTE
17
```

## Explanation

The route determined by the drone is:
~[autostrada5.png|width=18em]

It can be seen that all areas, except ($2, 2$) and ($2, 4$) are simple, meaning they are not intersections, and each has a paving cost of $C_z = 1$.

In ($2, 2$) we have a +-type intersection, so the paving cost will be $C_p = 3$.
In ($2, 4$) we have a $\cup$-type intersection, so the paving cost will be $C_t = 2$.

In total, the cost is $12 \cdot 1 + 1 \cdot 2 + 1 \cdot 3 = 17$.

