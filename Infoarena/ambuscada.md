## Ambush

General Andrei has an army of $N$ soldiers and plans an ambush to capture some strategic objectives. For each soldier, $C_i$ is known, representing their effort capacity, and $T_i$ is the time in minutes that a soldier can use their full effort capacity. Andrei received from his superiors a list of $P$ objectives, for each objective knowing $D_i$, the difficulty level of attacking it. General Andrei also received precise indications. He can send an ambush group consisting of exactly $K$ soldiers. A group of soldiers can capture an objective if the sum of their effort capacities is greater than or equal to the difficulty level of the objective. Since once a soldier has used their effort capacity, they are too tired to perform other actions, the time a group of soldiers takes to capture an objective is the maximum time that a soldier in the group uses their effort capacity. Therefore, Andrei asks you to answer $M$ questions received from the head commander. The head commander asked $M$ questions, the $i$-th question being "what is the highest difficulty of an objective that can be captured in at most $X_i$ minutes?".

## Input data

The input file `ambush.in` contains on the first line four natural numbers, $N$ $K$ $M$ and $P$, having the meaning from the problem statement. The next $N$ lines each contain two natural numbers, $C_i$ and $T_i$, having the meaning from the problem statement. On the $N+2$-nd line contain $P$ natural numbers representing the difficulty levels of the objectives. There follow $M$ lines, each containing a natural number $X_i$, representing the questions asked by the head commander.

## Output data

The output file `ambush.out` will contain $M$ lines, each containing the answer to one of the questions asked by the commander. If there is no objective that can be captured by a group of exactly $K$ soldiers, print $-1$, otherwise print the maximum difficulty of an objective that can be captured.

## Constraints and clarifications

$1 \leq N, K, M, P \leq 100 \, 000$
$1 \leq C_i, T_i, X_i \leq 500 \, 000$
$1 \leq D_i \leq 10^{12}$

Due to the fact that soldiers have personalities, no two different soldiers $i$ and $j$ exist for which $C_i = C_j$ or $T_i = T_j$.

## Example

`ambush.in`
```
3 2 4 3 
2 1 
3 2 
4 3 
4 6 5 
1 
2 
3 
4 
```

`ambush.out`
```
-1 
5 
6 
6 
```

## Explanation

It is not possible to capture any objective in 1 minute because there is only one soldier available, and a group consisting of exactly 2 soldiers needs to be sent to the ambush. Soldiers 1 and 2 can be sent to capture the objective with difficulty 5 in 2 minutes, and soldiers 2 and 3 can be sent to capture the objective with difficulty 6 in 3 minutes.