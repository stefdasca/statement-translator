
# Task

For an array $A$ with $N$ numbers, the cost of an interval is defined as follows:
```cpp
int f(int l, int r){
    int cost = 0;
    for(int i = l; i \leq r; i += A[i])
        cost += A[i];
    return cost;
}
```

Given an array $P$ with $N$ elements and a number $Q$, you need to respond to $Q$ queries of the form: for given $l$ and $r$ ($l \leq r$) calculate $\\displaystyle \\sum_{i=l}^{r} f(i,r)$.

# Input data

The first line contains $N$ and $Q$, the number of elements in the array and the number of queries, respectively. The next line contains $N$ natural numbers separated by spaces. The following $Q$ lines contain exactly $2$ numbers ($l$ and $r$).

# Output data

Each of the $Q$ lines will contain the answer to the respective query.

# Constraints and clarifications

* $1 \leq N, Q \leq 2 \cdot 10^5$
* $1 \leq A_i \leq 30$

# Example 1

`stdin`
```
10 6
6 2 3 3 3 6 4 6 3 2 
3 9
1 7
3 7
3 9
5 10
2 6
```

`stdout`
```
44
48
29
44
30
26
```
# Example 2

`stdin`
```
19 13
1 3 2 4 1 1 3 2 4 4 6 1 4 2 2 6 5 1 3 
5 14
4 9
4 16
5 9
6 8
8 10
4 4
1 7
2 9
2 18
7 8
9 9
10 17
```

`stdout`
```
69 //nice
24
131
18
9
14
4
40
39
201
5
4
68 //😩😩😩😩😩😩😩😩😩😩😩😩😩😩
```
