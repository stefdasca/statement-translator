```markdown
RAU-Gigel is thinking about a game: $N$ soldiers, numbered from $1$ to $N$ are caught in an ambush. They are subjected to $M$ cannon attacks. The attacks affect not just one soldier, but a range of soldiers, causing each of them a certain amount of damage. For example, the attack $(3,7,5)$ affects soldiers $3$, $4$, $5$, $6$, $7$ with $5$ damage. Initially, all soldiers have $V$ lives. RAU-Gigel wonders how many soldiers remain alive after the $M$ attacks.

# Task
Given $N$, $M$, $V$, and then $M$ cannon attacks of the form $(i,j,k)$ with the meaning: every soldier in the closed interval $[i,j]$ loses $k$ lives, RAU-Gigel wants to know how many soldiers in his entire army remain alive after the $M$ attacks.

# Input data
The file `ambuscada.in` contains the natural numbers $N$, $M$, and $V$ separated by a space, then $M$ lines each containing 3 natural numbers $i$, $j$, $k$ separated by a space, with the meaning described above.

# Output data
The file `ambuscada.out` will contain a single natural number representing the number of soldiers remaining alive.

# Constraints and clarifications
- $2 \le N \le 10^9$
- $1 \le M \le 10^5$
- $1 \le V \le 10^9$
- In all tests, $1 \le i \le j \le N$ and $1 \le k \le V$.
- For tests worth 30 points, $N \le 10^5$ and $M \le 50$.

# Example
`ambuscada.in`
```
6 4 10
2 5 2
1 3 7
2 6 3
3 5 6
```
`ambuscada.out`
```
2
```

## Explanation
Initially all soldiers had $10$ lives.

After the first shot: $10\ 8\ 8\ 8\ 8\ 10$.

After the second shot: $3\ 1\ 1\ 8\ 8\ 10$.

After the third shot: $3\ 0\ 0\ 5\ 5\ 7$.

After the fourth shot: $3\ 0\ 0\ 0\ 0\ 1$.

Finally, $2$ soldiers remain alive.
```