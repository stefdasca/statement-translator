*League of Legends* is a popular online game that is often more enjoyable when played together with friends. During a match, a player's main objectives are to kill as many enemies as possible (Kills), to be killed as few times as possible (Deaths), and to help teammates kill enemies (Assists). Thus, a common method to approximate a player's level is the KDA (Kills, Deaths, Assists), a whole number that combines the three objectives of a player. The KDA is calculated automatically, so the method of calculation is not of interest.

Gigel has $N$ friends, and for each, he knows their KDA. Since all of Gigel's friends are very good, their KDA is a positive integer. For a LoL tournament, he wants to form teams of $k$ friends. To ensure everyone has fun, his goal is to balance the teams as much as possible, so friends with a high KDA are not on the same team as friends with a low KDA.

To see how balanced a team is, he plans to use a *balance coefficient* (`qE`). The balance coefficient of a team can be found as follows: take all possible pairs of players in the team, calculate the absolute difference between their KDAs, and then the balance coefficient is the minimum of these calculated differences. A team is more balanced the smaller its `qE`.

# Task

Given a list containing the KDAs of Gigel's $N$ friends and the size of a team $k$, Gigel wants to find out the `qE` of the most unbalanced team. He calculates the `qE` of all possible teams ($\frac{N!}{k!(N-k)!}$ in number) and then chooses the maximum possible `qE`.

# Input data

The first line contains the numbers $N$ and $k$. The next line contains $N$ positive integers, representing the KDAs of Gigel's $N$ friends.

# Output data

Print a single integer representing the maximum possible `qE` of a team formed from $k$ friends.

# Constraints and clarifications

* $1 \leq k \leq N \leq 100\ 000$;
* The KDA of a player is a natural number less than or equal to $10^5$;
* For $10$ points, $k = 2$;
* For $20$ points, $1 \leq N \leq 35$.

# Example

`stdin`
```
5 3
1 3 4 6 7
```

`stdout`
```
3
```

# Explanation

Possible teams are:
* $\{1, 3, 4\}$ with `qE` $1$;
* $\{1, 3, 6\}$ with `qE` $2$;
* $\{1, 3, 7\}$ with `qE` $2$;
* $\{1, 4, 6\}$ with `qE` $2$;
* $\{1, 4, 7\}$ with `qE` $3$;
* $\{1, 6, 7\}$ with `qE` $1$;
* $\{3, 4, 6\}$ with `qE` $1$;
* $\{3, 4, 7\}$ with `qE` $1$;
* $\{3, 6, 7\}$ with `qE` $1$;
* $\{4, 6, 7\}$ with `qE` $1$.

Therefore, the maximum possible `qE` is $3$, obtained by forming the team $\{1, 4, 7\}$.