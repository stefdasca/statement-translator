## Task

Gigel wants to reach the Old Town as quickly as possible to watch the much-anticipated match between Romania and Greece. Therefore, he will use public transportation. Confused by the multitude of options he has, he is thinking of simplifying his life somehow. After a very thorough study of the numbers written on the buses in Bucharest, he realizes that two buses with the numbers $A$ and $B$ have the same route if AT LEAST ONE of the following conditions is met: Either $A$ divides $B$ or $B$ divides $A$. There exists another bus with the number $C$ such that $A$ divides $C$ or $C$ divides $A$, and $B$ divides $C$ or $C$ divides $B$. For example: buses $2$, $3$, $6$ run on the same route because $2$ divides $6$ and $3$ divides $6$; buses $3$, $15$, $10$, $20$ form two routes, with buses $3$, $15$ on the first route, and $10$, $20$ on the second route. Doesn't this rule simplify your life too? Of course. Therefore, Gigel asks you: How many different routes exist in Bucharest? Given $N$, the number of buses in Bucharest, and an array $a_i$ of $N$ natural numbers representing the numbers written on the $N$ buses. If you answer Gigel correctly, your life will be simplified, and you will receive $100$ points, which you can celebrate after tonight's match!

## Input data

The input file `autobuze.in` contains on the first line the natural number $N$, and on the second line $N$ natural numbers, representing the numbers written on the $N$ buses.

## Output data

In the output file `autobuze.out` there will be a single natural number, representing the number of different routes that exist.

## Constraints

$1 \leq N \leq 50000$

$2 \leq a_i \leq 10000000$

Given that Romania is stronger than Greece, there are no two buses with the same number.

For tests worth $50$p, $N \leq 7000$

## Example

`autobuze.in`
```
7
3 7 14 12 28 5 15
```

`autobuze.out`
```
2
```

## Explanation

Buses $3$, $12$, $5$, $15$ run on the same route, while $7$, $14$, $28$ run on another route. In total, there are two different routes.