## Wwt

It is the year $21XX$, and you find yourself on the mysterious planet Algo. You have been sent by the evil empire Adaimtir to provoke a third world war on this planet. On the planet Algo, there is only one continent, which can be visualized as a sequence of $N$ plots of land. There are also $K$ countries, indexed from $1$ to $K$. Each plot of land is owned by a country. We say that two countries $A$ and $B$ are in conflict if and only if country $A$ owns a plot $x$ and country $B$ owns a plot $y$ such that $x$ and $y$ are adjacent. With the funds given to you by the empire, you plan to create a new country that can buy any number of plots from any other countries, with the goal of bringing the world to the brink of a world war. This happens if and only if the countries can be partitioned into two sets $P$ and $Q$ such that:
- no pair of countries from $P$ is in conflict 
- no pair of countries from $Q$ is in conflict 
- there exists at least one country $A$ in $P$ and at least one country $B$ in $Q$ such that $A$ and $B$ are in conflict.

Now you wonder: "In how many ways can I buy plots such that the world is brought to the brink of a world war?" Two ways of buying plots are considered different if and only if there is a plot bought in one that is not bought in the other.

## Input data

The input file `wwt.in` will contain, on the first line, the numbers $N$ and $K$. The second line will contain $N$ numbers, where the $i$-th number represents the index of the country that owns the $i$-th plot.

## Output data

The output file `wwt.out` will contain the required number, modulo $1000000007$.

## Constraints

$1 \leq N \leq 200$

$1 \leq K \leq 10$

For tests worth 9 points,
$N \leq 15$
$K \leq 3$

For other tests worth an additional 33 points,
$K \leq 5$

For other tests worth an additional 25 points,
$K \leq 8$

The plots owned by a country do not necessarily need to be continuous.

It is possible for a country to own no plots.

## Example

`wwt.in`
```
4 3
1 2 3 1
```
`wwt.out`
```
11
```

`wwt.in`
```
10 3
1 2 3 2 2 2 3 1 3 3
```
`wwt.out`
```
423
```

## Explanation

In the first example, if the index of the new country is $4$, then the following are valid ways of buying plots:
```
4 2 3 1
1 2 3 4
1 4 3 4
4 4 3 1
4 4 3 4
4 2 4 1
1 2 4 4
4 2 4 4
4 4 4 1
1 4 4 4
1 4 4 1
```