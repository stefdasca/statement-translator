Tassadar participates in the Starcraft World Championship $2$. There are $N$ players in the championship. Player $i$ has won $W_i$ matches and still has to play $R_{ij}$ matches with player $j$. If a player wins a match, they receive one point, and if they lose, they receive no points.
After all the matches have been played, the ranking is made in descending order of points, and the player with the most points will be named the winner of the championship. If multiple players have the same number of points as the first place, they will all be considered winners.

# Task

Tassadar is a curious person and wants to find out which players could potentially win the championship. We say that a player could win the championship if there is a way to assign results to the remaining matches such that at the end no player has more points than the respective player.

# Input data

The input file `tournament.in` contains on the first line the number $N$ of participants. The next line contains $N$ numbers $W_i$, indicating that participant $i$ has won $W_i$ matches so far. The following $N$ lines contain $N$ numbers $R_{ij}$, indicating that there are still $R_{ij}$ matches to be played between players $i$ and $j$.

# Output data

The output file `tournament.out` will contain on the first line the number of players who can be winners. The next line contains the indices of the players who can be winners, separated by a space, in ascending order by indices.

# Constraints and clarifications

* $1 \leq N \leq 50$
* The total number of matches in the championship (both already played and yet to be played) will not exceed $10^9$
* For test cases worth $20$ points, it is guaranteed that the total number of matches in the championship does not exceed $20$
* $R_{ii} = 0$ for any $i$ and $R_{ij} = R_{ji}$ for any $i$ and $j$
* Players are indexed from $0$

# Example

`tournament.in`
```
3
2 0 2
0 2 2
2 0 0
2 0 0
```

`tournament.out`
```
2
0 2
```

## Explanation

If player $2$ wins the two matches against player $0$, and player $0$ wins the two matches against player $1$, in the end, players $0$ and $2$ will each have $4$ points, and player $1$ will have $0$ points. Thus, players $0$ and $2$ can be winners of the championship. Regardless of the match results, player $1$ cannot win the championship.