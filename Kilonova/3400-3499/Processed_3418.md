The advanced civilization of the Moisilians lives in Galaxy G, which is composed of $N$ celestial bodies, numbered from $1$ to $N$. These bodies are of two types: planets and satellites, each body having an assigned gravity ($G_i$). Between two celestial bodies, there may exist an elevator that makes it possible to travel between them. The energy required to travel by elevator between two bodies, $i$ and $j$, is calculated as follows:

- If both bodies are planets, the energy cost is equal to the least common multiple of their gravities ( $cmmmc(G_i, G_j)$ );
- If one body is a planet and the other is a satellite, the energy cost is equal to the greatest common divisor of their gravities ( $cmmdc(G_i, G_j)$ );
- Between two satellites, the energy cost will always be $1$.

Tragically, one planet has been infected with a highly contagious virus. If a planet $i$ is infected, then all planets connected by an elevator will be, in turn, infected one day after the infection of planet $i$ (if they are not already infected). Fortunately, satellites cannot be infected nor can they spread the virus, as they are not populous enough. Therefore, the queen of Galaxy G chooses a planet as a refuge and wishes to find out the minimum energy cost required to move from it to any other planet.

# Task

The queen, being occupied with other matters, orders Rareș, a skilled Moisilian, to find out:

1. Given the planet $K$ from which the infection starts spreading on day $1$, after how many days will the other planets be infected?
2. With the planet $K$ being chosen as a refuge by the queen, what is the minimum energy cost required to reach any other planet from planet $K$?

# Input data

In the input file `galaxia.in` we have:

- The first line contains the number $C$, which will have the value $1$ or $2$, indicating the task to be solved;
- The second line contains the numbers $N$ and $M$, representing the number of celestial bodies and the number of elevators between bodies, respectively;
- The next $N$ lines contain two numbers, $T_i$ and $G_i$, which represent the type of celestial body $i$ ($1$ for planet, $0$ for satellite) and its gravity (on line $i + 2$ are the type and gravity of body $i$);
- The following $M$ lines contain two numbers, $A$ and $B$, indicating that there is an elevator between bodies $A$ and $B$;
- The last line contains the value $K$, which represents:
  * The index of the planet from which the infection starts if $C=1$;
  * The index of the planet chosen by the queen as a refuge if $C=2$.

# Output data

In the output file `galaxia.out` we have:

- If $C=1$, it will first display $N_p$, the number of planets, and on the next $N_p$ lines, it will display, with space between them, $i$ and $T_i$, indicating that planet $i$ will be infected after $T_i$ days. (If the planet will never be infected, $T_i = -1$);
- If $C=2$, it will first display $N_p$, the number of planets, and on the next $N_p$ lines, it will show, with space between them, $i$ and $E_i$, indicating that to reach planet $i$, the minimum required energy cost is $E_i$ (if $K = i$, $E_i = 0$).

# Constraints and clarifications

- For both tasks, the planets must be displayed in ascending order
- $C \in \{1, 2\}$
- $1 \le N \le 50 \ 000$
- At least one planet is given ($N_p \ge 1$)
- $0 \le M \le 300 \ 000$
- $T_i \in \{0, 1\}; 1 \le G_i \le 1 \ 000 \ 000$, where $1 \le i \le N$
- $1 \le K \le N$
- The celestial body with index $K$ will always be a planet.
- We can move from any celestial body $A$ to any body $B$, with the condition $A \neq B$

| # |      Score      | Constraints |
|:-----:|:--------------------:|:-------:|
|   1   |  20  |    $C = 1; 1 \leq N \leq 100$   |
|   2   | 30 |    $C = 1; 1 \leq N \leq 50 \ 000$   |
|   3   |  30  |    $C = 2; 1 \leq N \leq 100$   |
|   4   | 20 | $C = 2; 1 \le N \le 50 \ 000$   |

# Example 1

`galaxia.in`

```
1
9 13
0 5
1 8
1 2
0 7
0 9
1 10
0 3
1 20
1 14
1 2
1 3
1 4
2 4
3 5
3 7
4 5
4 6
4 8
4 9
5 8
6 7
6 8
6
```

`galaxia.out`
```
5
2 -1
3 -1
6 1
8 2
9 -1
```

# Example 2

`galaxia.in`
```
2
9 13
0 5
1 8
1 2
0 7
0 9
1 10
0 3
1 20
1 14
1 2
1 3
1 4
2 4
3 5
3 7
4 5
4 6
4 8
4 9
5 8
6 7
6 8
6
```
`galaxia.out`
```
5
2 2
3 2
6 0
8 2
9 8
```

# Explanation

~[galaxie.png]

- The green bodies with bold numbers are the planets whereas the red bodies with italic numbers are the satellites; in the image, the energy costs between celestial bodies are highlighted.

In the first example, the task is $1$ and planet $6$ is infected on day $1$. Only planet $8$ is connected to planet $6$, so planet $8$ will be infected on day $2$. The infection does not reach other planets because planets $6$ and $8$ are isolated from them through satellites $4$, $5$, and $7$.

In the second example, the task is $2$, so we need to find out the minimum energy cost required to reach each planet from planet $6$. Thus, the path $2 \rightarrow 4 \rightarrow 6$ has a cost of $2$, the path $3 \rightarrow 7 \rightarrow 6$ has a cost of $2$, the path $8 \rightarrow 4 \rightarrow 6$ has a cost of $2$, and the path $9 \rightarrow 4 \rightarrow 6$ has a cost of $8$.