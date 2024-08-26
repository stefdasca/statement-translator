# On Seven Paths

Georgel, a great lover of alcohol and an informatics olympian, has just discovered the concept of pub crawling (https://en.wikipedia.org/wiki/Pub_crawl). Very excited, he learned and found out about $N$ pubs that are connected by one-way streets. He has decided to go on a pub crawl starting from the bar identified by number $1$ which is next to his school, and aims to reach bar $N$, located on Cramei Street, where our protagonist lives. After a careful analysis, he found an alcohol index for each pub. Knowing a safety coefficient $K$, he wants to plan his route so that the product of the alcohol indices along the way contains $K$ to the smallest possible power. If he manages to determine such an optimal path, our hero will reach home successfully. Georgel cannot solve this mystery alone, which is why he is asking for help.

## Input data

The input file `pesaptecarari.in` will contain on the first line 3 numbers $N$, $M$, $K$ representing the number of bars, the number of streets linking the bars, and the safety coefficient $K$, respectively. The next line contains $N$ values, $A_i$ representing the alcohol index for each of the $N$ pubs. The next $M$ lines contain 2 numbers each: $x$, $y$ indicating that there is a one-way street from $x$ to $y$.

## Output data

The output file `pesaptecarari.out` will contain on the first line the minimum power at which $K$ appears in the product of the alcohol indices for the optimal route between bar $1$ and $N$. On the next line, print a route from bar $1$ to bar $N$.

## Constraints and clarifications

$1 \leq N \leq 10^5$

$1 \leq M \leq 7 * 10^5$

$2 \leq K \leq 10^{12}$

$0 \leq A_i \leq 10^{12}$

$1 \leq x \leq N$

$1 \leq y \leq N$

If there are multiple optimal routes, any of them can be printed.

## Example

`pesaptecarari.in`

```
5 5 4
3 2 8 2 2
1 2
1 3
2 4
3 5
4 5
```

`pesaptecarari.out`

```
1
1 2 4 5
```

## Explanation

There are two routes between $1$ and $5$: 
1. The first one is $1 \rightarrow 2 \rightarrow 4 \rightarrow 5$, with the product $3 * 2 * 2 * 2 = 24$ $\Rightarrow$ the maximum power at which $4$ appears is $1$
2. The second one is $1 \rightarrow 3 \rightarrow 5$, with the product $3 * 8 * 2 = 48$ $\Rightarrow$ the maximum power at which $4$ appears is $2$