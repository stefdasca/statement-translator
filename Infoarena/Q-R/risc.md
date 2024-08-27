## Task

Bianca is a secret agent at the BBB agency. She has a map with $N$ strategic objectives, connected by $M$ bidirectional roads, each with a certain length $L_i$. For each objective, Bianca knows the risk level $R_i$ of that objective (the higher the risk level, the greater the chances that Bianca will be caught and incarcerated). Now Bianca is trying to execute the plan for the next mission. She asks $Q$ questions such as: what is the minimum path between objectives $X_i$ and $Y_i$ such that any intermediate node they pass through has a risk of at most $RM_i$? Help Bianca to successfully complete her mission.

## Input data

The input file `risc.in` will contain on the first line three natural numbers $N$, $M$, and $Q$, separated by spaces, with the meanings given in the statement. The next line contains $N$ numbers, the $i$-th of which is $R_i$, the risk of the $i$-th objective. The following $M$ lines each contain three numbers $X_i$, $Y_i$, and $L_i$ representing the fact that there is a bidirectional road of length $L_i$ between objectives $X_i$ and $Y_i$. The next $Q$ lines each contain three numbers $X_i$, $Y_i$, and $RM_i$ representing one of Bianca's questions.

## Output data

The output file `risc.out` will contain $Q$ lines. On the $i$-th line you will print the answer to Bianca's $i$-th question, representing the minimum distance between objectives $X_i$ and $Y_i$ such that any intermediate node on the path between these nodes has a risk not greater than $RM_i$, or $-1$ if no such path exists.

## Constraints and clarifications

$1 \leq N \leq 300$

$1 \leq M \leq N^2$

$1 \leq Q \leq 100\,000$

$1 \leq L_i \leq 100\,000$

$1 \leq R_i, RM_i \leq 100\,000$

For $50\%$ of the tests $N \leq 100$

Note: For a question $X_i$, $Y_i$, $RM_i$, only intermediate objectives must have a risk of at most $RM_i$.

Two objectives can be connected by multiple roads.

The minimum path from an objective to itself has a distance of $0$.

## Example

`risc.in` 
```
5 6 6 
5 4 3 2 1 
1 2 1 
2 3 1 
3 4 5 
4 1 3 
4 5 10 
5 2 2 
2 3 1 
1 3 1 
2 3 1 
4 4 2 
1 4 2 
3 4 2
```

`risc.out`
```
3
1
4
0
-1
6
```