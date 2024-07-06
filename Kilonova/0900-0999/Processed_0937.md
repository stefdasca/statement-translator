~[tunel.png|align=right]

Tommy is a spoiled cat who loves to wander through any tunnel. Therefore, his owners built him a new toy, consisting of $N$ interconnected tunnels (labeled with distinct numbers from $1$ to $N$). All tunnels have the same length, are made of $M$ identical unit elements (numbered with distinct numbers from $1$ to $M$), and have exits at both ends. The connection between two adjacent tunnels is made through a unit element called a passage. In the example in Figure $1$, the toy consists of $4$ tunnels, each tunnel being made up of $9$ unit elements.

To make it more challenging, the owners place a reward in the last unit element of the last tunnel.

~[tunel1.png]

Being a clever cat, Tommy has already learned all the rules of the game:

* he can enter through the left end of any tunnel (through unit element 1);
* he does not pass through the same passage many times;
* if he is not next to a passage, he continues to move through the tunnel to the right;
* if he reaches a passage, he then passes through it into the adjacent tunnel;
* if he reaches the last unit element of the tunnel labeled $N$, then Tommy exits this tunnel with the reward, even if there is a passage connecting this last element to the last element of tunnel $N - 1$ (see Figure 2.b);
* if he reaches the last unit element of the tunnel labeled $N - 1$ and there is a passage that connects this element with the last unit element of the tunnel labeled $N$, then Tommy passes through this passage into the last element of the last tunnel, takes the reward, and exits the tunnel (see Figure 2.a). In case this passage does not exist, Tommy exits tunnel $N - 1$ without the reward;
* if he reaches the last unit element of a tunnel labeled less than $N - 1$, then Tommy exits the tunnel without the reward.

Help Tommy reach the reward as quickly as possible while following the rules of the game!

# Task

Write a program that reads the natural numbers $N, M$ and $X$, and then determines:

* the label of the tunnel through which Tommy exits if he enters the tunnel labeled $X$ while following the rules of the game;
* the number $L$ of unit elements (of tunnels and passages) that Tommy should pass through, following the rules of the game, to reach the reward.

# Input data

The file `tunel.in` contains the following:

The first line contains a natural number $C$ representing the task from the problem that needs to be solved $1$ or $2$.

The second line of the file contains three natural numbers $N, M$ and $X$, separated by a space, with the significance from the problem statement. The following $N - 1$ lines describe the passages between tunnels. The first line among these $N - 1$ indicates the passages between the tunnels labeled $1$ and $2$, the next line indicates the passages between the tunnels labeled $2$ and $3$, $\dots$, the last of these $N - 1$ lines indicates the passages between the tunnels labeled $N - 1$ and $N$.

The first number on each of these lines represents the number $P$ of passages, and the following $P$ distinct numbers, written in ascending order, represent the positions of the unit elements (among the two tunnels) connected by the $P$ passages.

# Output data

If $C = 1$, the file `tunel.out` will contain a natural number on the first line representing the answer to task $1$.

If $C = 2$, the file `tunel.out` will contain the natural number $L$ on the first line representing the answer to task $2$.

# Constraints and clarifications

* $3 \leq N \leq 1\ 000$;
* $4 \leq M \leq 20\ 000$;
* $1 \leq P \leq M - 2$;
* There can be at most $150\ 000$ passages interconnecting the tunnels.
* There can be neighboring passages that connect the unit elements of two adjacent tunnels (see Figure $1$) where tunnels $1$ and $2$ are interconnected by neighboring passages between elements $6$ and $7$).
* The first unit element in each tunnel is not connected to any passage.
* The last unit element in the tunnels labeled $1, 2, \dots, N - 2$ is not connected to any passage.
* Any unit element can be connected to at most one passage.
* Any two tunnels labeled with consecutive numbers are interconnected by at least one passage.
* For each entry into a tunnel, there exists a path to exit.
* For each test, there exists at least one entry into a tunnel through which Tommy can reach the reward exit in tunnel $N$.
* For task $1$ there are $40$ points awarded, and for task $2$ there are $60$ points awarded.

# Example 1

`tunel.in`
```
1
4 9 4
3 2 4 6
2 3 5
3 4 6 9
```

`tunel.out`
```
1
```

## Explanation

Task $1$ is solved. $N = 4$, $M = 9$, $X = 4$.

Tommy, enters through the tunnel labeled $X = 4$ and exits through the tunnel labeled $1$ (see Figure $2$.d).

# Example 2

`tunel.in`
```
2
4 9 4
3 2 4 6
2 3 5
3 4 6 9
```

`tunel.out`
```
4
```

## Explanation

Task $2$ is solved. $N = 4, M = 9, X = 4$. Figures $2$.a, $2$.b, $2$.c, $2$.d contain Tommy's passage through the tunnels for each of the four entries. Only $2$ of these passages lead Tommy to the reward (see Figure $2$.a and Figure $2$.b). If Tommy enters through tunnel $2$, then he reaches the reward by passing through the minimum number $L = 17 = min(17,19)$ unit elements.

~[tunel2.png]