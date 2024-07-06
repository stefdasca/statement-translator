# Task

RANDy is now very interested in winning the grand prize at the new lotteries opened in his country. Because he has relations everywhere, he got a list of the winning numbers from all the $N$ lotteries available. The winning numbers are expressed in base 12 (the numbers can begin with digit $0$).

However, the lotteries could not agree on which letters (upper case English alphabet letters) should be used for $10$ and $11$, so each made its own choice. Even though he has such a great advantage, RANDy still doesn't know the rules to win the lottery. He thinks that in order to win the prize from a lottery he needs to guess only one digit from the winning number.

He doesn't know how to write, so help him learn the minimum number of digits in order to win (in his conception) at each lottery.

# Input

The first line of the input contains a single number, $N$ ($1 \le N \le 2.5 * 10^5$), representing the number of lotteries. Each of the next $N$ lines contains a number written in base 12, representing the winning numbers.

The sum of lengths of all the numbers is at most $4 * 10^6$.

For test worth $13$ points, all the numbers will be written in base $10$.

For test worth $21$ more points, all numbers will be written in base $12$, but only with digits $10$ and $11$.

For test worth $27$ more points, $1 \le N \le 5\ 000$.

# Output

The only line of the output contains a single integer, $K$, representing the minimum number of digits RANDy has to learn how to write in order for him to believe he can win every lottery.

# Example 1

`stdin`
```
4
AABAA
B112
DAA
1777768CD
```

`stdout`
```
2
```

# Explanation

RANDy can learn the following two digits: $1$ and $A$. He can write $"1"$ for lotteries $2$ and $4$ and $"A"$ for lotteries $1$ and $3$. Thus, he thinks that he wins at all of them.