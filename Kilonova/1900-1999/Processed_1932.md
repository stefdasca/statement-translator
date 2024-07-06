```markdown
A positive integer $K$ is given and $N = 2^K$. $N$ competitors, numbered from $0$ to $N-1$, participate in a tournament. For each competitor $i$, their power $p_i$ is known. The powers are distinct positive integers and strictly less than $N$. In other words, the sequence $p$ is a permutation of the integers from $0$ to $N-1$. A match between two competitors is won by the player with the higher power.

In the first round of the tournament, matches take place as follows: the first match is between competitors $0$ and $1$, the second match between competitors $2$ and $3$, and so on. The $m$-th match is between competitors $2 \cdot m-2$ and $2 \cdot m-1$. The last match of the first round will be between players $N-2$ and $N-1$.

Starting from the second round, the matches will proceed as follows: the first match will be between the winners of the first two matches from the previous round, the second match between the winners of the next two matches, and so on. The last match will be between the winners of the last two matches from the previous round. The tournament will continue until the tournament winner is determined.

# Task

Imagine the following scenario: you are the competitor with **power** $x$ and you want to **win as many matches** in the tournament as possible. To achieve this, you have the right to make **at most** $y$ swap exchanges between the participants in the tournament. In an exchange, the positions of the two players in the initial match table of the first round are swapped.

After making **at most** $y$ exchanges, the tournament begins and follows the rules described above, but due to these changes, it is possible for some matches to have different winners.

In this problem, you will need to implement two functions.

```cpp
void init (int N, int *p)
```

This function will be called by the commission's grader exactly once. This call will pass through the parameter $N$ the value described in the statement and through the parameter $p$ the starting address of an array of integers containing the powers of the $N$ competitors.

```cpp
int query (int x, int y)
```

This function will be called multiple times in the commission's grader after the single call to the `init` function. The function should solve a scenario as described above. Through the parameter $x$ the function receives the **power** of a competitor and through the parameter $y$ a **maximum number of allowed exchanges** and must return the maximum number of matches that the player with power $x$ could win if they make at most $y$ convenient exchanges in the initial match table.

**ATTENTION**: A player can be swapped with any other player – including the player with **power** $x$.

# Constraints and clarifications

* $2 \leq K \leq 20$
* $0 \leq x, y \leq N-1$ for each call of the `query` function
* The `query` function will be called by the commission's grader at most $5 \times 10^5$ times.
* For 15 points $K \leq 10$, the number of calls to the `query` function $\leq 1 \ 000$
* For another 20 points $K \leq 17$, the $x$ values of the queries are given in ascending order
* For another 10 points $K = 18$
* For another 10 points $K = 19$
* For the remaining 45 points $K = 20$
* The pointer received in the `init` function can be used in any way (including modifying the memory)

# Example

`Grader action`
```
init( 4, {3, 2, 0, 1}) 
query (1, 0)
query (0, 2)
query (3, 1)
query (2, 2)
```

`Effect`
```
1
0
2
1
```

# Explanation

In the tournament, there are $4$ players: Player $0$ has power $3$, Player $1$ has power $2$, Player $2$ has power $0$, Player $3$ has power $1$.

For the first query, no exchanges are allowed. In the first round, the player with power $1$ wins the match against the player with power $0$. In the second round, the player with power $1$ loses to the player with power $3$. 

For the second query, $2$ exchanges are allowed. Regardless of the number of exchanges made, the player with power $0$ will lose in the first round because they have the lowest power in the entire tournament. 

For the third query, only one exchange is allowed. Regardless of the number of exchanges, the player with power $3$ will win any match because they have the highest power. Thus, after winning the first match with one of the opponents, they will win the match with the winner of the match between the other two, thus becoming the tournament champion.

# Example 2

`Grader action`
```
init( 8, {2, 7, 3, 0, 1, 4, 6, 5})
query (3, 1) 
query (3, 0)
query (1, 5)
query (4, 7)
query (7, 7)
```

`Effect`
```
2
1
1
2
3
```
```