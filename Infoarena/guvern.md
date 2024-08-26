# Government

Due to all the special abilities he has shown so far, TractoMarm has been hired by the Secret Services to spy on the government of a foreign country. The government consists of $N$ ministers, arranged in a hierarchical structure in the form of a tree (an undirected connected acyclic graph), where node $1$ represents the root (the prime minister). For each minister, a number is known, representing their level of cooperation with the Secret Services. TractoMarm must select the largest possible set of ministers from the $N$, simultaneously respecting the following requirements of the Secret Services:
1. A selected minister must have a higher level of cooperation than all the selected ministers subordinated to him.
2. Let $y$ be the level of cooperation of a selected minister (let this be $x$); among all ministers on the path from $x$ to $1$, the one with the minimum level of cooperation that is greater than or equal to $y$ must be selected.

If you wish to take TractoMarm's place, you must prove yourself worthy and solve this problem!

## Input data

The input file `guvern.in` contains on the first line $N$, the number of ministers. On the following $N - 1$ lines, pairs of numbers $(x, y)$ will represent a direct relationship between ministers $x$ and $y$. The next line contains $N$ distinct natural numbers, the $i$-th number representing the level of cooperation of minister $i$. 

## Output data

The output file `guvern.out` will contain a single line, representing the maximum number of ministers that can be selected, according to the rules of the Secret Services.

## Constraints and clarifications

$1 \leq N \leq 200\,000$

$-10^9 \leq$ the level of cooperation of a minister $\leq 10^9$

## Example

`guvern.in` 
```
10
3 2
10 1
8 7
7 9
2 8
4 6
10 7
5 3
2 6
9
15 2 11 4 12 5 7 3 17 4
```

`guvern.out`
```
4
```

## Explanation

Two possible solutions would be:
1. The selected ministers are those with order numbers $4\, 6\, 2\, 10$
2. The selected ministers are those with order numbers $3\, 9\, 7\, 1$