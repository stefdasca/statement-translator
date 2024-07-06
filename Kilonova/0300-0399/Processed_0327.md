```markdown
# Task

Carlo, as many other people in Provincia di Treviso, produces a lot of rubbish with each activity he carries out during his day.

Still, he is a strong advocate of separate waste collection, and for this reason he has $N$ trash bins at home, indexed from $0$ to $N-1$, each one for a different type of garbage (plastic, cans, glass, ...).

Every trash bin has a capacity of $C_i$ bags, that can never be exceeded, otherwise Treviso's image would be hurt.

Fortunately, every night the *S.A.V.N.O.*, garbage truck passes by and can completely empty a **single continuous interval** of trash cans, removing all of their contents. Note that the garbage truck can clear at most one interval per night.
Obviously, such a great service comes at a cost (the *waste-tax*): the price of clearing an interval is the **sum of the unused capacities** for each trash bin in that interval.

More formally, if $U_i$ is the number of bags in the $i$-th trash bin, the price of emptying an interval $[L, R]$ is: $\\sum_{i=L}^{R}{C_i - U_i}$.

Carlo, after struggling for quite some time with keeping the bins empty, decides to manage his trash more efficiently. Right now, all of his bins are empty. Over the next $K$ days, on day $j$ ($j=0,1,\ldots, K-1$), he will produce $Q_j$ bags of a single garbage type $T_j$, which he will put in the right trash bin. Every evening he will decide whether to call the *neturb\`in* to empty a range of his bins.

After those $K$ days, Carlo will go to Milan, and he would like to have **all his trash bins emptied** before leaving home.

He doesn't have a lot of money, so help him find out the minimal amount he will have to spend.

# Input data

The first line contains the integers $N$ ($1 \le N \le 2 \ 10^5$) and $K$ ($1 \le K \le 2 \ 10^5$), the number of trash bins and the number of days. 
The second line contains $N$ integers $C_i$ ($1 \le C_i \le 10^9$), the capacity of the trash bins.

Each of the following $K$ lines contain two integers: $T_j (0 \le T_j \le N-1)$, $Q_j (1 \le Q_j \le 10^9)$, the type of trash and the number of bags Carlo will produce on day $j$, respectively.

For tests worth $8$ points: $N \le 3, K \le 6$

For tests worth $9$ more points: $N \le 5, K \le 7$

For tests worth $25$ more points: Carlo produces each type of trash at least once.

For tests worth $20$ more points: Over the $K$ days, Carlo produces at most $C_i$ bags of trash of type $i$, for each $i=0 \ldots N-1$

# Output data

You need to print a single integer: the minimum price Carlo has to pay to have all his trash bins emptied after the $K$ days.

# Example 1

`stdin`
```
2 3
5 7
0 4
1 1
1 7
```

`stdout`
```
7
```

# Example 2

`stdin`
```
5 7
66 73 68 79 78
2 50
3 69
0 1
2 20
4 12
1 44
3 11
```

`stdout`
```
304
```
```