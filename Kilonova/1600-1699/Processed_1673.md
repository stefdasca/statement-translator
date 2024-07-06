To mitigate the economic crisis effects by increasing the number of viewers (and thus advertising revenue), the editorial team of a prestigious television channel's show "Shocks and Contests" has decided to organize a K1 fighting tournament. $N$ athletes will participate in this tournament. Each of them has a rating, calculated based on their previous results. The amount of money they receive for each fight they participate in is equal to this rating. After each fight, the winner's rating increases by the value of the loser's rating.

# Task

As the television channel aims for the highest profit possible, its managers want to schedule the fights so as to pay the fighters the least total amount. Knowing there are no tied fights and that the tournament ends only after a winner has been established, determine the minimum total amount the organizers can pay. The total amount paid by the television channel is obtained by summing the amounts paid to all fighters throughout the tournament.

# Input data

The input file `k1.in` contains a value $N$ on the first line, representing the number of fighters invited to the tournament, and the following $N$ lines each contain a non-zero natural number $x_i$, representing the initial rating of the $i$-th fighter.

# Output data

The output file `k1.out` contains a single natural number $s$, representing the minimum total amount the television channel can pay the fighters.

# Constraints and clarifications

* $1 \leq N \leq 1 \ 000 \ 000$;
* $1 \leq x_i \leq 10 \ 000$

# Example

`k1.in`
```
3
1
1
1
```

`k1.out`
```
5
```

## Explanation

In the first fight, $2$ athletes each with a rating of $1$ participate. In the final match, a fighter with a rating of $2$ (the winner of the first fight) and another with a rating of $1$ (the one who did not participate in the first fight) will compete. The winner of the first match receives a total of $3$ ($1$ for the first fight and $2$ for the second one), and the one who lost the first fight and the one who only participated in the last fight each receive $1$, so the television will pay a total of $5$.