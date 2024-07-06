> Do you want to do a "buffer overflow" or "overflow the buffer"?

After returning from vacation, $N$ friends need to settle the debts accumulated during their holiday.

There are $N$ friends and $M$ relationships of the type $x_i, y_i, w_i$, which represent that the friend with index $x_i$ pays the friend with index $y_i$ an amount of $w_i$ Vbucks (the most stable currency at the moment). Because many such payments are redundant, find another set of maximum $N$ relationships that is equivalent$^1$ to the original one.

The problem would be simple if we stopped here, but unfortunately, after an excursion, certain enmity relationships appeared among the $N$ friends. More precisely, there are $Q$ pairs of friends (or rather, former friends) $u_i, v_i$ who do not want to transfer money to each other (in the final equivalent payments, $u_i$ cannot pay $v_i$ and vice versa).

However, it is possible that no set of relationships exists that satisfies both the equivalence with the initial ones and the restrictions imposed by the enmity relationships. If this is the case, print $-1$.

# Input data

The first line contains two integers $N$ and $M$ - the number of friends and the number of relationships.

The next $M$ lines contain three integers $x_i, y_i, w_i$ - representing the initial $M$ relationships.

The next line contains a single integer $Q$ - the number of enmity relationships.

The next $Q$ lines contain the enmity relationships that appeared during the excursion $u_i, v_i$.

# Output data

If there is no solution that satisfies the task, print $-1$ on the first line. Otherwise, on the first line, print the number of final transactions $K$, where $K \le N$, and on the next $K$ lines, print the payments.

# Constraints and clarifications
* $^1$Two sets of relationships are considered equivalent if after all payments are made, each friend would lose/gain the same amount of money.
* $1 \leq N \leq 10^5$;
* $1 \leq M \leq 10^5$;
* $1 \leq x_i, y_i \leq N$;
* $1 \leq w_i \leq 10^9$;
* $0 \leq Q \leq 10^5$;
* $1 \leq u_i, v_i \leq N$.

# Scoring

|#|Points|Constraints|
|-|-|--------|
|0|0|Examples|
|1|30|$1 \leq n \leq 5 \ 000$|
|2|20|$Q = 0$|
|3|50|No other restrictions|

# Example 1
`stdin`
```
6 6
4 5 34
1 3 98
1 2 41
2 3 20
5 6 35
4 6 37
11
2 4
3 4
5 6
1 4
1 2
2 6
3 6
3 5
1 6
2 5
1 5
```
`stdout`
```
4
3 2 21
1 3 139
5 4 1
4 6 72
```

# Example 2
`stdin`
```
5 8
1 3 38
2 5 9
1 2 21
4 5 76
3 5 12
1 5 48
2 3 43
1 4 46
7
3 5
1 5
2 4
1 3
2 5
1 4
1 2
```
`stdout`
```
-1
```