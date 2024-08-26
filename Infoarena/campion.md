# Champion

Zaharel is working hard on the infoarena 2.0 website. His job is to build a user rating system based on the competitions each participant has joined. Firstly, he needs to count how many participants have been champions over time. To simplify the problem, we will consider time moments as real numbers between $0$ and $T$. Each of the $N$ infoarena users started competing at time $0$ and had a rating $R_i$ $(1 \leq i \leq N)$. It is also known that each contestant improves their rating by $D_i$ $(1 \leq i \leq N)$ for each unit of time that passes. A user is called a champion if there is a moment in time when they had the highest rating among all users. If two or more users each have the highest rating at a moment in time, they are all considered champions.

##  Task

Help Zaharel determine the number of users who have been champions.

##  Input data

In the file `campion.in` contains on the first line the natural numbers $N$ and $T$ representing the number of users and the upper limit of time moments. Following are $N$ lines each containing two natural numbers $R_i$ $D_i$, representing the initial rating and the value by which it improves per unit of time, for each user.

##  Output data

The output file `campion.out` will contain a single line which will contain the number of contestants who have been champions.

##  Constraints and clarifications

$$1 \leq N \leq 20\ 000$$
$$0 \leq T \leq 100\ 000\ 000$$
$$0 \leq R_i \leq 1\ 000\ 000\ 000$$
$$0 \leq D_i \leq 1\ 000$$
The rating of each user will not exceed $2\ 000\ 000\ 000$ at any moment of time within the interval $[0\ \ldots\ T]$
All numbers in the input file are natural numbers.
There may exist users with the same starting rating and the same improvement value.

##  Example

`campion.in`
```
3 6 
20 0
4 2
15 1
```

`campion.out`
```
2
```

##  Explanation

Contestant $1$ is initially a champion, and at time $5$ contestant $3$ becomes a champion. Contestant $2$ becomes a champion at time $11$, but $T = 6$, so it is not taken into account.