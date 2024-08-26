# Simulation

Because last year you did not manage to help Hektor pass the exams, he has to take them again this year. Time passes, time comes, and the simulations are approaching. Last year, Hektor did not study for the Romanian language simulation because he said back then that there was plenty of time until the exams and he had enough time to study (obviously, he was wrong). The country in which Hektor lives has the shape of a tree with nodes. Because he is an international mobster, he knows a Romanian teacher in each node of the country who can give him a commentary to learn for the simulation. Each commentary is characterized by two numbers $a_{i}$ and $b_{i}$, representing the refinement of the commentary (its beauty and stylistic value) and $b_{i}$ representing the effort needed to memorize it. There are exactly $d$ days until the simulation, and Hektor knows his schedule well. For each of the $d$ days, he has some business to fulfill, thus being required to travel from node $u$ to node $v$. Because this year Hektor is focused on studying and not just on dirty business, he wants to know the maximum total refinement he could get if he could take some commentaries from the path from node $u$ to node $v$ with the property that their total learning effort is at most equal to $E$ (he dedicates a little time to learning, but he still has some much more important business to resolve and cannot afford to tire himself too much with learning).

## Task

## Input data

The input file `simulare.in` contains on the first line the numbers $N$ and $M$. The next $N$ lines contain two natural numbers $a_{i}$ and $b_{i}$ which represent the refinement and learning effort of the commentary in node $i$. The next $N-1$ lines contain two natural numbers $x$ and $y$ meaning that there is an edge between nodes $x$ and $y$. The next $M$ lines contain three natural numbers $u$, $v$ and $E$.

## Output data

In the output file `simulare.out` there must be $M$ lines, on line $i$ being the maximum possible sum of the refinements of a subset of commentaries from the path from node $u$ to node $v$ with the property that the sum of their efforts is less than or equal to $E$.

## Constraints

$1 \leq N \leq 2000$ 

$1 \leq M \leq 20000$ 

$1 \leq a_{i} \leq 1000$ 

$1 \leq b_{i} \leq 1\ 000\ 000$ 

## Example

`simulare.in`

```plaintext
10 6
5 5
3 9
4 4
10 1
3 1
8 10
1 5
1 1
1 9
5 7
10 7
9 7
5 9
3 10
4 5
8 10 1 5
6 1 2 1
8 7 10 1 5
14 1 4 12
1 1 18
6 9 20
6 1 14
6 8 18
5 16
8 10
```

`simulare.out`

```plaintext
14
12
18
20
14
16
```