Tradition is that upon retirement, for each day of service to the sultan, the grand vizier receives a bonus determined by the country's great council. Thus, vizier Magir received a total bonus of $411$ gold coins for just $5$ days of service because the council decided on a sum of $53$ gold coins for the first day, $200$ gold coins for the second day, $12$ gold coins for the third day, $144$ gold coins for the fourth day, and only $2$ gold coins for the fifth day.

Vizier Jibal, famous for his contribution to resolving the regional conflict, is granted the right upon retirement to modify the sums determined by the council, but not too much. He can merge the digits of the determined sums and then split them as he wishes so that the sum received each day does not exceed $999$ gold coins and receives at least one gold coin for each day of activity. Thus, if he has only $5$ days of activity, paid with $23$, $417$, $205$, $5$, and respectively $40$ gold coins, totalling $680$ gold coins, he can opt for a new distribution of the council's determined sums as follows: for the first day he requests $2$ gold coins, for the second $3$, for the third $417$, for the fourth $205$, and for the fifth $540$ gold coins, thus receiving $1\ 167$ gold coins in total.

# Task

For the number of days $n$ and the $n$ sums determined by the council for Jibal, write a program that determines the highest total bonus that can be obtained by merging and splitting the digits of the given sums.

# Input data

The input file `suma.in` contains:
- the first line contains a natural number $n$ representing the number of days of activity.
- the next line contains $n$ natural numbers separated by spaces $s_1$, $s_2$, $\dots$, $s_n$ representing the sums assigned by the council.

# Output data

The output file `suma.out` will contain a single line on which one natural number representing the maximum total bonus that can be obtained is printed.

# Constraints and clarifications

* $1 < n < 501$
* $0 < s_i < 1\ 000$
* In any distribution, each sum must be a proper value (must not start with $0$).
* Any sum in a distribution must be non-zero.
* For $20\%$ of the tests, $n \leq 10$, for $50\%$ of the tests $n \leq 50$.

# Example 1

`suma.in`
```
3
58 300 4
```

`suma.out`
```
362
```

## Explanation

The highest bonus ($362$) is obtained exactly for the distribution: $58 \ 300 \ 4$.

# Example 2

`suma.in`
```
5
23 417 205 5 40
```

`suma.out`
```
1608
```

## Explanation

The highest bonus ($1\ 608$) is obtained for the distribution: $2 \ 341 \ 720 \ 5 \ 540$.