## Task

The young noble $Naelav$ wishes to win the heart of the very beautiful and skilled $Adnana$, the daughter of King $Arpsod$, ruler of the kingdom of $Valores$. He thinks of impressing her by making armors entirely out of $haur$ for her dragons. However, his father refuses to spend so much money on a teenage crush, so $Naelav$ leaves the kingdom, threatening the people with his catapult, which hurls stone-hard slabs. The kingdom of $Valores$ consists of $N$ cities arranged in a line. Thus, from city $i$ one can reach cities $i+1$ and $i-1$, except for cities $1$ and $N$. A long series of $x$ episodes follows. In each episode, $Naelav$ besieges a certain city $i$, extracts $v_i$ coins of $haur$ from its treasury, and heads to one of the adjacent cities. He can attack a city multiple times for the same amount, but not in consecutive episodes. We know that the first city that has already been besieged is his hometown, city number $1$. To give as many spoilers to your friends as possible, you think about finding out what would be the maximum value that $Naelav$ could collect in the next $x$ episodes, in $Q$ such scenarios.

## Input data

The input file `easyvect.in` contains on the first line the number $T$, the number of tests. Each test will contain the numbers $N$ and $Q$ the number of cities, and respectively the number of queries, and a sequence of $N$ numbers on the next line, representing the amount of coins that can be obtained $v_i$ from each city in one episode. On the following $Q$ lines are described the numbers $x$, representing the number of episodes the series could have.

## Output data

The output file `easyvect.out` will contain $T*Q$ lines, one for each query.

## Constraints and clarifications

$1 \leq T \leq 10$

$2 \leq N \leq 10^5$

$1 \leq Q \leq 10^5$

$1 \leq v_i \leq 10^5$

$1 \leq x \leq 10^9$, for each of the $Q$ queries

Note! The result can exceed 32-bit numbers.

$Naelav$ is more of a peasant than a noble

Upset that he cannot win over $Adnana$, $Naelav$ locks himself in his room and plays with his little dragon.

## Example

```easyvect.in
1
3 2
5 2 1
1
2
```

```easyvect.out
7
12
```

## Explanation

For the first query, the chosen path is $5 \rightarrow 2$ and the sum is $7$.

For the second query, the chosen path is $5 \rightarrow 2 \rightarrow 5$ and the sum is $12$.