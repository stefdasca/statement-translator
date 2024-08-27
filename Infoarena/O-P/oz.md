## Task

In the enchanted land of Oz, there is a wizard whose goal is to save the world. However, malevolent forces try to hinder him and, for this, they challenge the wizard to a game whose winner will decide the fate of the world. Thus, the forces of evil randomly choose an array of $N$ non-zero natural numbers and give the wizard $M$ triplets in the form $(i \ j \ d)$, meaning that the greatest common divisor between the $i$-th and $j$-th number in the array is $d$. The goal of the game is to find the initial array starting from the $M$ triplets. If the forces of evil cheat and there is no solution, this should also be specified.

## Input data

The input file `oz.in` contains on the first line the numbers $N$ and $M$, separated by exactly one space. The next $M$ lines contain one triplet in the form $(i \ j \ d)$, as stated in the problem.

## Output data

The output file `oz.out` will contain a single line, which will contain $N$ natural numbers, indicating a possible solution. Additionally, the solution must have the property that each of the $N$ numbers does not exceed 2 billion. It is guaranteed that if there is a solution, there will be at least one that meets this property. If there is no solution, only $-1$ will be printed.

## Constraints and clarifications

$1 \leq N \leq 10 \ 000$

$1 \leq M \leq 100 \ 000$

For any triplet $(i \ j \ d)$, the following holds:
$1 \leq i, j \leq N$

$i$ is different from $j$

$1 \leq d \leq 2 \ 000 \ 000 \ 000$ 

## Example

`oz.in`
```
4 3
1 4 2
2 3 5
1 3 6
```

`oz.out`
```
12 5 30 14
```

## Explanation

The greatest common divisor between $12$ and $14$ is $2$, between $5$ and $30$ is $5$, and between $12$ and $30$ is $6$. Therefore, these numbers represent a solution as they meet all the conditions stated.