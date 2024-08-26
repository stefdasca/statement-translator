## Task

The eccentric Mayor $Droom$ has implemented a new strange road system in the municipality of $Suieb$. The municipality can be represented as an undirected graph with $N$ nodes and $M$ edges. Note that parallel edges can also exist. He numbers the days consecutively, starting with day $0$. On day $0$, he imposes a given one-way direction for all roads. He also defines $f(i)$ as the sum, modulo $2$, of the digits of $i$ when $i$ is written in binary. On day $i$, if $f(i) = 0$, then the roads are one-way in the same direction as on day $0$, while if $f(i) = 1$, then the roads are one-way in the opposite direction. He also introduces a new rule: you must traverse from one intersection to another exactly once per day – of course, using the roads in the specified direction for that particular day. It is guaranteed that this is possible at any intersection on any day. Gabitza, an innocent citizen of the municipality, wonders: given $Q$ tuples $(a_i, b_i, c_i)$ and assuming Gabitza is at intersection $a_i$ on day $0$, in how many ways can $Gabi$ reach intersection $b_i$ on day $c_i$, modulo $10^9 + 7$?

## Input Data

The input file `droom.in` will contain on the first line a number $T$, the number of tests. Each test is composed of several lines. The first line contains two natural numbers $N, M$. The next $M$ lines contain pairs of numbers $x, y$, indicating that there is a road between intersections $x$ and $y$, with the road being one-way from $x$ to $y$ on day $0$. The next line contains $Q$. The following $Q$ lines contain the values $(a_i, b_i, c_i)$, in order.

## Output Data

The output file `droom.out` will contain the answers for each test, in order. For each test, print the answer for each tuple $(a_i, b_i, c_i)$ on a new line.

## Constraints

$1 \leq N \leq 20$

$M \leq 10\ 000$

$Q \leq 200$

$1 \leq a_i, b_i \leq N$

$0 \leq c_i \leq 10^{18}$

$T \leq 50$

## Example

droom.in
```
2
3 7
3 2
3 2
2 1
1 3
3 2
1 3
2 1
3 1
3
1 3 7
1 3 6
1 3 6
3 8
1 2
1 2
1 3
2 3
3 2
2 1
3 1
3
1 3 1
3 2 8
3 2 4 
```

droom.out 
```
2
1 
3
2
8
```