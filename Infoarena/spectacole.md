## Task

Even Antonio has heard about the interval scheduling problem. However, being a very well-known and much too "classic" problem for Antonio's tastes, he proposes the following version of the interval scheduling problem. Good luck! 

There are $N$ theater halls and $M$ shows. Each of the $M$ shows is given by 3 numbers $s_i$, $x_i$, and $y_i$ representing the hall where the show is held, the start time, and the end time, respectively.

It is known that to move between halls Antonio must pass through a central hall, and the roads from this central hall to a theater hall and back are not identical. Specifically, the travel time from hall number $i$ to the central hall is $A_i$, and from the central hall to hall $i$ is $B_i$. There is no other way for Antonio to travel between two halls $i$ and $j$, thus, to travel from hall $i$ to hall $j$ Antonio needs $A_i + B_j$ units of time. 

Antonio wants to see as many shows as possible, following these rules:
- Antonio will only watch complete shows. In other words, Antonio is not allowed to leave the hall before the show ends.
- If Antonio is in hall $i$ watching a show that ends at time $T$, he has two options:
  - He can stay in hall $i$ and watch any show that starts at a time greater than or equal to $T$.
  - He can leave at time $T$ to any hall $j$ ($i$ different from $j$), arriving in hall $j$ at time $T + A_i + B_j$. Thus, he can watch any show that starts in hall $j$ at a time greater than or equal to $T + A_i + B_j$.

## Input data

The input file `spectacole.in` contains two natural numbers $N$ and $M$, representing the number of theater halls, and the number of shows, respectively. The next line will contain $N$ numbers representing the values $A_1, A_2, \dots, A_N$. The third line will contain another $N$ numbers representing the values $B_1, B_2, \dots, B_N$. The following $M$ lines will each contain 3 integer values. The $i$-th of these lines will contain the values $s_i$, $x_i$, and $y_i$.

## Output data

The output file `spectacole.out` will contain a single natural number, representing the maximum number of shows Antonio can see while following the above rules.

## Constraints and clarifications

$1 \leq N \leq 2000$ 

$1 \leq M \leq 20000$

$1 \leq s_i \leq N$

$0 \leq x_i < y_i \leq 1\ 000\ 000\ 000$ 

$0 \leq A_i, B_i \leq 1\ 000\ 000\ 000$

It is guaranteed that there are no two shows running simultaneously in the same hall.

For tests worth 30 points $N \leq 100$ and $y_i \leq 1\ 250$ 

For tests worth another 20 points $N \leq 500$ and $y_i \leq 1\ 250$ 

For tests worth 20 points (but not necessarily different from the above 30 + 20 points) $A_i = B_i = 0$

## Example

`spectacole.in`

```
2 4
2 2
3 3
1 0 5
1 5 13
2 10 15
2 15 20
```

`spectacole.out`

```
3
```

## Explanation

Antonio will watch the first show that takes place in hall $1$. At the time of 5, he will move to hall $2$ where he will watch shows 3 and 4.