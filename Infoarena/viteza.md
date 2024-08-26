## Task

Disappointed by the recent results in the Europa League semifinals, Alex bought a new car and is now eager to test it on the roads of Bucharest. The map of the capital can be represented by $N$ intersections uniquely identified by natural numbers between $1$ and $N$ and by bidirectional streets connecting these intersections. Alex knows that he can reach any intersection from any other by following only the existing streets. Moreover, there is a unique path between any two intersections (the street network is actually a tree). Each intersection has an associated speed limit, represented by a natural number. For reasons still unclear, speed limits exist only at intersections, not on the streets connecting them. Because Alex is a responsible driver, he does not want to exceed the speed limits at intersections, but he still wants to drive as fast as possible. Thus, he asks himself several questions of the form: how many intersections on the unique path between $x$ and $y$ have a speed limit less than or equal to $k$? Because you are Alex's best friend, it is your duty to help him and answer all his questions.

## Input data

The first line of the file viteza.in contains two numbers $N$ and $M$, the number of intersections and the number of questions from Alex, respectively. Each of the next $N-1$ lines contains a pair of natural numbers separated by a space, representing two intersections between which there is a street. On line $N+1$ there are $N$ natural numbers, the $i$-th number on the line representing the speed limit at the intersection identified by the number $i$. The last $M$ lines describe the questions. Each line of the $M$ lines contains 3 natural numbers $x$, $y$, and $k$, separated by a space, for which the answer to the question must be found: "how many intersections on the path between $x$ and $y$ (including $x$ and $y$) have a speed limit less than or equal to $k$?".

## Output data

The file viteza.out must contain exactly $M$ lines, each line containing the answer to the $i$-th question from the input file.

## Constraints

$1 \leq N, M \leq 100000$

The speed limits at intersections are natural numbers from the interval $[0, 100000]$

For each of the $M$ questions:

$1 \leq x, y \leq N$
 
$0 \leq k \leq 100000$

## Example

viteza.in
```
5 4
1 2
2 3
2 4
5 1
4 5 7 1 2
4 3 6
3 5 1
2 2 2
6 4 1
```

viteza.out
```
2
1
1
1
```