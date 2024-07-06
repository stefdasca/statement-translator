```markdown
# Task

Alessandro is a famous juggler and everyone loves him. He was asked to organize multiple shows, and he needs some help scheduling them.

Alessandro needs to take part in $N$ different shows, numbered from $0$ to $N-1$. Each show must be assigned a day in which he performs it.
Show $i$ starts at a specific time $A_i$ and ends at a specific time $B_i$ of its assigned day.
He has to decide the day to perform each show, note that Alessandro can decide to perform each show on a different day, so the intervals are allowed to overlap.

Alessandro can perform two shows in the same day if the first show ends exactly at the time when the second show starts. Formally, he can perform shows $i$ and $j$ on the same day if $B_i = A_j$. He can also perform three or more shows in the same day if the first show ends exactly when the second shows starts, the second show ends exactly when the third shows start, and so on. He may schedule the shows in any order.
Note that he can't perform two shows in the same day if the first show ends strictly before the second show starts and there are no shows between.

What is the minimum number of days Alessandro needs to perform every show? Note that Alessandro can always perform every show in at most $N$ days by assigning each show a different day.

# Input

The first line contains a single integer $N$ ($1 \le N \le 2 * 10^5$), the number of shows. 

The following $N$ lines contain two integers each: $A_i$ and $B_i$ ($0 \le A_i < B_i \le 10^9$) for each $i=0\ldots N-1$.

For tests worth $20$ points, there is at most one pair of shows that can be performed in the same day.

For tests worth $35$ more points, ($N \le 1000$) and ($0 \le A_i < B_i \le 1000$).

# Output

You need to write a single line with an integer: the minimum number of days Alessandro needs to perform every show.

# Example 1

`stdin`
```
4
4 9
2 4
9 12
1 4
```

`stdout`
```
2
```

# Example 2

`stdin`
```
5
1 5
4 5
5 8
5 9
1 9
```

`stdout`
```
3
```

# Notes

In the **first sample case** Alessandro can perform shows $0$, $2$ and $3$ in the first day and show $1$ in the second day.

In the **second sample case**, there are multiple solutions, all of which take three days. For example, a possible solution is to perform shows $0$ and $3$ in the first day, $4$ in the second day and $1$ and $2$ in the third day.
```
