# Fifty

In the graceful times of TopCoder, most of the problem constraints were equal to $50$. Because of this, problem setters sometimes found unorthodox methods to require solving many queries through a small-sized input. For example, let's assume we want to produce many queries involving two natural numbers $X$ and $Y$. One solution is to provide a string of characters 'a' and 'b' and to consider that each subarray of it represents a query in which $X$ is equal to the number of 'a's in the subarray, and $Y$ is equal to the number of 'b's in the subarray. Thus, we can "store" $O(N ^ 2)$ queries in $O(N)$ space. In this problem, you are given $M$ queries which must explicitly "appear" in the input, and you have to produce a string of characters of exact length $N$ that encodes these queries. For example, if $N = 7$, $M = 2$ and the two queries that must be included are $X = 4$, $Y = 2$, and $X = 3$, $Y = 3$, then the string 'abaabab' is a valid answer because it contains the subarrays 'abaaba' and 'baabab' which encode these two queries.

## Input data

The input file `fifty.in` will contain on its first line the number $T$, denoting the number of tests. The structure of a test is as follows: the first line will contain the numbers $N$ and $M$. The next $M$ lines will contain a pair of numbers $X Y$, representing the values of the respective query.

## Output data

The output file `fifty.out` will contain exactly $T$ lines, each containing a string of characters 'a' and 'b' or the value $-1$ if no solution exists.

## Constraints and clarifications

$1 \leq T \leq 100$

$1 \leq N \leq 50$

$1 \leq M \leq 500$

Any correct solution is accepted. If no solution exists, $-1$ will be printed.

$0 \leq X, Y \leq N$

$X$ and $Y$ will not both be $0$ for any query.

## Example

`fifty.in`
```
1
7 2
4 2
3 3
```

`fifty.out`
```
abaabab
```